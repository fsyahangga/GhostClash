"""Synthesise PERANG DEDEMIT audio: the background music and one ultimate sound per dedemit.

Nothing here is a recording. The music is a slow pelog gamelan loop (gong, kempul, kenong, slenthem, saron, a low
drone and wind); each ultimate sound is built from formant-filtered voices (giggles, wails, growls), noise, gongs
and coins. Replace any file with a real recording later and keep the same path.

Run from the project root:  python guide/tools/build_dedemit_audio.py
Needs Python 3 with numpy and scipy, and ffmpeg on PATH (for MP3). Afterwards run: node guide/tools/update_precache.mjs
"""
import subprocess, tempfile
from pathlib import Path
import numpy as np
from scipy import signal
from scipy.io import wavfile

SR = 44100
RNG = np.random.default_rng(7)
ROOT = Path.cwd()

# ------------------------------------------------------------------ building blocks
def t_(dur): return np.arange(int(SR * dur)) / SR

def env(n, a=.005, r=None, curve=4.0):
    e = np.ones(n); na = max(1, int(SR * a)); e[:na] = np.linspace(0, 1, na)
    if r is not None:
        nr = min(n, int(SR * r)); e[-nr:] *= np.exp(-curve * np.linspace(0, 1, nr))
    return e

def metal(freq, dur, partials=((1, 1, 1.6), (2.76, .45, 3.5), (5.4, .2, 6), (8.93, .08, 9)), amp=1.0, detune=.0):
    """Struck bronze bar or kettle: inharmonic partials, each with its own decay (ratio, level, decay rate)."""
    t = t_(dur); out = np.zeros_like(t)
    for ratio, lvl, dec in partials:
        f = freq * ratio
        out += lvl * np.sin(2 * np.pi * f * t) * np.exp(-dec * t)
        if detune: out += lvl * .6 * np.sin(2 * np.pi * f * (1 + detune) * t) * np.exp(-dec * t)
    out *= env(len(t), .002); return amp * out / max(1e-9, np.abs(out).max())

def gong(freq=58, dur=7.0, amp=1.0):
    t = t_(dur)
    out = (np.sin(2 * np.pi * freq * t) + .9 * np.sin(2 * np.pi * (freq + .7) * t)) * np.exp(-.45 * t)   # the slow "ombak" beat
    out += .5 * np.sin(2 * np.pi * freq * 2.01 * t) * np.exp(-.9 * t) + .25 * np.sin(2 * np.pi * freq * 2.93 * t) * np.exp(-1.6 * t)
    hum = np.sin(2 * np.pi * freq * .5 * t) * np.exp(-.3 * t) * .3
    out = (out + hum) * env(len(t), .03)
    return amp * out / np.abs(out).max()

def noise(dur): return RNG.standard_normal(int(SR * dur))

def band(x, lo, hi, order=2):
    b, a = signal.butter(order, [lo / (SR / 2), min(hi, SR / 2 - 100) / (SR / 2)], 'band'); return signal.lfilter(b, a, x)

def lowpass(x, f, order=2):
    b, a = signal.butter(order, f / (SR / 2)); return signal.lfilter(b, a, x)

def highpass(x, f, order=2):
    b, a = signal.butter(order, f / (SR / 2), 'high'); return signal.lfilter(b, a, x)

def resonate(x, f, bw):
    r = np.exp(-np.pi * bw / SR); th = 2 * np.pi * f / SR
    return signal.lfilter([1 - r], [1, -2 * r * np.cos(th), r * r], x)

VOWELS = {'i': (300, 2300, 3000), 'e': (480, 1900, 2600), 'a': (750, 1250, 2600), 'o': (480, 850, 2500), 'u': (330, 800, 2300), 'm': (250, 1100, 2200)}

def voice(f0, dur, vowel='a', vib=(5.5, .02), breath=.15, amp=1.0):
    """Formant voice: a band-limited sawtooth at f0(t) (scalar or array) through three resonators."""
    n = int(SR * dur); t = np.arange(n) / SR
    f = np.full(n, float(f0)) if np.isscalar(f0) else np.interp(np.linspace(0, 1, n), np.linspace(0, 1, len(f0)), f0)
    f = f * (1 + vib[1] * np.sin(2 * np.pi * vib[0] * t) + .004 * lowpass(RNG.standard_normal(n), 20) * 10)
    ph = 2 * np.pi * np.cumsum(f) / SR; src = np.zeros(n)
    for k in range(1, 30):
        mask = (f * k) < SR / 2 - 500
        src += mask * np.sin(k * ph) / k
    src += breath * highpass(RNG.standard_normal(n), 1500)
    F = VOWELS[vowel]; out = sum(resonate(src, fr, 80 + fr * .06) * g for fr, g in zip(F, (1, .6, .35)))
    return amp * out / max(1e-9, np.abs(out).max())

def bursts(make, times, total):
    out = np.zeros(int(SR * total))
    for start, piece in zip(times, make):
        i = int(SR * start); out[i:i + len(piece)] += piece[:max(0, len(out) - i)]
    return out

def reverb(x, secs=1.4, mix=.32, tone=4000):
    ir = lowpass(noise(secs), tone) * np.exp(-5 * np.linspace(0, 1, int(SR * secs)))
    wet = signal.fftconvolve(x, ir)[:len(x) + int(SR * secs)]
    dry = np.concatenate([x, np.zeros(len(wet) - len(x))])
    wet /= max(1e-9, np.abs(wet).max()); return dry * (1 - mix) + wet * mix * np.abs(dry).max()

def pad(x, total):
    n = int(SR * total); return np.concatenate([x, np.zeros(max(0, n - len(x)))])[:n]

def thud(freq=70, dur=.35, amp=1.0):
    t = t_(dur); f = freq * (1 + 1.5 * np.exp(-25 * t))
    return amp * np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-9 * t)

def whoosh(dur, lo=300, hi=3000, rise=True):
    n = int(SR * dur); x = noise(dur); out = np.zeros(n); seg = 512
    for i in range(0, n, seg):
        p = i / n; c = lo + (hi - lo) * (p if rise else 1 - p)
        out[i:i + seg] = band(x[max(0, i - 2048):i + seg], c * .7, c * 1.3)[-len(out[i:i + seg]):]
    return out * np.sin(np.pi * np.linspace(0, 1, n)) ** .8

def coins(dur, hits=9):
    out = np.zeros(int(SR * dur))
    for _ in range(hits):
        i = int(RNG.uniform(0, dur * .7) * SR); f = RNG.uniform(2600, 4800)
        c = metal(f, .35, partials=((1, 1, 14), (1.51, .6, 18), (2.39, .4, 22)), amp=RNG.uniform(.3, .7))
        out[i:i + len(c)] += c[:len(out) - i]
    return out

def norm(x, peak=.89): return x / max(1e-9, np.abs(x).max()) * peak

def trim_tail(x, floor_db=-48, fade=.15):
    a = np.abs(x) / max(1e-9, np.abs(x).max()); idx = np.nonzero(a > 10 ** (floor_db / 20))[0]
    end = min(len(x), (idx[-1] if len(idx) else len(x)) + int(SR * .05)); y = x[:end].copy()
    nf = min(len(y), int(SR * fade)); y[-nf:] *= np.linspace(1, 0, nf); return y

def write_mp3(x, path, rate='128k', loop=False):
    path = Path(path); path.parent.mkdir(parents=True, exist_ok=True)
    if not loop: x = trim_tail(x)
    with tempfile.NamedTemporaryFile(suffix='.wav', delete=False) as f: tmp = f.name
    wavfile.write(tmp, SR, (norm(x) * 32767).astype(np.int16))
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', tmp, '-ac', '1', '-codec:a', 'libmp3lame', '-b:a', rate, str(path)], check=True)
    Path(tmp).unlink()
    print(f'{path}  {len(x) / SR:.2f} s')

# ------------------------------------------------------------------ music: "Malam Dedemit", a pelog loop
PELOG = [0, 120, 270, 540, 670, 785, 950]          # approximate pelog cents above 1 (ding)
def pelog(step, base=146.83):                        # base D3
    o, k = divmod(step, 7); return base * 2 ** o * 2 ** (PELOG[k] / 1200)

def music():
    bpm = 66; beat = 60 / bpm; cycles = 4; beats = 16 * cycles; total = beats * beat
    n = int(SR * total); tail = int(SR * 8); out = np.zeros(n + tail)
    def add(x, at, gain=1.0):
        i = int(SR * at); out[i:i + len(x)] += gain * x[:len(out) - i]
    # balungan (slenthem/demung): a slow melody per cycle; 0 = rest
    melody = [[1, 2, 1, 6, 5, 3, 2, 1, 3, 2, 3, 5, 6, 5, 3, 2],
              [2, 3, 2, 1, 6, 5, 6, 1, 3, 5, 3, 2, 1, 6, 5, 6],
              [5, 6, 5, 3, 2, 1, 2, 3, 6, 5, 3, 2, 3, 2, 1, 2],
              [1, 0, 1, 6, 5, 0, 5, 3, 2, 3, 5, 6, 5, 3, 2, 1]]
    for c in range(cycles):
        for b in range(16):
            at = (c * 16 + b) * beat; s = melody[c][b]
            if s: add(metal(pelog(s - 1, 73.4), 2.2, amp=1, detune=.004), at, .32)                  # slenthem, low and soft
            if s and b % 2 == 0: add(metal(pelog(s - 1, 293.66), 1.0, amp=1, detune=.006), at + beat * .5, .10)   # saron echo
            if b % 4 == 3 and b != 15: add(gong(98, 3.0), at, .18)                                   # kempul
            if b == 7: add(metal(pelog(4, 146.83), 2.5, partials=((1, 1, 1.2), (2.02, .4, 2.5), (3.1, .15, 4))), at, .16)  # kenong
        add(gong(55, 8.0), (c * 16 + 15) * beat, .55)                                               # gong ageng ends the gongan
    t = np.arange(len(out)) / SR
    drone = .05 * (np.sin(2 * np.pi * 36.7 * t) + .5 * np.sin(2 * np.pi * 55 * t)) * (1 + .35 * np.sin(2 * np.pi * .07 * t))
    wind = .05 * band(RNG.standard_normal(len(out)), 300, 1100) * (.5 + .5 * np.sin(2 * np.pi * .05 * t + 1))
    out += drone + wind
    loop = out[:n].copy(); loop[:tail] += out[n:n + tail]                                          # wrap the tail for a seamless loop
    return reverb(loop, 2.2, .28, 3000)[:n]

# ------------------------------------------------------------------ ultimate sounds
def giggle(f0s, vowel, on=.11, gap=.05, amp=1.0, last=None):
    pieces, times, t = [], [], 0.0
    for k, f in enumerate(f0s):
        d = last if (last and k == len(f0s) - 1) else on
        v = voice(np.linspace(f * 1.08, f * .92, 8), d, vowel, vib=(7, .03), breath=.25) * env(int(SR * d), .01, d * .6, 3)
        pieces.append(v); times.append(t); t += d + gap
    return bursts(pieces, times, t + .05) * amp

def ult_kuntilanak():
    g = giggle([980, 1040, 1000, 960, 920, 880, 1100], 'i', .1, .045, last=.55)
    return reverb(pad(g, 1.9), 1.6, .45, 5000)

def ult_pocong():
    total = 1.8; out = np.zeros(int(SR * total))
    for k, at in enumerate((.0, .38, .76)):
        th = thud(62 - k * 4, .4) + .25 * lowpass(noise(.4), 400) * np.exp(-12 * t_(.4))
        i = int(SR * at); out[i:i + len(th)] += th
    creak = band(noise(1.0), 600, 900) * (np.sin(2 * np.pi * 14 * t_(1.0)) > .6) * .4
    out[int(SR * .2):int(SR * .2) + len(creak)] += creak
    out += pad(.3 * whoosh(1.8, 200, 900), total)
    return reverb(out, 1.2, .3, 3000)

def ult_sundelbolong():
    w = voice([360, 430, 520, 500, 470, 420, 330], 1.8, 'u', vib=(5.2, .045), breath=.3) * env(int(SR * 1.8), .25, .8)
    return reverb(w, 2.0, .5, 3500)

def ult_wewegombel():
    g = giggle([260, 250, 240, 235, 230, 215], 'e', .12, .06, last=.4)
    return reverb(pad(g, 1.7), 1.3, .35, 4000)

def ult_genderuwo():
    d = 1.5; n = int(SR * d); t = t_(d)
    g = voice(np.linspace(78, 62, 6), d, 'o', vib=(3, .04), breath=.6) * (1 + .6 * np.sin(2 * np.pi * 27 * t)) * env(n, .08, .6)
    g += .5 * lowpass(noise(d), 300) * env(n, .05, .8)
    out = pad(g, 1.9); th = thud(48, .5, 1.2); i = int(SR * 1.25); out[i:i + len(th)] += th[:len(out) - i]
    return reverb(out, 1.0, .25, 2500)

def ult_eyangsukmocapo():
    total = 2.2; out = pad(gong(70, total, 1.0), total)
    hum = voice(110, 1.6, 'm', vib=(4.5, .01), breath=.05) * env(int(SR * 1.6), .3, .6) * .5
    out[int(SR * .15):int(SR * .15) + len(hum)] += hum
    bell = metal(880, 1.2, partials=((1, 1, 2.2), (2.4, .4, 4), (4.1, .2, 6))) * .35; out[int(SR * .9):int(SR * .9) + len(bell)] += bell
    return reverb(out, 1.8, .3, 4000)

def ult_leyak():
    total = 1.7; out = pad(whoosh(1.4, 250, 2600) * 1.2, total)
    s = voice(np.linspace(1150, 1500, 8), .8, 'a', vib=(8, .04), breath=.35) * env(int(SR * .8), .05, .4) * .7
    out[int(SR * .55):int(SR * .55) + len(s)] += s
    out += pad(.25 * lowpass(noise(total), 900) * (1 + np.sin(2 * np.pi * 9 * t_(total))), total)    # crackling fire
    return reverb(out, 1.2, .3, 4500)

def ult_kuyang():
    total = 1.7; out = np.zeros(int(SR * total))
    s = voice(np.linspace(1600, 950, 10), 1.0, 'a', vib=(9, .05), breath=.4) * env(int(SR * 1.0), .02, .5)
    out[:len(s)] += s
    for k in range(6):
        fl = lowpass(noise(.12), 500) * np.hanning(int(SR * .12)) * .7; i = int(SR * (.9 + k * .12)); out[i:i + len(fl)] += fl[:len(out) - i]
    return reverb(out, 1.3, .35, 4000)

def ult_palasik():
    total = 1.8; out = pad(whoosh(1.1, 2200, 300, rise=False) * 1.2, total)
    laugh = giggle([150, 145, 140], 'o', .14, .07) * .6; i = int(SR * 1.0); out[i:i + len(laugh)] += laugh[:len(out) - i]
    out += pad(.2 * highpass(noise(total), 4000) * env(int(SR * total), .2, 1.0), total)
    return reverb(out, 1.5, .4, 3500)

def ult_tuyul():
    total = 1.6; out = pad(coins(1.5, 14), total)
    g = giggle([620, 660, 600, 640], 'i', .08, .04) * .7; out[int(SR * .2):int(SR * .2) + len(g)] += g[:len(out) - int(SR * .2)]
    return reverb(out, .9, .2, 6000)

def ult_jenglot():
    total = 1.6; out = pad(highpass(noise(1.0), 3500) * env(int(SR * 1.0), .15, .5) * .8, total)
    for k in range(7):
        c = band(noise(.02), 2000, 6000) * np.hanning(int(SR * .02)); i = int(SR * (.9 + k * .08)); out[i:i + len(c)] += c[:len(out) - i]
    s = voice(np.linspace(900, 1300, 6), .45, 'i', vib=(10, .05), breath=.4) * env(int(SR * .45), .02, .3) * .6
    out[int(SR * 1.05):int(SR * 1.05) + len(s)] += s[:len(out) - int(SR * 1.05)]
    return reverb(out, 1.0, .3, 5000)

def ult_beguganjang():
    d = 2.0; n = int(SR * d); t = t_(d); f = np.linspace(38, 115, n)
    saw = signal.sawtooth(2 * np.pi * np.cumsum(f) / SR) * env(n, .3, .4)
    out = lowpass(saw, 600) * .8 + .3 * band(noise(d), 200, 700) * env(n, .4, .5)
    w = voice(np.linspace(120, 90, 6), 1.2, 'o', vib=(3, .03), breath=.8) * env(int(SR * 1.2), .3, .5) * .4
    out[int(SR * .6):int(SR * .6) + len(w)] += w
    return reverb(out, 2.0, .45, 2500)

ULTS = {  # slot: (path the engine plays, maker)
    'isolde': ('assets/isolde/audio/isolde-ultimate.mp3', ult_pocong),
    'arco':   ('assets/audio/arco-ultimate-dylan.mp3', ult_kuntilanak),
    'edda':   ('assets/edda/audio/edda-ultimate.mp3', ult_sundelbolong),
    'zanni':  ('assets/zanni/audio/zanni-ultimate.mp3', ult_wewegombel),
    'haldor': ('assets/haldor/audio/haldor-ultimate.mp3', ult_genderuwo),
    'solan':  ('assets/solan/audio/solan-ultimate.mp3', ult_eyangsukmocapo),
    'fenr':   ('assets/fenr/audio/fenr-ultimate-holden.mp3', ult_leyak),
    'cora':   ('assets/cora/audio/cora-ultimate-anika.mp3', ult_kuyang),
    'rhea':   ('assets/rhea/audio/rhea-ultimate.mp3', ult_palasik),
    'nib':    ('assets/nib/audio/nib-ultimate.mp3', ult_tuyul),
    'mira':   ('assets/mira/audio/mira-ultimate-luna.mp3', ult_jenglot),
    'naja':   ('assets/naja/audio/naja-ultimate-soraya.mp3', ult_beguganjang),
}

if __name__ == '__main__':
    import sys
    want = sys.argv[1:]
    if not want or 'music' in want: write_mp3(music(), ROOT / 'assets/audio/music/malam-dedemit.mp3', '112k', loop=True)
    for slot, (path, make) in ULTS.items():
        if not want or slot in want: write_mp3(make(), ROOT / path)
