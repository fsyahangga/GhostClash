<div align="center">

# 👻 GHOST CLASH

**A 2D browser fighting game — Hantu Nusantara vs Hantu Mancanegara.**
Twelve chibi ghosts from folklore around the world, cinematic ultimates and a CPU that reads your moves. Runs in any modern browser, on desktop and mobile, with no install.

![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-ES2020-F7DF1E?style=flat-square&logo=javascript&logoColor=black)
![Canvas 2D](https://img.shields.io/badge/Canvas-2D-4a90d9?style=flat-square)
![Dependencies](https://img.shields.io/badge/dependencies-0-brightgreen?style=flat-square)
[![Code license: MIT](https://img.shields.io/badge/code-MIT-blue?style=flat-square)](LICENSE)
[![Assets license: CC BY-NC 4.0](https://img.shields.io/badge/assets-CC_BY--NC_4.0-lightgrey?style=flat-square)](LICENSE-ASSETS.md)

</div>

---

GHOST CLASH is built on [Aether Clash](https://github.com/bangtutorial/aether-clash) by Bang Tutorial ([YouTube tutorial](https://www.youtube.com/watch?v=UN_0bNC2wTU)). The engine, combat and CPU are unchanged; each of the twelve kit slots is now played by a ghost whose legend fits that slot's moves.

> [!NOTE]
> **Work in progress.** Eleven ghosts already have their own art: portraits, select art, cut-ins and placeholder puppet sprites built from one base image each (`guide/tools/build_ghost_assets.py`). Jiangshi, skill icons, effects, arena backgrounds and voices are still the original Aether Clash assets. Prompts for every ghost are in [guide/ghost-prompts.md](guide/ghost-prompts.md); which files to replace is in [guide/ghost-roster.md](guide/ghost-roster.md).

## 👻 Roster

| Ghost | Faction | Origin | Basic | Ultimate | Engine slot |
| --- | --- | --- | --- | --- | --- |
| **POCONG** — The Shroud Hopper | Nusantara | Jawa / Melayu | Kafan Chain | Hujan Pocong | `isolde` |
| **KUNTILANAK** — The Waru Wailer | Nusantara | Kalimantan / Melayu | Kuku Panjang | Malam Pohon Waru | `arco` |
| **GENDERUWO** — The Banyan Brute | Nusantara | Jawa | Tinju Rimba | Amuk Beringin | `haldor` |
| **TUYUL** — The Little Pickpocket | Nusantara | Jawa | Gigit Kecil | Pesugihan Kilat | `nib` |
| **KUYANG** — The Midnight Head | Nusantara | Kalimantan | Cakar Malam | Pesta Kuyang | `cora` |
| **LEYAK** — The Night Flame | Nusantara | Bali | Cakar Bara | Malam Pengleakan (wujud celeng) | `fenr` |
| **JIANGSHI** — The Talisman Hopper | Mancanegara | Tiongkok | Telapak Kaku | Jimat Terlepas | `edda` |
| **KUCHISAKE-ONNA** — The Masked Question | Mancanegara | Jepang | Gunting Cepat | Buka Masker | `zanni` |
| **LA LLORONA** — The Weeping River | Mancanegara | Meksiko | Selendang Ratapan | Banjir Ratapan | `naja` |
| **BANSHEE** — The Keening Herald | Mancanegara | Irlandia | Tangan Kabut | Keening | `solan` |
| **BLOODY MARY** — The Mirror Witch | Mancanegara | Inggris / AS | Pecahan Kaca | Cermin Seribu | `rhea` |
| **DULLAHAN** — The Headless Rider | Mancanegara | Irlandia | Cambuk Rantai | Kereta Maut | `mira` |

Arenas: **Rumah Kosong**, **Pabrik Gula Tua**, **Makam Kamboja**, **Hutan Larangan** and **Candi Purnama** (background art still to be generated, see [guide/ghost-stages.md](guide/ghost-stages.md)).

Every ghost has a 3-hit basic chain, two skills and an ultimate with a full-screen cut-in. Modes: VS Computer (best of 3, four CPU levels) and Training.

## 🎮 Controls

### Keyboard

| Key | Action |
| --- | --- |
| `A` / `D` | Move left / right |
| Double-tap `A` / `D` and hold | Run |
| `W` | Jump (press again in the air to double jump) |
| `S` | Crouch on the ground, fast fall in the air; double-tap for a somersault double jump |
| `Space` | Basic attack (tap up to 3 times for the full chain) |
| `I` | Skill 1 |
| `O` | Skill 2 |
| `P` | Ultimate |
| `Esc` | Pause / resume |
| `R` | Restart (the round in Training, the match in VS Computer) |

Skills cancel a basic attack at any moment. The ultimate pose locks you for only 0.5 s; the summon then finishes on its own while you keep fighting.

In the menus: `W A S D` / arrow keys to select, `Enter` to confirm, `Esc` to go back.

### Touch (phones and tablets)

- **Left**: ◀ ▼ ▶ with ▲ above ▼. Slide your finger between buttons; double-tap ◀/▶ to run, tap ▲ again in the air to double jump.
- **Right**: a big **Basic Attack** button with **Skill 1 / Skill 2 / Ultimate** around it, showing each fighter's icons and cooldowns.
- Phones open `mobile.html` automatically in landscape. Add `?touch=1` to force the mobile layout on desktop, or `?touch=0` to turn it off.

## 🚀 Getting started

The game is a set of static files, so there is nothing to install or build.

```bash
git clone https://github.com/fsyahangga/GhostClash.git
cd GhostClash

# any static file server works, for example:
python -m http.server 8000
# or
npx serve .
```

Then open <http://localhost:8000/>.

> [!TIP]
> Serve the folder over `http://localhost` or HTTPS to get the loading screen and the service-worker cache. Opening `index.html` straight from disk (`file://`) still plays, just without caching.

**Browser support:** current Chrome, Edge, Firefox and Safari (desktop and mobile). Audio starts after the first click or tap, because browsers require a user gesture.

## 🌐 Deployment

Upload the folder to any static host (nginx, Apache, LiteSpeed, Caddy, GitHub Pages, Netlify and so on). All paths are relative, so it works at a domain root or in a subfolder such as `https://example.com/ghostclash/`.

Server checklist:

- Open the game **with the trailing slash** (`/ghostclash/`) and redirect `/ghostclash` to it.
- Serve `.js` as JavaScript, `.webp` as `image/webp`, `.mp3` as `audio/mpeg`, `.mp4` as `video/mp4` and `.ttf` as `font/ttf`.
- Send `Cache-Control: no-cache` for the game files. The game keeps its own hashed copies in Cache Storage, so updates show up immediately.
- Serve MP3/MP4 files with range requests (the default for static files) and without gzip.

Step-by-step instructions for nginx, Apache/LiteSpeed and Caddy, plus a script that checks every file after upload, are in **[DEPLOY.md](DEPLOY.md)**. An `.htaccess` for Apache/LiteSpeed is included.

## 🗂️ Project structure

```text
.
├── index.html        # desktop entry: menu, HUD, dialogs, script order
├── mobile.html       # landscape shell for phones (rotation, fullscreen)
├── style.css         # arena HUD, cut-ins, touch controls
├── menu.css          # main menu, character and arena select, results
├── game.js           # engine: loop, physics, combat, CPU brain, summons, rendering, HUD
├── menu.js           # front end: menu flow, roster, arena and difficulty select
├── match.js          # match rules: rounds, timer, stages, difficulty tuning
├── announcer.js      # announcer voice queue
├── touch.js          # on-screen touch controls
├── fenr.js … edda.js # one kit file per engine slot (moves, balance, timings)
├── ghosts.js         # GHOST CLASH roster: which ghost plays each slot, names, faction, skill names, cut-in text
├── preload.js        # first-visit loading screen, fills the cache
├── precache.js       # generated list of runtime files with sizes and hashes
├── sw.js             # service worker: cache-first images, network-first code
├── files.json        # file list with sizes (used by the deploy check)
├── LICENSE           # MIT (source code)
├── LICENSE-ASSETS.md # CC BY-NC 4.0 (art, audio, guides) and exceptions
├── guide/            # design and production guides (Bahasa Indonesia)
├── docs/screenshots/ # images for this README
└── assets/
    ├── <fighter>/    # sprite atlas (WebP) + manifest.js, portrait, icons, cut-in, FX, voice
    ├── audio/        # announcer clips and background music
    ├── menu/         # menu art, arena backgrounds, character select art
    ├── ui/           # shared HUD art (ARCO kit, drone, cut-in)
    └── fonts/        # Rajdhani (SIL Open Font License)
```

## 📚 Guides

The [`guide/`](guide/) folder holds the design and production notes behind the game (in Bahasa Indonesia). Start from [guide/README.md](guide/README.md).

| Topic | Guide |
| --- | --- |
| **Ghost roster, slot mapping and asset swap** | [ghost-roster.md](guide/ghost-roster.md) |
| **Image prompts for all 12 ghosts** | [ghost-prompts.md](guide/ghost-prompts.md) |
| **Five haunted arenas and their background prompts** | [ghost-stages.md](guide/ghost-stages.md) |
| Adding a new fighter, step by step | [character-workflow.md](guide/character-workflow.md) |
| Shared gameplay rules (movement, combos, HP, cooldowns) | [gameplay-standard.md](guide/gameplay-standard.md) |
| Sprite prompts, pipeline, QA and known issues | [sprite-prompts.md](guide/sprite-prompts.md), [sprite-pipeline.md](guide/sprite-pipeline.md), [sprite-qa.md](guide/sprite-qa.md), [sprite-known-issues.md](guide/sprite-known-issues.md) |
| CPU brain and difficulty benchmark | [cpu-ai.md](guide/cpu-ai.md) |
| Menu flow and match rules | [main-menu.md](guide/main-menu.md) |
| Announcer and ultimate voices | [announcer-system.md](guide/announcer-system.md), [ultimate-voice.md](guide/ultimate-voice.md) |
| Arena backgrounds and menu video | [stage-background.md](guide/stage-background.md), [menu-video.md](guide/menu-video.md) |
| One reference per fighter (kit, balance, assets, voice) | [arco](guide/arco-reference.md) · [fenr](guide/fenr-reference.md) · [mira](guide/mira-reference.md) · [cora](guide/cora-reference.md) · [naja](guide/naja-reference.md) · [haldor](guide/haldor-reference.md) · [zanni](guide/zanni-reference.md) · [isolde](guide/isolde-reference.md) · [rhea](guide/rhea-reference.md) · [solan](guide/solan-reference.md) · [nib](guide/nib-reference.md) · [edda](guide/edda-reference.md) |

The guides also mention the full production workspace (raw generation sources, pipeline tools, sprite lab pages). Those are several GB and are not part of this repository.

## 🔧 How it works

- **Fixed-step simulation.** The game advances in 1/120 s steps with a seeded random generator, so combat plays the same way on every machine.
- **Sprites.** Each fighter is a WebP sprite atlas (idle, walk, run, jump, crouch, three attacks, two skills, ultimate, hurt, down and recover) with a manifest of frames, foot anchors and measured hit points. Sprites are drawn pixel-exact, never rescaled at runtime.
- **Kits.** The rules for each fighter (damage, reach, cooldowns, projectile and summon behaviour) live in their own small file. The player and the CPU use exactly the same kit.
- **CPU brain.** The CPU reacts with a human-like delay: it jumps projectiles, backs out of attacks, punishes recovery, anti-airs and confirms combos. Each difficulty level changes reaction time, aggression and mistakes.
- **Loading.** `precache.js` lists every runtime file with a content hash. `preload.js` downloads them into Cache Storage behind the loading screen, and `sw.js` serves images and fonts from there. On later visits only files whose hash changed are downloaded again.

## 🙏 Credits

- **Ghost roster and GHOST CLASH adaptation**: [fsyahangga](https://github.com/fsyahangga)
- **Original game, engine, code and current art/audio**: [Aether Clash](https://github.com/bangtutorial/aether-clash) by [Bang Tutorial](https://www.youtube.com/watch?v=UN_0bNC2wTU) — visuals generated with Higgsfield (GPT Image), voices and announcer with ElevenLabs via Higgsfield, background music "Midday Showdown" made with Suno
- **Typography**: [Rajdhani](https://fonts.google.com/specimen/Rajdhani) by Indian Type Foundry, under the SIL Open Font License (see `assets/fonts/OFL.txt`)

## 📄 License

- **Source code** (HTML, CSS, JavaScript) is released under the [MIT License](LICENSE).
- **Assets** (characters, sprites, artwork, effects, video, voices, background music, screenshots and the `guide/` documents) are released under [CC BY-NC 4.0](LICENSE-ASSETS.md): free to share and adapt with credit, but not for commercial use.
- **Exception**: the Rajdhani font keeps the [SIL Open Font License](assets/fonts/OFL.txt). See [LICENSE-ASSETS.md](LICENSE-ASSETS.md).

<div align="center">

If you enjoyed the project, give it a ⭐ and check out the [tutorial on YouTube](https://www.youtube.com/watch?v=UN_0bNC2wTU)!

</div>
