const PRESETS = {
  jee_photo:  { w: 413, h: 531, minKb: 15, maxKb: 180, slate: false },
  jee_sign:   { w: 413, h: 177, minKb: 6,  maxKb: 28,  slate: false },
  upsc_photo: { w: 500, h: 500, minKb: 25, maxKb: 250, slate: true  },
  ssc_photo:  { w: 413, h: 531, minKb: 22, maxKb: 48,  slate: false },
  ssc_sign:   { w: 472, h: 236, minKb: 11, maxKb: 19,  slate: false },
  pan_photo:  { w: 213, h: 213, minKb: 10, maxKb: 48,  slate: false }
};

let cropper = null;
const presetSelect = document.getElementById("presetSelect");
const widthInput = document.getElementById("widthInput");
const heightInput = document.getElementById("heightInput");
const minKbInput = document.getElementById("minKbInput");
const maxKbInput = document.getElementById("maxKbInput");
const addSlateCheck = document.getElementById("addSlateCheck");
const slateFields = document.getElementById("slateFields");
const fileInput = document.getElementById("fileInput");

function updateCropAspect() {
  if (!cropper) return;
  const w = parseInt(widthInput.value, 10) || 413;
  const h = parseInt(heightInput.value, 10) || 531;
  const slateH = addSlateCheck.checked ? Math.round(h * 0.18) : 0;
  cropper.setAspectRatio(w / (h - slateH));
}

presetSelect.addEventListener("change", () => {
  const p = PRESETS[presetSelect.value];
  if (!p) return;
  widthInput.value = p.w;
  heightInput.value = p.h;
  minKbInput.value = p.minKb;
  maxKbInput.value = p.maxKb;
  addSlateCheck.checked = p.slate;
  slateFields.classList.toggle("hidden", !p.slate);
  updateCropAspect();
});

addSlateCheck.addEventListener("change", () => {
  slateFields.classList.toggle("hidden", !addSlateCheck.checked);
  updateCropAspect();
});

fileInput.addEventListener("change", () => {
  if (!fileInput.files || fileInput.files.length === 0) return;
  const file = fileInput.files.item(0);
  const cropWrap = document.getElementById("cropContainer");
  const cropImg = document.getElementById("cropImage");
  cropImg.src = URL.createObjectURL(file);
  cropWrap.classList.remove("hidden");

  if (cropper) cropper.destroy();
  if (typeof Cropper !== "undefined") {
    cropper = new Cropper(cropImg, {
      viewMode: 1,
      dragMode: "move",
      autoCropArea: 0.9,
      responsive: true
    });
    updateCropAspect();
  }
});

async function canvasToBlob(canvas, quality) {
  return new Promise((resolve) => canvas.toBlob(resolve, "image/jpeg", quality));
}

async function compressToExactRange(canvas, minKb, maxKb) {
  let low = 0.05, high = 0.98;
  let bestBlob = await canvasToBlob(canvas, 0.85);
  for (let i = 0; i < 10; i++) {
    const mid = (low + high) / 2;
    const blob = await canvasToBlob(canvas, mid);
    const sizeKb = blob.size / 1024;
    bestBlob = blob;
    if (sizeKb >= minKb && sizeKb <= maxKb) break;
    if (sizeKb > maxKb) high = mid; else low = mid;
  }
  return bestBlob;
}

document.getElementById("processBtn").addEventListener("click", async () => {
  if (!fileInput.files || fileInput.files.length === 0) {
    alert("Please select an image file first.");
    return;
  }

  const targetW = parseInt(widthInput.value, 10);
  const targetH = parseInt(heightInput.value, 10);
  const minKb = parseFloat(minKbInput.value);
  const maxKb = parseFloat(maxKbInput.value);
  const useSlate = addSlateCheck.checked;
  const slateHeight = useSlate ? Math.round(targetH * 0.18) : 0;
  const photoAreaH = targetH - slateHeight;

  const canvas = document.createElement("canvas");
  canvas.width = targetW;
  canvas.height = targetH;
  const ctx = canvas.getContext("2d");

  ctx.fillStyle = "#FFFFFF";
  ctx.fillRect(0, 0, targetW, targetH);

  if (cropper) {
    const cropped = cropper.getCroppedCanvas({ width: targetW, height: photoAreaH, fillColor: "#FFFFFF" });
    ctx.drawImage(cropped, 0, 0, targetW, photoAreaH);
  } else {
    const img = new Image();
    img.src = URL.createObjectURL(fileInput.files.item(0));
    await img.decode();
    ctx.drawImage(img, 0, 0, targetW, photoAreaH);
  }

  if (useSlate) {
    ctx.fillStyle = "#FFFFFF";
    ctx.fillRect(0, photoAreaH, targetW, slateHeight);
    ctx.strokeStyle = "#000000";
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.moveTo(0, photoAreaH);
    ctx.lineTo(targetW, photoAreaH);
    ctx.stroke();

    const nameText = (document.getElementById("candidateName").value || "CANDIDATE NAME").toUpperCase();
    const dateText = document.getElementById("photoDate").value || "DOP: DD-MM-YYYY";
    const fontSize = Math.max(11, Math.round(slateHeight * 0.34));

    ctx.fillStyle = "#000000";
    ctx.font = `bold ${fontSize}px Arial, sans-serif`;
    ctx.textAlign = "center";
    ctx.fillText(nameText, targetW / 2, photoAreaH + slateHeight * 0.44);
    ctx.fillText(dateText, targetW / 2, photoAreaH + slateHeight * 0.84);
  }

  const finalBlob = await compressToExactRange(canvas, minKb, maxKb);
  const finalKb = (finalBlob.size / 1024).toFixed(2);
  const url = URL.createObjectURL(finalBlob);

  document.getElementById("previewBox").innerHTML = `<img src="${url}" class="max-h-full max-w-full rounded shadow" />`;
  document.getElementById("outDims").textContent = `${targetW} × ${targetH} px`;
  document.getElementById("outSize").textContent = `${finalKb} KB`;

  const dl = document.getElementById("downloadLink");
  dl.href = url;
  dl.download = `${presetSelect.value}_${Math.round(finalKb)}KB.jpg`;
  document.getElementById("resultStats").classList.remove("hidden");
});
