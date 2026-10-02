# Roster PERANG DEDEMIT

PERANG DEDEMIT memakai engine Aether Clash. Dua belas slot kit lama (`arco`, `fenr`, `mira`, …) tetap menjadi ID internal, dan setiap slot dimainkan oleh satu dedemit Nusantara yang legendanya paling cocok dengan gerakan slot itu. Nama, golongan, julukan, nama jurus, teks cut-in, status HUD, dan teks legenda di Kitab Dedemit semuanya ada di [ghosts.js](../ghosts.js). Damage, jangkauan, cooldown, dan CPU tidak diubah; satu-satunya mekanik baru adalah tali Pocong yang mengikat lawan.

Arena ada di [ghost-stages.md](ghost-stages.md). Prompt gambar lama ada di [ghost-prompts.md](ghost-prompts.md).

## Dua golongan

- **Makhluk Halus**: arwah penasaran dan penunggu tempat angker.
- **Ilmu Hitam**: manusia penganut ilmu hitam yang melepas kepalanya di malam hari, dan makhluk peliharaan yang dikirim untuk mencuri atau mencelakai.

## Pemetaan slot dan jurus

Urutan tabel sama dengan urutan grid pilih karakter dan Kitab Dedemit.

| Dedemit | Golongan | Slot | Spasi | I | O | P (ultimate) |
| --- | --- | --- | --- | --- | --- | --- |
| Pocong | Makhluk Halus | `isolde` | Sundulan Kafan: tiga sundulan berjangkauan panjang | Tali Pocong: tali dilempar naik, lawan terikat diam 0,7 s | Lompat Pocong: lompatan menerjang | Hujan Pocong: tiga pocong jatuh dari langit |
| Kuntilanak | Makhluk Halus | `arco` | Cakar Kuku | Tawa Melengking: gelombang tawa lurus | Jatuh dari Waru: hantaman area | Malam Pohon Waru: arwah menyambar dari udara |
| Sundel Bolong | Makhluk Halus | `edda` | Cakar Dendam | Arwah Memantul: bola arwah memantul dua kali | Balas Dendam: bertahan 0,55 s, serangan pertama dibalas | Dendam Kesumat: arwah raksasa menghentak tiga kali |
| Wewe Gombel | Makhluk Halus | `zanni` | Tangan Panjang | Selendang Melayang: terbang lalu kembali | Gondol!: lawan diseret mendekat | Sarang Aren: tiga pusaran selendang |
| Genderuwo | Makhluk Halus | `haldor` | Tinju Rimba: rantai paling berat | Lempar Batu Gaib: batu melambung | Seruduk Rimba | Amuk Beringin: tiga hantaman tanah |
| Eyang Sukmo Capo | Makhluk Halus | `solan` | Tongkat Pusaka | Gelombang Sukma: tenaga dalam setinggi dada | Hentak Bumi: lompat lalu menghentak | Sabda Keramat: tiga gelombang |
| Leyak | Ilmu Hitam | `fenr` | Cakar Bara | Api Leyak: bola api | Terjang Malam | Malam Pengleakan: wujud api 12 s (Cakar Geni, Terkam Geni, Pekik Malam) |
| Kuyang | Ilmu Hitam | `cora` | Cakar Malam | Pita Arwah: kipas tiga proyektil | Kibas Rambut | Pesta Kuyang: kawanan kepala terbang |
| Palasik | Ilmu Hitam | `rhea` | Gigit Melayang | Kepala Mengambang: proyektil lambat | Isap Sari: pusaran isap 230 px di depan | Tiga Kepala: tiga kepala mengorbit |
| Tuyul | Ilmu Hitam | `nib` | Gigit Kecil: rantai tercepat | Lempar Koin: koin kepeng tercepat | Copet Kilat: dash, menyelinap ke belakang lawan | Pesugihan Kilat: tiga karung koin pengejar |
| Jenglot | Ilmu Hitam | `mira` | Cakar Jenglot | Kuku Terbang | Terkam Jenglot: terkaman | Hujan Jenglot: dua belas jenglot berjatuhan |
| Begu Ganjang | Ilmu Hitam | `naja` | Tangan Ganjang: jangkauan terpanjang | Bayang Merayap: gelombang di tanah | Putaran Ganjang: depan dan belakang | Begu Menjulang: bayangan mengejar, menjulang tiga kali |

Angka umum: basic 6/8/12, Skill 1 16 dmg CD 3 s, Skill 2 24 dmg CD 6 s; ultimate sesuai `<slot>-reference.md`.

## Tali Pocong (mekanik baru)

Proyektil yang punya properti `bind` (detik) mengikat targetnya: pemain mendapat tambahan `hurtTime`, CPU ditahan oleh `bindTime`, keduanya berhenti bergeser, dan tiga lilitan tali digambar mengikuti target. Nilainya `piercer.bind` di [isolde.js](../isolde.js) (0,7 s); kodenya `bindHit` di game.js. Jurus lain bisa memakai mekanik yang sama dengan menambahkan `bind` pada proyektilnya.

## Gambar base dan aset sementara

Gambar base tiap dedemit (satu pose penuh, hadap kanan, latar magenta atau hijau polos) ada di `assets/ghosts/base/<dedemit>.webp`. Gambar hantu mancanegara yang tidak dipakai lagi disimpan di `assets/ghosts/base/_arsip/`. Dari gambar base, [build_ghost_assets.py](tools/build_ghost_assets.py) membuat untuk slotnya:

- atlas sprite dengan tata letak slot lama; setiap state adalah pose base yang ditekan, dicondongkan, digeser, atau diputar;
- metrics bounds/tinggi dari frame baru (emitter dan playback tetap);
- portrait HUD, art pilih karakter, cut-in ultimate, dan empat ikon jurus;
- efek: bentuk generik diwarnai ulang dengan warna dedemit (dari salinan asli di `assets/ghosts/fx-src`), objek khas diganti dengan sosok dedemit itu sendiri, koin kepeng, tali pocong, atau bola arwah.

Ukuran tiap dedemit diatur dengan `scale` (Jenglot kecil, Begu Ganjang menjulang) dan `lift` (Palasik melayang) di tabel `GHOSTS` dalam skrip itu; crop portrait dengan `portrait=[cx, cy, ukuran]`.

Membangun ulang satu dedemit (butuh Python dengan Pillow dan numpy, serta Node.js):

    python guide/tools/build_ghost_assets.py pocong
    node guide/tools/update_precache.mjs

Yang masih bawaan Aether Clash: suara (announcer dan voice ultimate dimatikan untuk semua dedemit sampai ada rekaman baru; set `voice: true` di ghosts.js setelah file suaranya ditimpa).
