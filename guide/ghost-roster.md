# Roster GHOST CLASH

GHOST CLASH memakai engine Aether Clash apa adanya. Dua belas slot kit lama (`arco`, `fenr`, `mira`, …) tetap menjadi ID internal, dan setiap slot sekarang dimainkan oleh satu hantu yang legendanya paling cocok dengan gerakan slot itu. Semua nama, faksi, judul, nama skill, teks cut-in, dan status HUD berasal dari [ghosts.js](../ghosts.js). Damage, jangkauan, cooldown, dan CPU tidak diubah, jadi balance hasil benchmark lama tetap berlaku.

Prompt gambar untuk setiap hantu ada di [ghost-prompts.md](ghost-prompts.md). Aturan pipeline sprite tetap mengikuti [character-workflow.md](character-workflow.md), [sprite-prompts.md](sprite-prompts.md), dan [sprite-qa.md](sprite-qa.md).

## Pemetaan slot

Urutan tabel sama dengan urutan grid pilih karakter: enam Nusantara di atas, enam Mancanegara di bawah.

| Hantu | Faksi | Asal | Slot engine | Alasan pemetaan |
| --- | --- | --- | --- | --- |
| POCONG — The Shroud Hopper | Nusantara | Jawa / Melayu | `isolde` | Serbuan lurus jadi lompatan; ultimate tiga tombak dari langit jadi tiga pocong jatuh |
| KUNTILANAK — The Waru Wailer | Nusantara | Kalimantan / Melayu | `arco` | Proyektil jadi tawa melengking; summon dari udara jadi arwah pohon waru |
| GENDERUWO — The Banyan Brute | Nusantara | Jawa | `haldor` | Lemparan melambung = lempar batu; tiga hantaman tanah = amuk beringin |
| TUYUL — The Little Pickpocket | Nusantara | Jawa | `nib` | Rantai tercepat dan dash yang menyelinap ke belakang lawan = copet kilat |
| KUYANG — The Midnight Head | Nusantara | Kalimantan | `cora` | Tiga sapuan kawanan gagak jadi kawanan kepala terbang |
| LEYAK — The Night Flame | Nusantara | Bali | `fenr` | Transformasi serigala jadi wujud celeng (babi hutan) |
| JIANGSHI — The Talisman Hopper | Mancanegara | Tiongkok | `edda` | Counter guard jadi perisai jimat; roh kura-kura yang menghentak jadi jiangshi raksasa yang melompat |
| KUCHISAKE-ONNA — The Masked Question | Mancanegara | Jepang | `zanni` | Lengan gunting, cincin bumerang, dan tarikan dekat |
| LA LLORONA — The Weeping River | Mancanegara | Meksiko | `naja` | Cambuk panjang = selendang; gelombang tanah dan ular pasir jadi arus sungai |
| BANSHEE — The Keening Herald | Mancanegara | Irlandia | `solan` | Gelombang bulan sabit dan tiga auman jadi ratapan |
| BLOODY MARY — The Mirror Witch | Mancanegara | Inggris / AS | `rhea` | Planet melayang dan tiga planet mengorbit jadi cermin |
| DULLAHAN — The Headless Rider | Mancanegara | Irlandia | `mira` | Petarung berat dengan tembakan lurus, tackle, dan hujan proyektil |

## Kit yang berjalan di game

Ini perilaku nyata di game sekarang, diturunkan dari slot engine. Angka damage/cooldown: basic 6/8/12, Skill 1 16 dmg CD 3 s, Skill 2 24 dmg CD 6 s, ultimate sesuai slot (lihat `<slot>-reference.md`).

| Hantu | Space (basic) | I (Skill 1) | O (Skill 2) | P (Ultimate) |
| --- | --- | --- | --- | --- |
| POCONG | KAFAN CHAIN: tiga tusukan jarak panjang | TALI KAFAN: proyektil naik, anti-air | LOMPAT POCONG: serbuan cepat 560 px/s | HUJAN POCONG: tiga hantaman dari langit |
| KUNTILANAK | KUKU PANJANG | TAWA MELENGKING: proyektil lurus | JATUH DARI WARU: hantaman ke tanah | MALAM POHON WARU: summon dari udara |
| GENDERUWO | TINJU RIMBA: rantai paling berat | LEMPAR BATU GAIB: batu melambung ke posisi lawan | SERUDUK RIMBA: serudukan bahu | AMUK BERINGIN: tiga hantaman di depan |
| TUYUL | GIGIT KECIL: rantai tercepat | LEMPAR KOIN: lemparan datar tercepat | COPET KILAT: dash, bila kena menyelinap ke belakang lawan | PESUGIHAN KILAT: tiga proyektil pengejar |
| KUYANG | CAKAR MALAM | PITA ARWAH: kipas tiga proyektil | SAPUAN MALAM: sapuan angin | PESTA KUYANG: tiga lintasan kawanan |
| LEYAK | CAKAR BARA | API LEYAK: proyektil | TERJANG MALAM: lunge | MALAM PENGLEAKAN: wujud celeng 12 s (TARING CELENG / TERKAM CELENG / LOLONG MALAM) |
| JIANGSHI | TELAPAK KAKU | JIMAT MELOMPAT: memantul dua kali di tanah | PERISAI JIMAT: guard 0.55 s, hit pertama dibalas | JIMAT TERLEPAS: tiga hentakan berjalan |
| KUCHISAKE-ONNA | GUNTING CEPAT | GUNTING BUMERANG: pergi lalu pulang | WATASHI, KIREI?: tarik lawan mendekat | BUKA MASKER: tiga gunting raksasa bumerang |
| LA LLORONA | SELENDANG RATAPAN: jangkauan terjauh | AIR MATA SUNGAI: gelombang di tanah | PUSARAN SUNGAI: putaran depan-belakang | BANJIR RATAPAN: arus mengejar lalu tiga semburan |
| BANSHEE | TANGAN KABUT | RATAPAN: gelombang setinggi dada | TERKAM KABUT: lompat lalu hantam lantai | KEENING: tiga gelombang ratapan |
| BLOODY MARY | PECAHAN KACA | CERMIN MELAYANG: proyektil lambat 3.2 s | PANGGIL TIGA KALI: pusaran 230 px di depan | CERMIN SERIBU: tiga objek mengorbit |
| DULLAHAN | CAMBUK RANTAI | TATAPAN KEPALA: proyektil lurus | TERJANG KSATRIA: tackle | KERETA MAUT: 12 proyektil jatuh |

Skill khas dari dokumen konsep yang belum ada di engine (teleport Kuntilanak, hisap HP Kuyang, curi bar ultimate Tuyul, klon Bloody Mary, tanda Dullahan, ikat Pocong) butuh kode baru di `game.js` dan kit file slotnya. Kerjakan satu per satu setelah sprite hantunya jadi.

## Mengganti aset sebuah slot

Cara paling aman: timpa file slot dengan nama yang sama, ukuran yang sama, dan format yang sama. Kode tidak perlu diubah.

| Jenis | File yang ditimpa | Catatan |
| --- | --- | --- |
| Sprite atlas | `assets/<slot>/run/sprite-sheet-alpha.webp` + `assets/<slot>/manifest.js` | Hasil pipeline lengkap (14 state / 50 frame). ARCO: `assets/mecha/`. FENR: `assets/fenr/human/` dan `assets/fenr/wolf/` |
| Portrait HUD | `assets/<slot>/ui/portrait.webp` (384×384) | ARCO: `assets/ui/arco-avatar.webp`. FENR: `portrait-human.webp` dan `portrait-wolf.webp` |
| Cut-in ultimate | `assets/<slot>/ui/cutin.webp` (1600×686) | ARCO: `assets/ui/ultimate-cutin.webp` |
| Ikon skill | `assets/<slot>/ui/icon-basic/skill1/skill2/ultimate.webp` (256×256) | ARCO: `assets/ui/attack, skill1, skill2, squadron-icon.webp`. FENR: `icon-human-*`, `icon-wolf-*`, `icon-ultimate` |
| Art pilih karakter | `assets/menu/<slot>-select.webp` | Ukur dari file lama |
| VFX | `assets/<slot>/ui/fx-*.webp` (PNG alpha 256) | Daftar per slot di bawah |
| Suara | `assets/audio/announcer/select_<slot>.mp3`, `<slot>_wins.mp3`, voice ultimate di `assets/<slot>/audio/` | Lalu set `voice: true` untuk hantu itu di ghosts.js |

VFX per slot dan penggantinya:

| Hantu (slot) | File fx lama → isi baru |
| --- | --- |
| POCONG (`isolde`) | piercer → simpul tali kafan · skyfall → pocong jatuh · shatter → debu kafan · frost → jejak kain |
| KUNTILANAK (`arco`) | `assets/ui/drone.png` → kepala kuntilanak melayang |
| GENDERUWO (`haldor`) | slag → batu gaib · splash → pecahan kerikil · steam → debu rimba · quake → akar beringin pecah |
| TUYUL (`nib`) | letter → koin emas · plane → karung koin terbang · slip → kilatan copet · stamp → cap koin |
| KUYANG (`cora`) | feather → pita arwah merah · gust → sapuan rambut · raven → kepala kuyang terbang |
| LEYAK (`fenr`) | claw → cakar bara · gale → bola api leyak · rush → jejak api · bite → taring celeng · howl → gelombang api · transform → kobaran berubah wujud |
| JIANGSHI (`edda`) | stone → jimat kuning · ripple → riak qi · shell → kubah jimat · tortoise → jiangshi raksasa · stomp → hentakan tanah |
| KUCHISAKE-ONNA (`zanni`) | ring → gunting berputar · bigring → gunting raksasa · snatch → kilatan tarikan · confetti → kelopak sakura |
| LA LLORONA (`naja`) | sandwave → gelombang air · cyclone → pusaran air · serpent → tangan sungai · ripple → riak air |
| BANSHEE (`solan`) | crescent → gelombang suara · roar → ratapan besar · impact → hantaman kabut · sunburst → cincin bulan pucat |
| BLOODY MARY (`rhea`) | drift → cermin kecil · planet → cermin raksasa · well → pusaran kaca · burst → pecahan kaca |
| DULLAHAN (`mira`) | star → sinar mata biru · rocket → api arwah jatuh · burst → ledakan api biru · crash → hantaman ksatria |

Setelah mengganti atau menambah file apa pun, jalankan dari root proyek:

    node guide/tools/update_precache.mjs

Skrip itu menulis ulang `precache.js` dan `files.json`, jadi loading screen mengunduh versi baru dan service worker tidak menyajikan gambar lama.

## Menambah atau mengubah teks hantu

Edit entri slotnya di [ghosts.js](../ghosts.js): `name`, `tag`, `title`, `faction`, `detail`, `style`, `color`, `names` (Space, I, O, P), `status`, `cutin`. Leyak punya blok `beast` untuk wujud celeng. Tidak ada tempat lain yang perlu diubah.
