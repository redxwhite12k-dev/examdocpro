self.addEventListener("install", e => e.waitUntil(caches.open("edp-v1").then(c => c.addAll(["/","/index.html","/assets/css/style.css","/assets/js/engine.js","/assets/js/pdf_engine.js","/assets/js/exams_pro.js"]))));
self.addEventListener("fetch", e => e.respondWith(caches.match(e.request).then(r => r || fetch(e.request))));
