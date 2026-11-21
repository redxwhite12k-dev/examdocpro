import re
from datetime import date

DOMAIN = "https://examdocpro.redxwhite12k.workers.dev"
TODAY = date.today().isoformat()
base = open("index.html", "r", encoding="utf-8").read()

footer = """<footer style="max-width:960px;margin:30px auto;padding:18px;border-top:1px solid #30363d;text-align:center;font-size:0.9rem;color:#8b949e;"><p><a href="jee-main-photo-signature-resizer.html" style="color:#58a6ff">JEE Main</a> | <a href="neet-ug-photo-postcard-compressor.html" style="color:#58a6ff">NEET UG</a> | <a href="upsc-photo-name-date-slate-maker.html" style="color:#58a6ff">UPSC</a> | <a href="ssc-cgl-chsl-photo-signature-tool.html" style="color:#58a6ff">SSC</a> | <a href="pan-card-nsdl-uti-photo-resizer.html" style="color:#58a6ff">PAN Card</a> | <a href="pdf-marksheet-compressor-under-300kb.html" style="color:#58a6ff">PDF Compressor</a></p><p><a href="about.html" style="color:#8b949e">About</a> | <a href="privacy-policy.html" style="color:#8b949e">Privacy Policy</a> | <a href="terms.html" style="color:#8b949e">Terms</a> | <a href="contact.html" style="color:#8b949e">Contact</a></p></footer>"""

if "privacy-policy.html" not in base:
    base = base.replace("</body>", footer + "\n</body>")
    open("index.html", "w", encoding="utf-8").write(base)

exams = [
    ("jee-main-photo-signature-resizer.html", "JEE Main Photo & Signature Resizer (10KB-200KB)", "Passport photo 10KB-200KB JPG, signature 4KB-30KB JPG, and Class 10/category certificate PDF 50KB-300KB."),
    ("neet-ug-photo-postcard-compressor.html", "NEET UG Passport & 4x6 Postcard Photo Resizer", "Passport & 4x6 postcard photo 10KB-200KB JPG, signature 4KB-30KB, and thumb impression 10KB-200KB."),
    ("upsc-photo-name-date-slate-maker.html", "UPSC Photo Resizer with Name & Date Slate (20KB-300KB)", "350x350 to 1000x1000 px JPG (20KB-300KB) with printed Name and Date slate at the bottom."),
    ("ssc-cgl-chsl-photo-signature-tool.html", "SSC CGL, CHSL & GD Photo & Signature Resizer", "Photo 20KB-50KB (3.5x4.5 cm) and signature 10KB-20KB (4.0x2.0 cm) in JPEG format."),
    ("pan-card-nsdl-uti-photo-resizer.html", "PAN Card Photo & Signature Resizer (NSDL & UTI)", "Photo 213x213 px under 30KB (300 DPI) and signature under 50KB-60KB for NSDL/Protean & UTIITSL."),
    ("pdf-marksheet-compressor-under-300kb.html", "PDF Marksheet & Certificate Compressor (50KB-300KB)", "Compress PDF marksheets and certificates between 50KB and 300KB offline without uploading.")
]

urls = [f"{DOMAIN}/", f"{DOMAIN}/about.html", f"{DOMAIN}/privacy-policy.html", f"{DOMAIN}/terms.html", f"{DOMAIN}/contact.html"]

for slug, title, info in exams:
    h = re.sub(r"<title>.*?</title>", f"<title>{title} | ExamDocPro</title>", base, flags=re.DOTALL)
    h = h.replace("</head>", f'<meta name="description" content="{info}"><link rel="canonical" href="{DOMAIN}/{slug}"></head>')
    sec = f'<section style="max-width:960px;margin:20px auto;padding:20px;background:#161b22;border:1px solid #30363d;border-radius:12px;color:#e6edf3;"><h1>{title}</h1><p>{info}</p></section>'
    h = h.replace("<footer", sec + "\n<footer")
    open(slug, "w", encoding="utf-8").write(h)
    urls.append(f"{DOMAIN}/{slug}")

xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://sitemaps.org">\n' + "\n".join(f"  <url><loc>{u}</loc><lastmod>{TODAY}</lastmod></url>" for u in urls) + "\n</urlset>"
open("sitemap.xml", "w", encoding="utf-8").write(xml)
open("robots.txt", "w", encoding="utf-8").write(f"User-agent: *\nAllow: /\nSitemap: {DOMAIN}/sitemap.xml\n")
print("Chunk 2 done!")
