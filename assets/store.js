(function(){
  'use strict';
  var WA='919980881230', ADVANCE=99, KEY='gn-cart', DETAILS='gn-details', ORDERS='gn-orders', PENDING='gn-pending';
  var P=null, $=function(id){return document.getElementById(id);};
  var CFG=null;function getConfig(){if(!CFG){CFG=fetch('/api/config').then(function(r){return r.ok?r.json():{};}).catch(function(){return {};});}return CFG;}
  function rs(n){return '₹'+Number(n).toLocaleString('en-IN');}
  function el(tag,cls,text){var e=document.createElement(tag);if(cls){e.className=cls;}if(text!=null){e.textContent=text;}return e;}
  function load(k,d){try{var v=JSON.parse(localStorage.getItem(k)||'null');return v==null?d:v;}catch(e){return d;}}
  function save(k,v){try{localStorage.setItem(k,JSON.stringify(v));}catch(e){}}
  function cart(){var c=load(KEY,{});return c&&typeof c==='object'?c:{};}
  /* a Night Cream + a Face Wash in the cart become the cheaper Glow Duo automatically */
  var paired=false;
  function pair(c){var n=Math.min(c.cream||0,c.wash||0);if(n>0&&(!P||P.duo)){c.cream-=n;c.wash-=n;c.duo=(c.duo||0)+n;paired=true;}return c;}
  function setCart(c){pair(c);Object.keys(c).forEach(function(k){if(!(c[k]>0)||(P&&!P[k])){delete c[k];}else{c[k]=Math.min(10,Math.floor(c[k]));}});save(KEY,c);badge();renderDrawer();}
  function count(){var c=cart();return Object.keys(c).reduce(function(a,k){return a+c[k];},0);}
  function lines(){var c=cart();return Object.keys(c).filter(function(k){return P&&P[k];}).map(function(k){var p=P[k];return {id:k,qty:c[k],p:p,sub:p.price*c[k],mrp:p.mrp*c[k]};});}
  function totals(){var l=lines();return {lines:l,total:l.reduce(function(a,x){return a+x.sub;},0),mrp:l.reduce(function(a,x){return a+x.mrp;},0)};}
  function add(id,q){var c=cart();c[id]=(c[id]||0)+(q||1);setCart(c);}
  function badge(pop){var b=document.querySelector('.cart-count');if(!b){return;}var n=count();b.textContent=n;b.hidden=!n;if(pop){b.classList.add('pop');setTimeout(function(){b.classList.remove('pop');},320);}}
  function toast(text,action){var t=document.querySelector('.toast');if(!t){t=el('div','toast');t.setAttribute('role','status');document.body.appendChild(t);}
    t.textContent='';t.appendChild(el('span',null,text));if(action){var b=el('button',null,action[0]);b.type='button';b.addEventListener('click',action[1]);t.appendChild(b);}
    t.classList.add('show');clearTimeout(t._h);t._h=setTimeout(function(){t.classList.remove('show');},3200);}
  function qtyOf(btn){if(!btn.hasAttribute('data-useqty')){return 1;}var o=document.querySelector('[data-qty] output');return o?Number(o.textContent)||1:1;}
  var still=window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* menu */
  var mb=document.querySelector('.menu-btn');if(mb){mb.addEventListener('click',function(){var n=$('nav'),o=!n.classList.contains('open');n.classList.toggle('open',o);mb.setAttribute('aria-expanded',String(o));});}

  /* 3D tilt on cards and pictures */
  function tilt(card){
    if(still||window.matchMedia('(hover: none)').matches){return;}
    card.addEventListener('mousemove',function(e){var r=card.getBoundingClientRect(),x=(e.clientX-r.left)/r.width,y=(e.clientY-r.top)/r.height;
      card.classList.add('live');card.style.setProperty('--ry',((x-.5)*12)+'deg');card.style.setProperty('--rx',((.5-y)*10)+'deg');card.style.setProperty('--mx',(x*100)+'%');card.style.setProperty('--my',(y*100)+'%');});
    card.addEventListener('mouseleave',function(){card.classList.remove('live');card.style.setProperty('--ry','0deg');card.style.setProperty('--rx','0deg');});
  }
  [].slice.call(document.querySelectorAll('.tilt')).forEach(tilt);

  /* reveal on scroll */
  var rv=[].slice.call(document.querySelectorAll('.reveal'));
  if('IntersectionObserver' in window&&!still){var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target);}});},{threshold:.12,rootMargin:'0px 0px -40px 0px'});rv.forEach(function(x,i){x.style.transitionDelay=(i%3)*90+'ms';io.observe(x);});}
  else{rv.forEach(function(x){x.classList.add('in');});}

  /* advanced layer: scroll progress, hero spotlight + parallax word, word-by-word headline, magnetic buttons */
  (function(){
    var bar=document.querySelector('.progress'),hw=document.querySelector('.hero-word'),hero=document.querySelector('.hero'),spot=document.querySelector('.spot'),tick=false;
    function onScroll(){if(tick){return;}tick=true;requestAnimationFrame(function(){tick=false;var h=document.documentElement.scrollHeight-innerHeight,y=window.scrollY;
      if(bar){bar.style.setProperty('--p',h>0?(y/h).toFixed(4):0);}
      if(hw&&!still&&y<1200){hw.style.setProperty('--hy',(y*0.35).toFixed(1)+'px');}});}
    window.addEventListener('scroll',onScroll,{passive:true});onScroll();
    if(hero&&spot&&!still){hero.addEventListener('pointermove',function(e){if(e.pointerType!=='mouse'){return;}var r=hero.getBoundingClientRect();spot.style.setProperty('--cx',(e.clientX-r.left)+'px');spot.style.setProperty('--cy',(e.clientY-r.top)+'px');});}
    var h1=document.querySelector('.hero h1');
    if(h1&&!still){var n=0;
      (function split(node){[].slice.call(node.childNodes).forEach(function(c){
        if(c.nodeType===3){var parts=c.textContent.split(/(\s+)/),frag=document.createDocumentFragment();parts.forEach(function(t){if(!t){return;}if(/^\s+$/.test(t)){frag.appendChild(document.createTextNode(t));return;}var w=document.createElement('span');w.className='w';w.textContent=t;w.style.animationDelay=(0.15+n++*0.07)+'s';frag.appendChild(w);});node.replaceChild(frag,c);}
        else if(c.nodeType===1&&!c.classList.contains('h1-brand')){split(c);}
      });})(h1);}
    if(!still&&window.matchMedia('(hover: hover) and (pointer: fine)').matches){
      [].slice.call(document.querySelectorAll('.btn:not(.block)')).forEach(function(b){b.classList.add('mag');
        b.addEventListener('mousemove',function(e){var r=b.getBoundingClientRect(),x=e.clientX-r.left-r.width/2,y=e.clientY-r.top-r.height/2;b.style.transform='translate('+(x*0.18).toFixed(1)+'px,'+(y*0.3).toFixed(1)+'px)';});
        b.addEventListener('mouseleave',function(){b.style.transform='';});});
    }
  })();

  /* product page gallery + quantity */
  [].slice.call(document.querySelectorAll('.thumbs button')).forEach(function(b,i,all){b.addEventListener('click',function(){var m=$('pdp-img');m.style.opacity=0;setTimeout(function(){m.src=b.getAttribute('data-src');m.style.opacity=1;},160);all.forEach(function(x){x.classList.toggle('on',x===b);});});});
  var pimg=$('pdp-img');if(pimg){pimg.style.transition='opacity .2s';}
  var qty=document.querySelector('[data-qty]');
  if(qty){var out=qty.querySelector('output');qty.querySelector('[data-dec]').addEventListener('click',function(){out.textContent=Math.max(1,Number(out.textContent)-1);});qty.querySelector('[data-inc]').addEventListener('click',function(){out.textContent=Math.min(10,Number(out.textContent)+1);});}

  /* fly-to-cart: the product picture lifts, turns and flies into the bag icon */
  function fly(fromBtn,id,done){
    var target=document.querySelector('.cart-btn');var src=(P[id]||{}).img;
    var holder=fromBtn.closest('.card')||document.querySelector('.pdp');var pic=holder&&holder.querySelector('img');
    if(still||!target||!pic){done();return;}
    var a=pic.getBoundingClientRect(),b=target.getBoundingClientRect(),s=Math.min(a.width,180);
    var f=el('div','flyer');var i=el('img');i.src=src||pic.src;i.alt='';f.appendChild(i);
    f.style.width=f.style.height=s+'px';f.style.left=(a.left+a.width/2-s/2)+'px';f.style.top=(a.top+a.height/2-s/2)+'px';document.body.appendChild(f);
    requestAnimationFrame(function(){requestAnimationFrame(function(){
      var dx=b.left+b.width/2-(a.left+a.width/2),dy=b.top+b.height/2-(a.top+a.height/2);
      f.style.transform='translate('+dx+'px,'+dy+'px) scale(.12) rotateY(540deg) rotateZ(-20deg)';f.style.opacity='.4';});});
    setTimeout(function(){f.remove();done();},820);
  }

  /* cart drawer */
  var dw=document.querySelector('.drawer-wrap'),dbg=document.querySelector('.drawer-bg');
  function openCart(){if(!dw){location.href='/cart/';return;}renderDrawer();dw.classList.add('open');dbg.classList.add('open');dw.setAttribute('aria-hidden','false');document.body.style.overflow='hidden';document.body.classList.add('drawer-open');var tt=document.querySelector('.toast');if(tt){tt.classList.remove('show');}}
  function closeCart(){if(!dw){return;}dw.classList.remove('open');dbg.classList.remove('open');dw.setAttribute('aria-hidden','true');document.body.style.overflow='';document.body.classList.remove('drawer-open');}
  document.addEventListener('keydown',function(e){if(e.key==='Escape'){closeCart();}});
  function sumRows(box,rows){box.textContent='';rows.forEach(function(r){var d=el('div',r[2]||'');d.appendChild(el('span',null,r[0]));d.appendChild(el('b',null,r[1]));box.appendChild(d);});}
  function lineNode(x,editable,after){
    var row=el('div','line');var img=el('img');img.src=x.p.img;img.alt='';img.width=72;img.height=72;row.appendChild(img);
    var mid=el('div');var a=el('a');a.href=x.p.url;a.style.textDecoration='none';a.appendChild(el('b',null,x.p.name));mid.appendChild(a);
    if(editable){var q=el('div','qty');var dec=el('button',null,'−'),o=el('output',null,String(x.qty)),inc=el('button',null,'+');dec.type=inc.type='button';
      dec.addEventListener('click',function(){var c=cart();c[x.id]=Math.max(0,c[x.id]-1);setCart(c);after();});
      inc.addEventListener('click',function(){var c=cart();c[x.id]=Math.min(10,c[x.id]+1);setCart(c);after();});
      q.appendChild(dec);q.appendChild(o);q.appendChild(inc);var w=el('div');w.appendChild(q);var rm=el('button','rm','Remove');rm.type='button';rm.addEventListener('click',function(){var c=cart();delete c[x.id];setCart(c);after();});w.appendChild(rm);mid.appendChild(w);}
    else{mid.appendChild(el('span','sub','Qty '+x.qty));}
    row.appendChild(mid);var amt=el('div','amt',rs(x.sub));if(x.mrp>x.sub){amt.appendChild(el('s',null,rs(x.mrp)));}row.appendChild(amt);return row;
  }
  /* cart upsell: one item away from the Glow Duo */
  function upsellNode(after){
    var c=cart(),d=P&&P.duo,need=null;if(!d||!P.cream||!P.wash){return null;}
    if((c.cream||0)>(c.wash||0)){need='wash';}else if((c.wash||0)>(c.cream||0)){need='cream';}
    if(!need){return null;}
    var have=need==='wash'?'cream':'wash',extra=d.price-P[have].price,save=P.cream.price+P.wash.price-d.price;
    var box=el('div','upsell');var img=el('img');img.src=P[need].img;img.alt='';img.width=56;img.height=56;box.appendChild(img);
    var txt=el('div');txt.appendChild(el('b',null,'Add '+P[need].short+' for just '+rs(extra)+' more'));
    txt.appendChild(el('span',null,'Your order becomes the Glow Duo'+(save>0?' · save '+rs(save):'')));box.appendChild(txt);
    var btn=el('button','btn sm','Add');btn.type='button';btn.addEventListener('click',function(){add(need,1);badge(true);if(paired){paired=false;}after();});box.appendChild(btn);
    return box;
  }
  function waText(extra){var t=totals();return 'Hi GlutaNex, I would like to order:\n'+t.lines.map(function(x){return '- '+x.p.name+' x'+x.qty+' = '+rs(x.sub);}).join('\n')+'\nTotal: '+rs(t.total)+(extra||'');}
  function renderDrawer(){
    var box=$('drawer-lines');if(!box||!P){return;}var t=totals();box.textContent='';
    if(!t.lines.length){box.appendChild(el('div','empty','Your cart is empty.'));$('drawer-go').hidden=true;$('drawer-wa').hidden=true;sumRows($('drawer-sum'),[]);return;}
    t.lines.forEach(function(x){box.appendChild(lineNode(x,true,renderDrawer));});
    var ud=upsellNode(renderDrawer);if(ud){box.appendChild(ud);}
    $('drawer-go').hidden=false;$('drawer-wa').hidden=false;$('drawer-wa').href='https://wa.me/'+WA+'?text='+encodeURIComponent(waText());
    sumRows($('drawer-sum'),[['MRP',rs(t.mrp)],['You save','− '+rs(t.mrp-t.total),'save'],['Shipping','Free'],['Total',rs(t.total),'total']]);
  }

  function boot(){
    badge();renderDrawer();
    document.addEventListener('click',function(e){
      var a=e.target.closest('[data-add]'),b=e.target.closest('[data-buy]');
      if(e.target.closest('[data-open-cart]')){openCart();return;}
      if(e.target.closest('[data-close-cart]')){closeCart();return;}
      if(a){var id=a.getAttribute('data-add'),q=qtyOf(a);fly(a,id,function(){add(id,q);badge(true);if(paired){paired=false;var dp=P.duo||{},sv=(P.cream&&P.wash&&dp.price)?(P.cream.price+P.wash.price-dp.price):0;toast('Upgraded to Glow Duo'+(sv>0?' · save '+rs(sv):''),['View cart',openCart]);}else{toast((P[id]||{}).short+' added to cart',['View cart',openCart]);}});}
      if(b){add(b.getAttribute('data-buy'),qtyOf(b));location.href='/checkout/';}
    });
    var bb=$('buybar'),acts=document.querySelector('.pdp .acts');
    if(bb&&acts){var bt=false;var chk=function(){bt=false;var r=acts.getBoundingClientRect(),f=document.querySelector('footer'),fr=f?f.getBoundingClientRect().top:1e9,on=r.bottom<0&&fr>innerHeight-20;bb.classList.toggle('on',on);document.body.classList.toggle('bar-on',on);};
      window.addEventListener('scroll',function(){if(!bt){bt=true;requestAnimationFrame(chk);}},{passive:true});window.addEventListener('resize',chk);chk();}
    if($('cart-lines')){renderCart();}
    if($('checkout')){checkout();}
    if($('track-form')){trackPage();}
  }
  fetch('/assets/products.json').then(function(r){return r.json();}).then(function(d){P=d;boot();}).catch(function(){P={};badge();});

  function renderCart(){
    var box=$('cart-lines'),t=totals();box.textContent='';
    if(!t.lines.length){var e=el('div','empty');e.appendChild(el('p',null,'Your cart is empty.'));var s=el('a','btn','Shop now');s.href='/shop/';s.style.marginTop='16px';e.appendChild(s);box.appendChild(e);$('to-checkout').hidden=true;sumRows($('cart-sum'),[]);return;}
    t.lines.forEach(function(x){box.appendChild(lineNode(x,true,renderCart));});var uc=upsellNode(renderCart);if(uc){box.appendChild(uc);}$('to-checkout').hidden=false;
    sumRows($('cart-sum'),[['MRP',rs(t.mrp)],['You save','− '+rs(t.mrp-t.total),'save'],['Shipping','Free'],['Total',rs(t.total),'total']]);
  }

  /* ---------------- checkout: 3 steps that turn in 3D ---------------- */
  function checkout(){
    var F={name:$('co-name'),phone:$('co-phone'),address:$('co-address'),pin:$('co-pin'),city:$('co-city')};
    var btn=$('co-pay'),err=$('co-err'),busy=false,lastMode='online',step=1,stage=$('stage3d'),steps=[].slice.call(document.querySelectorAll('.step')),nav=[].slice.call(document.querySelectorAll('#steps-nav span'));
    var saved=load(DETAILS,null);if(saved){Object.keys(F).forEach(function(k){if(typeof saved[k]==='string'){F[k].value=saved[k].slice(0,300);}});}
    var online=true;
    var leadsOn=false;
    getConfig().then(function(c){if(c&&c.leads){leadsOn=true;$('consent-row').hidden=false;fit();var sv=load(DETAILS,null);if(sv&&sv.consent){$('co-consent').checked=true;}}if(c&&c.razorpay===false){online=false;
      document.querySelector('input[name=pay][value=online]').closest('label').classList.add('off');document.querySelector('input[name=pay][value=online]').disabled=true;
      document.querySelector('input[name=pay][value=cod]').closest('label').classList.add('off');document.querySelector('input[name=pay][value=cod]').disabled=true;
      document.querySelector('input[name=pay][value=wa]').checked=true;render();}});
    function fit(){var on=steps[step-1];stage.style.height=on.offsetHeight+'px';}
    function go(n){step=n;steps.forEach(function(s,i){s.classList.toggle('on',i===n-1);s.classList.toggle('past',i<n-1);});nav.forEach(function(s,i){s.classList.toggle('on',i===n-1);s.classList.toggle('done',i<n-1);});fit();
      if(n===3){review();}var first=steps[n-1].querySelector('input,textarea');if(first&&n<3){setTimeout(function(){first.focus({preventScroll:true});},350);}
      var top=stage.getBoundingClientRect().top+window.pageYOffset-120;if(window.pageYOffset>top){window.scrollTo({top:top,behavior:'smooth'});}}
    window.addEventListener('resize',fit);
    function mobile(v){var d=String(v).replace(/\D/g,'');if(d.length===12&&d.slice(0,2)==='91'){d=d.slice(2);}else if(d.length===11&&d.charAt(0)==='0'){d=d.slice(1);}return /^[6-9]\d{9}$/.test(d)&&!/^(\d)\1{9}$/.test(d)?d:'';}
    function check(n){
      if(n===1){if(F.name.value.trim().length<2){return [F.name,'Please enter your full name.'];}if(!mobile(F.phone.value)){return [F.phone,'Please enter a 10-digit Indian mobile number.'];}}
      if(n===2){if(F.address.value.trim().length<8){return [F.address,'Please enter your full address with house number and street.'];}if(!/^[1-9]\d{5}$/.test(F.pin.value.trim())){return [F.pin,'Please enter a 6-digit pincode.'];}if(F.city.value.trim().length<2){return [F.city,'Please enter your city.'];}}
      return null;}
    function clearErr(){[].slice.call(document.querySelectorAll('.fielderr')).forEach(function(x){x.remove();});Object.keys(F).forEach(function(k){F[k].classList.remove('bad');});}
    function show(p){clearErr();p[0].classList.add('bad');var fe=el('p','fielderr',p[1]);p[0].insertAdjacentElement('afterend',fe);p[0].focus({preventScroll:true});fit();}
    Object.keys(F).forEach(function(k){F[k].addEventListener('input',function(){F[k].classList.remove('bad');var n=F[k].nextElementSibling;if(n&&n.className==='fielderr'){n.remove();fit();}});});
    function remember(){var o={};Object.keys(F).forEach(function(k){o[k]=F[k].value.trim();});o.consent=!!($('co-consent')&&$('co-consent').checked);save(DETAILS,o);}
    function lead(st){if(!leadsOn||!mobile(F.phone.value)){return;}var c=$('co-consent').checked;
      if(!c&&!lead.sent){return;}lead.sent=lead.sent||c;
      var body=st==='done'||!c?{phone:mobile(F.phone.value),status:'done'}:{phone:mobile(F.phone.value),consent:true,name:F.name.value.trim(),address:F.address.value.trim(),city:F.city.value.trim(),pin:F.pin.value.trim(),step:st,items:lines().map(function(x){return {id:x.id,qty:x.qty};})};
      try{fetch('/api/lead',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body),keepalive:true}).catch(function(){});}catch(e){}}
    [].slice.call(document.querySelectorAll('[data-next]')).forEach(function(b){b.addEventListener('click',function(){var p=check(step);if(p){show(p);return;}clearErr();remember();lead(step+1);go(step+1);});});
    [].slice.call(document.querySelectorAll('[data-back]')).forEach(function(b){b.addEventListener('click',function(){go(step-1);});});
    function mode(){return document.querySelector('input[name=pay]:checked').value;}
    function review(){var r=$('co-review');r.textContent='';var a=el('div');a.appendChild(el('b',null,F.name.value.trim()+' · +91 '+mobile(F.phone.value)));r.appendChild(a);r.appendChild(el('div',null,F.address.value.trim()+', '+F.city.value.trim()+' '+F.pin.value.trim()));fit();}
    function render(){
      var t=totals(),box=$('co-lines');box.textContent='';
      if(!t.lines.length){box.appendChild(el('p','muted','Your cart is empty.'));var s=el('a','btn','Shop now');s.href='/shop/';box.appendChild(s);btn.disabled=true;return;}
      t.lines.forEach(function(x){box.appendChild(lineNode(x,true,render));});btn.disabled=false;
      var m=mode();$('amt-online').textContent=$('amt-cod').textContent=$('amt-wa').textContent=rs(t.total);
      $('cod-note').textContent='Pay '+rs(ADVANCE)+' now (refundable), '+rs(Math.max(0,t.total-ADVANCE))+' at delivery';$('cod-terms').hidden=m!=='cod';
      var rows=[['MRP',rs(t.mrp)],['You save','− '+rs(t.mrp-t.total),'save'],['Shipping','Free']];
      if(m==='cod'){rows.push(['Pay now (advance)',rs(ADVANCE),'total']);rows.push(['Pay at delivery',rs(t.total-ADVANCE)]);}else{rows.push([m==='wa'?'Order total':'You pay',rs(t.total),'total']);}
      sumRows($('co-sum'),rows);
      if(!busy){btn.textContent=m==='online'?'Pay '+rs(t.total)+' securely':m==='cod'?'Pay '+rs(ADVANCE)+' to confirm':'Send on WhatsApp';}
      if(step===3){fit();}
    }
    [].slice.call(document.querySelectorAll('input[name=pay]')).forEach(function(r){r.addEventListener('change',render);});
    render();setTimeout(fit,60);
    var pend=load(PENDING,null);if(pend&&Date.now()-pend.at<3*864e5&&lines().length&&!check(1)&&!check(2)){go(3);}
    var pinSeen='',cityAuto='';
    function pinLookup(){var pin=F.pin.value.trim();if(!/^[1-9]\d{5}$/.test(pin)){$('pin-note').hidden=true;pinSeen='';return;}if(pin===pinSeen){return;}pinSeen=pin;
      fetch('/api/pincode?pin='+pin).then(function(r){return r.ok?r.json():null;}).then(function(d){if(!d||!d.ok||F.pin.value.trim()!==pin){return;}
        if(d.city&&(!F.city.value.trim()||F.city.value===cityAuto)){F.city.value=d.city;cityAuto=d.city;}
        var parts=[[d.city,d.state].filter(Boolean).join(', ')];
        if(d.days){var by=new Date();by.setDate(by.getDate()+2+d.days);parts.push('delivery by '+by.toLocaleDateString('en-IN',{weekday:'short',day:'numeric',month:'short'}));}
        if(d.cod===false){parts.push('Cash on Delivery not available here');var c=document.querySelector('input[name=pay][value=cod]');c.disabled=true;c.closest('label').classList.add('off');}
        $('pin-note').textContent=parts.filter(Boolean).join(' · ');$('pin-note').hidden=false;fit();}).catch(function(){});}
    F.pin.addEventListener('input',pinLookup);pinLookup();
    function loadRzp(done,fail){if(window.Razorpay){done();return;}var s=document.createElement('script');s.src='https://checkout.razorpay.com/v1/checkout.js';s.onload=done;s.onerror=fail;document.head.appendChild(s);}
    function stop(text){busy=false;render();if(text){err.textContent=text;err.hidden=false;fit();}}
    function pay(advance){
      var t=totals();lastMode=advance?'cod':'online';$('not-yet').hidden=true;err.hidden=true;busy=true;btn.textContent='Opening secure payment…';remember();
      fetch('/api/create-order',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({items:t.lines.map(function(x){return {id:x.id,qty:x.qty};}),mode:advance?'advance':'full',name:F.name.value.trim(),phone:mobile(F.phone.value),address:F.address.value.trim(),city:F.city.value.trim(),pincode:F.pin.value.trim()})})
      .then(function(r){return r.ok?r.json():Promise.reject(r.status);})
      .then(function(o){loadRzp(function(){var done=false;
        var rz=new window.Razorpay({key:o.key_id,order_id:o.order_id,amount:o.amount,currency:o.currency,name:'GlutaNex',description:advance?'Advance for Cash on Delivery':'GlutaNex order',prefill:{name:F.name.value.trim(),contact:mobile(F.phone.value)},theme:{color:'#F07C1C'},
          handler:function(resp){done=true;try{localStorage.removeItem(PENDING);}catch(e){}fetch('/api/verify',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(resp)}).then(function(r){return r.json();}).then(function(v){thanks(resp.razorpay_payment_id,o,!!v.ok);}).catch(function(){thanks(resp.razorpay_payment_id,o,false);});},
          modal:{ondismiss:function(){stop();if(!done){save(PENDING,{at:Date.now()});$('ny-switch').textContent=lastMode==='cod'?'Pay the full amount online instead':'Switch to Cash on Delivery';$('not-yet').hidden=false;fit();}}}});
        rz.on('payment.failed',function(){stop('The payment did not go through. Please try again.');});rz.open();},function(){stop('The payment window could not load. Check your connection, or order on WhatsApp.');});})
      .catch(function(){stop('Online payment is not available right now. Please try again in a few minutes, or order on WhatsApp.');});
    }
    $('ny-retry').addEventListener('click',function(){pay(lastMode==='cod');});
    $('ny-switch').addEventListener('click',function(){var v=lastMode==='cod'?'online':'cod';document.querySelector('input[name=pay][value='+v+']').checked=true;render();pay(v==='cod');});
    $('co-form').addEventListener('submit',function(e){e.preventDefault();if(busy){return;}var p=check(1)||check(2);if(p){go(p[0]===F.name||p[0]===F.phone?1:2);show(p);return;}var m=mode();remember();
      if(m==='wa'){lead('done');window.open('https://wa.me/'+WA+'?text='+encodeURIComponent(waText('\n\nName: '+F.name.value.trim()+'\nMobile: '+F.phone.value.trim()+'\nAddress: '+F.address.value.trim()+', '+F.city.value.trim()+' '+F.pin.value.trim())),'_blank','noopener');return;}
      if(!online){return;}pay(m==='cod');});
    function thanks(pid,o,ok){
      lead('done');var t=totals(),cod=o.balance>0;var past=load(ORDERS,[]).filter(function(x){return x&&x.id!==pid;});past.unshift({id:pid,at:Date.now()});save(ORDERS,past.slice(0,5));setCart({});
      var wrap=$('checkout');wrap.textContent='';var box=el('div','panel thanks');box.style.gridColumn='1 / -1';
      box.appendChild(el('span','tick','✓'));box.appendChild(el('h2',null,ok?(cod?'Order confirmed. Thank you!':'Payment received. Thank you!'):'Payment submitted. We are confirming it.'));
      box.appendChild(el('p','muted','We will pack your order within 1 to 2 business days and ship it free.'));
      var s=el('div','sum'),rows=[['Items',t.lines.map(function(x){return x.p.short+(x.qty>1?' ×'+x.qty:'');}).join(', ')]];
      if(cod){rows.push(['Advance paid',rs(ADVANCE)]);rows.push(['Pay at delivery',rs(o.balance),'total']);}else{rows.push(['Paid online',rs(o.total),'total']);}
      rows.push(['Order number',pid]);sumRows(s,rows);box.appendChild(s);
      var tr=el('a','btn block','Track this order');tr.href='/track-order/?id='+encodeURIComponent(pid);box.appendChild(tr);
      var rm=el('a','btn ghost block','🔔 Turn on routine reminders');rm.href='/reminders/';box.appendChild(rm);
      var wa=el('a','btn wa block','Get updates on WhatsApp');wa.href='https://wa.me/'+WA+'?text='+encodeURIComponent('Hi GlutaNex, I placed an order. Order number: '+pid);wa.target='_blank';wa.rel='noopener';box.appendChild(wa);
      wrap.appendChild(box);window.scrollTo({top:0,behavior:'smooth'});
      if(typeof gtag==='function'){gtag('event','purchase',{transaction_id:pid,value:o.total,currency:'INR'});}
      if(typeof fbq==='function'){fbq('track','Purchase',{value:o.total,currency:'INR'},{eventID:pid});}
    }
  }

  /* ---------------- track ---------------- */
  function trackPage(){
    var byPhone=true,out=$('t-out'),go=$('t-go');
    function setMode(p){byPhone=p;$('by-phone-box').hidden=!p;$('by-id-box').hidden=p;$('by-phone').classList.toggle('on',p);$('by-id').classList.toggle('on',!p);}
    $('by-phone').addEventListener('click',function(){setMode(true);});$('by-id').addEventListener('click',function(){setMode(false);});
    function day(s){var d=new Date(String(s).replace(' ','T'));return isNaN(d)?String(s):d.toLocaleDateString('en-IN',{day:'numeric',month:'short',year:'numeric'});}
    function showNodes(n){out.textContent='';n.forEach(function(x){if(x){out.appendChild(x);}});out.hidden=false;}
    function help(){var a=el('a','btn ghost','Ask us on WhatsApp');a.href='https://wa.me/'+WA+'?text='+encodeURIComponent('Hi GlutaNex, I want to check my order.');a.target='_blank';a.rel='noopener';a.style.marginTop='14px';return a;}
    function steps(n){var ol=el('ol','tsteps');['Placed','Packed','Shipped','Delivered'].forEach(function(t,i){ol.appendChild(el('li',i<n?'done':'',t));});return ol;}
    function render(d){
      if(d.paid===false){return showNodes([el('h2',null,'Payment not completed'),el('p','muted','This order was not paid, so it has not been dispatched.'),help()]);}
      if(!d.shipped){return showNodes([el('h2',null,'Order received'),steps(1),el('p',null,'Your order is being packed. Tracking appears here once the courier collects it.'),help()]);}
      var delivered=/deliver/i.test(d.status||'')&&!/out for|undeliver|not deliver/i.test(d.status||'');
      var n=[el('h2',null,d.status||'Shipped'),steps(delivered?4:3)],bits=[];if(d.courier){bits.push('Courier: '+d.courier);}if(d.awb){bits.push('Tracking no.: '+d.awb);}if(d.expected&&!delivered){bits.push('Expected by '+day(d.expected));}n.push(el('p',null,bits.join(' · ')));
      if(d.track_url){var a=el('a','btn','Open courier tracking');a.href=d.track_url;a.target='_blank';a.rel='noopener';a.style.marginTop='14px';n.push(a);}showNodes(n);
    }
    function run(){var u;
      if(byPhone){var ph=$('t-phone').value.replace(/\D/g,'').slice(-10),pn=$('t-pin').value.trim();if(!/^[6-9]\d{9}$/.test(ph)){return showNodes([el('p','oerr','Please enter the 10-digit mobile number used on the order.')]);}if(!/^[1-9]\d{5}$/.test(pn)){return showNodes([el('p','oerr','Please enter the 6-digit delivery pincode.')]);}u='/api/track?phone='+ph+'&pin='+pn;}
      else{var id=$('t-id').value.trim().replace(/\s+/g,'');if(id.length<8){return showNodes([el('p','oerr','Please enter your payment ID or tracking number.')]);}u='/api/track?id='+encodeURIComponent(id);}
      go.disabled=true;go.textContent='Checking…';
      fetch(u).then(function(r){return r.json().then(function(j){return {ok:r.ok,j:j};});}).then(function(x){if(x.ok&&x.j.found){render(x.j);}else{showNodes([el('h2',null,'We could not find that order'),el('p','muted','Check the details, or message us.'),help()]);}})
      .catch(function(){showNodes([el('h2',null,'Tracking is not available right now'),help()]);}).then(function(){go.disabled=false;go.textContent='Track order';});}
    $('track-form').addEventListener('submit',function(e){e.preventDefault();run();});
    var q=new URLSearchParams(location.search).get('id');if(q){setMode(false);$('t-id').value=q;run();}
  }

  /* ---------------- GlutaNex assistant ---------------- */
  function assistant(){
    if(document.getElementById('checkout')||document.getElementById('leads-out')){return;}
    var KEYC='gn-chat',hist=[];try{hist=JSON.parse(sessionStorage.getItem(KEYC)||'[]');}catch(e){hist=[];}
    var fab=el('button','ask-fab');fab.type='button';fab.setAttribute('aria-label','Ask about glutathione');fab.innerHTML='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 12a8 8 0 0 1-11.6 7.1L4 20l1-4.6A8 8 0 1 1 21 12Z"/><path d="M9.5 9.5a2.5 2.5 0 1 1 3.4 2.3c-.6.3-.9.8-.9 1.4V14"/><path d="M12 17h.01"/></svg><span>Ask</span>';
    var pan=el('div','ask-panel');pan.setAttribute('role','dialog');pan.setAttribute('aria-label','GlutaNex assistant');pan.hidden=true;
    pan.innerHTML='<div class="ask-h"><div><b>Ask GlutaNex</b><span>Answers from our glutathione guides · not medical advice</span></div><button class="icon-btn" type="button" aria-label="Close">×</button></div><div class="ask-log" aria-live="polite"></div><div class="ask-chips"></div><form class="ask-f"><input type="text" maxlength="500" placeholder="Ask about glutathione, use, delivery…" aria-label="Your question"><button class="btn sm" type="submit">Send</button></form>';
    document.body.appendChild(fab);document.body.appendChild(pan);
    var log=pan.querySelector('.ask-log'),inp=pan.querySelector('input'),chips=pan.querySelector('.ask-chips'),busy=false;
    ['What is glutathione?','How do I use the Night Cream?','Is glutathione safe?','Delivery and Cash on Delivery?','ग्लूटाथियोन के फायदे?'].forEach(function(q){var c=el('button','chip',q);c.type='button';c.addEventListener('click',function(){ask(q);});chips.appendChild(c);});
    function md(t){var h=t.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
      h=h.replace(/\[([^\]]{1,80})\]\((\/[a-z0-9\/\-]*)\)/gi,'<a href="$2">$1</a>').replace(/\*\*([^*]{1,120})\*\*/g,'<b>$1</b>');
      return h.split(/\n{2,}/).map(function(par){if(/^\s*[-•*] /m.test(par)){return '<ul>'+par.split(/\n/).filter(Boolean).map(function(l){return '<li>'+l.replace(/^\s*[-•*] /,'')+'</li>';}).join('')+'</ul>';}return '<p>'+par.replace(/\n/g,'<br>')+'</p>';}).join('');}
    function bubble(role,text){var b=el('div','msg '+role);if(role==='assistant'){b.innerHTML=md(text);}else{b.textContent=text;}log.appendChild(b);log.scrollTop=log.scrollHeight;return b;}
    function persist(){try{sessionStorage.setItem(KEYC,JSON.stringify(hist.slice(-12)));}catch(e){}}
    if(!hist.length){bubble('assistant','Hi! Ask me anything about glutathione, our Night Cream and Face Wash, how to use them, or delivery. You can ask in English or Hindi.');}else{hist.forEach(function(m){bubble(m.role,m.content);});chips.hidden=true;}
    function ask(q){q=String(q||'').trim();if(!q||busy){return;}busy=true;chips.hidden=true;bubble('user',q);inp.value='';var w=bubble('assistant','');w.classList.add('typing');w.innerHTML='<i></i><i></i><i></i>';
      fetch('/api/ask',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({q:q,history:hist.slice(-6)})}).then(function(r){return r.json().then(function(j){return {ok:r.ok,status:r.status,j:j};});})
      .then(function(x){var a=x.ok&&x.j.answer?x.j.answer:(x.status===429?'Lots of questions right now. Please message us on WhatsApp at +91 99808 81230 and we will help.':'Sorry, I could not answer that just now. Please message us on WhatsApp at +91 99808 81230.');
        w.classList.remove('typing');w.innerHTML=md(a);if(x.ok&&x.j.answer){hist.push({role:'user',content:q},{role:'assistant',content:a});persist();}log.scrollTop=log.scrollHeight;})
      .catch(function(){w.classList.remove('typing');w.innerHTML=md('Sorry, something went wrong. Please message us on WhatsApp at +91 99808 81230.');})
      .then(function(){busy=false;});}
    pan.querySelector('form').addEventListener('submit',function(e){e.preventDefault();ask(inp.value);});
    function open(o){pan.hidden=!o;fab.classList.toggle('on',o);document.body.classList.toggle('ask-open',o);if(o){setTimeout(function(){inp.focus({preventScroll:true});},60);log.scrollTop=log.scrollHeight;}}
    fab.addEventListener('click',function(){open(pan.hidden);});pan.querySelector('.ask-h button').addEventListener('click',function(){open(false);});
    document.addEventListener('keydown',function(e){if(e.key==='Escape'&&!pan.hidden){open(false);}});
  }
  getConfig().then(function(c){if(c&&c.ask){assistant();}});

  /* ---------------- install as an app ---------------- */
  if('serviceWorker' in navigator&&location.protocol==='https:'){window.addEventListener('load',function(){navigator.serviceWorker.register('/sw.js').catch(function(){});});}
  (function(){var box=$('install-app'),btn=$('install-btn'),deferred=null;if(!box){return;}
    var standalone=(window.matchMedia&&window.matchMedia('(display-mode: standalone)').matches)||navigator.standalone;if(standalone){return;}
    window.addEventListener('beforeinstallprompt',function(e){e.preventDefault();deferred=e;box.hidden=false;});
    btn.addEventListener('click',function(){if(deferred){deferred.prompt();deferred.userChoice.then(function(){deferred=null;box.hidden=true;});}else{$('install-hint').textContent='On iPhone: tap the Share button, then "Add to Home Screen".';btn.hidden=true;}});
    var ios=/iphone|ipad|ipod/i.test(navigator.userAgent)&&!window.MSStream;if(ios){box.hidden=false;}
    window.addEventListener('appinstalled',function(){box.hidden=true;});})();
})();
