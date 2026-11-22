self.addEventListener('install', e => {
  e.waitUntil(caches.open('examdocpro-v1').then(c => c.addAll(['/','/index.html','/assets/css/style.css','/assets/js/engine.js','/assets/js/pdf_engine.js'])));
});
self.addEventListener('fetch', e => {
  e.respondWith(caches.match(e.request).then(r => r || fetch(e.request)));
});