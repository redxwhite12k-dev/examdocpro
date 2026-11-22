extra_css = """
/* Top-Notch SaaS Polish */
.preset-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(135px, 1fr)); gap: 8px; margin: 14px 0; }
.preset-chip { background: #1f2937; border: 1px solid #374151; color: #f3f4f6; padding: 8px 10px; border-radius: 8px; font-size: 0.82rem; font-weight: 600; cursor: pointer; transition: all 0.2s; text-align: center; }
.preset-chip:hover, .preset-chip.active { background: #2563eb; border-color: #3b82f6; color: #fff; transform: translateY(-1px); }
.trust-strip { display: flex; flex-wrap: wrap; justify-content: center; gap: 12px; margin: 12px auto 20px; font-size: 0.8rem; color: #9ca3af; }
.trust-badge { background: rgba(31,41,55,0.7); border: 1px solid #374151; padding: 5px 12px; border-radius: 999px; }
"""
with open("assets/css/style.css", "a", encoding="utf-8") as f:
    f.write(extra_css)
print("Chunk 1: SaaS CSS upgraded!")
