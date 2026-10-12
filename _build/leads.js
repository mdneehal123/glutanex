/* GlutaNex owner page: unfinished checkouts. The owner code is kept only in this browser tab. */
(function(){
  'use strict';
  var $=function(id){return document.getElementById(id);};
  var form=$('leads-login'),out=$('leads-out'),err=$('leads-err'),code='';
  if(!form){return;}
  try{code=sessionStorage.getItem('gn-owner')||'';}catch(e){}
  function el(t,c,x){var e=document.createElement(t);if(c){e.className=c;}if(x!=null){e.textContent=x;}return e;}
  function rs(n){return '₹'+Number(n||0).toLocaleString('en-IN');}
  function ago(t){var m=Math.round((Date.now()-t)/60000);if(m<60){return m+' min ago';}var h=Math.round(m/60);if(h<48){return h+' h ago';}return Math.round(h/24)+' days ago';}
  function api(method,body){return fetch('/api/leads',{method:method,headers:{'Content-Type':'application/json','x-owner-code':code},body:body?JSON.stringify(body):undefined}).then(function(r){return r.json().then(function(j){return {s:r.status,j:j};});});}
  function fail(s,j){var m={429:'Too many wrong codes. Owner pages are locked for 15 minutes.',401:'Wrong owner code.',503:j&&j.error==='database_missing'?'The database is not connected yet. In Vercel: Storage → add Upstash Redis to this project, then redeploy.':'Set OWNER_CODE in Vercel → Settings → Environment Variables, then redeploy.'}[s]||'Could not load the list. Try again.';
    err.textContent=m;err.hidden=false;if(s===401){try{sessionStorage.removeItem('gn-owner');}catch(e){}}}
  var STEP={1:'Entered name and phone',2:'Entered address',3:'Reached payment'};
  function load(){err.hidden=true;out.textContent='Loading…';
    api('GET').then(function(x){if(x.s!==200){out.textContent='';fail(x.s,x.j);return;}
      try{sessionStorage.setItem('gn-owner',code);}catch(e){}form.hidden=true;render(x.j.leads||[]);})
    .catch(function(){out.textContent='';fail(0);});}
  function render(list){out.textContent='';
    var head=el('div','leads-head');head.appendChild(el('b',null,list.length+' unfinished checkout'+(list.length===1?'':'s')));var rf=el('button','btn ghost sm','Refresh');rf.type='button';rf.addEventListener('click',load);head.appendChild(rf);out.appendChild(head);
    if(!list.length){out.appendChild(el('p','muted','Nothing here right now. New entries appear when a customer ticks the WhatsApp box at checkout and does not finish.'));return;}
    list.forEach(function(l){var c=el('div','lead'+(l.contacted?' done':''));
      var top=el('div','lead-top');top.appendChild(el('b',null,(l.name||'No name')+' · +91 '+l.phone));top.appendChild(el('span','muted',ago(l.updated)));c.appendChild(top);
      if(l.items){c.appendChild(el('p',null,l.items+(l.total?' · '+rs(l.total):'')));}
      var where=[l.address,l.city,l.pin].filter(Boolean).join(', ');if(where){c.appendChild(el('p','muted',where));}
      c.appendChild(el('p','lead-step',(STEP[l.step]||'Started checkout')+(l.contacted?' · messaged':'')));
      var first=(l.name||'').split(' ')[0];
      var msg='Hi'+(first?' '+first:'')+', this is GlutaNex. You were placing an order'+(l.items?' for '+l.items:'')+' on our website. Can I help you complete it? You can pay online, choose Cash on Delivery, or just reply here to order.';
      var acts=el('div','lead-acts');
      var wa=el('a','btn wa sm','WhatsApp');wa.href='https://wa.me/91'+l.phone+'?text='+encodeURIComponent(msg);wa.target='_blank';wa.rel='noopener';
      wa.addEventListener('click',function(){api('POST',{phone:l.phone,action:'contacted'});c.classList.add('done');});
      var rm=el('button','btn ghost sm','Remove');rm.type='button';rm.addEventListener('click',function(){api('POST',{phone:l.phone,action:'delete'}).then(function(){c.remove();});});
      acts.appendChild(wa);acts.appendChild(rm);c.appendChild(acts);out.appendChild(c);});
  }
  form.addEventListener('submit',function(e){e.preventDefault();code=$('owner-code').value.trim();if(code.length<6){err.textContent='Enter your owner code.';err.hidden=false;return;}load();});
  if(code){load();}
})();
