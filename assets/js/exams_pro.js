window.EXAM_PRESETS_PRO = [
  { id: "jee", name: "JEE Main (Photo 10-200KB)", w: 350, h: 450, minK: 10, maxK: 200, dpi: 200 },
  { id: "neet", name: "NEET UG Postcard (4x6 in)", w: 400, h: 600, minK: 10, maxK: 200, dpi: 200 },
  { id: "upsc", name: "UPSC CSE / NDA (20-300KB)", w: 500, h: 500, minK: 20, maxK: 300, dpi: 300 },
  { id: "ssc", name: "SSC CGL / CHSL / GD (20-50KB)", w: 350, h: 450, minK: 20, maxK: 50, dpi: 200 },
  { id: "tgpsc", name: "TGPSC / TSPSC Telangana (10-50KB)", w: 350, h: 450, minK: 10, maxK: 50, dpi: 200 },
  { id: "appsc", name: "APPSC Andhra Pradesh (10-50KB)", w: 350, h: 450, minK: 10, maxK: 50, dpi: 200 },
  { id: "ibps", name: "IBPS / SBI Bank PO & Clerk (20-50KB)", w: 200, h: 230, minK: 20, maxK: 50, dpi: 200 },
  { id: "rrb", name: "RRB Railway NTPC / Group D (20-50KB)", w: 350, h: 450, minK: 20, maxK: 50, dpi: 200 },
  { id: "gate", name: "GATE / CUET UG (5-200KB)", w: 480, h: 640, minK: 5, maxK: 200, dpi: 300 },
  { id: "pan", name: "PAN Card NSDL / UTI (213x213 px)", w: 213, h: 213, minK: 5, maxK: 30, dpi: 300 },
  { id: "sig", name: "Universal Signature (4-20KB)", w: 400, h: 200, minK: 4, maxK: 20, dpi: 200 }
];
document.addEventListener("DOMContentLoaded", () => {
  const sel = document.querySelector("select");
  if (sel && window.EXAM_PRESETS_PRO) {
    sel.innerHTML = window.EXAM_PRESETS_PRO.map(p =>
      `<option value="${p.id}" data-w="${p.w}" data-h="${p.h}" data-min="${p.minK}" data-max="${p.maxK}">${p.name}</option>`
    ).join("");
  }
  const url = location.pathname.toLowerCase();
  const match = window.EXAM_PRESETS_PRO.find(p => url.includes(p.id));
  if (match && sel) { sel.value = match.id; sel.dispatchEvent(new Event("change")); }
});
