/* GlutaNex app: keeps the shop fast and usable on weak connections. Version 944aaf7889 */
var V='gn-944aaf7889', CORE=["/", "/offline/", "/shop/", "/glutathione/", "/assets/site.css?v=dc54f20d82", "/assets/store.js?v=dc54f20d82", "/assets/jar3d.js?v=dc54f20d82", "/assets/products.json", "/assets/img/glutanex-glutathione-night-cream-jar.webp", "/assets/img/glutanex-logo-dark.png", "/assets/img/glutanex-logo-light.png", "/assets/whatsapp-glyph-green.svg", "/icon-192.png", "/assets/fonts/manrope.woff", "/assets/fonts/cormorant.woff"];
self.addEventListener('install',function(e){e.waitUntil(caches.open(V).then(function(c){return c.addAll(CORE);}).then(function(){return self.skipWaiting();}));});
self.addEventListener('activate',function(e){e.waitUntil(caches.keys().then(function(ks){return Promise.all(ks.filter(function(k){return k!==V;}).map(function(k){return caches.delete(k);}));}).then(function(){return self.clients.claim();}));});
self.addEventListener('push',function(e){var d={};try{d=e.data?e.data.json():{};}catch(x){d={body:e.data?e.data.text():''};}
  e.waitUntil(self.registration.showNotification(d.title||'GlutaNex',{body:d.body||'',icon:'/icon-192.png',badge:'/icon-192.png',tag:d.tag||'gn',data:{url:d.url||'/'}}));});
self.addEventListener('notificationclick',function(e){e.notification.close();var url=(e.notification.data&&e.notification.data.url)||'/';
  e.waitUntil(clients.matchAll({type:'window',includeUncontrolled:true}).then(function(cs){for(var i=0;i<cs.length;i++){if('focus' in cs[i]){cs[i].navigate(url);return cs[i].focus();}}return clients.openWindow(url);}));});
self.addEventListener('fetch',function(e){
  var r=e.request,u=new URL(r.url);
  if(r.method!=='GET'){return;}
  if(u.origin===location.origin&&(u.pathname.indexOf('/api/')===0||/^\/(checkout|leads)\//.test(u.pathname))){return;}
  if(u.origin!==location.origin&&!/fonts\.(googleapis|gstatic)\.com$/.test(u.hostname)){return;}
  if(r.mode==='navigate'){
    e.respondWith(fetch(r).then(function(res){var cp=res.clone();caches.open(V).then(function(c){c.put(r,cp);});return res;}).catch(function(){return caches.match(r).then(function(m){return m||caches.match('/offline/');});}));
    return;}
  e.respondWith(caches.match(r).then(function(m){var net=fetch(r).then(function(res){if(res&&(res.ok||res.type==='opaque')){var cp=res.clone();caches.open(V).then(function(c){c.put(r,cp);});}return res;}).catch(function(){return m;});return m||net;}));
});
