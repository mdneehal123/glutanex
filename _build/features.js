/* Wholesale enquiry form: builds a WhatsApp message (nothing is stored on our side). */
(function(){
  'use strict';
  var f=document.getElementById('wsform');if(!f){return;}
  var $=function(id){return document.getElementById(id);},err=$('ws-err');
  f.addEventListener('submit',function(e){e.preventDefault();
    var biz=$('ws-biz').value.trim(),name=$('ws-name').value.trim(),ph=$('ws-phone').value.replace(/\D/g,'').slice(-10),city=$('ws-city').value.trim(),pin=$('ws-pin').value.trim();
    var c=Math.max(0,Math.floor(+$('ws-cream').value||0)),w=Math.max(0,Math.floor(+$('ws-wash').value||0));
    var bad=!biz?'Please enter your business name.':!name?'Please enter your name.':!/^[6-9]\d{9}$/.test(ph)?'Please enter a valid 10-digit mobile number.':!city?'Please enter your city.':(c+w)<6?'The minimum wholesale order is 6 pieces in total.':'';
    if(bad){err.textContent=bad;err.hidden=false;return;}err.hidden=true;
    var msg='Hi GlutaNex, wholesale enquiry:\n\nBusiness: '+biz+' ('+$('ws-type').value+')\nName: '+name+'\nMobile: '+ph+'\nCity: '+city+(pin?' '+pin:'')+'\nNight Cream: '+c+' pcs\nFace Wash: '+w+' pcs'+($('ws-note').value.trim()?'\nNote: '+$('ws-note').value.trim():'')+'\n\nPlease share wholesale prices.';
    window.open('https://wa.me/919980881230?text='+encodeURIComponent(msg),'_blank','noopener');
  });
})();
/* Unboxing reward form: sends the Reel link and order number to us on WhatsApp. */
(function(){
  'use strict';
  var f=document.getElementById('ubform');if(!f){return;}
  var $=function(id){return document.getElementById(id);},err=$('ub-err');
  try{var d=JSON.parse(localStorage.getItem('gn-details')||'{}');if(d&&d.phone){$('ub-phone').value=d.phone;}var o=JSON.parse(localStorage.getItem('gn-orders')||'[]');if(o&&o[0]&&o[0].id){$('ub-order').value=o[0].id;}}catch(e){}
  f.addEventListener('submit',function(e){e.preventDefault();
    var ord=$('ub-order').value.trim(),ph=$('ub-phone').value.replace(/\D/g,'').slice(-10),link=$('ub-link').value.trim();
    var bad=!/^pay_\w{6,}$/.test(ord)?'Please enter your order number (it starts with pay_).':!/^[6-9]\d{9}$/.test(ph)?'Please enter the 10-digit mobile number on your order.':!/^https:\/\/(www\.)?instagram\.com\/(reel|reels|p)\//.test(link)?'Please paste the link to your Instagram Reel.':'';
    if(bad){err.textContent=bad;err.hidden=false;return;}err.hidden=true;
    window.open('https://wa.me/919980881230?text='+encodeURIComponent('Hi GlutaNex, here is my unboxing Reel for the ₹150 reward.\n\nOrder: '+ord+'\nMobile: '+ph+'\nReel: '+link),'_blank','noopener');
  });
})();
