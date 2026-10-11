/* GlutaNex reminders page: subscribe this phone to routine and refill notifications. */
(function(){
  'use strict';
  var $=function(id){return document.getElementById(id);};
  var btn=$('rem-save'),st=$('rem-status'),R=$('rem-routine'),F=$('rem-refill');if(!btn){return;}
  var supported='serviceWorker' in navigator&&'PushManager' in window&&'Notification' in window;
  var standalone=(window.matchMedia&&window.matchMedia('(display-mode: standalone)').matches)||navigator.standalone;
  var ios=/iphone|ipad|ipod/i.test(navigator.userAgent);
  var orders=[];try{orders=JSON.parse(localStorage.getItem('gn-orders')||'[]');}catch(e){}
  var last=orders[0]&&orders[0].at,refillAt=last?last+40*864e5:Date.now()+40*864e5;if(refillAt<Date.now()+864e5){refillAt=Date.now()+3*864e5;}
  $('rem-refill-note').textContent='One message around '+new Date(refillAt).toLocaleDateString('en-IN',{day:'numeric',month:'long'})+', when a 30 g jar is usually running low.';
  function say(t){st.textContent=t;}
  function b64(s){var p='='.repeat((4-s.length%4)%4),b=atob((s+p).replace(/-/g,'+').replace(/_/g,'/')),a=new Uint8Array(b.length);for(var i=0;i<b.length;i++){a[i]=b.charCodeAt(i);}return a;}
  if(ios&&!standalone){$('rem-ios').hidden=false;btn.disabled=true;say('Add GlutaNex to your home screen first (see below).');return;}
  if(!supported){btn.disabled=true;say('This browser does not support reminders. Try Chrome on Android, or the GlutaNex app on iPhone.');return;}
  function current(){return navigator.serviceWorker.register('/sw.js').then(function(){return navigator.serviceWorker.ready;}).then(function(reg){return reg.pushManager.getSubscription().then(function(s){return {reg:reg,sub:s};});});}
  current().then(function(x){if(x.sub){btn.textContent='Save reminder settings';say('Reminders are on for this phone.');var off=document.createElement('button');off.type='button';off.className='btn ghost block';off.textContent='Turn off all reminders';off.style.marginTop='8px';btn.after(off);
    off.addEventListener('click',function(){fetch('/api/push',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({action:'unsubscribe',sub:x.sub.toJSON()})}).catch(function(){}).then(function(){return x.sub.unsubscribe();}).then(function(){say('Reminders are off.');off.remove();btn.textContent='Turn on reminders';});});}}).catch(function(){});
  btn.addEventListener('click',function(){
    if(!R.checked&&!F.checked){say('Choose at least one reminder.');return;}
    btn.disabled=true;say('Asking your phone for permission…');
    Notification.requestPermission().then(function(p){if(p!=='granted'){throw new Error('denied');}return current();})
    .then(function(x){if(x.sub){return x.sub;}return fetch('/api/push').then(function(r){if(!r.ok){throw new Error('off');}return r.json();}).then(function(j){return x.reg.pushManager.subscribe({userVisibleOnly:true,applicationServerKey:b64(j.key)});});})
    .then(function(sub){return fetch('/api/push',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({sub:sub.toJSON(),routine:R.checked,refill:F.checked,refillAt:refillAt})});})
    .then(function(r){if(!r.ok){throw new Error('save');}return r.json();})
    .then(function(){say('Done! Reminders are on. You should get a confirmation notification now.');btn.textContent='Save reminder settings';})
    .catch(function(e){say(e.message==='denied'?'Notifications are blocked. Allow them for GlutaNex in your phone or browser settings, then try again.':e.message==='off'?'Reminders are not switched on yet. Please try again later.':'Something went wrong. Please try again.');})
    .then(function(){btn.disabled=false;});});
})();
