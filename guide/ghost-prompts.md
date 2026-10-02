# Prompt gambar hantu GHOST CLASH

Prompt base, portrait, dan cut-in untuk 12 hantu. Pemetaan slot dan daftar file ada di [ghost-roster.md](ghost-roster.md); template strip animasi dan aturan ukuran ada di [sprite-prompts.md](sprite-prompts.md).

Aturan umum:

- Prompt ditulis dalam bahasa Inggris; model gambar paling patuh dengan bahasa Inggris.
- Base: rasio 1:1, generate 2–4 varian, kunci satu. Jangan lampirkan gambar karakter Aether Clash lama; base hantu ini jadi referensi 1 untuk semua strip, portrait, dan cut-in.
- Chroma magenta #FF00FF, kecuali hantu yang memakai merah (Genderuwo, Kuyang, Leyak, Bloody Mary) memakai hijau #00FF00. Set `--chroma-key` pipeline sesuai.
- Seram tanpa gore: darah dan organ diganti cahaya, pita arwah, atau api.
- Portrait 1:1 384 px, cut-in 21:9 (1600×686), ikon 1:1 256 px. Tanpa teks; judul dibuat HTML.

## 1. POCONG — The Shroud Hopper (slot `isolde`)

Tidak punya kaki: walk/run = siklus lompatan kecil (1 squash, 2 lepas landas, 3 puncak dengan kaki terikat rapat, 4 mendarat squash). Run = lompatan lebih jauh dan rendah, badan condong.

Base:

```text
Create an original ghost fighter from scratch for a 2D side-scrolling fighting game: POCONG, the shrouded hopping ghost of Indonesian folklore.
Game sprite, full-body side view, standing in a relaxed idle pose, facing RIGHT.
Shared art style: fine hi-bit pixel art with clean readable pixel clusters, crisp 1 px dark outline, rich soft shading, cute-creepy anime chibi anatomy about 3 heads tall. NOT chunky low-res blocks, NOT a blurry painting.
Character design: the whole body is wrapped tightly in an off-white burial shroud like a cocoon, no arms or legs visible. The shroud is tied with knotted cloth bands on top of the head, at the neck and at the ankles; the top knot sticks up like two floppy ears. A round pale grey-blue face peeks out of the shroud opening, with dark sunken eye rings, glowing cyan pupils and a small mischievous grin. Frayed cloth edges, faint ash-grey dust smudges, two loose cloth strips fluttering behind.
Silhouette: a tall rounded capsule leaning slightly forward, bound feet together as if about to hop.
Dominant palette: off-white, bone beige, ash grey, cyan eye glow.
The whole body and cloth strips fully visible and uncropped, centered, about 70% of the image height, on an invisible ground line near the bottom.
Do not copy any existing fighting-game character; no mecha parts, no animal ears.
Background: perfectly flat solid pure magenta #FF00FF, no gradient, no floor, no shadow, no text, no border. Do not use any pink, red or purple on the character.
```

Portrait:

```text
Portrait illustration (1:1) of the same character as reference 1: close-up of POCONG's face framed by the shroud opening, wide glowing cyan eyes and a cheeky grin, top knot visible, soft moonlight from the left. Readable in a small HUD frame, same palette, no border, no text.
```

Cut-in:

```text
Ultimate cut-in banner (21:9) of the same character as reference 1: POCONG mid-leap toward the viewer on the LEFT third, shroud strips whipping, dozens of tiny pocong silhouettes falling from a moonlit sky behind. Dynamic diagonal composition, right two-thirds dark empty space for a title. No text, no logo, no gore.
```

## 2. KUNTILANAK — The Waru Wailer (slot `arco`)

Melayang: walk/run = meluncur tanpa langkah (ujung gaun naik-turun, rambut berayun). Run = badan condong, rambut terseret ke belakang.

Base:

```text
Create an original ghost fighter from scratch for a 2D side-scrolling fighting game: KUNTILANAK, the laughing white-gown ghost woman of Indonesian and Malay folklore.
Game sprite, full-body side view, floating in a relaxed idle pose, facing RIGHT.
Shared art style: fine hi-bit pixel art with clean readable pixel clusters, crisp 1 px dark outline, rich soft shading, cute-creepy anime chibi anatomy about 3 heads tall. NOT chunky low-res blocks, NOT a blurry painting.
Character design: a slender ghost woman in a long flowing off-white gown with a tattered hem that hides her feet. Extremely long straight jet-black hair reaching the ground, a few strands falling over one side of her face. Pale ashen-blue skin, long dark fingernails, large dark eyes with tiny glowing white pupils, a wide eerie smile. A small white waru flower tucked in her hair.
Silhouette: a tall narrow column with a heavy curtain of hair trailing behind, arms hanging loosely with clawed hands forward, hem hovering just above the ground line.
Dominant palette: off-white, ash grey, jet black, pale blue skin glow.
The whole body and all the hair fully visible and uncropped, centered, about 70% of the image height, on an invisible ground line near the bottom.
Do not copy any existing fighting-game character; no mecha parts, no animal ears.
Background: perfectly flat solid pure magenta #FF00FF, no gradient, no floor, no shadow, no text, no border. Do not use any pink, red or purple on the character.
```

Portrait:

```text
Portrait illustration (1:1) of the same character as reference 1: KUNTILANAK with head tilted, long black hair covering half her face, one glowing eye visible, giggling behind a clawed hand. Cold pale lighting. Readable in a small HUD frame, same palette, no border, no text.
```

Cut-in:

```text
Ultimate cut-in banner (21:9) of the same character as reference 1: KUNTILANAK hanging upside down from a twisted waru tree branch on the LEFT third, hair cascading toward the ground, laughing, full moon behind. Dynamic diagonal composition, right two-thirds dark empty space for a title. No text, no logo, no gore.
```

## 3. GENDERUWO — The Banyan Brute (slot `haldor`)

Jalan berat seperti gorila: buku jari kadang menyentuh tanah saat run.

Base:

```text
Create an original ghost fighter from scratch for a 2D side-scrolling fighting game: GENDERUWO, the giant hairy forest spirit of Javanese folklore.
Game sprite, full-body side view, standing in a relaxed idle pose, facing RIGHT.
Shared art style: fine hi-bit pixel art with clean readable pixel clusters, crisp 1 px dark outline, rich soft shading, cute-creepy anime chibi anatomy, bulkier than a normal chibi. NOT chunky low-res blocks, NOT a blurry painting.
Character design: a huge hulking ape-like spirit covered in thick shaggy dark brown and charcoal fur. Broad shoulders, long heavy arms with big knuckles hanging to the knees, short bowed legs. Heavy brow, glowing ember-orange eyes, wide flat nose, two small tusks and a toothy smirk. A tattered dark brown batik waist cloth tied with rope, a few dry tan banyan leaves and thin roots tangled in the fur. A rough grey boulder held in the right hand.
Silhouette: a wide hunched gorilla-like mass, top-heavy, head low between the shoulders.
Dominant palette: dark brown, charcoal, earthy batik brown, stone grey, ember-orange eyes.
The whole body and boulder fully visible and uncropped, centered, about 75% of the image height, on an invisible ground line near the bottom.
Do not copy any existing fighting-game character; no mecha parts, no animal ears.
Background: perfectly flat solid pure green #00FF00, no gradient, no floor, no shadow, no text, no border. Do not use any green on the character.
```

Portrait:

```text
Portrait illustration (1:1) of the same character as reference 1: fierce close-up of GENDERUWO, glowing ember-orange eyes in shadowy fur, tusked smirk, a dry leaf caught in the fur. Low warm light from below. Readable in a small HUD frame, same palette, no border, no text.
```

Cut-in:

```text
Ultimate cut-in banner (21:9) of the same character as reference 1: a towering giant GENDERUWO rising behind a massive banyan tree on the LEFT third, fist raised high, rocks and roots flying. Dynamic diagonal composition, right two-thirds dark empty space for a title. No text, no logo, no gore.
```

## 4. TUYUL — The Little Pickpocket (slot `nib`)

Run = lari jinjit diam-diam, kepala besar bergoyang, karung memantul di bahu.

Base:

```text
Create an original ghost fighter from scratch for a 2D side-scrolling fighting game: TUYUL, the small bald pickpocket spirit of Javanese folklore.
Game sprite, full-body side view, in a sneaky tiptoe idle pose, facing RIGHT.
Shared art style: fine hi-bit pixel art with clean readable pixel clusters, crisp 1 px dark outline, rich soft shading, cute-creepy anime chibi anatomy, smaller than the rest of the roster. NOT chunky low-res blocks, NOT a blurry painting.
Character design: a tiny bald goblin-like spirit with a big round head, large pointed ears, big shiny black eyes with white highlights and a cheeky buck-toothed grin. Pale ashen-grey skin, skinny limbs, bare feet. Wears a loose brown sleeveless tunic and patched brown shorts tied with string. A bulging brown cloth sack of gold coins slung over the left shoulder, a few coins glinting at the opening.
Silhouette: small and compact, oversized head, crouched forward on tiptoes, sack bulging behind.
Dominant palette: ash grey, earthy brown, gold, glossy black eyes.
The whole body and sack fully visible and uncropped, centered, about 55% of the image height, on an invisible ground line near the bottom.
Do not copy any existing fighting-game character; no mecha parts, no animal ears.
Background: perfectly flat solid pure magenta #FF00FF, no gradient, no floor, no shadow, no text, no border. Do not use any pink, red or purple on the character.
```

Portrait:

```text
Portrait illustration (1:1) of the same character as reference 1: TUYUL peeking over his coin sack with a sly buck-toothed grin, holding up one shiny gold coin. Warm candle-like light. Readable in a small HUD frame, same palette, no border, no text.
```

Cut-in:

```text
Ultimate cut-in banner (21:9) of the same character as reference 1: TUYUL leaping on the LEFT third with arms full of gold coins, a rain of coins and many tiny tuyul silhouettes running behind him. Dynamic diagonal composition, right two-thirds dark empty space for a title. No text, no logo, no gore.
```

## 5. KUYANG — The Midnight Head (slot `cora`)

Idle: kepala melayang naik-turun di atas leher, pita arwah berayun. Tanpa darah/organ di semua frame.

Base:

```text
Create an original ghost fighter from scratch for a 2D side-scrolling fighting game: KUYANG, the flying-head night spirit of Borneo folklore.
Game sprite, full-body side view, standing in a relaxed idle pose, facing RIGHT.
Shared art style: fine hi-bit pixel art with clean readable pixel clusters, crisp 1 px dark outline, rich soft shading, cute-creepy anime chibi anatomy about 3 heads tall. NOT chunky low-res blocks, NOT a blurry painting.
Character design: a dark sorceress in a deep indigo sarong and a simple long-sleeved black top, barefoot. Her head floats a hand's width above her neck, detached; between head and neck hang several glowing crimson spirit ribbons made of light (stylized, no gore, no organs, no blood). Long loose black hair drifting upward, pale skin, glowing crimson eyes, a sly hungry smile with tiny fangs. A small clay oil lamp with a crimson flame hangs from her left hand.
Silhouette: slim body with a clearly separated floating head and a fan of glowing ribbons below it.
Dominant palette: indigo, black, pale skin, crimson glow, clay brown.
The whole body, head, ribbons and lamp fully visible and uncropped, centered, about 70% of the image height, on an invisible ground line near the bottom.
Do not copy any existing fighting-game character; no mecha parts, no animal ears.
Background: perfectly flat solid pure green #00FF00, no gradient, no floor, no shadow, no text, no border. Do not use any green on the character.
```

Portrait:

```text
Portrait illustration (1:1) of the same character as reference 1: KUYANG's floating head in close-up, black hair rising, glowing crimson ribbons beneath the chin, sly fanged smile, crimson eyes. Dark night lighting. Readable in a small HUD frame, same palette, no border, no text.
```

Cut-in:

```text
Ultimate cut-in banner (21:9) of the same character as reference 1: KUYANG's head swooping toward the viewer on the LEFT third, crimson ribbons trailing like comet tails, many small glowing heads in the dark sky behind. Dynamic diagonal composition, right two-thirds dark empty space for a title. No text, no logo, no gore.
```

## 6. LEYAK — The Night Flame (slot `fenr`)

Slot FENR punya dua atlas: wujud manusia (`assets/fenr/human/`) dan wujud celeng (`assets/fenr/wolf/`). Buat base kedua: celeng hitam bertaring dengan surai api dan aksesori emas yang sama. Hindari kain poleng dan Rangda (sakral).

Base:

```text
Create an original ghost fighter from scratch for a 2D side-scrolling fighting game: LEYAK, the shapeshifting night witch of Balinese folklore.
Game sprite, full-body side view, standing in a relaxed idle pose, facing RIGHT.
Shared art style: fine hi-bit pixel art with clean readable pixel clusters, crisp 1 px dark outline, rich soft shading, cute-creepy anime chibi anatomy about 3 heads tall. NOT chunky low-res blocks, NOT a blurry painting.
Character design: a wild witch spirit with a mask-like face: big round bulging eyes with tiny pupils, small curved fangs and a long playful tongue hanging out. Messy white-grey hair flaring upward like flames. Wears a black wrap skirt and sash with gold flame patterns, gold arm cuffs and anklets, long dark claws. A small orange flame burns in her open right palm.
Silhouette: hunched witch stance with knees bent, hair flaring tall above the head, clawed hands spread.
Dominant palette: black, gold, white-grey hair, orange flame, pale ochre skin.
The whole body, hair and flame fully visible and uncropped, centered, about 70% of the image height, on an invisible ground line near the bottom.
Do not copy any existing fighting-game character; no mecha parts, no animal ears.
Background: perfectly flat solid pure green #00FF00, no gradient, no floor, no shadow, no text, no border. Do not use any green on the character.
```

Portrait:

```text
Portrait illustration (1:1) of the same character as reference 1: LEYAK in close-up, bulging eyes wide, tongue out in a mocking grin, flame-like white hair, lit from below by the flame in her palm. Readable in a small HUD frame, same palette, no border, no text.
```

Cut-in:

```text
Ultimate cut-in banner (21:9) of the same character as reference 1: LEYAK transforming into a giant floating flaming head on the LEFT third, orange fire swirling, gold sparks against a black temple-silhouette night. Dynamic diagonal composition, right two-thirds dark empty space for a title. No text, no logo, no gore.
```

## 7. JIANGSHI — The Talisman Hopper (slot `edda`)

Walk/run = lompatan dua kaki yang kaku, lengan selalu lurus ke depan (1 jongkok kaku, 2 melenting, 3 lurus di udara, 4 mendarat kaku).

Base:

```text
Create an original ghost fighter from scratch for a 2D side-scrolling fighting game: JIANGSHI, the stiff hopping corpse of Chinese folklore.
Game sprite, full-body side view, standing stiffly in an idle pose with both arms stretched straight forward, facing RIGHT.
Shared art style: fine hi-bit pixel art with clean readable pixel clusters, crisp 1 px dark outline, rich soft shading, cute-creepy anime chibi anatomy about 3 heads tall. NOT chunky low-res blocks, NOT a blurry painting.
Character design: a stiff undead wearing a dark navy Qing-dynasty official robe with gold cloud embroidery and a square embroidered badge on the chest, wide sleeves, black cloth boots. A round official hat with an upturned brim and a gold bead on top. A long yellow paper talisman with black ink brush strokes hangs from the hat brim over the face. Pale grey-blue skin, long dark fingernails, sleepy half-closed eyes with tiny glowing white pupils, a small stiff frown.
Silhouette: a straight vertical plank, legs pressed together, both arms held horizontally forward.
Dominant palette: dark navy, gold, talisman yellow, pale grey-blue skin.
The whole body, arms and talisman fully visible and uncropped, centered, about 70% of the image height, on an invisible ground line near the bottom.
Do not copy any existing fighting-game character; no mecha parts, no animal ears.
Background: perfectly flat solid pure magenta #FF00FF, no gradient, no floor, no shadow, no text, no border. Do not use any pink, red or purple on the character.
```

Portrait:

```text
Portrait illustration (1:1) of the same character as reference 1: JIANGSHI in close-up, yellow talisman fluttering aside to reveal one sleepy glowing eye, official hat tilted. Cold lantern light. Readable in a small HUD frame, same palette, no border, no text.
```

Cut-in:

```text
Ultimate cut-in banner (21:9) of the same character as reference 1: the talisman tearing off JIANGSHI's hat on the LEFT third, eyes snapping wide open, a long line of hopping jiangshi silhouettes behind in a misty bamboo night. Dynamic diagonal composition, right two-thirds dark empty space for a title. No text, no logo, no gore.
```

## 8. KUCHISAKE-ONNA — The Masked Question (slot `zanni`)

Wajah di balik masker tetap tertutup di semua frame sprite; mulut lebar hanya muncul di cut-in.

Base:

```text
Create an original ghost fighter from scratch for a 2D side-scrolling fighting game: KUCHISAKE-ONNA, the masked woman of Japanese urban legend.
Game sprite, full-body side view, standing in a relaxed idle pose, facing RIGHT.
Shared art style: fine hi-bit pixel art with clean readable pixel clusters, crisp 1 px dark outline, rich soft shading, cute-creepy anime chibi anatomy about 3 heads tall. NOT chunky low-res blocks, NOT a blurry painting.
Character design: a tall slim woman in a long belted tan trench coat with the collar up, dark stockings and black heeled shoes. Very long straight black hair with blunt bangs. A large white surgical mask covers her mouth and nose. Sharp dark eyes with tiny white pupils, a calm unsettling stare. Oversized silver tailor's shears held in the right hand, blades pointing down.
Silhouette: a long narrow coat shape, hair hanging to the waist, giant shears beside the leg.
Dominant palette: tan, black, white mask, steel silver.
The whole body and shears fully visible and uncropped, centered, about 70% of the image height, on an invisible ground line near the bottom.
Do not copy any existing fighting-game character; no mecha parts, no animal ears.
Background: perfectly flat solid pure magenta #FF00FF, no gradient, no floor, no shadow, no text, no border. Do not use any pink, red or purple on the character.
```

Portrait:

```text
Portrait illustration (1:1) of the same character as reference 1: KUCHISAKE-ONNA in close-up, fingers touching the edge of her white mask, head slightly tilted, eyes smiling eerily. Flickering streetlight from above. Readable in a small HUD frame, same palette, no border, no text.
```

Cut-in:

```text
Ultimate cut-in banner (21:9) of the same character as reference 1: KUCHISAKE-ONNA on the LEFT third pulling her mask down to reveal a stylized impossibly wide toothy grin (no blood, no wounds), giant shears opening behind her under a lonely streetlight. Dynamic diagonal composition, right two-thirds dark empty space for a title. No text, no logo, no gore.
```

## 9. LA LLORONA — The Weeping River (slot `naja`)

Basic slot NAJA adalah cambuk panjang: gambar selendang/kerudung panjang yang dicambukkan, ujungnya sejauh urumi lama.

Base:

```text
Create an original ghost fighter from scratch for a 2D side-scrolling fighting game: LA LLORONA, the weeping river ghost of Mexican folklore.
Game sprite, full-body side view, floating in a sorrowful idle pose, facing RIGHT.
Shared art style: fine hi-bit pixel art with clean readable pixel clusters, crisp 1 px dark outline, rich soft shading, cute-creepy anime chibi anatomy about 3 heads tall. NOT chunky low-res blocks, NOT a blurry painting.
Character design: a ghost woman in a long white lace dress with a soaked, dripping hem and a long sheer white veil. Long wet black hair clinging to her shoulders, two orange marigold flowers in her hair. Pale blue-white skin, sad downturned eyes, glowing pale-blue tear streaks running down her cheeks, a few water droplets falling from her sleeves. One hand raised to her face as if weeping.
Silhouette: a drooping bell-shaped gown with a trailing veil, head bowed slightly.
Dominant palette: white, pale blue glow, black hair, marigold orange.
The whole body, veil and hem fully visible and uncropped, centered, about 70% of the image height, on an invisible ground line near the bottom.
Do not copy any existing fighting-game character; no mecha parts, no animal ears.
Background: perfectly flat solid pure magenta #FF00FF, no gradient, no floor, no shadow, no text, no border. Do not use any pink, red or purple on the character.
```

Portrait:

```text
Portrait illustration (1:1) of the same character as reference 1: LA LLORONA in close-up, glowing blue tears, wet hair framing her face, marigolds in her hair, veil lifting in the wind. Moonlit river reflections. Readable in a small HUD frame, same palette, no border, no text.
```

Cut-in:

```text
Ultimate cut-in banner (21:9) of the same character as reference 1: LA LLORONA on the LEFT third with arms spread, screaming as a ghostly river surges up behind her, marigold petals swirling in the water. Dynamic diagonal composition, right two-thirds dark empty space for a title. No text, no logo, no gore.
```

## 10. BANSHEE — The Keening Herald (slot `solan`)

Slot SOLAN memakai pedang besar; ganti dengan sapuan tangan berkabut dan sisir perak. Skill 2 = lompat maju lalu menghantam lantai.

Base:

```text
Create an original ghost fighter from scratch for a 2D side-scrolling fighting game: BANSHEE, the wailing spirit of Irish folklore.
Game sprite, full-body side view, floating in a relaxed idle pose, facing RIGHT.
Shared art style: fine hi-bit pixel art with clean readable pixel clusters, crisp 1 px dark outline, rich soft shading, cute-creepy anime chibi anatomy about 3 heads tall. NOT chunky low-res blocks, NOT a blurry painting.
Character design: a spectral woman in a tattered slate-grey hooded cloak over a pale grey dress, the hem dissolving into wisps of mist. Extremely long flowing silver-white hair spilling out of the hood. Pale grey skin, large glowing ice-blue eyes, a small closed mouth. Holds a long ornate silver comb in her right hand.
Silhouette: a hooded teardrop shape with a long river of silver hair and misty tail.
Dominant palette: slate grey, silver-white, pale grey, ice-blue glow.
The whole body, hair and misty hem fully visible and uncropped, centered, about 70% of the image height, on an invisible ground line near the bottom.
Do not copy any existing fighting-game character; no mecha parts, no animal ears.
Background: perfectly flat solid pure magenta #FF00FF, no gradient, no floor, no shadow, no text, no border. Do not use any pink, red or purple on the character.
```

Portrait:

```text
Portrait illustration (1:1) of the same character as reference 1: BANSHEE in close-up, hood half fallen, silver hair drifting, slowly combing her hair, ice-blue eyes glowing. Misty moorland moonlight. Readable in a small HUD frame, same palette, no border, no text.
```

Cut-in:

```text
Ultimate cut-in banner (21:9) of the same character as reference 1: BANSHEE on the LEFT third with mouth wide open in a mighty wail, silver hair blasting backward, concentric pale-blue sound rings over a foggy cliff. Dynamic diagonal composition, right two-thirds dark empty space for a title. No text, no logo, no gore.
```

## 11. BLOODY MARY — The Mirror Witch (slot `rhea`)

Proyektil dan ultimate slot RHEA berupa bola yang mengorbit; ganti fx planet dengan cermin oval berbingkai emas.

Base:

```text
Create an original ghost fighter from scratch for a 2D side-scrolling fighting game: BLOODY MARY, the mirror ghost of English and American legend.
Game sprite, full-body side view, standing in a relaxed idle pose, facing RIGHT.
Shared art style: fine hi-bit pixel art with clean readable pixel clusters, crisp 1 px dark outline, rich soft shading, cute-creepy anime chibi anatomy about 3 heads tall. NOT chunky low-res blocks, NOT a blurry painting.
Character design: a ghost woman in a black Victorian mourning gown with crimson ribbons, a high lace collar and puffed sleeves. Long wavy dark hair. Porcelain-pale face with thin silver hairline cracks like a broken mirror (stylized, no blood), glowing crimson eyes, a faint knowing smile. An ornate gold-framed hand mirror in the left hand and a long dagger-shaped mirror shard in the right hand.
Silhouette: a full bell-shaped gown, upright elegant posture, mirror held up beside the face.
Dominant palette: black, crimson, porcelain white, gold, silver glass.
The whole body, mirror and shard fully visible and uncropped, centered, about 70% of the image height, on an invisible ground line near the bottom.
Do not copy any existing fighting-game character; no mecha parts, no animal ears.
Background: perfectly flat solid pure green #00FF00, no gradient, no floor, no shadow, no text, no border. Do not use any green on the character.
```

Portrait:

```text
Portrait illustration (1:1) of the same character as reference 1: BLOODY MARY in close-up, half her face reflected in the gold hand mirror, crimson eyes glowing, cracked porcelain skin. Single candle light in darkness. Readable in a small HUD frame, same palette, no border, no text.
```

Cut-in:

```text
Ultimate cut-in banner (21:9) of the same character as reference 1: BLOODY MARY stepping out of a large ornate mirror on the LEFT third, glass shards bursting outward, many mirrors behind her each showing her reflection. Dynamic diagonal composition, right two-thirds dark empty space for a title. No text, no logo, no gore.
```

## 12. DULLAHAN — The Headless Rider (slot `mira`)

Idle: api leher berkedip naik-turun, kepala yang dibawa berkedip dan menyeringai. Tanpa darah di leher, hanya api biru.

Base:

```text
Create an original ghost fighter from scratch for a 2D side-scrolling fighting game: DULLAHAN, the headless rider of Irish folklore.
Game sprite, full-body side view, standing in a relaxed idle pose, facing RIGHT.
Shared art style: fine hi-bit pixel art with clean readable pixel clusters, crisp 1 px dark outline, rich soft shading, cute-creepy anime chibi anatomy about 3 heads tall. NOT chunky low-res blocks, NOT a blurry painting.
Character design: a small knight in dark iron armor with rivets and a tattered navy cape. There is no head on the neck; a pale blue ghost flame rises from the empty collar instead. The knight carries its own head under the left arm like a lantern: a pale face with short messy silver hair, glowing blue eyes and a smug grin. A long dark iron chain whip coiled in the right hand.
Silhouette: a stocky armored body with a flame where the head should be and a round head tucked at the hip, cape flaring behind.
Dominant palette: dark iron grey, navy, pale skin, silver hair, ghost-blue flame.
The whole body, carried head, cape and whip fully visible and uncropped, centered, about 70% of the image height, on an invisible ground line near the bottom.
Do not copy any existing fighting-game character; no mecha parts, no animal ears.
Background: perfectly flat solid pure magenta #FF00FF, no gradient, no floor, no shadow, no text, no border. Do not use any pink, red or purple on the character.
```

Portrait:

```text
Portrait illustration (1:1) of the same character as reference 1: DULLAHAN's detached head held up in an armored gauntlet, smug grin, glowing blue eyes, the ghost flame of the neck visible behind. Cold blue light. Readable in a small HUD frame, same palette, no border, no text.
```

Cut-in:

```text
Ultimate cut-in banner (21:9) of the same character as reference 1: DULLAHAN on the LEFT third raising its head high like a lantern while a black driverless coach pulled by headless black horses thunders out of the fog behind. Dynamic diagonal composition, right two-thirds dark empty space for a title. No text, no logo, no gore.
```

## Ikon skill dan VFX

Ikon (1:1, satu gambar per slot Space, I, O, P):

```text
Game skill icon, 1:1: a single bold symbol of <SKILL ACTION, e.g. a knotted shroud rope snapping forward>, readable at 64 px, matching the palette of reference 1. Dark navy background, no numbers, no keybind letters, no border, no text.
```

VFX (1:1, 256 px setelah cutout; isi tiap file ada di tabel VFX ghost-roster.md):

```text
A single game visual effect sprite: <EFFECT, e.g. a glowing pale-blue tear-water wave rolling along the ground>, side view, moving to the RIGHT, matching the palette of reference 1. Hi-bit pixel art, crisp edges, no character, no text. Generous padding on perfectly flat pure <CHROMA> background.
```
