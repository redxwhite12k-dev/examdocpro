DOMAIN = "https://examdocpro.redxwhite12k.workers.dev"

pages = {
    "about.html": ("About ExamDocPro", "<h2>About ExamDocPro</h2><p>ExamDocPro is a free, offline-first Indian exam document formatter for JEE Main, NEET UG, UPSC, SSC, and PAN applications. All processing happens 100% locally in your browser without uploading files to any server.</p>"),
    "privacy-policy.html": ("Privacy Policy - ExamDocPro", f"<h2>Privacy Policy</h2><p>ExamDocPro ({DOMAIN}) processes all photos, signatures, and PDF certificates locally on your device. Zero files are uploaded or stored on external servers.</p><p>We use Google AdSense to display ads. Google uses cookies to serve ads based on prior visits. You can opt out via Google Ads Settings.</p>"),
    "terms.html": ("Terms & Conditions - ExamDocPro", "<h2>Terms & Conditions</h2><p>ExamDocPro is provided as a free formatting utility. Always verify final pixel dimensions, DPI, and KB size against official NTA, UPSC, SSC, or NSDL notifications before final portal submission.</p>"),
    "contact.html": ("Contact - ExamDocPro", "<h2>Contact Us</h2><p>For support, bug reports, or new exam preset requests, email: <strong>redxwhite12k@gmail.com</strong></p>")
}

for fname, (title, body) in pages.items():
    html = f"""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0"><title>{title}</title><link rel="stylesheet" href="assets/css/style.css"><style>.box{{max-width:800px;margin:40px auto;padding:24px;background:#161b22;border:1px solid #30363d;border-radius:12px;color:#e6edf3;line-height:1.7}}.box a{{color:#58a6ff}}</style></head><body><div class="box"><p><a href="index.html">&larr; Back to Tool</a></p>{body}<hr style="border-color:#30363d;margin:20px 0"><p><a href="index.html">Home</a> | <a href="about.html">About</a> | <a href="privacy-policy.html">Privacy</a> | <a href="terms.html">Terms</a> | <a href="contact.html">Contact</a></p></div></body></html>"""
    open(fname, "w", encoding="utf-8").write(html)
print("Chunk 1 done!")
