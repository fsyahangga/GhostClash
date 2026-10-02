"""Build the PERANG DEDEMIT logo set: app icons (PWA, Apple, favicon) and the share image.

The mark is Pocong's head rising in front of a turmeric full moon on a night-jungle field. The share image puts the
title, in IM Fell English, over the home key art.
Run from the project root:  python guide/tools/build_brand.py
Needs Pillow, numpy and fonttools (pip install pillow numpy fonttools brotli).
"""
import io, math, sys
from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont
from fontTools.ttLib import TTFont

ROOT = Path.cwd()
sys.path.insert(0, str(ROOT / 'guide/tools'))
import build_ghost_assets as B

MALAM, KAFAN, KUNYIT = (14, 26, 22), (237, 230, 211), (217, 162, 58)
OUT = ROOT / 'assets/brand'

def radial(size, inner, outer, cx=.5, cy=.42, r=.75):
    w, h = size; y, x = np.mgrid[0:h, 0:w]
    d = np.clip(np.hypot((x / w - cx) / r, (y / h - cy) / r), 0, 1)[..., None]
    return Image.fromarray((np.array(inner) * (1 - d) + np.array(outer) * d).astype(np.uint8), 'RGB')

def moon(d):
    """A full moon from shroud ivory to turmeric at the rim, with a few faint maria and a warm glow."""
    y, x = np.mgrid[0:d, 0:d]; r = np.hypot(x - d / 2, y - d / 2) / (d / 2)
    base = np.array(KAFAN, float) * (1 - r[..., None] ** 2 * .6) + np.array(KUNYIT, float) * (r[..., None] ** 2 * .6)
    rng = np.random.default_rng(5)
    for _ in range(5):
        cx, cy, rr = rng.uniform(.3, .7) * d, rng.uniform(.3, .7) * d, rng.uniform(.05, .1) * d
        k = np.exp(-(((x - cx) ** 2 + (y - cy) ** 2) / (2 * rr ** 2)))[..., None]; base = base * (1 - .09 * k)
    a = np.clip((1 - r) * d / 2, 0, 1)                    # 1 px antialiased rim
    m = Image.fromarray(np.dstack([base.clip(0, 255), a * 255]).astype(np.uint8), 'RGBA')
    g = int(d * 1.5); glow = Image.new('RGBA', (g, g)); o = (g - d) // 2
    ImageDraw.Draw(glow).ellipse((o, o, o + d, o + d), fill=(*KUNYIT, 170))
    glow = glow.filter(ImageFilter.GaussianBlur(d * .09)); glow.alpha_composite(m, (o, o)); return glow

def pocong_head():
    """Pocong from the top knot to the neck tie, cut from the base picture."""
    p = B.base_path('pocong'); fig = B.cutout(p, 'magenta'); bb = B.cutout_box(p, 'magenta')
    full = Image.new('RGBA', Image.open(p).size); full.alpha_composite(fig, bb[:2])
    head = full.crop((500, 20, 960, 640)); head = head.crop(head.getbbox())
    a = np.asarray(head).astype(np.float32); h = a.shape[0]; fade = np.ones(h); n = int(h * .22)
    fade[-n:] = np.linspace(1, 0, n) ** 1.4                 # the shroud dissolves into the mist instead of a cut edge
    a[..., 3] *= fade[:, None]; return Image.fromarray(a.astype(np.uint8), 'RGBA')

def emblem(size, safe=1.0, ring=True):
    """Square icon. safe < 1 keeps the art inside the maskable safe zone."""
    S = 1024; im = radial((S, S), (40, 72, 56), (5, 11, 9), cy=.38).convert('RGBA')
    c = S / 2; k = safe
    md = int(S * .6 * k); mo = moon(md)
    im.alpha_composite(mo, (int(c - S * .1 * k - mo.width / 2), int(c - S * .13 * k - mo.height / 2)))
    head = pocong_head(); hh = int(S * .8 * k); head = head.resize((int(head.width * hh / head.height), hh), Image.LANCZOS)
    shadow = Image.new('RGBA', head.size, (0, 0, 0, 0)); shadow.putalpha(head.split()[3].filter(ImageFilter.GaussianBlur(16)).point(lambda v: int(v * .75)))
    hx = int(c + S * .07 * k - head.width / 2); hy = int(c + S * .5 * k - hh + S * .04 * k)
    im.alpha_composite(shadow, (hx + 12, hy + 16)); im.alpha_composite(head, (hx, hy))
    mist = Image.new('RGBA', (S, S)); ImageDraw.Draw(mist).ellipse((-S * .3, S * (.5 + .38 * k), S * 1.3, S * 1.45), fill=(*MALAM, 235))
    im.alpha_composite(mist.filter(ImageFilter.GaussianBlur(34)))
    if ring:
        mask = Image.new('L', (S, S), 0); ImageDraw.Draw(mask).ellipse((8, 8, S - 8, S - 8), fill=255)
        out = Image.new('RGBA', (S, S)); out.paste(im, (0, 0), mask)
        d = ImageDraw.Draw(out); d.ellipse((14, 14, S - 14, S - 14), outline=(*KUNYIT, 255), width=24); d.ellipse((44, 44, S - 44, S - 44), outline=(*KUNYIT, 80), width=4)
        im = out
    return im.resize((size, size), Image.LANCZOS)

def fell(px):
    p = OUT / 'IMFellEnglish.ttf'
    if not p.exists():
        f = TTFont(ROOT / 'assets/fonts/im-fell-english-latin-400-normal.woff2'); f.flavor = None; f.save(p)
    return ImageFont.truetype(str(p), px)

def share_image():
    W, H = 1200, 630
    art = Image.open(ROOT / 'assets/menu/home-dedemit.webp').convert('RGBA'); s = H / art.height
    art = art.resize((int(art.width * s), H), Image.LANCZOS); bg = art.crop((art.width - W, 0, art.width, H))
    shade = Image.linear_gradient('L').rotate(90).resize((W, H)).point(lambda v: int(max(0, 255 - v * 1.7)))
    bg = Image.composite(Image.new('RGBA', (W, H), (*MALAM, 255)), bg, shade.point(lambda v: int(v * .9)))
    d = ImageDraw.Draw(bg); f = fell(124); x, y = 64, 120
    for txt, col, dy in (('Perang', KAFAN, 0), ('Dedemit', KUNYIT, 118)):
        d.text((x + 4, y + dy + 5), txt, font=f, fill=(3, 8, 6)); d.text((x, y + dy), txt, font=f, fill=col)
    d.text((x + 2, y + 270), 'Dua belas dedemit Nusantara.\nSatu malam, satu arena.', font=fell(34), fill=(214, 208, 191), spacing=8)
    icon = emblem(132); bg.alpha_composite(icon, (W - 132 - 40, H - 132 - 36))
    return bg.convert('RGB')

if __name__ == '__main__':
    OUT.mkdir(parents=True, exist_ok=True)
    big = emblem(1024)
    for n in (512, 192): big.resize((n, n), Image.LANCZOS).save(OUT / f'icon-{n}.png', optimize=True)
    m = emblem(1024, safe=.8, ring=False)
    for n in (512, 192): m.resize((n, n), Image.LANCZOS).save(OUT / f'icon-maskable-{n}.png', optimize=True)
    m.convert('RGB').resize((180, 180), Image.LANCZOS).save(OUT / 'apple-touch-icon.png', optimize=True)
    fav = emblem(256); fav.save(ROOT / 'favicon.ico', sizes=[(16, 16), (32, 32), (48, 48)])
    fav.resize((64, 64), Image.LANCZOS).save(OUT / 'favicon-64.png', optimize=True)
    share_image().save(OUT / 'share.jpg', quality=88)
    (OUT / 'IMFellEnglish.ttf').unlink(missing_ok=True)
    print('brand assets written to', OUT)
