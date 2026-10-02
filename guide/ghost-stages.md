# Arena PERANG DEDEMIT

Lima arena malam bertema tempat angker Nusantara. Gambar sumber (1672×941) ada di `assets/ghosts/arena/`; versi game 1280×720 menimpa file slot lama, dan nama, tagline, waktu, serta `groundY` ada di [match.js](../match.js).

| Arena | ID slot | Sumber | File game | groundY | Tagline | Waktu |
| --- | --- | --- | --- | --- | --- | --- |
| Rumah Kosong | `bellora` | `arena/rumah.webp` | `assets/stage.webp` | 600 | Pendopo tua yang lampunya tak pernah padam | Malam Jumat Kliwon |
| Pabrik Gula Tua | `sunspire` | `arena/pabrik.webp` | `assets/menu/sunspire.webp` | 600 | Mesinnya berhenti, giling tetap berbunyi | Tengah malam |
| Makam Kamboja | `harbor` | `arena/makam.webp` | `assets/menu/azure-harbor.webp` | 600 | Bunga kamboja jatuh tanpa angin | Bulan purnama |
| Hutan Larangan | `elderwood` | `arena/hutan.webp` | `assets/menu/elderwood.webp` | 600 | Jangan bersiul di bawah beringin | Malam berkabut |
| Kawah Akar Geni | `moonrise` | `arena/kawah.webp` | `assets/menu/moonrise.webp` | 572 | Akar tua menyimpan bara gunung | Bulan sabit |

`groundY` diukur dari pita lantai tiap gambar di ukuran 1280×720 (garis kaki petarung). Kawah Akar Geni lebih tinggi karena di bawah pita tanahnya ada akar. Key art menu utama (`assets/menu/home-dedemit.webp`) memakai Makam Kamboja dengan barisan dedemit di depannya.

Mengganti satu arena: skala gambar baru ke 1280×720 (resample BOX), simpan sebagai WebP dengan nama file di tabel, ukur garis lantainya (skrip di [stage-background.md](stage-background.md)), isi `groundY` di match.js, lalu jalankan `node guide/tools/update_precache.mjs`.

Prompt di bawah adalah prompt awal untuk empat arena pertama; Candi Purnama sudah diganti Kawah Akar Geni.

## Aturan umum

- Model Seedream 5.0 Pro (`seedream_v5_pro`), rasio 16:9, 2k, `count: 2`. Lampirkan base salah satu hantu sebagai referensi gaya saja.
- Semua arena malam, tetapi **lantai harus terang** (cahaya bulan, lampu minyak, obor, petromaks) supaya sprite tetap terbaca. Langit dan latar jauh boleh gelap.
- Tengah layar kosong. Landmark di sepertiga kiri atau kanan.
- Tidak ada hantu, sosok, atau wajah di latar. Hantu hanya dari sprite petarung, supaya pemain tidak bingung membaca siapa lawannya.
- Hindari simbol agama yang spesifik dan sakral (kain poleng, arca dewa utuh, tulisan ayat). Nisan polos dan candi reruntuhan sudah cukup memberi suasana.

Setelah memilih varian:

1. Skala ke 1280×720 dengan resample BOX, simpan sebagai WebP dengan nama file di tabel.
2. Ukur pita lantai dengan skrip di stage-background.md, ganti rumus warna sesuai material lantai (kayu, ubin, tanah, batu). Isi `groundY` arena itu di match.js.
3. Jalankan `node guide/tools/update_precache.mjs`.

## 1. Rumah Kosong (`bellora`)

```text
Reference image is a STYLE reference only (a sprite from the same game): match its art style, color richness and shading. Do NOT draw the character or any character.

Create ONE complete, single-screen background for a 2D side-view FIGHTING GAME stage, a haunted night on a Friday in rural Java, in one coherent image (not layers). Composition from top to bottom: a dark indigo sky with a pale full moon partly behind thin clouds; in the background an abandoned Dutch colonial mansion with tall white columns, peeling plaster, broken wooden shutters and tall dark windows, one window faintly lit by an oil lamp, placed on the LEFT third; old mango and frangipani trees on the right third; then an overgrown front yard. The bottom 30% of the image is the fighting floor seen from the side at a slightly elevated angle: a wide horizontal band of cracked old patterned Dutch floor tiles (tegel kunci, faded grey and ochre) running across the entire width (centered at about 80% of the image height), lit softly by moonlight and two hanging oil lamps on the porch, with dry leaves and scattered dust, bordered by low weeds in front and the porch steps behind. The floor is flat and level, NOT a cross-section, no underground layers. Keep the middle of the image open and uncluttered for gameplay, nothing large in the foreground. No characters, no ghosts, no faces, no animals, no text, no UI, no border.
```

## 2. Pabrik Gula Tua (`sunspire`)

```text
Reference image is a STYLE reference only (a sprite from the same game): match its art style, color richness and shading. Do NOT draw the character or any character.

Create ONE complete, single-screen background for a 2D side-view FIGHTING GAME stage, midnight at an abandoned colonial-era sugar factory in Java, in one coherent image (not layers). Composition from top to bottom: a dark teal night sky with drifting low clouds; a tall red-brick chimney with rusted iron bands on the RIGHT third, and the factory hall with broken arched windows, rusty steel trusses and a giant still flywheel on the LEFT third; a few old sugarcane lorry wagons on narrow rails at the far back; dry sugarcane stalks along the edges. The bottom 30% of the image is the fighting floor seen from the side at a slightly elevated angle: a wide horizontal band of worn grey concrete with embedded narrow-gauge rails running across the entire width (centered at about 80% of the image height), lit by two flickering industrial lamps and moonlight, with scattered sugarcane husks, rust stains and puddles reflecting the light. The floor is flat and level, NOT a cross-section, no underground layers. Keep the middle of the image open and uncluttered for gameplay, nothing large in the foreground. No characters, no ghosts, no faces, no animals, no text, no UI, no border.
```

## 3. Makam Kamboja (`harbor`)

```text
Reference image is a STYLE reference only (a sprite from the same game): match its art style, color richness and shading. Do NOT draw the character or any character.

Create ONE complete, single-screen background for a 2D side-view FIGHTING GAME stage, an old village cemetery in Indonesia at dusk turning to night, thin white fog over the ground, in one coherent image (not layers). Composition from top to bottom: a deep violet-to-orange twilight sky fading into night, first stars appearing; silhouettes of tall bamboo and coconut palms far behind; rows of simple weathered stone and wooden grave markers on low mounds, small plain whitewashed tomb walls, and a big frangipani (kamboja) tree dropping white-yellow flowers on the LEFT third; a small old roofed gate (gapura) on the RIGHT third. The bottom 30% of the image is the fighting floor seen from the side at a slightly elevated angle: a wide horizontal band of packed reddish-brown earth path running across the entire width (centered at about 80% of the image height), lit by a row of small oil lanterns on bamboo poles and soft moonlight, with fallen frangipani flowers and dry leaves, bordered by short grass in front and the grave mounds behind. The floor is flat and level, NOT a cross-section, no underground layers. Keep the middle of the image open and uncluttered for gameplay, nothing large in the foreground. No characters, no ghosts, no faces, no animals, no text, no religious inscriptions, no UI, no border.
```

## 4. Hutan Larangan (`elderwood`)

```text
Reference image is a STYLE reference only (a sprite from the same game): match its art style, color richness and shading. Do NOT draw the character or any character.

Create ONE complete, single-screen background for a 2D side-view FIGHTING GAME stage, a forbidden tropical rainforest in Java on a misty night, in one coherent image (not layers). Composition from top to bottom: a dark green-black canopy with small gaps showing a cold moon; giant buttress-root trees and hanging lianas in the background; a huge ancient banyan tree (beringin) with curtains of aerial roots, with a faded plain white cloth tied around its trunk and a small woven tray of flowers at its base, placed on the RIGHT third; a mossy stone shrine and wild ferns on the LEFT third; drifting fog and a few green fireflies. The bottom 30% of the image is the fighting floor seen from the side at a slightly elevated angle: a wide horizontal band of flat damp forest clearing with dark brown earth and flat moss-covered stones running across the entire width (centered at about 80% of the image height), lit by pale moonbeams through the canopy and two small torches, with fallen leaves and roots kept flat into the ground, bordered by ferns in front and tree roots behind. The floor is flat and level, NOT a cross-section, no underground layers. Keep the middle of the image open and uncluttered for gameplay, nothing large in the foreground. No characters, no ghosts, no faces, no animals, no text, no UI, no border.
```

## 5. Candi Purnama (`moonrise`)

```text
Reference image is a STYLE reference only (a sprite from the same game): match its art style, color richness and shading. Do NOT draw the character or any character.

Create ONE complete, single-screen background for a 2D side-view FIGHTING GAME stage, the ruins of a forgotten Hindu-Buddhist temple in the Indonesian jungle under a huge full moon, in one coherent image (not layers). Composition from top to bottom: a deep blue night sky with a giant glowing full moon and faint clouds; distant volcano silhouette; a crumbling dark andesite stone temple with a stepped roof and carved panels (plain abstract relief patterns, no statues of deities), overgrown with vines, on the LEFT third; a split gate (candi bentar) ruin on the RIGHT third; frangipani and jungle trees around. The bottom 30% of the image is the fighting floor seen from the side at a slightly elevated angle: a wide horizontal band of large flat grey andesite paving stones with moss in the cracks running across the entire width (centered at about 80% of the image height), brightly lit by silver moonlight and a few small oil lamps, with fallen flower petals, bordered by low jungle plants in front and broken stone steps behind. The floor is flat and level, NOT a cross-section, no underground layers. Keep the middle of the image open and uncluttered for gameplay, nothing large in the foreground. No characters, no ghosts, no faces, no animals, no text, no UI, no border.
```

## Thumbnail menu

Pemilih arena memakai gambar latar yang sama sebagai thumbnail, jadi tidak perlu gambar terpisah. Kalau poster menu utama (`assets/menu/home-factions.webp` dan videonya) ikut diganti, pakai dua panji faksi: panji Nusantara dengan motif kain kafan dan bunga melati, panji Mancanegara dengan motif jimat kuning dan cermin, berlatar Rumah Kosong.
