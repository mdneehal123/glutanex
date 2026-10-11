/* GlutaNex hero jar: the real product photo on a 3D stage.
   The jar tilts with the pointer (or a finger drag), floats, catches a moving light,
   and a gold orbit with a glowing dot passes behind and in front of it. No library. */
(function(){
  'use strict';
  function el(tag,cls,parent){var e=document.createElement(tag);if(cls){e.className=cls;}if(parent){parent.appendChild(e);}return e;}
  function build(stage){
    var src=stage.getAttribute('data-src'), alt=stage.getAttribute('data-alt')||'';
    var still=window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    stage.style.setProperty('--jar','url("'+new URL(src,location.href).href+'")');
    el('div','j3-glow',stage);
    el('div','j3-ring j3-back',stage);
    var dot=el('i','j3-dot',stage);
    var shadow=el('div','j3-shadow',stage);
    var scene=el('div','j3-scene',stage);
    var tiltEl=el('div','j3-tilt',scene);
    var img=stage.querySelector('.j3-seed');if(img){img.classList.remove('j3-seed');tiltEl.appendChild(img);}else{img=el('img','j3-img',tiltEl);img.src=src;img.alt=alt;img.decoding='async';}img.draggable=false;
    el('div','j3-sweep',tiltEl);
    /* ingredient hotspots: dots ride on the jar; tapping one opens a small card */
    var spots=[];try{spots=JSON.parse(stage.getAttribute('data-spots')||'[]');}catch(e){spots=[];}
    var card=el('div','j3-card',stage),openDot=null;card.hidden=true;card.setAttribute('role','status');
    function place(){if(!openDot){return;}var sr=stage.getBoundingClientRect(),dr=openDot.getBoundingClientRect(),cw=card.offsetWidth,ch=card.offsetHeight;
      var x=dr.left+dr.width/2-sr.left,y=dr.top-sr.top,left=Math.max(8,Math.min(sr.width-cw-8,x-cw/2)),top=y-ch-12;if(top<4){top=y+dr.height+12;card.classList.add('below');}else{card.classList.remove('below');}
      card.style.left=left+'px';card.style.top=top+'px';card.style.setProperty('--ax',Math.max(14,Math.min(cw-14,x-left))+'px');}
    function close(){var hs=stage.parentNode;if(hs){hs.classList.remove('spot-open');}if(openDot){openDot.classList.remove('on');openDot.setAttribute('aria-expanded','false');}openDot=null;card.hidden=true;}
    spots.forEach(function(sp,i){var b=el('button','j3-dot-spot',tiltEl);b.type='button';b.style.left=sp.x+'%';b.style.top=sp.y+'%';b.style.animationDelay=(i*0.35)+'s';
      b.setAttribute('aria-label',sp.n);b.setAttribute('aria-expanded','false');
      b.addEventListener('pointerdown',function(e){e.stopPropagation();});
      b.addEventListener('click',function(e){e.stopPropagation();if(openDot===b){close();return;}close();openDot=b;b.classList.add('on');b.setAttribute('aria-expanded','true');
        card.innerHTML='';var t=document.createElement('b');t.textContent=sp.n;var d=document.createElement('span');d.textContent=sp.d;card.appendChild(t);card.appendChild(d);card.hidden=false;if(stage.parentNode){stage.parentNode.classList.add('spot-open');}place();});});
    document.addEventListener('click',function(e){if(openDot&&!card.contains(e.target)){close();}});
    document.addEventListener('keydown',function(e){if(e.key==='Escape'){close();}});
    var refl=el('img','j3-reflect',scene);refl.src=src;refl.alt='';refl.setAttribute('aria-hidden','true');refl.draggable=false;
    el('div','j3-ring j3-front',stage);
    for(var s=0;s<7;s++){var sp=el('i','j3-spark',stage);sp.style.left=(12+Math.random()*76)+'%';sp.style.top=(10+Math.random()*70)+'%';sp.style.animationDelay=(Math.random()*5)+'s';sp.style.animationDuration=(3.5+Math.random()*3)+'s';}

    var rx=0,ry=0,tx=0,ty=0,vx=0,vy=0,dragging=false,hover=false,sx=0,sy=0,bx=0,by=0,t0=performance.now(),orbit=0;
    function frame(now){
      var t=(now-t0)/1000;
      /* gentle idle sway when nobody is touching it */
      if(!dragging&&!hover&&!still&&!openDot){ty=Math.sin(t*0.55)*16;tx=-5+Math.sin(t*0.8)*4;}else if(openDot&&!dragging){tx=0;ty=0;}
      /* springy follow */
      vx+=(tx-rx)*0.08;vy+=(ty-ry)*0.08;vx*=0.78;vy*=0.78;rx+=vx;ry+=vy;
      var fl=still?0:Math.sin(t*1.4)*8, sc=still?0:Math.min(1,Math.max(0,window.scrollY/700));
      tiltEl.style.transform='translateY('+(-fl+sc*60).toFixed(1)+'px) rotateX('+(rx+sc*14).toFixed(2)+'deg) rotateY('+(ry+sc*24).toFixed(2)+'deg) scale('+(1-sc*0.12).toFixed(3)+')';
      tiltEl.style.setProperty('--lx',(50+ry*2.4).toFixed(1)+'%');
      refl.style.transform='translateX(-50%) translateY('+(fl*0.6).toFixed(1)+'px) rotateY('+ry.toFixed(2)+'deg) scaleY(-1)';
      shadow.style.transform='translateX(-50%) scale('+(1-fl*0.012).toFixed(3)+')';
      shadow.style.opacity=(0.85-fl*0.02).toFixed(2);
      /* orbiting dot: behind the jar on the far half, in front on the near half */
      if(!still){orbit+=0.006;}
      var c=Math.cos(orbit),sn=Math.sin(orbit),R=Math.min(stage.clientWidth*0.44,300);
      dot.style.transform='translate('+(c*R).toFixed(1)+'px,'+(sn*R*0.2).toFixed(1)+'px) scale('+(0.75+0.35*(sn+1)/2).toFixed(2)+')';
      dot.style.zIndex=sn>0?6:1;
      if(openDot){place();}
      requestAnimationFrame(frame);
    }
    requestAnimationFrame(frame);

    /* pointer: tilt toward the cursor; drag: stronger tilt that springs back on release */
    stage.addEventListener('pointermove',function(e){
      var r=stage.getBoundingClientRect(),px=(e.clientX-r.left)/r.width-0.5,py=(e.clientY-r.top)/r.height-0.5;
      if(dragging){ty=Math.max(-38,Math.min(38,by+(e.clientX-sx)*0.25));tx=Math.max(-22,Math.min(22,bx-(e.clientY-sy)*0.15));return;}
      if(e.pointerType==='mouse'){hover=true;ty=px*30;tx=-py*18;}
    });
    stage.addEventListener('pointerdown',function(e){dragging=true;sx=e.clientX;sy=e.clientY;bx=tx;by=ty;stage.classList.add('grab');try{stage.setPointerCapture(e.pointerId);}catch(err){}});
    function up(){if(!dragging){return;}dragging=false;stage.classList.remove('grab');tx=0;ty=0;}
    stage.addEventListener('pointerup',up);stage.addEventListener('pointercancel',up);
    stage.addEventListener('pointerleave',function(e){if(e.pointerType==='mouse'&&!dragging){hover=false;}});
  }
  [].slice.call(document.querySelectorAll('[data-jar3d]')).forEach(build);
})();
