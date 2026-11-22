html = open("index.html", "r", encoding="utf-8").read()

pro_widget = """
<section style="max-width:920px;margin:18px auto;padding:18px;background:#111827;border:1px solid #374151;border-radius:12px;color:#f3f4f6;">
  <h2 style="font-size:1.1rem;color:#60a5fa;margin-bottom:8px;">TSPSC / State PSC Combined Photo + Signature Sheet Maker</h2>
  <p style="font-size:0.85rem;color:#9ca3af;margin-bottom:12px;">Merge your passport photo (top) and signature (bottom) into one single JPG under 50KB—required for TSPSC/TGPSC, APPSC, and State PSC portals.</p>
  <div style="display:flex;flex-wrap:wrap;gap:10px;margin-bottom:12px;">
    <label style="font-size:0.82rem;">1. Select Photo: <input type="file" id="combPhoto" accept="image/*"></label>
    <label style="font-size:0.82rem;">2. Select Signature: <input type="file" id="combSign" accept="image/*"></label>
    <button type="button" onclick="mergePhotoSign()" style="background:#2563eb;color:#fff;border:none;padding:8px 16px;border-radius:8px;font-weight:700;cursor:pointer;">Merge &amp; Download Joint JPG</button>
  </div>
  <canvas id="combCanvas" width="275" height="430" style="display:none;"></canvas>
</section>
<script>
async function mergePhotoSign() {
  const pFile = document.getElementById('combPhoto').files;
  const sFile = document.getElementById('combSign').files;
  if (!pFile || !sFile) { alert('Please select both Photo and Signature files first.'); return; }
  const loadImg = f => new Promise(res => { const i = new Image(); i.onload = () => res(i); i.src = URL.createObjectURL(f); });
  const [pImg, sImg] = await Promise.all([loadImg(pFile), loadImg(sFile)]);
  const c = document.getElementById('combCanvas'), ctx = c.getContext('2d');
  ctx.fillStyle = '#ffffff'; ctx.fillRect(0, 0, 275, 430);
  ctx.drawImage(pImg, 12, 10, 250, 310);
  ctx.strokeStyle = '#cbd5e1'; ctx.strokeRect(12, 328, 250, 88);
  ctx.drawImage(sImg, 16, 332, 242, 80);
  let q = 0.9, dataUrl = c.toDataURL('image/jpeg', q);
  while (dataUrl.length * 0.75 > 48000 && q > 0.2) { q -= 0.08; dataUrl = c.toDataURL('image/jpeg', q); }
  const a = document.createElement('a'); a.href = dataUrl; a.download = 'ExamDocPro_Combined_Photo_Sign.jpg'; a.click();
}
</script>
"""

if "combCanvas" not in html and "<footer" in html:
    html = html.replace("<footer", pro_widget + "\n<footer")
    open("index.html", "w", encoding="utf-8").write(html)
print("Upgrade 1: Combined Photo+Sign Maker added!")
