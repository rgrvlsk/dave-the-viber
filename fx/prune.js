// Finds `!important` flags the live page does not need. Run after fx/inject2.js, on a FLAT build (NEST False):
//   const f = eval(await (await fetch(B + "fx/prune.js?" + Date.now())).text()); window.__job = f(flatCssUrl);
// It returns at once and works in the background (an evaluate over 15 s closes the tab). Poll window.__prog:
// state "done" gives removable (flag indexes in text order), neededList, untested (rules matching nothing here),
// finalDiff and baseDrift (both must be 0). A killed run resumes with f(url, {removable, needed}).
// A flag passes when no computed standard property of any element or ::before/::after changes. That proves this
// page state only: apply the static guard in HANDOFF.md ("!important pruning") before editing src2/.
(async (url, known) => {
  const css = await (await fetch(url + "?" + Date.now())).text();
  const theme = document.adoptedStyleSheets.find((s) => s !== window.__skRoles && s !== window.__skFreeze);
  const ch = new MessageChannel(); window.__ch = ch;
  const tick = () => new Promise((r) => { ch.port1.onmessage = r; ch.port2.postMessage(0); });
  // flags and their rule selector (top-level style rules only)
  const flags = []; let depth = 0, start = 0, pre = "", q = null;
  for (let i = 0; i < css.length; i++) {
    const c = css[i];
    if (q) { if (c === "\\") i++; else if (c === q) q = null; continue; }
    if (c === '"' || c === "'") q = c;
    else if (c === "{") { if (depth === 0) pre = css.slice(start, i); depth++; }
    else if (c === "}") { depth--; if (depth === 0) start = i + 1; }
    else if (c === "!" && css.startsWith("!important", i)) {
      const ds = Math.max(css.lastIndexOf(";", i), css.lastIndexOf("{", i)) + 1;
      flags.push({ pos: i, sel: depth === 1 && pre[0] !== "@" ? pre : null, prop: css.slice(ds, css.indexOf(":", ds)) });
    }
  }
  const variant = (set) => { let out = "", last = 0; for (const k of [...set].sort((a, b) => a - b)) { out += css.slice(last, flags[k].pos); last = flags[k].pos + 10; } return out + css.slice(last); };
  const snap = async () => {
    const out = []; const els = document.querySelectorAll("*"); let n = 0;
    for (const e of els) {
      for (const p of ["", "::before", "::after"]) {
        const cs = getComputedStyle(e, p || null);
        if (p && cs.content === "none") { out.push(""); continue; }
        let s = ""; for (let i = 0; i < cs.length; i++) { const k = cs[i]; if (k.charCodeAt(1) === 45) break; s += cs.getPropertyValue(k) + ";"; }
        out.push(s);
      }
      if (++n % 250 === 0) await tick();
    }
    return out;
  };
  const P = window.__prog = { flags: flags.length, state: "base", trials: 0, removable: [], needed: [], untested: [], log: [] };
  const apply = async (set) => { theme.replaceSync(variant(set)); await tick(); };
  await apply([]); const t0 = performance.now(); const base = await snap(); P.snapMs = Math.round(performance.now() - t0);
  const test = async (set) => { await apply(set); const s = await snap(); P.trials++; if (s.length !== base.length) return -1; let d = 0; for (let i = 0; i < s.length; i++) if (s[i] !== base[i]) d++; return d; };
  const cand = [];
  flags.forEach((f, k) => { let ok = false; if (f.sel) { try { ok = !!document.querySelector(f.sel.replace(/::?(before|after)/g, "")); } catch (e) {} } (ok ? cand : P.untested).push(k); });
  P.cand = cand.length;
  let todo = cand;
  if (known) { P.removable.push(...known.removable); P.needed.push(...known.needed); todo = cand.filter((k) => !known.removable.includes(k) && !known.needed.includes(k)); }
  else { P.state = "all"; P.allDiff = await test(cand); }
  const queue = []; for (let i = 0; i < todo.length; i += 10) queue.push(todo.slice(i, i + 10));
  P.state = "bisect";
  while (queue.length) {
    const g = queue.shift(); const d = await test(g);
    if (d === 0) P.removable.push(...g);
    else if (g.length === 1) P.needed.push(g[0]);
    else { const h = g.length >> 1; queue.unshift(g.slice(0, h), g.slice(h)); }
    P.left = queue.reduce((a, b) => a + b.length, 0);
  }
  P.state = "final"; P.finalDiff = await test(P.removable); P.baseDrift = await test([]);
  P.result = P.removable.map((k) => [k, flags[k].sel.slice(0, 200), flags[k].prop]);
  P.neededList = P.needed.map((k) => [k, flags[k].sel.slice(0, 80), flags[k].prop]);
  window.__pruned = variant(P.removable); await apply(P.removable); window.__skCss = window.__pruned;
  P.state = "done";
})
