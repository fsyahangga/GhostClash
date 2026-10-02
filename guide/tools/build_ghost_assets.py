"""Build GHOST CLASH placeholder assets from one base image per ghost.

From assets/ghosts/base/<ghost>.(webp|png) (full body, facing RIGHT, flat magenta or green background) this writes,
for the ghost's engine slot:
  - a puppet sprite atlas with the slot's exact layout (same cells, rows and anchor), where each state is the base
    pose squashed, leaned, shifted or rotated (idle breath, walk bob, lunge, hurt recoil, fall ...);
  - the slot's metrics bounds/heights recomputed from those frames (emitters and playback stay as tuned);
  - HUD portrait (384x384), character-select art and the ultimate cut-in (1600x686).
It is a stand-in until real animation strips go through the sprite pipeline (guide/character-workflow.md).

Run from the project root:  python guide/tools/build_ghost_assets.py [ghost ...]
Needs Python 3 with Pillow and numpy (pip install pillow numpy) and Node.js on PATH (to read/write manifest.js).
Afterwards run:  node guide/tools/update_precache.mjs
"""
import json, math, subprocess, sys
from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

ROOT = Path.cwd()
BASE_DIR = ROOT / 'assets/ghosts/base'

# slot = engine kit slot; atlas/manifest = files to rewrite; portrait = [cx, cy, size] in base pixels (1254 px images);
# color = glow colour for portrait and cut-in.
GHOSTS = {
    'pocong':     dict(slot='isolde', key='magenta', portrait=[760, 440, 430], color=(120, 200, 210)),
    'kuntilanak': dict(slot='arco',   key='magenta', portrait=[800, 410, 460], color=(150, 170, 200)),
    'genderuwo':  dict(slot='haldor', key='green',   portrait=[920, 400, 440], color=(230, 120, 40)),
    'tuyul':      dict(slot='nib',    key='magenta', portrait=[770, 420, 460], color=(230, 190, 70)),
    'kuyang':     dict(slot='cora',   key='green',   portrait=[860, 400, 440], color=(220, 40, 60)),
    'leyak':      dict(slot='fenr',   key='green',   portrait=[890, 540, 460], color=(250, 140, 40)),
    'kuchisake':  dict(slot='zanni',  key='magenta', portrait=[760, 400, 400], color=(200, 170, 120)),
    'llorona':    dict(slot='naja',   key='magenta', portrait=[850, 430, 440], color=(120, 190, 230)),
    'banshee':    dict(slot='solan',  key='magenta', portrait=[860, 400, 440], color=(150, 200, 240)),
    'bloodymary': dict(slot='rhea',   key='green',   portrait=[780, 370, 420], color=(200, 30, 50)),
    'dullahan':   dict(slot='mira',   key='magenta', portrait=[940, 620, 400], color=(90, 150, 255)),
    'jiangshi':   dict(slot='edda',   key='magenta', portrait=[640, 400, 440], color=(240, 210, 80)),
}
SLOT_FILES = {
    'arco':  dict(atlas=['assets/mecha/run/sprite-sheet-alpha.webp'], manifest=['assets/mecha/manifest.js'], prefix=['MECHA'],
                  portrait=['assets/ui/arco-avatar.webp'], select='assets/menu/arco-select.webp', cutin='assets/ui/ultimate-cutin.webp'),
    'fenr':  dict(atlas=['assets/fenr/human/run/sprite-sheet-alpha.webp', 'assets/fenr/wolf/run/sprite-sheet-alpha.webp'],
                  manifest=['assets/fenr/human/manifest.js', 'assets/fenr/wolf/manifest.js'], prefix=['FENR_HUMAN', 'FENR_WOLF'],
                  portrait=['assets/fenr/ui/portrait-human.webp', 'assets/fenr/ui/portrait-wolf.webp'],
                  select='assets/menu/fenr-select.webp', cutin='assets/fenr/ui/cutin.webp'),
}
def slot_files(slot):
    if slot in SLOT_FILES: return SLOT_FILES[slot]
    return dict(atlas=[f'assets/{slot}/run/sprite-sheet-alpha.webp'], manifest=[f'assets/{slot}/manifest.js'], prefix=[slot.upper()],
                portrait=[f'assets/{slot}/ui/portrait.webp'], select=f'assets/menu/{slot}-select.webp', cutin=f'assets/{slot}/ui/cutin.webp')

# ---------------------------------------------------------------- cutout
def cutout(path, key):
    a = np.asarray(Image.open(path).convert('RGB')).astype(np.float32)
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    if key == 'magenta':
        spill = np.minimum(r, b) - g          # how much "magenta" is in the pixel
        dist = np.sqrt((r - 255) ** 2 + g ** 2 + (b - 255) ** 2)
    else:
        spill = g - np.maximum(r, b)
        dist = np.sqrt(r ** 2 + (g - 255) ** 2 + b ** 2)
    alpha = np.clip((dist - 60) / 70, 0, 1)   # soft edge between 60 and 130 colour distance from the key
    # Despill: remove the key colour that bled into edges and semi-transparent cloth.
    s = np.clip(spill, 0, None) * (spill > 25)
    if key == 'magenta': r, b = r - s * .85, b - s * .85
    else: g = g - s * .85
    rgb = np.stack([r, g, b], -1).clip(0, 255)
    img = Image.fromarray(np.dstack([rgb, alpha * 255]).astype(np.uint8), 'RGBA')
    # Drop specks left over from compression noise.
    m = (np.asarray(img)[..., 3] > 0).astype(np.uint8) * 255
    m = np.asarray(Image.fromarray(m).filter(ImageFilter.MinFilter(3)).filter(ImageFilter.MaxFilter(5)))
    arr = np.asarray(img).copy(); arr[..., 3] = np.minimum(arr[..., 3], m); img = Image.fromarray(arr, 'RGBA')
    return img.crop(img.getbbox())

def feet_x(img):
    """Horizontal centre of the lowest 12% of the figure: where the fighter stands."""
    a = np.asarray(img)[..., 3] > 40
    h = a.shape[0]; rows = a[int(h * .88):]
    xs = np.nonzero(rows)[1]
    return float(xs.mean()) if len(xs) else img.width / 2

# ---------------------------------------------------------------- puppet poses
def pose(state, i, n):
    """(scale_x, scale_y, angle_deg [+ = lean back], dx, dy, flash, ground) for frame i of a state."""
    t = i / max(1, n - 1)
    P = dict(sx=1, sy=1, ang=0, dx=0, dy=0, flash=0, ground=True)
    if state == 'idle':   P.update(sy=[1, .985, .97, .985][i % 4], sx=[1, 1.006, 1.012, 1.006][i % 4])
    elif state == 'walk': P.update(dy=[0, -4, 0, -4][i % 4], ang=[-2, 0, -2, 0][i % 4], sy=[1, .99, 1, .99][i % 4])
    elif state == 'run':  P.update(dy=[0, -7, 0, -7][i % 4], ang=[-9, -7, -9, -7][i % 4], sx=1.03, sy=.97)
    elif state == 'jump': P.update(ang=-8, sy=1.05, sx=.97)
    elif state == 'doublejump': P.update(sx=.86, sy=.74)
    elif state == 'crouch': P.update(sy=[.86, .76, .74, .74][i % 4], sx=[1.04, 1.08, 1.08, 1.08][i % 4])
    elif state.startswith('attack'):
        k = int(state[-1])
        P.update(dx=[-6, 14 + 4 * k, 24 + 6 * k, 6][i % 4], ang=[6, -8 - 2 * k, -12 - 3 * k, -2][i % 4],
                 sx=[.98, 1.03, 1.06, 1][i % 4], sy=[1, .98, .96, 1][i % 4])
    elif state == 'skill1': P.update(dx=[-8, 4, 18, 4][i % 4], ang=[8, -4, -10, -2][i % 4], sx=[.97, 1.02, 1.05, 1][i % 4])
    elif state == 'skill2': P.update(dx=[-4, 22, 40, 10][i % 4], ang=[4, -14, -18, -4][i % 4], sx=[1, 1.06, 1.1, 1][i % 4], sy=[1, .95, .93, 1][i % 4])
    elif state == 'ultimate': P.update(sy=[1, 1.04, 1.07, 1.02][i % 4], ang=[0, 5, 8, 2][i % 4], flash=[0, 0, .25, 0][i % 4])
    elif state == 'hurt': P.update(dx=[-10, -14, -8, -2][i % 4], ang=[12, 15, 9, 3][i % 4], flash=[.55, .2, 0, 0][i % 4])
    elif state == 'down': P.update(dx=[-12, -24, -32, -34][i % 4], ang=[30, 62, 86, 90][i % 4], flash=[.3, 0, 0, 0][i % 4])
    elif state == 'recover': P.update(dx=[-30, -20, -8, 0][i % 4], ang=[70, 40, 15, 0][i % 4], sy=[1, .9, .95, 1][i % 4])
    return P

def render_frame(fig, fx, P, cell_w, cell_h, ax, ay, tint=None):
    w, h = fig.size
    sw, sh = max(1, round(w * P['sx'])), max(1, round(h * P['sy']))
    img = fig.resize((sw, sh), Image.LANCZOS)
    if tint is not None:
        arr = np.asarray(img).astype(np.float32); c = np.array(tint, np.float32)
        arr[..., :3] = arr[..., :3] * .72 + c * .28; img = Image.fromarray(arr.clip(0, 255).astype(np.uint8), 'RGBA')
    if P['flash']:
        arr = np.asarray(img).astype(np.float32); arr[..., :3] += (255 - arr[..., :3]) * P['flash']
        img = Image.fromarray(arr.clip(0, 255).astype(np.uint8), 'RGBA')
    R = int(max(sw, sh) * 1.2) + 4
    canvas = Image.new('RGBA', (2 * R, 2 * R))
    px, py = fx * P['sx'], sh            # pivot = feet point
    canvas.paste(img, (round(R - px), round(R - py)), img)
    if P['ang']: canvas = canvas.rotate(P['ang'], resample=Image.BICUBIC, center=(R, R))
    cell = Image.new('RGBA', (cell_w, cell_h))
    big =Image.new('RGBA', (cell_w + 4 * R, cell_h + 4 * R))
    big.alpha_composite(canvas, (round(2 * R + ax - R + P['dx']), round(2 * R + ay - R)))
    bb = big.getbbox()
    if bb is None: return cell, None
    shift_y = 0
    if P['ground']: shift_y = (2 * R + ay) - bb[3]          # stand on the ground line
    shift_y += P['dy']
    shift_x = 0
    l, r = bb[0] - 2 * R, bb[2] - 2 * R
    margin = 6
    if l < margin: shift_x = margin - l                      # keep long falls inside the cell
    if r + shift_x > cell_w - margin: shift_x -= (r + shift_x) - (cell_w - margin)
    cell.alpha_composite(big.crop((2 * R - shift_x, 2 * R - shift_y, 2 * R - shift_x + cell_w, 2 * R - shift_y + cell_h)))
    return cell, cell.getbbox()

# ---------------------------------------------------------------- manifest.js io (via node)
def read_manifest(path):
    js = "const vm=require('vm');const s={window:{}};vm.runInNewContext(require('fs').readFileSync(process.argv[1],'utf8'),s);console.log(JSON.stringify(s.window));"
    return json.loads(subprocess.check_output(['node', '-e', js, str(path)]))

def write_manifest(path, data):
    path.write_text(''.join(f'window.{k} = {json.dumps(v, separators=(", ", ": "))};\n' for k, v in data.items()), encoding='utf-8')

def build_atlas(fig, atlas_path, manifest_path, prefix, height, tint=None):
    data = read_manifest(manifest_path)
    man, met = data[prefix + '_MANIFEST'], data[prefix + '_METRICS']
    lay = man['frame_layout']; cw, ch = lay['cellWidth'], lay['cellHeight']
    ax, ay = met['anchor']['x'], met['anchor']['y']
    scale = height / fig.height
    f = fig.resize((max(1, round(fig.width * scale)), height), Image.LANCZOS)
    max_w = cw - 24                                       # very wide ghosts are narrowed to fit the cell
    if f.width > max_w: f = f.resize((max_w, round(f.height * max_w / f.width)), Image.LANCZOS)
    fx = feet_x(f)
    sheet = Image.new('RGBA', (lay['sheetWidth'], lay['sheetHeight']))
    for state, rects in lay['rows'].items():
        n = len(rects)
        frames_out = []
        for i, rc in enumerate(rects):
            cell, bb = render_frame(f, fx, pose(state, i, n), rc['w'], rc['h'], ax, ay, tint)
            sheet.alpha_composite(cell, (rc['x'], rc['y']))
            if bb: frames_out.append({'frame': i, 'bounds': {'left': bb[0] - ax, 'right': bb[2] - ax, 'top': bb[1] - ay, 'bottom': bb[3] - ay}, 'height': ay - bb[1]})
        if state in met.get('states', {}): met['states'][state]['frames'] = frames_out
    sheet.save(atlas_path, 'WEBP', lossless=True, method=6)
    man['base_image'] = 'assets/ghosts/base (puppet placeholder, guide/tools/build_ghost_assets.py)'
    write_manifest(manifest_path, data)

# ---------------------------------------------------------------- UI art
def glow_bg(size, color, dark=(10, 14, 24)):
    w, h = size
    bg = Image.new('RGB', size, dark)
    g = Image.new('L', size, 0); d = ImageDraw.Draw(g)
    d.ellipse((-w * .2, -h * .1, w * .9, h * 1.2), fill=150)
    g = g.filter(ImageFilter.GaussianBlur(min(w, h) * .18))
    return Image.composite(Image.new('RGB', size, tuple(int(c * .55) for c in color)), bg, g)

def portrait(raw, box, color, out, size=384):
    cx, cy, s = box
    crop = raw.crop((cx - s // 2, cy - s // 2, cx + s // 2, cy + s // 2)).resize((size, size), Image.LANCZOS)
    bg = glow_bg((size, size), color); bg.paste(crop, (0, 0), crop)
    bg.save(out, 'WEBP', quality=92)

def select_art(fig, out):
    old = Image.open(out); W, H = old.size
    s = min((W * .96) / fig.width, (H * .96) / fig.height)
    f = fig.resize((round(fig.width * s), round(fig.height * s)), Image.LANCZOS)
    c = Image.new('RGBA', (W, H)); c.alpha_composite(f, ((W - f.width) // 2, H - f.height))
    c.save(out, 'WEBP', quality=92)

def cutin(fig, color, out, W=1600, H=686):
    bg = glow_bg((W, H), color).convert('RGBA')
    d = ImageDraw.Draw(bg)
    for k in range(9):                                   # diagonal speed streaks
        x = 380 + k * 140; d.polygon([(x, 0), (x + 40, 0), (x - 260, H), (x - 300, H)], fill=(*color, 18))
    s = (H * 1.25) / fig.height
    f = fig.resize((round(fig.width * s), round(fig.height * s)), Image.LANCZOS)
    bg.alpha_composite(f, (max(-80, 420 - f.width // 2), int(H * .06)))
    shade = Image.linear_gradient('L').rotate(90).resize((W, H))      # dark right side for the HTML title
    shade = shade.point(lambda v: int(v * .75))
    bg = Image.composite(Image.new('RGBA', (W, H), (6, 8, 14, 255)), bg, shade)
    bg.convert('RGB').save(out, 'WEBP', quality=90)

# ---------------------------------------------------------------- main
def base_path(name):
    for ext in ('webp', 'png'):
        p = BASE_DIR / f'{name}.{ext}'
        if p.exists(): return p

def build(name):
    cfg = GHOSTS[name]; p = base_path(name)
    if not p: print(f'skip {name}: no base image'); return
    sf = slot_files(cfg['slot'])
    raw = Image.open(p).convert('RGBA')
    fig = cutout(p, cfg['key'])
    # Portrait crops come from the cut-out figure placed back on the original canvas size.
    full = Image.new('RGBA', raw.size); bb = cutout_box(p, cfg['key']); full.alpha_composite(fig, bb[:2])
    for i, (atlas, manifest, prefix) in enumerate(zip(sf['atlas'], sf['manifest'], sf['prefix'])):
        data = read_manifest(ROOT / manifest)
        height = data[prefix + '_METRICS']['states']['idle']['frames'][0]['height']
        tint = (255, 110, 30) if (cfg['slot'] == 'fenr' and i == 1) else None   # Leyak's beast form glows like embers
        build_atlas(fig, ROOT / atlas, ROOT / manifest, prefix, height, tint)
    for i, out in enumerate(sf['portrait']):
        portrait(full, cfg['portrait'], (255, 110, 30) if i else cfg['color'], ROOT / out)
    select_art(fig, ROOT / sf['select'])
    cutin(fig, cfg['color'], ROOT / sf['cutin'])
    print(f'{name}: slot {cfg["slot"]} updated')

def cutout_box(p, key):
    a = np.asarray(Image.open(p).convert('RGB')).astype(np.float32)
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    dist = np.sqrt((r - 255) ** 2 + g ** 2 + (b - 255) ** 2) if key == 'magenta' else np.sqrt(r ** 2 + (g - 255) ** 2 + b ** 2)
    m = Image.fromarray(((dist > 60) * 255).astype(np.uint8)).filter(ImageFilter.MinFilter(3)).filter(ImageFilter.MaxFilter(5))
    return m.getbbox()

if __name__ == '__main__':
    for n in (sys.argv[1:] or list(GHOSTS)): build(n)
