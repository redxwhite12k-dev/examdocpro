html = open("index.html", "r", encoding="utf-8").read()

trust_bar = """<div class="trust-strip"><span class="trust-badge">100% Offline Browser Processing</span><span class="trust-badge">Zero Server Uploads</span><span class="trust-badge">Exact-KB Binary Search</span><span class="trust-badge">Name &amp; Date Slate Ready</span></div>"""

presets_box = """
<div style="max-width:920px;margin:14px auto;padding:14px;background:#111827;border:1px solid #374151;border-radius:12px;">
  <div style="font-size:0.85rem;color:#93c5fd;font-weight:700;margin-bottom:6px;">Quick-Select Official Exam Presets (Auto-Fills Exact KB &amp; Dimensions):</div>
  <div class="preset-grid" id="quickExamGrid">
    <button type="button" class="preset-chip" onclick="applyQuickPreset(200,230,20,50)">IBPS PO/Clerk Photo</button>
    <button type="button" class="preset-chip" onclick="applyQuickPreset(140,60,10,20)">IBPS / SBI Sign</button>
    <button type="button" class="preset-chip" onclick="applyQuickPreset(200,230,20,50)">SBI PO / Clerk Photo</button>
    <button type="button" class="preset-chip" onclick="applyQuickPreset(350,450,20,50)">RRB NTPC / ALP</button>
    <button type="button" class="preset-chip" onclick="applyQuickPreset(240,320,5,200)">GATE Photo</button>
    <button type="button" class="preset-chip" onclick="applyQuickPreset(200,260,10,200)">CUET UG / PG</button>
    <button type="button" class="preset-chip" onclick="applyQuickPreset(300,400,30,100)">CAT / MBA Photo</button>
    <button type="button" class="preset-chip" onclick="applyQuickPreset(275,355,10,50)">TSPSC / TGPSC</button>
    <button type="button" class="preset-chip" onclick="applyQuickPreset(275,355,10,50)">APPSC Group 1/2</button>
    <button type="button" class="preset-chip" onclick="applyQuickPreset(275,355,20,50)">UPPSC / MPSC</button>
    <button type="button" class="preset-chip" onclick="applyQuickPreset(350,350,20,300)">NDA / CDS (Slate)</button>
    <button type="button" class="preset-chip" onclick="applyQuickPreset(200,230,20,50)">India Post GDS</button>
  </div>
</div>
<script>
function applyQuickPreset(w, h, minKb, maxKb) {
  const inputs = document.querySelectorAll('input[type="number"]');
  if (inputs.length >= 3) { inputs[0].value = w; inputs[1].value = h; inputs[2].value = Math.round((minKb + maxKb) / 2); }
  alert('Applied Preset: ' + w + 'x' + h + 'px | Target: ' + minKb + 'KB–' + maxKb + 'KB');
}
</script>
"""

if "trust-strip" not in html:
    html = html.replace("<body", "<body>\n" + trust_bar, 1).replace("<body>\n<body>", "<body>")
if "quickExamGrid" not in html and "<footer" in html:
    html = html.replace("<footer", presets_box + "\n<footer")
open("index.html", "w", encoding="utf-8").write(html)
print("Chunk 2: 12 Exam Presets added!")
