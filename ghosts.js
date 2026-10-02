/* GHOST CLASH roster overlay.
   The engine still runs the twelve original kit slots (arco, fenr, mira ...). Each slot is now played by a ghost whose
   legend fits that slot's moves best. This file only changes what the player sees and hears: names, faction, titles,
   skill names, cut-in text and status lines. Damage, reach, cooldowns and the CPU stay exactly as tuned.
   Load order: after every kit file and the announcer manifest, before announcer.js / game.js / menu.js.
   Placeholder art comes from assets/ghosts/base via guide/tools/build_ghost_assets.py; new voice clips: set voice:true. */
(() => {
  'use strict';
  const FACTIONS = {
    nusantara: { label: 'NUSANTARA', blurb: 'Hantu-hantu legenda Indonesia: pocong, kuntilanak, genderuwo, tuyul, kuyang dan leyak.' },
    mancanegara: { label: 'MANCANEGARA', blurb: 'Arwah legenda dari Tiongkok, Jepang, Meksiko, Irlandia dan Inggris.' }
  };
  // voice:false mutes the slot's old name clips (select, wins, ultimate) until clips for the ghost are recorded.
  const GHOSTS = {
    isolde: {
      id: 'pocong', name: 'POCONG', tag: 'THE SHROUD HOPPER', title: 'SHROUD HOPPER', faction: 'nusantara', origin: 'Jawa / Melayu',
      detail: 'Talinya belum dilepas. Lompatannya belum selesai.', style: 'Rushdown / lompatan kafan dan tali pocong', color: '#e8e4d8',
      names: ['KAFAN CHAIN', 'TALI KAFAN', 'LOMPAT POCONG', 'HUJAN POCONG'], status: 'TALI TERIKAT',
      cutin: { top: 'HUJAN', bottom: 'POCONG', detail: 'TIGA POCONG JATUH DARI LANGIT' }, voice: false
    },
    arco: {
      id: 'kuntilanak', name: 'KUNTILANAK', tag: 'THE WARU WAILER', title: 'WARU WAILER', faction: 'nusantara', origin: 'Kalimantan / Melayu',
      detail: 'Kalau tawanya terdengar jauh, ia sudah di belakangmu.', style: 'Aerial / tawa melengking dan sambaran dari pohon', color: '#f1f1f6',
      names: ['KUKU PANJANG', 'TAWA MELENGKING', 'JATUH DARI WARU', 'MALAM POHON WARU'], status: 'HIHIHIHI...',
      cutin: { top: 'MALAM', bottom: 'POHON WARU', detail: 'ARWAH WARU MENYAPU ARENA' }, voice: false
    },
    haldor: {
      id: 'genderuwo', name: 'GENDERUWO', tag: 'THE BANYAN BRUTE', title: 'BANYAN BRUTE', faction: 'nusantara', origin: 'Jawa',
      detail: 'Penunggu beringin. Batu pertamanya selalu peringatan.', style: 'Heavy tank / lempar batu dan serudukan rimba', color: '#a8744a',
      names: ['TINJU RIMBA', 'LEMPAR BATU GAIB', 'SERUDUK RIMBA', 'AMUK BERINGIN'], status: 'RIMBA BANGUN',
      cutin: { top: 'AMUK', bottom: 'BERINGIN', detail: 'TIGA HANTAMAN PENUNGGU BERINGIN' }, voice: false
    },
    nib: {
      id: 'tuyul', name: 'TUYUL', tag: 'THE LITTLE PICKPOCKET', title: 'LITTLE PICKPOCKET', faction: 'nusantara', origin: 'Jawa',
      detail: 'Kecil, gundul, dan dompetmu sudah kosong.', style: 'Rushdown / koin lempar dan copet kilat', color: '#e6c25a',
      names: ['GIGIT KECIL', 'LEMPAR KOIN', 'COPET KILAT', 'PESUGIHAN KILAT'], status: 'KANTONG TERBUKA',
      cutin: { top: 'PESUGIHAN', bottom: 'KILAT', detail: 'TIGA KARUNG KOIN PENGEJAR' }, voice: false
    },
    cora: {
      id: 'kuyang', name: 'KUYANG', tag: 'THE MIDNIGHT HEAD', title: 'MIDNIGHT HEAD', faction: 'nusantara', origin: 'Kalimantan',
      detail: 'Tengah malam, kepalanya pergi berburu sendiri.', style: 'Agile / pita arwah dan kepala terbang', color: '#d0505a',
      names: ['CAKAR MALAM', 'PITA ARWAH', 'SAPUAN MALAM', 'PESTA KUYANG'], status: 'KEPALA LAPAR',
      cutin: { top: 'PESTA', bottom: 'KUYANG', detail: 'TIGA SAPUAN KEPALA TERBANG' }, voice: false
    },
    fenr: {
      id: 'leyak', name: 'LEYAK', tag: 'THE NIGHT FLAME', title: 'NIGHT FLAME', faction: 'nusantara', origin: 'Bali',
      detail: 'Malam hari ia berganti rupa. Apinya tidak.', style: 'Shapeshifter / api leyak dan wujud celeng', color: '#f29b3a',
      names: ['CAKAR BARA', 'API LEYAK', 'TERJANG MALAM', 'MALAM PENGLEAKAN'],
      beast: { cls: 'WUJUD CELENG', deck: 'LEYAK · CELENG', names: ['TARING CELENG', 'TERKAM CELENG', 'LOLONG MALAM', 'MALAM PENGLEAKAN'], status: 'CELENG MENGAMUK', timer: 'CELENG' },
      status: 'API MENYALA', cutin: { top: 'MALAM', bottom: 'PENGLEAKAN', detail: 'BERUBAH WUJUD JADI CELENG' }, voice: false
    },
    edda: {
      id: 'jiangshi', name: 'JIANGSHI', tag: 'THE TALISMAN HOPPER', title: 'TALISMAN HOPPER', faction: 'mancanegara', origin: 'Tiongkok',
      detail: 'Selama jimatnya menempel, ia masih mau menunggu.', style: 'Counter / jimat melompat dan perisai jimat', color: '#f2d24b',
      names: ['TELAPAK KAKU', 'JIMAT MELOMPAT', 'PERISAI JIMAT', 'JIMAT TERLEPAS'], status: 'JIMAT MENEMPEL',
      cutin: { top: 'JIMAT', bottom: 'TERLEPAS', detail: 'TIGA LOMPATAN JIANGSHI RAKSASA' }, voice: false
    },
    zanni: {
      id: 'kuchisake', name: 'KUCHISAKE-ONNA', tag: 'THE MASKED QUESTION', title: 'MASKED QUESTION', faction: 'mancanegara', origin: 'Jepang',
      detail: 'Ia hanya bertanya satu hal. Jawab dengan hati-hati.', style: 'Trickster / gunting bumerang dan tarikan dekat', color: '#c9b48a',
      names: ['GUNTING CEPAT', 'GUNTING BUMERANG', 'WATASHI, KIREI?', 'BUKA MASKER'], status: 'MASKER TERPASANG',
      cutin: { top: 'BUKA', bottom: 'MASKER', detail: 'GUNTING RAKSASA PULANG-PERGI' }, voice: false
    },
    naja: {
      id: 'llorona', name: 'LA LLORONA', tag: 'THE WEEPING RIVER', title: 'WEEPING RIVER', faction: 'mancanegara', origin: 'Meksiko',
      detail: 'Air matanya mengalir sampai ke sungai. Jangan dekat-dekat.', style: 'Mid-range / selendang panjang dan arus sungai', color: '#9fd0e8',
      names: ['SELENDANG RATAPAN', 'AIR MATA SUNGAI', 'PUSARAN SUNGAI', 'BANJIR RATAPAN'], status: 'SUNGAI MENANGIS',
      cutin: { top: 'BANJIR', bottom: 'RATAPAN', detail: 'TIGA TANGAN SUNGAI MUNCUL' }, voice: false
    },
    solan: {
      id: 'banshee', name: 'BANSHEE', tag: 'THE KEENING HERALD', title: 'KEENING HERALD', faction: 'mancanegara', origin: 'Irlandia',
      detail: 'Ratapannya datang lebih dulu. Kabar buruknya menyusul.', style: 'Powerhouse / gelombang ratapan dan terkaman kabut', color: '#bcd7ee',
      names: ['TANGAN KABUT', 'RATAPAN', 'TERKAM KABUT', 'KEENING'], status: 'SUARA TERTAHAN',
      cutin: { top: 'THE', bottom: 'KEENING', detail: 'TIGA GELOMBANG RATAPAN' }, voice: false
    },
    rhea: {
      id: 'bloodymary', name: 'BLOODY MARY', tag: 'THE MIRROR WITCH', title: 'MIRROR WITCH', faction: 'mancanegara', origin: 'Inggris / Amerika',
      detail: 'Sebut namanya tiga kali. Lalu jangan menoleh.', style: 'Zoner / cermin melayang dan panggilan cermin', color: '#c7485e',
      names: ['PECAHAN KACA', 'CERMIN MELAYANG', 'PANGGIL TIGA KALI', 'CERMIN SERIBU'], status: 'CERMIN MENUNGGU',
      cutin: { top: 'CERMIN', bottom: 'SERIBU', detail: 'TIGA CERMIN RAKSASA MENGORBIT' }, voice: false
    },
    mira: {
      id: 'dullahan', name: 'DULLAHAN', tag: 'THE HEADLESS RIDER', title: 'HEADLESS RIDER', faction: 'mancanegara', origin: 'Irlandia',
      detail: 'Kepalanya di tangan. Namamu sudah di bibirnya.', style: 'Heavy / tatapan kepala dan terjangan ksatria', color: '#7fa6d9',
      names: ['CAMBUK RANTAI', 'TATAPAN KEPALA', 'TERJANG KSATRIA', 'KERETA MAUT'], status: 'NAMA DISEBUT',
      cutin: { top: 'KERETA', bottom: 'MAUT', detail: 'DUA BELAS API ARWAH BERJATUHAN' }, voice: false
    }
  };
  for (const g of Object.values(GHOSTS)) g.cls = FACTIONS[g.faction].label;

  // Skill names live in each kit; point them at the ghost names so the HUD, touch buttons and logs all agree.
  const kits = { mira: window.Mira, cora: window.Cora, naja: window.Naja, haldor: window.Haldor, zanni: window.Zanni, isolde: window.Isolde, rhea: window.Rhea, solan: window.Solan, nib: window.Nib, edda: window.Edda };
  for (const [slot, kit] of Object.entries(kits)) if (kit && Array.isArray(kit.names)) kit.names = [...GHOSTS[slot].names];
  if (window.Fenr?.kits) { window.Fenr.kits.human.names = [...GHOSTS.fenr.names]; window.Fenr.kits.wolf.names = [...GHOSTS.fenr.beast.names]; }

  // Old announcer clips say the previous fighter names; drop them for ghosts without new recordings.
  const clips = window.ANNOUNCER_MANIFEST?.clips;
  if (clips) for (const [slot, g] of Object.entries(GHOSTS)) if (!g.voice) { delete clips['select_' + slot]; delete clips[slot + '_wins']; }

  window.GHOST_FACTIONS = FACTIONS;
  window.GHOSTS = GHOSTS;
})();
