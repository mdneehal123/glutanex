/* GlutaNex app: keeps the shop fast and usable on weak connections. Version 834c4f4050 */
var V='gn-834c4f4050', CORE=["/", "/offline/", "/shop/", "/glutathione/", "/assets/site.css", "/assets/store.js", "/assets/jar3d.js", "/assets/products.json", "/assets/img/jar-cut.webp", "/assets/img/glutanex-logo-dark.png", "/assets/img/glutanex-logo-light.png", "/assets/whatsapp-glyph-green.svg", "/icon-192.png"];
self.addEventListener('install',function(e){e.waitUntil(caches.open(V).then(function(c){return c.addAll(CORE);}).then(function(){return self.skipWaiting();}));});
self.addEventListener('activate',function(e){e.waitUntil(caches.keys().then(function(ks){return Promise.all(ks.filter(function(k){return k!==V;}).map(function(k){return caches.delete(k);}));}).then(function(){return self.clients.claim();}));});
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
