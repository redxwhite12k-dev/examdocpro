const tabPhoto = document.getElementById("tabPhoto");
const tabPdf = document.getElementById("tabPdf");
const photoSection = document.getElementById("photoSection");
const pdfSection = document.getElementById("pdfSection");

tabPhoto.addEventListener("click", () => {
  tabPhoto.classList.add("active");
  tabPdf.classList.remove("active");
  photoSection.classList.remove("hidden");
  pdfSection.classList.add("hidden");
});

tabPdf.addEventListener("click", () => {
  tabPdf.classList.add("active");
  tabPhoto.classList.remove("active");
  pdfSection.classList.remove("hidden");
  photoSection.classList.add("hidden");
});

document.getElementById("pdfProcessBtn").addEventListener("click", async () => {
  const fileInput = document.getElementById("pdfFileInput");
  const statusEl = document.getElementById("pdfStatus");
  if (!fileInput.files || fileInput.files.length === 0) {
    alert("Please select a PDF or Marksheet Image first.");
    return;
  }

  const file = fileInput.files.item(0);
  const maxPdfKb = parseFloat(document.getElementById("pdfMaxKb").value) || 200;
  statusEl.textContent = "Compressing & formatting document locally...";

  try {
    const { PDFDocument } = PDFLib;
    const outPdf = await PDFDocument.create();
    const pageCanvases = [];

    if (file.type === "application/pdf") {
      const arrayBuffer = await file.arrayBuffer();
      const pdf = await pdfjsLib.getDocument({ data: arrayBuffer }).promise;
      for (let p = 1; p <= pdf.numPages; p++) {
        const page = await pdf.getPage(p);
        const viewport = page.getViewport({ scale: 1.5 });
        const canvas = document.createElement("canvas");
        canvas.width = viewport.width;
        canvas.height = viewport.height;
        await page.render({ canvasContext: canvas.getContext("2d"), viewport }).promise;
        pageCanvases.push(canvas);
      }
    } else {
      const img = new Image();
      img.src = URL.createObjectURL(file);
      await img.decode();
      const canvas = document.createElement("canvas");
      const scale = Math.min(1, 1400 / Math.max(img.width, img.height));
      canvas.width = Math.round(img.width * scale);
      canvas.height = Math.round(img.height * scale);
      canvas.getContext("2d").drawImage(img, 0, 0, canvas.width, canvas.height);
      pageCanvases.push(canvas);
    }

    // Binary search JPEG quality across pages to fit strictly under maxPdfKb
    let low = 0.1, high = 0.92, finalBytes = null;
    for (let iter = 0; iter < 7; iter++) {
      const mid = (low + high) / 2;
      const testDoc = await PDFDocument.create();
      for (const c of pageCanvases) {
        const jpgDataUrl = c.toDataURL("image/jpeg", mid);
        const jpgBytes = await fetch(jpgDataUrl).then(r => r.arrayBuffer());
        const jpgImage = await testDoc.embedJpg(jpgBytes);
        const page = testDoc.addPage([jpgImage.width, jpgImage.height]);
        page.drawImage(jpgImage, { x: 0, y: 0, width: jpgImage.width, height: jpgImage.height });
      }
      finalBytes = await testDoc.save();
      const sizeKb = finalBytes.byteLength / 1024;
      if (sizeKb <= maxPdfKb && sizeKb >= maxPdfKb * 0.65) break;
      if (sizeKb > maxPdfKb) high = mid; else low = mid;
    }

    const finalKb = (finalBytes.byteLength / 1024).toFixed(2);
    const blob = new Blob([finalBytes], { type: "application/pdf" });
    const url = URL.createObjectURL(blob);

    statusEl.innerHTML = `<strong style="color:#34d399;">Ready! Compressed to ${finalKb} KB</strong> (${pageCanvases.length} page(s))`;
    const dl = document.getElementById("pdfDownloadLink");
    dl.href = url;
    dl.download = `ExamDocPro_${Math.round(finalKb)}KB.pdf`;
    document.getElementById("pdfResultBox").classList.remove("hidden");
  } catch (err) {
    statusEl.textContent = "Error reading file. Make sure it is a valid non-password PDF or JPG/PNG.";
  }
});
