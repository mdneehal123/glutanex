/* Routine tracker: tap "Done tonight" after applying the Night Cream. The count lives on our server
   (one tap per day, India time), tied to the buyer's order. 56 nights unlock a ₹200 code. */
(function(){
  'use strict';
  var root=document.getElementById('rt');if(!root){return;}
  var KEY='gn-streak',GOAL=56;
  function el(t,c,x){var e=document.createElement(t);if(c){e.className=c;}if(x!=null){e.textContent=x;}return e;}
  function load(k,d){try{var v=JSON.parse(localStorage.getItem(k));return v==null?d:v;}catch(e){return d;}}
  function save(k,v){try{localStorage.setItem(k,JSON.stringify(v));}catch(e){}}
  function api(body){return fetch('/api/routine',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)}).then(function(r){return r.json().then(function(j){j._status=r.status;return j;});});}
  function msg(t){root.textContent='';var p=el('div','panel rt-card');p.appendChild(el('p',null,t));root.appendChild(p);}

  function join(prefill){
    root.textContent='';var p=el('form','panel rt-card rt-join');p.noValidate=true;
    p.appendChild(el('h2',null,'Start your tracker'));
    p.appendChild(el('p','muted','Use the order number from your order confirmation (it starts with pay_) and the mobile number you ordered with.'));
    var f1=el('div','f');f1.appendChild(el('label',null,'Order number'));var o=el('input');o.placeholder='pay_XXXXXXXXXXXX';o.autocomplete='off';o.spellcheck=false;o.value=prefill.order||'';f1.appendChild(o);p.appendChild(f1);
    var f2=el('div','f');f2.appendChild(el('label',null,'Mobile number'));var ph=el('input');ph.type='tel';ph.inputMode='numeric';ph.maxLength=14;ph.value=prefill.phone||'';f2.appendChild(ph);p.appendChild(f2);
    var er=el('p','oerr');er.hidden=true;p.appendChild(er);
    var b=el('button','btn block','Start tracking');b.type='submit';p.appendChild(b);
    p.addEventListener('submit',function(e){e.preventDefault();go(o.value.trim(),ph.value);});
    root.appendChild(p);
    function go(order,phone){er.hidden=true;b.disabled=true;b.textContent='Checking…';
      api({action:'join',order:order,phone:phone}).then(function(v){b.disabled=false;b.textContent='Start tracking';
        if(v.ok){save(KEY,{token:v.token});show(v);return;}
        er.textContent=v.error==='phone_mismatch'?'That mobile number does not match this order.':v.error==='no_cream'?'This order has no Night Cream. The tracker is for Night Cream routines.':'We could not find that order. Check the order number (it starts with pay_).';er.hidden=false;})
      .catch(function(){b.disabled=false;b.textContent='Start tracking';er.textContent='Something went wrong. Please try again.';er.hidden=false;});}
    if(prefill.order&&prefill.phone){go(prefill.order,prefill.phone);}
  }

  function tip(n){return n<5?'Weeks 1–2: use the Night Cream 2–3 nights a week. Count each night you use it.':n<12?'Weeks 3–4: every other night if your skin is comfortable.':n<GOAL?'Every night now if your skin is happy. Sunscreen every morning.':'You did it. Keep going with sunscreen every morning.';}

  function show(v){
    root.textContent='';var tok=load(KEY,{}).token;
    var c=el('div','panel rt-card');
    var top=el('div','rt-top');
    var ring=document.createElementNS('http://www.w3.org/2000/svg','svg');ring.setAttribute('viewBox','0 0 120 120');ring.setAttribute('class','rt-ring');
    var pct=Math.min(1,v.nights/GOAL),C=2*Math.PI*52;
    ring.innerHTML='<circle cx="60" cy="60" r="52" fill="none" stroke="#F3ECE1" stroke-width="10"/><circle cx="60" cy="60" r="52" fill="none" stroke="url(#rg)" stroke-width="10" stroke-linecap="round" stroke-dasharray="'+C.toFixed(1)+'" stroke-dashoffset="'+(C*(1-pct)).toFixed(1)+'" transform="rotate(-90 60 60)"/><defs><linearGradient id="rg" x1="0" x2="1"><stop offset="0" stop-color="#F7C08A"/><stop offset="1" stop-color="#E8742A"/></linearGradient></defs>';
    var rw=el('div','rt-ringwrap');rw.appendChild(ring);var num=el('div','rt-num');num.appendChild(el('b',null,String(v.nights)));num.appendChild(el('span',null,'of '+GOAL+' nights'));rw.appendChild(num);top.appendChild(rw);
    var side=el('div','rt-side');side.appendChild(el('p','rt-streak',v.streak>1?'🔥 '+v.streak+' nights in a row':v.streak===1?'🔥 1 night: keep it going':'Start tonight'));side.appendChild(el('p','muted rt-tip',tip(v.nights)));top.appendChild(side);c.appendChild(top);
    var btn=el('button','btn block rt-done',v.doneToday?'✓ Done tonight':'Done tonight');btn.type='button';btn.disabled=!!v.doneToday;
    btn.addEventListener('click',function(){btn.disabled=true;btn.textContent='Saving…';api({action:'checkin',token:tok}).then(function(n){if(n.ok){show(n);if(navigator.vibrate){navigator.vibrate(30);}}else{btn.disabled=false;btn.textContent='Done tonight';}}).catch(function(){btn.disabled=false;btn.textContent='Done tonight';});});
    c.appendChild(btn);
    var grid=el('div','rt-grid');for(var i=0;i<GOAL;i++){var d=el('i',i<v.nights?'on':'');if(i===6||i===20||i===55){d.classList.add('ms');}grid.appendChild(d);}c.appendChild(grid);
    var badges=el('div','rt-badges');[[7,'7 nights'],[21,'21 nights'],[56,'Full course']].forEach(function(x){var bd=el('div','rt-badge'+(v.nights>=x[0]?' got':''));bd.appendChild(el('b',null,v.nights>=x[0]?'★':String(x[0])));bd.appendChild(el('span',null,x[1]));badges.appendChild(bd);});c.appendChild(badges);
    var rwd=el('div','rt-reward');
    if(v.claimed||v.code){var code=v.code||v.claimed.code;rwd.classList.add('got');rwd.appendChild(el('b',null,'₹'+(v.reward||200)+' off your next order'));rwd.appendChild(el('code',null,code));rwd.appendChild(el('span',null,'Saved on this phone: it fills in by itself at checkout.'));
      try{var list=load('gn-codes',[]);if(!Array.isArray(list)){list=[];}if(!list.some(function(x){return x.code===code;})){list.push({code:code,off:v.reward||200,exp:(v.exp||(v.claimed&&v.claimed.exp)||Date.now()+60*864e5)});save('gn-codes',list);}}catch(e){}}
    else if(v.nights>=GOAL){rwd.classList.add('ready');rwd.appendChild(el('b',null,'🎉 Your ₹'+(v.reward||200)+' reward is ready'));var cl=el('button','btn','Claim ₹'+(v.reward||200)+' off');cl.type='button';cl.addEventListener('click',function(){cl.disabled=true;api({action:'claim',token:tok}).then(function(n){if(n.ok){show(n);}else{cl.disabled=false;}});});rwd.appendChild(cl);}
    else{rwd.appendChild(el('b',null,'₹'+(v.reward||200)+' off unlocks at night '+GOAL));rwd.appendChild(el('span',null,(GOAL-v.nights)+' nights to go. One tap counts per day.'));}
    c.appendChild(rwd);
    var lk=el('p','rt-links');var a=el('a',null,'🔔 Turn on night reminders');a.href='/reminders/';lk.appendChild(a);c.appendChild(lk);
    root.appendChild(c);
  }

  fetch('/api/config').then(function(r){return r.json();}).catch(function(){return {};}).then(function(cfg){
    if(!cfg||!cfg.rewards){msg('The routine tracker is switching on soon. Please check back in a day or two.');return;}
    var st=load(KEY,null);
    if(st&&st.token){fetch('/api/routine?token='+encodeURIComponent(st.token)).then(function(r){return r.json();}).then(function(v){if(v.ok){show(v);}else{save(KEY,null);start();}}).catch(function(){msg('Could not load your tracker. Check your connection.');});}
    else{start();}
  });
  function start(){var m=/[?&]o=(pay_\w+)/.exec(location.search),det=load('gn-details',{})||{};join({order:m?m[1]:'',phone:(det.phone||'').replace(/\D/g,'').slice(-10)});}
})();
