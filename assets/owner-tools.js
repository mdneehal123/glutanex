/* Owner tools on the owner page: create a reward code (e.g. for an unboxing Reel) and upload a packed-parcel photo.
   Uses the same owner code as the list above (kept only in this browser tab). */
(function(){
  'use strict';
  var box=document.getElementById('owner-tools');if(!box){return;}
  var $=function(id){return document.getElementById(id);};
  function code(){var c='';try{c=sessionStorage.getItem('gn-owner')||'';}catch(e){}return c||($('owner-code')&&$('owner-code').value.trim())||'';}
  function say(id,t,ok){var p=$(id);p.textContent=t;p.className='ot-msg '+(ok?'ok':'bad');p.hidden=false;}
  var ERR={429:'Too many wrong codes: owner tools are locked for 15 minutes.',401:'Wrong owner code. Enter it at the top first.',503:'Not switched on yet: add the Redis database and OWNER_CODE in Vercel, then redeploy.'};
  /* reward code */
  $('ot-code-go').addEventListener('click',function(){var ph=$('ot-phone').value.replace(/\D/g,'').slice(-10),off=+$('ot-off').value,note=$('ot-note').value;
    if(!/^[6-9]\d{9}$/.test(ph)){return say('ot-code-msg','Enter the customer\'s 10-digit mobile number.');}
    fetch('/api/coupon',{method:'POST',headers:{'Content-Type':'application/json','x-owner-code':code()},body:JSON.stringify({phone:ph,off:off,days:60,kind:note==='Unboxing Reel'?'unbox':'manual',note:note})})
    .then(function(r){return r.json().then(function(j){return {s:r.status,j:j};});}).then(function(x){if(!x.j.ok){return say('ot-code-msg',ERR[x.s]||'Could not create the code.');}
      var exp=new Date(x.j.exp).toLocaleDateString('en-IN',{day:'numeric',month:'short',year:'numeric'});say('ot-code-msg','✓ '+x.j.code+' · ₹'+x.j.off+' off · valid till '+exp,true);
      var a=document.createElement('a');a.className='btn wa sm';a.target='_blank';a.rel='noopener';a.textContent='Send to customer on WhatsApp';
      a.href='https://wa.me/91'+ph+'?text='+encodeURIComponent('Hi from GlutaNex! '+(note==='Unboxing Reel'?'Thank you for your unboxing Reel 💛 ':'')+'Here is ₹'+x.j.off+' off your next order: '+x.j.code+'\nUse it at checkout on glutanex.co.in with this mobile number. Valid till '+exp+' on orders of ₹399 or more.');
      $('ot-code-msg').appendChild(document.createElement('br'));$('ot-code-msg').appendChild(a);}).catch(function(){say('ot-code-msg','Could not create the code.');});});
  /* parcel photo: shrink to about 1000 px before upload */
  $('ot-photo-go').addEventListener('click',function(){var ord=$('ot-order').value.trim(),file=$('ot-file').files[0];
    if(!/^(pay|order)_\w{6,}$/.test(ord)){return say('ot-photo-msg','Enter the order number (pay_… or order_…).');}if(!file){return say('ot-photo-msg','Choose or take a photo first.');}
    say('ot-photo-msg','Uploading…',true);var img=new Image(),url=URL.createObjectURL(file);
    img.onload=function(){var s=Math.min(1,1000/Math.max(img.width,img.height)),c=document.createElement('canvas');c.width=Math.round(img.width*s);c.height=Math.round(img.height*s);c.getContext('2d').drawImage(img,0,0,c.width,c.height);URL.revokeObjectURL(url);
      var data=c.toDataURL('image/jpeg',0.72);if(data.length>390000){data=c.toDataURL('image/jpeg',0.5);}
      fetch('/api/parcel-photo',{method:'POST',headers:{'Content-Type':'application/json','x-owner-code':code()},body:JSON.stringify({order:ord,image:data})}).then(function(r){return r.json().then(function(j){return {s:r.status,j:j};});})
      .then(function(x){if(x.j.ok){say('ot-photo-msg','✓ Photo added. '+(x.j.name||'The customer')+' will see it on the tracking page.',true);$('ot-file').value='';}else{say('ot-photo-msg',x.j.error==='order_not_found'?'Order not found.':ERR[x.s]||'Upload failed.');}}).catch(function(){say('ot-photo-msg','Upload failed.');});};
    img.onerror=function(){say('ot-photo-msg','That file is not a photo.');};img.src=url;});
})();
