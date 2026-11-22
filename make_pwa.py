manifest = """{
  "name": "ExamDocPro - Offline Exam Document Formatter",
  "short_name": "ExamDocPro",
  "start_url": "/index.html",
  "display": "standalone",
  "background_color": "#0d1117",
  "theme_color": "#2563eb"
}"""
open("manifest.json", "w").write(manifest)

sw = """self.addEventListener('install', e => {
  e.waitUntil(caches.open('examdocpro-v1').then(c => c.addAll(['/','/index.html','/assets/css/style.css','/assets/js/engine.js','/assets/js/pdf_engine.js'])));
});
self.addEventListener('fetch', e => {
  e.respondWith(caches.match(e.request).then(r => r || fetch(e.request)));
});"""
open("sw.js", "w").write(sw)

html = open("index.html", "r", encoding="utf-8").read()
if "manifest.json" not in html:
    pwa_tags = '<link rel="manifest" href="manifest.json">\n<script>if("serviceWorker" in navigator){navigator.serviceWorker.register("sw.js");}</script>\n</head>'
    html = html.replace("</head>", pwa_tags)
    open("index.html", "w", encoding="utf-8").write(html)
print("Upgrade 2: Offline PWA App ready!")
