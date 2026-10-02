# Strip animasi dedemit

Taruh sprite strip (4 pose dalam satu baris, latar magenta atau hijau polos) di sini, satu folder per dedemit dengan nama yang sama dengan file base:

    assets/ghosts/strips/pocong/idle.png
    assets/ghosts/strips/pocong/walk.png
    assets/ghosts/strips/pocong/attack.png
    ...

Prompt dan langkahnya ada di [guide/ghost-animation-prompts.md](../../../guide/ghost-animation-prompts.md). Setelah menambah strip, jalankan `python guide/tools/build_ghost_assets.py <dedemit>` lalu `node guide/tools/update_precache.mjs`.
