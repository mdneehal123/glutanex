/* GlutaNex skin quiz: five taps, an honest routine, and a ready cart. Runs entirely in the browser;
   nothing is sent anywhere. The result can be shared as a link (?r=code). Cart buttons use the store's
   data-add / data-buy handlers. */
(function(){
  'use strict';
  var root=document.getElementById('quiz');if(!root){return;}
  var Q=[
    {k:'skin',q:'What is your skin type?',o:[['oily','Oily','Shiny by afternoon'],['dry','Dry','Feels tight, can flake'],['combo','Combination','Oily T-zone, dry cheeks'],['normal','Normal','Mostly comfortable'],['sens','Sensitive','Stings or reddens easily']]},
    {k:'goal',q:'What bothers you most?',o:[['tan','Sun tan','Darker after time outdoors'],['spots','Dark spots','Patches or pigmentation'],['dull','Dull skin','Looks tired, no glow'],['marks','Acne marks','Dark marks left by pimples'],['uneven','Uneven tone','Different shades across the face']]},
    {k:'use',q:'Are you using any of these now?',o:[['rx','A prescription cream','Tretinoin, adapalene or a cream from a doctor'],['acid','Exfoliating acids or peels','AHA, BHA, glycolic, peels'],['vitc','Vitamin C serum',''],['none','None of these','Just basics, or nothing']]},
    {k:'preg',q:'Are you pregnant, breastfeeding or planning a pregnancy?',o:[['no','No',''],['yes','Yes','']]},
    {k:'want',q:'How many steps do you want?',o:[['one','Just one product','Night cream only'],['two','A full routine','Face wash + night cream']]}
  ];
  var A={},i=0;
  function el(t,c,x){var e=document.createElement(t);if(c){e.className=c;}if(x!=null){e.textContent=x;}return e;}
  function code(){return Q.map(function(q){return A[q.k];}).join('-');}
  function decode(s){var p=String(s||'').split('-');if(p.length!==Q.length){return false;}for(var n=0;n<Q.length;n++){if(!Q[n].o.some(function(o){return o[0]===p[n];})){return false;}A[Q[n].k]=p[n];}return true;}

  function step(){
    root.textContent='';var card=el('div','qz-card');
    var bar=el('div','qz-bar');var fill=el('i');fill.style.width=((i)/Q.length*100)+'%';bar.appendChild(fill);card.appendChild(bar);
    card.appendChild(el('p','qz-n','Question '+(i+1)+' of '+Q.length));
    var q=Q[i];card.appendChild(el('h2','qz-q',q.q));
    var list=el('div','qz-opts');
    q.o.forEach(function(o){var b=el('button','qz-opt'+(A[q.k]===o[0]?' on':''));b.type='button';b.appendChild(el('b',null,o[1]));if(o[2]){b.appendChild(el('span',null,o[2]));}
      b.addEventListener('click',function(){A[q.k]=o[0];if(i<Q.length-1){i++;step();}else{result(true);}});list.appendChild(b);});
    card.appendChild(list);
    if(i>0){var back=el('button','qz-back','← Back');back.type='button';back.addEventListener('click',function(){i--;step();});card.appendChild(back);}
    root.appendChild(card);
    var top=root.getBoundingClientRect().top+window.scrollY-90;if(window.scrollY>top){window.scrollTo({top:top,behavior:'smooth'});}
  }

  function li(ul,html){var x=el('li');x.innerHTML=html;ul.appendChild(x);}
  var GUIDE={tan:['/glutathione-cream-for-summer-tan/','Summer tan routine'],spots:['/glutathione-for-dark-spots-and-tan/','Dark spots and tan'],dull:['/glutathione-benefits-for-skin/','Glutathione benefits for skin'],
    marks:['/glutathione-for-acne-marks/','Glutathione for acne marks'],uneven:['/glutathione-and-niacinamide/','Glutathione and niacinamide']};
  var SKIN={oily:['/glutathione-for-oily-skin/','Glutathione for oily skin'],dry:['/glutathione-cream-in-winter/','Routine for dry skin'],sens:['/glutathione-side-effects/','Side effects and patch testing']};

  function result(fresh){
    root.textContent='';var card=el('div','qz-card qz-res');
    card.appendChild(el('p','qz-n','Your result'));
    var preg=A.preg==='yes',rx=A.use==='rx';
    if(preg){
      card.appendChild(el('h2','qz-q','Talk to your doctor first'));
      card.appendChild(el('p','qz-lead','Glutathione has not been well studied in pregnancy or breastfeeding, and the GlutaNex Night Cream contains retinol, which is usually avoided. We do not recommend it for you right now.'));
      var u=el('ul','qz-list');li(u,'<b>Safe basics:</b> a gentle cleanser, a simple moisturiser and sunscreen every morning.');li(u,'Pregnancy can make dark patches (melasma) more likely, so daily sunscreen matters even more.');li(u,'Ask your doctor before adding any active ingredient.');card.appendChild(u);
      var a=el('a','btn ghost block','Read: glutathione in pregnancy');a.href='/glutathione-in-pregnancy/';card.appendChild(a);
    } else {
      var duo=A.want==='two'&&!rx;
      card.appendChild(el('h2','qz-q',rx?'Check with your dermatologist first':duo?'Your routine: the Glow Duo':'Your routine: the Night Cream'));
      card.appendChild(el('p','qz-lead',rx?'You are already using a prescription cream. The GlutaNex Night Cream contains retinol and salicylic acid, so using both can irritate. Ask your dermatologist before adding it.':
        'Glutathione with niacinamide and vitamin C, used at night with sunscreen every morning, can help '+({tan:'tan',spots:'dark spots',dull:'dull skin',marks:'acne marks',uneven:'uneven tone'}[A.goal])+' look lighter and more even over 8 to 12 weeks.'));
      var r=el('ul','qz-list');
      if(!rx){
        li(r,'<b>Night:</b> '+(duo?'cleanse with the Gluta Boost Face Wash, pat dry, then':'cleanse gently, pat dry, then')+' a pea-sized amount of Night Cream on face and neck.');
        li(r,'<b>Morning:</b> sunscreen SPF 30 or higher'+(A.goal==='tan'?', reapplied every 2–3 hours outdoors.':', every day.'));
        var start=A.skin==='sens'?'1–2 nights a week for two weeks':'2–3 nights a week for two weeks';
        li(r,'<b>Start slowly:</b> '+start+', then every other night, then nightly if your skin is comfortable.');
        if(A.skin==='sens'){li(r,'<b>Patch test first:</b> a little behind the ear for 24 hours before using it on your face.');}
        if(A.skin==='dry'){li(r,'<b>Dry skin:</b> add a plain moisturiser on top of the cream.');}
        if(A.skin==='oily'||A.skin==='combo'){li(r,'<b>Oily areas:</b> a thin layer is enough; use a matte sunscreen in the morning.');}
        if(A.use==='acid'){li(r,'<b>Acids or peels:</b> use the Night Cream on different nights from your acids, never on the same night.');}
        if(A.use==='vitc'){li(r,'<b>Vitamin C:</b> keep it for the morning under sunscreen; Night Cream at night.');}
        if(A.goal==='marks'){li(r,'<b>Acne marks:</b> treat active pimples first, and do not pick them.');}
      } else {
        li(r,'Keep following your dermatologist\'s routine, with sunscreen every morning.');li(r,'If they agree, the Night Cream is usually used on different nights from your prescription cream.');
      }
      li(r,'<b>Give it time:</b> a fresher look in 4–8 weeks, lighter tan and marks in 8–12 weeks. It does not change your natural skin colour.');
      card.appendChild(r);
      var acts=el('div','qz-acts');
      if(!rx){var buy=el('button','btn block',duo?'Get the Glow Duo':'Get the Night Cream');buy.type='button';buy.setAttribute('data-buy',duo?'duo':'cream');acts.appendChild(buy);
        var add=el('button','btn ghost block','Add to cart');add.type='button';add.setAttribute('data-add',duo?'duo':'cream');acts.appendChild(add);}
      card.appendChild(acts);
      var reads=el('p','qz-reads');reads.appendChild(document.createTextNode('Read next: '));[GUIDE[A.goal],SKIN[A.skin]].filter(Boolean).forEach(function(g,n){if(n){reads.appendChild(document.createTextNode(' · '));}var a2=el('a',null,g[1]);a2.href=g[0];reads.appendChild(a2);});card.appendChild(reads);
    }
    var url=location.origin+'/skin-quiz/?r='+code();
    var foot=el('div','qz-foot');var sh=el('a','btn wa sm','Share on WhatsApp');sh.href='https://wa.me/?text='+encodeURIComponent('My GlutaNex skin quiz result: '+url);sh.target='_blank';sh.rel='noopener';foot.appendChild(sh);
    var again=el('button','qz-back','Start again');again.type='button';again.addEventListener('click',function(){A={};i=0;history.replaceState(null,'','/skin-quiz/');step();});foot.appendChild(again);card.appendChild(foot);
    root.appendChild(card);
    if(fresh){history.replaceState(null,'','/skin-quiz/?r='+code());var top=root.getBoundingClientRect().top+window.scrollY-90;window.scrollTo({top:top,behavior:'smooth'});}
  }
  var m=/[?&]r=([a-z-]+)/.exec(location.search);if(m&&decode(m[1])){result(false);}else{step();}
})();
