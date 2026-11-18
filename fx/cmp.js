// Paired computed-style comparison of two builds on the current page state.
// f(urlA, urlB) -> {n, diff (A vs B), drift (A vs A again), examples}. Custom properties excluded.
(async (ua, ub) => {
  const get = async (u) => (window.__cmpCache ||= {})[u] ||= await (await fetch(u + "?" + Date.now())).text();
  const A = await get(ua), Bc = await get(ub);
  const theme = document.adoptedStyleSheets.find((s) => s !== window.__skRoles && s !== window.__skFreeze);
  const els = [...document.querySelectorAll("*")];
  const ser = (e, p) => { const cs = getComputedStyle(e, p); if (p && cs.content === "none") return ""; let s = ""; for (let i = 0; i < cs.length; i++) { const k = cs[i]; if (k.startsWith("--")) continue; s += k + ":" + cs.getPropertyValue(k) + ";"; } return s; };
  const snap = () => { const o = []; for (const e of els) { o.push(ser(e, null), ser(e, "::before"), ser(e, "::after")); } return o; };
  theme.replaceSync(A); const a = snap(); theme.replaceSync(Bc); const b = snap(); theme.replaceSync(A); const c = snap();
  theme.replaceSync(window.__skCss || A);
  let diff = 0, drift = 0; const ex = [];
  for (let i = 0; i < a.length; i++) {
    if (a[i] !== c[i]) drift++;
    if (a[i] !== b[i]) { diff++; if (ex.length < 5) { const x = a[i].split(";"), y = b[i].split(";"); const e = els[Math.floor(i / 3)]; ex.push(e.tagName + "." + (e.dataset.slot || e.className?.baseVal || e.className || "").toString().slice(0, 40) + ["", "::before", "::after"][i % 3] + " " + x.filter((v, j) => v !== y[j]).slice(0, 2).join(" ") + " => " + y.filter((v, j) => v !== x[j]).slice(0, 2).join(" ")); } }
  }
  return { n: els.length, entries: a.length, diff, drift, ex };
})
