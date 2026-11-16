// Whole-page text contrast scan: every visible text node vs its effective opaque background.
(() => {
  const cv = document.createElement("canvas"); cv.width = cv.height = 1;
  const cx = cv.getContext("2d", { willReadFrequently: true });
  const rgba = (c) => { cx.clearRect(0, 0, 1, 1); cx.fillStyle = "#000"; cx.fillStyle = c; cx.fillRect(0, 0, 1, 1); const d = cx.getImageData(0, 0, 1, 1).data; return [d[0], d[1], d[2], d[3] / 255]; };
  const over = (t, b) => [0, 1, 2].map((i) => t[i] * t[3] + b[i] * (1 - t[3])).concat(1);
  const lum = (c) => { const f = (v) => { v /= 255; return v <= 0.03928 ? v / 12.92 : ((v + 0.055) / 1.055) ** 2.4; }; return 0.2126 * f(c[0]) + 0.7152 * f(c[1]) + 0.0722 * f(c[2]); };
  const ratio = (a, b) => { const x = lum(a), y = lum(b); return (Math.max(x, y) + 0.05) / (Math.min(x, y) + 0.05); };
  const bgOf = (el) => {
    const stack = [];
    for (let e = el; e; e = e.parentElement) {
      const cs = getComputedStyle(e);
      const c = rgba(cs.backgroundColor);
      for (const p of ["::before"]) { const pc = getComputedStyle(e, p); if (pc.content !== "none" && pc.position === "absolute" && pc.inset === "0px") { const b = rgba(pc.backgroundColor); if (b[3] > 0) stack.push(b); } }
      if (c[3] > 0) stack.push(c);
      if (stack.length && stack[stack.length - 1][3] >= 0.99) break;
    }
    let bg = [26, 33, 48, 1];
    for (let i = stack.length - 1; i >= 0; i--) bg = over(stack[i], bg);
    return bg;
  };
  const out = [];
  const seen = new Set();
  const w = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  while (w.nextNode()) {
    const t = w.currentNode; const el = t.parentElement;
    if (!t.textContent.trim() || seen.has(el)) continue; seen.add(el);
    const r = el.getBoundingClientRect();
    if (!r.width || r.bottom < 0 || r.top > innerHeight || r.right < 0 || r.left > innerWidth) continue;
    const cs = getComputedStyle(el);
    if (cs.visibility === "hidden" || +cs.opacity === 0) continue;
    let op = 1; for (let e = el; e; e = e.parentElement) op *= +getComputedStyle(e).opacity;
    if (op < 0.05) continue;
    const bg = bgOf(el);
    let fg = rgba(cs.color); fg = [fg[0], fg[1], fg[2], fg[3] * op];
    const k = ratio(over(fg, bg), bg);
    if (k < (window.__skMin || 4.5)) out.push({ k: +k.toFixed(2), t: t.textContent.trim().slice(0, 30), cls: el.className.toString().slice(0, 70), x: Math.round(r.left), y: Math.round(r.top) });
  }
  return out.sort((a, b) => a.k - b.k).slice(0, 40);
})()
