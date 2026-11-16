// Judge for the sushi theme. Run in a page that has the theme loaded (fixture or real app).
// window.__skCss: theme text to validate. Returns invalid blocks, layout per row, contrast per row.
(async () => {
  await new Promise((r) => setTimeout(r, 500));
  const out = { invalid: [], rules: 0 };
  const text = window.__skCss || "";
  const flat = text.replace(/\/\*[\s\S]*?\*\//g, "");
  let depth = 0, start = 0;
  for (let i = 0; i < flat.length; i++) {
    if (flat[i] === "{") depth++;
    else if (flat[i] === "}") {
      depth--;
      if (depth === 0) {
        const b = flat.slice(start, i + 1).trim(); start = i + 1; out.rules++;
        const sheet = new CSSStyleSheet();
        try { sheet.insertRule(b); } catch (e) { out.invalid.push(b.slice(0, 100)); continue; }
        // Every written child block (nested rules, @media children, keyframes) must parse, at any depth.
        const kids = (blk) => {
          const inner = blk.slice(blk.indexOf("{") + 1, blk.lastIndexOf("}"));
          const res = []; let d = 0, s = 0, q = null;
          for (let k = 0; k < inner.length; k++) {
            const ch = inner[k];
            if (q) { if (ch === "\\") k++; else if (ch === q) q = null; continue; }
            if (ch === '"' || ch === "'") q = ch;
            else if (ch === "{") d++;
            else if (ch === "}") { d--; if (d === 0) { res.push(inner.slice(s, k + 1)); s = k + 1; } }
            else if (ch === ";" && d === 0) s = k + 1;
          }
          return res;
        };
        const same = (rule, blk) => {
          out.blocks = (out.blocks || 0) + 1;  // written blocks at all depths, each matched to a parsed rule
          if (!rule.cssRules) return;
          const ks = kids(blk);
          if (rule.cssRules.length !== ks.length) { out.invalid.push("group lost rules: " + blk.slice(0, 80)); return; }
          ks.forEach((k, n) => same(rule.cssRules[n], k));
        };
        same(sheet.cssRules[0], b);
        if (/:has\([^()]*(\([^()]*\)[^()]*)*:has\(/.test(b)) out.invalid.push("nested :has: " + b.slice(0, 80));
      }
    }
  }
  const cv = document.createElement("canvas"); cv.width = cv.height = 1;
  const cx = cv.getContext("2d", { willReadFrequently: true });
  const rgba = (c) => { cx.clearRect(0, 0, 1, 1); cx.fillStyle = "#000"; cx.fillStyle = c; cx.fillRect(0, 0, 1, 1); const d = cx.getImageData(0, 0, 1, 1).data; return [d[0], d[1], d[2], d[3] / 255]; };
  const over = (top, bot) => [0, 1, 2].map((i) => top[i] * top[3] + bot[i] * (1 - top[3])).concat(1);
  const lum = (c) => { const f = (v) => { v /= 255; return v <= 0.03928 ? v / 12.92 : ((v + 0.055) / 1.055) ** 2.4; }; return 0.2126 * f(c[0]) + 0.7152 * f(c[1]) + 0.0722 * f(c[2]); };
  const ratio = (a, b) => { const x = lum(a), y = lum(b); return +((Math.max(x, y) + 0.05) / (Math.min(x, y) + 0.05)).toFixed(2); };
  out.rows = [...document.querySelectorAll("[data-thread-item] > [data-testid=sidebar-row-card]")].filter((c) => { const r = c.getBoundingClientRect(); return r.bottom > 0 && r.top < innerHeight; }).slice(0, window.__skMax || 40).map((card) => {
    const c = card.getBoundingClientRect();
    const paper = rgba(getComputedStyle(card).backgroundColor);
    const lines = card.querySelectorAll(":scope > div > div");
    const top = (el) => el ? Math.round(el.getBoundingClientRect().top - c.top) : null;
    const title = card.querySelector(":scope > div > div:nth-child(2) > span");
    const project = card.querySelector(":scope > div > div:nth-child(1) > .flex-1");
    const branch = card.querySelector(":scope > div > div:nth-child(3) > span.flex.flex-1");
    const slot = card.querySelector(".group\\/sidebar-status-slot");
    const label = slot && slot.querySelector(":scope > span:first-child > *");
    const btns = slot ? [...slot.querySelectorAll(":scope > span:not(:first-child) button")] : [];
    const row = {
      t: (title?.textContent || "").slice(0, 16),
      lines: [top(title), top(project), top(branch)],
      titleH: title ? Math.round(title.getBoundingClientRect().height) : null,
      title: title && ratio(over(rgba(getComputedStyle(title).color), paper), paper),
      project: project && ratio(over(rgba(getComputedStyle(project).color), paper), paper),
      branch: branch && ratio(over(rgba(getComputedStyle(branch).color), paper), paper),
    };
    if (label && label.classList.contains("font-medium")) {
      const ls = getComputedStyle(label);
      const chip = over(rgba(ls.backgroundColor), paper);
      const lr = label.getBoundingClientRect();
      row.label = label.textContent; row.labelTop = Math.round(lr.top - c.top);
      row.labelC = ratio(rgba(ls.color), chip);
      row.iconC = ratio(rgba(ls.color), paper);
      row.icon = getComputedStyle(label, "::before").maskImage.slice(0, 40) !== "none";
      row.overlap = btns.some((b) => { const r = b.getBoundingClientRect(); return r.width && !(r.right <= lr.left || r.left >= lr.right || r.bottom <= lr.top || r.top >= lr.bottom); });
      row.btnTop = btns[0] ? Math.round(btns[0].getBoundingClientRect().top - c.top) : null;
    }
    // Line 3 (branch, PR, model) must stay visible and clear of the keys while they show.
    const keys = btns.filter((b) => getComputedStyle(b.parentElement).visibility !== "hidden").map((b) => b.getBoundingClientRect()).filter((r) => r.width);
    row.l3Lost = [...card.querySelectorAll(":scope > div > div:nth-child(3) *, :scope > div > div:nth-child(2) > span:not(:first-child) *")]
      .filter((e) => !e.children.length && e.getBoundingClientRect().width)
      .filter((e) => { const r = e.getBoundingClientRect(); return getComputedStyle(e).visibility === "hidden" || keys.some((k) => !(k.right <= r.left || k.left >= r.right || k.bottom <= r.top || k.top >= r.bottom)); }).length;
    return row;
  });
  return out;
})()
