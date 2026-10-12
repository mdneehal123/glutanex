/* "Talk to the jar": ask a question out loud in English, Hindi, Hinglish or a regional language;
   the jar answers out loud. Speech is turned into text by the phone's own speech service, the answer comes
   from the GlutaNex assistant (api/ask.js, voice mode) and is read aloud by the phone's own voice.
   Falls back to typing when the browser has no speech recognition. */
(function(){
  'use strict';
  var btns=[].slice.call(document.querySelectorAll('[data-talk]'));if(!btns.length){return;}
  var SR=window.SpeechRecognition||window.webkitSpeechRecognition,TTS=window.speechSynthesis;
  var LANGS=[['en','English','en-IN'],['hinglish','Hinglish','en-IN'],['hi','हिंदी','hi-IN'],['ta','தமிழ்','ta-IN'],['te','తెలుగు','te-IN'],['mr','मराठी','mr-IN'],['bn','বাংলা','bn-IN'],['kn','ಕನ್ನಡ','kn-IN']];
  var HINTS={en:['Will it suit oily skin?','How do I use it?','Is it safe?','Is Cash on Delivery available?'],hinglish:['Kya ye oily skin pe chalega?','Kaise lagana hai?','Safe hai kya?','COD milega?'],
    hi:['क्या यह ऑयली स्किन पर चलेगा?','इसे कैसे लगाएं?','क्या यह सुरक्षित है?','कैश ऑन डिलीवरी है?'],ta:['இது எண்ணெய் சருமத்திற்கு ஏற்றதா?','எப்படி பயன்படுத்துவது?'],te:['ఇది జిడ్డు చర్మానికి సరిపోతుందా?','ఎలా వాడాలి?'],
    mr:['हे तेलकट त्वचेला चालेल का?','कसे वापरायचे?'],bn:['এটা তৈলাক্ত ত্বকে চলবে?','কীভাবে ব্যবহার করব?'],kn:['ಇದು ಎಣ್ಣೆ ಚರ್ಮಕ್ಕೆ ಸೂಕ್ತವೇ?','ಹೇಗೆ ಬಳಸುವುದು?']};
  var NAMES={cream:'Night Cream',wash:'Face Wash',duo:'Glow Duo'};
  function el(t,c,x){var e=document.createElement(t);if(c){e.className=c;}if(x!=null){e.textContent=x;}return e;}
  function get(k,d){try{var v=localStorage.getItem(k);return v==null?d:v;}catch(e){return d;}}
  function set(k,v){try{localStorage.setItem(k,v);}catch(e){}}
  var pl=(document.documentElement.lang||'en').toLowerCase(),lang=get('gn-talk-lang',pl==='hi-latn'?'hinglish':pl.slice(0,2)==='hi'?'hi':LANGS.some(function(l){return l[0]===pl.slice(0,2);})?pl.slice(0,2):'en');
  var hist=[],sheet=null,state='idle',rec=null,voices=[];
  if(TTS){var lv=function(){voices=TTS.getVoices()||[];};lv();if('onvoiceschanged' in TTS){TTS.onvoiceschanged=lv;}}

  fetch('/api/config').then(function(r){return r.json();}).catch(function(){return {};}).then(function(c){if(c&&c.ask){btns.forEach(function(b){b.hidden=false;});}});
  btns.forEach(function(b){b.addEventListener('click',function(e){e.preventDefault();open();});});

  function L(){for(var i=0;i<LANGS.length;i++){if(LANGS[i][0]===lang){return LANGS[i];}}return LANGS[0];}
  function build(){
    sheet=el('div','talk');sheet.setAttribute('role','dialog');sheet.setAttribute('aria-modal','true');sheet.setAttribute('aria-label','Talk to the GlutaNex jar');sheet.hidden=true;
    var card=el('div','talk-card');
    var top=el('div','talk-top');top.appendChild(el('b',null,'Talk to the jar'));var x=el('button','talk-x','✕');x.type='button';x.setAttribute('aria-label','Close');x.addEventListener('click',close);top.appendChild(x);card.appendChild(top);
    var langs=el('div','talk-langs');LANGS.forEach(function(l){var c=el('button','talk-lang',l[1]);c.type='button';c.lang=l[2].slice(0,2);c.dataset.l=l[0];c.addEventListener('click',function(){lang=l[0];set('gn-talk-lang',lang);paintLang();hints();});langs.appendChild(c);});card.appendChild(langs);
    var stage=el('div','talk-stage');var jar=el('div','talk-jar');var img=el('img');img.src='/assets/img/jar-cut.webp';img.alt='GlutaNex Night Cream jar';jar.appendChild(img);stage.appendChild(jar);
    var orb=el('button','talk-orb');orb.type='button';orb.setAttribute('aria-label','Tap and speak');orb.innerHTML='<svg viewBox="0 0 24 24" width="30" height="30" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><rect x="9" y="3" width="6" height="11" rx="3"/><path d="M5 11a7 7 0 0 0 14 0M12 18v3"/></svg>';
    orb.addEventListener('click',function(){if(state==='listening'){stopListen();}else if(state==='speaking'){TTS&&TTS.cancel();setState('idle');}else{listen();}});stage.appendChild(orb);card.appendChild(stage);
    card.appendChild(el('p','talk-status',''));
    card.appendChild(el('p','talk-you',''));
    var ans=el('div','talk-ans');ans.hidden=true;card.appendChild(ans);
    card.appendChild(el('div','talk-hints'));
    var form=el('form','talk-type');var inp=el('input');inp.placeholder='Or type your question';inp.setAttribute('enterkeyhint','send');var go=el('button','btn sm','Ask');go.type='submit';form.appendChild(inp);form.appendChild(go);
    form.addEventListener('submit',function(e){e.preventDefault();var q=inp.value.trim();if(q){inp.value='';unlock();ask(q);}});card.appendChild(form);
    card.appendChild(el('p','talk-note','Answers come from our guides and are cosmetic information, not medical advice. Your voice is turned into text by your phone; we do not record it.'));
    sheet.appendChild(card);sheet.addEventListener('click',function(e){if(e.target===sheet){close();}});document.body.appendChild(sheet);
    document.addEventListener('keydown',function(e){if(e.key==='Escape'&&sheet&&!sheet.hidden){close();}});
  }
  function q(s){return sheet.querySelector(s);}
  function paintLang(){[].forEach.call(sheet.querySelectorAll('.talk-lang'),function(c){c.classList.toggle('on',c.dataset.l===lang);});}
  function hints(){var h=q('.talk-hints');h.textContent='';(HINTS[lang]||HINTS.en).forEach(function(t){var c=el('button','chip',t);c.type='button';c.addEventListener('click',function(){unlock();ask(t);});h.appendChild(c);});}
  function setState(s,text){state=s;sheet.dataset.state=s;var st=q('.talk-status');
    st.textContent=text!=null?text:s==='listening'?'Listening… speak now':s==='thinking'?'Thinking…':s==='speaking'?'Tap the mic to stop':SR?'Tap the mic and ask me anything':'Type your question below';}
  function open(){if(!sheet){build();}paintLang();hints();sheet.hidden=false;document.body.classList.add('talk-open');setState('idle');}
  function close(){if(!sheet){return;}stopListen();if(TTS){TTS.cancel();}sheet.hidden=true;document.body.classList.remove('talk-open');setState('idle');}
  /* iPhones only allow speech after a tap: speak a silent sound during the tap so the answer can be read later */
  function unlock(){if(!TTS){return;}try{var u=new SpeechSynthesisUtterance(' ');u.volume=0;TTS.speak(u);}catch(e){}}

  function listen(){
    if(!SR){setState('idle','Voice input is not available in this browser. Please type below.');q('.talk-type input').focus();return;}
    unlock();if(TTS){TTS.cancel();}
    try{rec=new SR();}catch(e){setState('idle','Voice input is not available here. Please type below.');return;}
    rec.lang=L()[2];rec.interimResults=true;rec.continuous=false;rec.maxAlternatives=1;
    var finalText='';q('.talk-you').textContent='';
    rec.onresult=function(e){var t='';for(var i=e.resultIndex;i<e.results.length;i++){t+=e.results[i][0].transcript;if(e.results[i].isFinal){finalText=t;}}q('.talk-you').textContent='“'+(finalText||t)+'”';if(!finalText){finalText='';}rec._last=t;};
    rec.onerror=function(e){setState('idle',e.error==='not-allowed'||e.error==='service-not-allowed'?'Microphone permission is off. Allow it in your browser settings, or type below.':e.error==='no-speech'?'I did not hear anything. Tap the mic and try again.':'Could not hear clearly. Try again, or type below.');};
    rec.onend=function(){var t=(finalText||rec._last||'').trim();rec=null;if(state==='listening'){if(t){ask(t);}else{setState('idle','I did not hear anything. Tap the mic and try again.');}}};
    try{rec.start();setState('listening');}catch(e){setState('idle','Could not start the microphone. Please type below.');}
  }
  function stopListen(){if(rec){try{rec.stop();}catch(e){}}}

  function clean(t){return String(t||'').replace(/\[([^\]]+)\]\([^)]+\)/g,'$1').replace(/[*_#`>]/g,'').replace(/https?:\/\/\S+/g,'').trim();}
  function ask(text){
    q('.talk-you').textContent='“'+text+'”';q('.talk-hints').hidden=true;setState('thinking');var ans=q('.talk-ans');ans.hidden=true;
    fetch('/api/ask',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({q:text,history:hist.slice(-6),voice:true,lang:lang})})
    .then(function(r){return r.json().then(function(j){return {ok:r.ok,status:r.status,j:j};});})
    .then(function(x){
      if(!x.ok||!x.j.answer){setState('idle',x.status===429?'Lots of questions today. Please message us on WhatsApp.':'Sorry, I could not answer just now. Try again, or message us on WhatsApp.');return;}
      var a=clean(x.j.answer);hist.push({role:'user',content:text},{role:'assistant',content:a});
      ans.textContent='';ans.appendChild(el('p',null,a));
      if(x.j.cart&&NAMES[x.j.cart]){var row=el('div','talk-cart');var add=el('button','btn sm','Add '+NAMES[x.j.cart]+' to cart');add.type='button';add.setAttribute('data-add',x.j.cart);row.appendChild(add);
        var buy=el('button','btn ghost sm','Buy now');buy.type='button';buy.setAttribute('data-buy',x.j.cart);row.appendChild(buy);ans.appendChild(row);}
      var again=el('button','talk-again','🎙️ Ask another question');again.type='button';again.addEventListener('click',listen);ans.appendChild(again);
      ans.hidden=false;speak(a);
    }).catch(function(){setState('idle','Sorry, I could not answer just now. Check your connection and try again.');});
  }
  function speak(text){
    if(!TTS){setState('idle','');return;}
    var code=L()[2],u=new SpeechSynthesisUtterance(text);u.lang=code;u.rate=lang==='en'||lang==='hinglish'?1:0.95;u.pitch=1.05;
    var v=voices.filter(function(x){return x.lang&&x.lang.replace('_','-').toLowerCase()===code.toLowerCase();})[0]||voices.filter(function(x){return x.lang&&x.lang.slice(0,2).toLowerCase()===code.slice(0,2);})[0];
    if(v){u.voice=v;}
    var jar=q('.talk-jar');
    u.onstart=function(){setState('speaking');};
    u.onboundary=function(){jar.classList.remove('beat');void jar.offsetWidth;jar.classList.add('beat');};
    u.onend=u.onerror=function(){if(state==='speaking'){setState('idle','Tap the mic to ask another question');}};
    TTS.cancel();TTS.speak(u);
    setTimeout(function(){if(state==='thinking'){setState('idle',v?'':'Your phone has no voice for this language, so here is my answer in text.');}},2500);
  }
})();
