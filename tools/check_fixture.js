(async () => {
  // 1. Every rule of the theme must survive the browser's parser.
  const text = await (await fetch("status-edge.css", { cache: "no-store" })).text();
  const flat = text.replace(/\/\*[\s\S]*?\*\//g, "");
  const blocks = []; let depth = 0, start = 0;
  for (let i = 0; i < flat.length; i++) {
    if (flat[i] === "{") depth++;
    else if (flat[i] === "}") { depth--; if (depth === 0) { blocks.push(flat.slice(start, i + 1).trim()); start = i + 1; } }
  }
  const invalid = [];
  for (const b of blocks) {
    const sheet = new CSSStyleSheet();
    try { sheet.insertRule(b); } catch (e) { invalid.push(b.slice(0, 90)); continue; }
    const r = sheet.cssRules[0];
    if (r instanceof CSSMediaRule) {
      const inner = b.slice(b.indexOf("{") + 1, b.lastIndexOf("}"));
      let d = 0, s = 0, n = 0;
      for (let i = 0; i < inner.length; i++) { if (inner[i] === "{") d++; else if (inner[i] === "}") { d--; if (d === 0) n++; } }
      if (r.cssRules.length !== n) invalid.push("media lost rules: " + b.slice(0, 60));
    }
  }
  // 2. Geometry and colours per row.
  const rgb = (c) => c;
  const rows = [...document.querySelectorAll("[data-thread-item] > [data-testid=sidebar-row-card]")].map((card) => {
    const c = card.getBoundingClientRect();
    const slot = card.querySelector(".group\\/sidebar-status-slot");
    const after = getComputedStyle(slot, "::after");
    const label = slot.querySelector(":scope > span:first-child > *");
    const title = card.querySelector(":scope > div > div:nth-child(2) > span");
    const project = card.querySelector(":scope > div > div:nth-child(1) > .flex-1");
    const branch = card.querySelector(":scope > div > div:nth-child(3) > span.flex.flex-1");
    const slotTop = slot.getBoundingClientRect().top - c.top;
    const bar = after.content === "none" ? null : {
      top: Math.round(slotTop + parseFloat(after.top)), h: Math.round(parseFloat(after.height)), color: after.backgroundColor,
      mask: after.maskImage !== "none" ? after.maskSize : "", opacity: after.opacity };
    return {
      t: title.textContent.slice(0, 14), bar,
      label: label && label.textContent, labelColor: label && getComputedStyle(label).color,
      titleColor: getComputedStyle(title).color, projectColor: getComputedStyle(project).color,
      branch: branch ? getComputedStyle(branch).fontFamily.split(",")[0] + " " + getComputedStyle(branch).fontSize : null,
      ring: getComputedStyle(card).boxShadow === "none" ? "" : getComputedStyle(card).boxShadow.slice(0, 40),
      line2Top: Math.round(project.getBoundingClientRect().top - c.top),
    };
  });
  return { rules: blocks.length, invalid, rows };
})()
