import re
from datetime import date

DOMAIN = "https://workers.dev"
TODAY = date.today().isoformat()
base = open("index.html", "r", encoding="utf-8").read()

new_pages = [
    ("ibps-sbi-po-clerk-photo-signature-resizer.html", "IBPS & SBI PO/Clerk Photo, Signature & Thumb Resizer", "Format IBPS & SBI photo (20KB-50KB, 200x230px), signature (10KB-20KB), and left thumb impression (20KB-50KB) offline."),
    ("rrb-ntpc-alp-group-d-photo-resizer.html", "RRB NTPC, ALP & Group D Photo & Signature Resizer", "Resize Railway RRB photo (20KB-50KB, 35x45mm) and signature (10KB-40KB) in exact JPG format."),
    ("gate-photo-signature-resizer.html", "GATE Photo & Signature Exact-KB Resizer (5KB-200KB)", "Compress GATE photograph (5KB-200KB) and signature (3KB-200KB) with white background offline."),
    ("cuet-ug-pg-photo-signature-compressor.html", "CUET UG & PG Photo, Signature & Certificate Compressor", "Resize NTA CUET photo (10KB-200KB), signature (4KB-30KB), and category PDF (50KB-300KB)."),
    ("tspsc-tgpsc-appsc-photo-signature-resizer.html", "TSPSC / TGPSC & APPSC Photo & Signature Resizer", "Format Telangana TGPSC & APPSC photo (under 50KB) and signature (under 30KB) offline in seconds."),
    ("nda-cds-afcat-photo-slate-maker.html", "NDA, CDS & AFCAT Photo Name & Date Slate Maker", "Create UPSC NDA/CDS photo (20KB-300KB, 350x350 to 1000x1000px) with printed Name & Date slate.")
]

for slug, title, desc in new_pages:
    h = re.sub(r"<title>.*?</title>", f"<title>{title} | ExamDocPro</title>", base, flags=re.DOTALL)
    h = h.replace("</head>", f'<meta name="description" content="{desc}"><link rel="canonical" href="{DOMAIN}/{slug}"></head>')
    sec = f'<section style="max-width:920px;margin:18px auto;padding:18px;background:#161b22;border:1px solid #30363d;border-radius:12px;color:#e6edf3;"><h1>{title}</h1><p>{desc}</p></section>'
    h = h.replace("<footer", sec + "\n<footer")
    open(slug, "w", encoding="utf-8").write(h)

import glob
all_html = sorted(glob.glob("*.html"))
urls = [f"{DOMAIN}/"] + [f"{DOMAIN}/{f}" for f in all_html if f != "index.html" and not f.startswith("google")]
xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://sitemaps.org">\n' + "\n".join(f"  <url><loc>{u}</loc><lastmod>{TODAY}</lastmod></url>" for u in urls) + "\n</urlset>"
open("sitemap.xml", "w", encoding="utf-8").write(xml)
print("Chunk 3: 6 more SEO pages + updated sitemap.xml done!")
