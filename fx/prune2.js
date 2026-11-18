// Paired per-flag test. f(url, ks) -> {k: "ok" | "none" | "drift" | "needed:prop,..."}.
// For flag k: style of every element (and ::before/::after) its rule matches, under the full CSS (a), without flag k (b),
// and the full CSS again (c). a != c is drift; a == b passes. Synchronous per flag, so page updates cannot interleave. The CSS is cached in window.__p2css (delete it to refetch); run on a FLAT build with motion frozen.
(async (url, ks) => {
  const css = window.__p2css ||= await (await fetch(url + "?" + Date.now())).text();
  const theme = document.adoptedStyleSheets.find((s) => s !== window.__skRoles && s !== window.__skFreeze);
  const flags = []; let depth = 0, start = 0, pre = "", q = null;
  for (let i = 0; i < css.length; i++) {
    const c = css[i];
    if (q) { if (c === "\\") i++; else if (c === q) q = null; continue; }
    if (c === '"' || c === "'") q = c;
    else if (c === "{") { if (depth === 0) pre = css.slice(start, i); depth++; }
    else if (c === "}") { depth--; if (depth === 0) start = i + 1; }
    else if (c === "!" && css.startsWith("!important", i)) flags.push({ pos: i, sel: depth === 1 && pre[0] !== "@" ? pre : null });
  }
  const split = (s) => { const out = []; let d = 0, st = 0, qq = null; for (let i = 0; i < s.length; i++) { const c = s[i]; if (qq) { if (c === "\\") i++; else if (c === qq) qq = null; continue; } if (c === '"' || c === "'") qq = c; else if (c === "(" || c === "[") d++; else if (c === ")" || c === "]") d--; else if (c === "," && !d) { out.push(s.slice(st, i)); st = i + 1; } } out.push(s.slice(st)); return out; };
  const ser = (e, p) => { const cs = getComputedStyle(e, p); let s = ""; for (let i = 0; i < cs.length; i++) { const k = cs[i]; if (k.startsWith("--")) continue; s += k + ":" + cs.getPropertyValue(k) + ";"; } return s; };
  const out = {};
  for (const k of ks) {
    const f = flags[k]; if (!f.sel) { out[k] = "nosel"; continue; }
    const pairs = [];
    for (const part of split(f.sel)) {
      const m = part.match(/::?(before|after)\s*$/); const base = m ? part.slice(0, m.index) : part;
      let els = []; try { els = document.querySelectorAll(base || "*"); } catch (e) { out[k] = "bad"; }
      for (const e of els) pairs.push([e, m ? "::" + m[1] : null]);
    }
    if (!pairs.length) { out[k] = out[k] || "none"; continue; }
    const snap = () => pairs.map(([e, p]) => ser(e, p));
    theme.replaceSync(css); const a = snap();
    theme.replaceSync(css.slice(0, f.pos) + css.slice(f.pos + 10)); const b = snap();
    theme.replaceSync(css); const c = snap();
    if (a.join("|") !== c.join("|")) { out[k] = "drift"; continue; }
    const diff = new Set();
    a.forEach((s, i) => { if (s !== b[i]) { const A = s.split(";"), B = b[i].split(";"); A.forEach((x, j) => { if (x !== B[j]) diff.add(x.split(":")[0]); }); } });
    out[k] = diff.size ? "needed:" + [...diff].slice(0, 4).join(",") + "@" + pairs.length : "ok@" + pairs.length;
  }
  return out;
})
