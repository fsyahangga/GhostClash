/* Deterministic first-to-two round rules; announcer cue names are ready for audio. */
(() => {
  const difficulties={
    // CPU brain knobs (game.js): reaction = delay before it reads the player; evade/punish/antiAir/ender = odds of
    // dodging a shot or startup, punishing recovery, anti-airing a jump, finishing a confirmed chain with a skill;
    // mistakes = odds of attacking into immunity or chaining blindly; wake = extra delay after being hit;
    // immunity = CPU post-hurt immunity in versus (the player always gets 0.9 s; Hard/Excellent use the same rule);
    // comboCap = hits in one continuous stun before that immunity starts early (stops re-started chain loops).
    easy:{label:'Easy',speed:.95,recovery:.6,reaction:.34,combo:2,skillEvery:2,ultimateAfter:10,aggression:.6,evade:.25,punish:.3,antiAir:.25,ender:.15,mistakes:.22,wake:.22,immunity:.45,comboCap:6},
    medium:{label:'Medium',speed:1.1,recovery:.38,reaction:.2,combo:3,skillEvery:1,ultimateAfter:7,aggression:.8,evade:.55,punish:.6,antiAir:.55,ender:.5,mistakes:.08,wake:.12,immunity:.9,comboCap:5},
    hard:{label:'Hard',speed:1.22,recovery:.22,reaction:.13,combo:3,skillEvery:1,ultimateAfter:5,aggression:.9,evade:.78,punish:.82,antiAir:.78,ender:.85,mistakes:.03,wake:.06,immunity:.9,comboCap:4},
    excellent:{label:'Excellent',speed:1.32,recovery:.12,reaction:.08,combo:3,skillEvery:1,ultimateAfter:3.5,aggression:.97,evade:.92,punish:.95,antiAir:.9,ender:1,mistakes:0,wake:.02,immunity:.9,comboCap:4}
  };
  // GHOST CLASH arenas. The ids stay the engine's stage slots; replace each image file in place with the ghost art from
  // guide/ghost-stages.md, then re-measure groundY on the new floor band (guide/stage-background.md).
  const stages={
    bellora:{name:'Rumah Kosong',short:'RUMAH',subtitle:'KOSONG',image:'assets/stage.webp',groundY:599,tag:'Jendelanya tak pernah ditutup',time:'MALAM JUMAT KLIWON'},
    sunspire:{name:'Pabrik Gula Tua',short:'PABRIK',subtitle:'GULA TUA',image:'assets/menu/sunspire.webp',groundY:599,tag:'Mesinnya berhenti, giling tetap berbunyi',time:'TENGAH MALAM'},
    harbor:{name:'Makam Kamboja',short:'MAKAM',subtitle:'KAMBOJA',image:'assets/menu/azure-harbor.webp',groundY:599,tag:'Bunga kamboja jatuh tanpa angin',time:'KABUT MAGRIB'},
    // groundY measured on the old 1280x720 floor band (elderwood 560-655, moonrise 570-705); re-measure after new art.
    elderwood:{name:'Hutan Larangan',short:'HUTAN',subtitle:'LARANGAN',image:'assets/menu/elderwood.webp',groundY:606,tag:'Jangan bersiul di bawah beringin',time:'MALAM BERKABUT'},
    moonrise:{name:'Candi Purnama',short:'CANDI',subtitle:'PURNAMA',image:'assets/menu/moonrise.webp',groundY:618,tag:'Leyak menari saat bulan penuh',time:'BULAN PURNAMA'}
  };
  function introTiming(m){const clips=window.ANNOUNCER_MANIFEST?.clips;m.fightAt=Math.max(1.05,(clips?.['round_'+m.round]?.duration||0)+.12);m.introDuration=Math.max(1.85,m.fightAt+(clips?.fight?.duration||0)+.10);}
  function create(mode='training') {const m={mode,phase:mode==='versus'?'intro':'fight',round:1,playerWins:0,enemyWins:0,seconds:90,phaseTime:0,fightCue:false,lastWinner:null,winner:null,koDuration:2.2};introTiming(m);return m;}
  function tick(m,dt,pHp,eHp) {
    const events=[];if(m.mode!=='versus'||m.phase==='complete')return events;
    m.phaseTime+=dt;
    if(m.phase==='intro') {
      if(!m.fightCue && m.phaseTime>=m.fightAt){m.fightCue=true;events.push({type:'cue',cue:'fight',round:m.round});}
      if(m.phaseTime>=m.introDuration){m.phase='fight';m.phaseTime=0;events.push({type:'fight'});}
    } else if(m.phase==='fight') {
      m.seconds=Math.max(0,m.seconds-dt);
      if(pHp<=0||eHp<=0||m.seconds===0){
        const winner=pHp===eHp?'draw':pHp>eHp?'player':'enemy';
        m.lastWinner=winner;if(winner==='player')m.playerWins++;if(winner==='enemy')m.enemyWins++;
        m.winner=m.playerWins===2?'player':m.enemyWins===2?'enemy':null;
        m.phase='ko';m.phaseTime=0;events.push({type:'round-end',winner,timeout:m.seconds===0,doubleKO:pHp<=0&&eHp<=0});
      }
    } else if(m.phase==='ko'&&m.phaseTime>=m.koDuration) {
      if(m.winner){m.phase='complete';events.push({type:'complete',winner:m.winner});}
      else {m.round=m.playerWins+m.enemyWins+1;m.phase='intro';m.phaseTime=0;m.seconds=90;m.fightCue=false;m.koDuration=2.2;introTiming(m);events.push({type:'next-round',round:m.round});}
    }
    return events;
  }
  window.MatchRules={create,tick,difficulties,stages};
})();
