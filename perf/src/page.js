// Injected into the T3 Code page. Defines window.__perf: theme control, CSSOM ablation, row cloning, scenarios.
(() => {
  if (window.__perf) return "already";
  const P = {};
  // The theme sheet: the only adopted sheet that styles the sidebar footer (custom property names change per build).
  const appSheet = document.adoptedStyleSheets.find((s) => s.cssRules.length > 50 && [...s.cssRules].some((r) => r.cssText.includes("sidebar-footer")));
  if (!appSheet) throw new Error("theme sheet not found");
  // The app may re-apply its theme (appearance switch): keep the harness in control of this sheet.
  const realReplace = CSSStyleSheet.prototype.replaceSync;
  appSheet.replaceSync = function (t) { P.appRewrites = (P.appRewrites || 0) + 1; };
  appSheet.replace = async function (t) { P.appRewrites = (P.appRewrites || 0) + 1; return this; };
  P.setTheme = (text) => { realReplace.call(appSheet, text); P.current = text; return appSheet.cssRules.length; };
  P.ruleCount = () => appSheet.cssRules.length;

  // ---- Ablation on CSSOM: spec = [{prop: "re", value?: "re"} | {sel: "re"} | {keyframes: "re"} | {media: "re"}]
  P.ablate = (text, spec) => {
    const s = new CSSStyleSheet();
    realReplace.call(s, text);
    const tests = spec.map((x) => ({ ...x, prop: x.prop && new RegExp(x.prop), value: x.value && new RegExp(x.value), sel: x.sel && new RegExp(x.sel), rsel: x.rsel && new RegExp(x.rsel), keyframes: x.keyframes && new RegExp(x.keyframes), media: x.media && new RegExp(x.media) }));
    let removedDecl = 0, removedRules = 0;
    const split = (q) => { const o = []; let d = 0, c = ""; for (const ch of q) { if (ch === "(") d++; if (ch === ")") d--; if (ch === "," && d === 0) { o.push(c.trim()); c = ""; } else c += ch; } o.push(c.trim()); return o; };
    const resolve = (sel, parent) => !parent ? sel : split(sel).map((x) => x.includes("&") ? x.replaceAll("&", `:is(${parent})`) : `:is(${parent}) ${x}`).join(", ");
    const walk = (list, parent) => {
      for (let i = list.length - 1; i >= 0; i--) {
        const r = list[i];
        const owner = r.parentRule || r.parentStyleSheet;
        if (r instanceof CSSKeyframesRule) {
          if (tests.some((t) => t.keyframes && t.keyframes.test(r.name))) { owner.deleteRule(i); removedRules++; }
          continue;
        }
        if (r instanceof CSSMediaRule && tests.some((t) => t.media && t.media.test(r.conditionText))) { owner.deleteRule(i); removedRules++; continue; }
        const full = r instanceof CSSStyleRule ? resolve(r.selectorText, parent) : parent;
        if (r instanceof CSSStyleRule && tests.some((t) => (t.sel && t.sel.test(r.selectorText)) || (t.rsel && t.rsel.test(full)))) { owner.deleteRule(i); removedRules++; continue; }
        if (r.style) {
          for (let j = r.style.length - 1; j >= 0; j--) {
            const p = r.style[j];
            const v = r.style.getPropertyValue(p);
            if (tests.some((t) => t.prop && t.prop.test(p) && (!t.value || t.value.test(v)))) { r.style.removeProperty(p); removedDecl++; }
          }
        }
        if (r.cssRules) walk(r.cssRules, full);
      }
    };
    walk(s.cssRules, null);
    const out = [...s.cssRules].map((r) => r.cssText).join("\n");
    return { css: out, removedDecl, removedRules };
  };

  // ---- Rows: clone real thread rows to reach n tickets.
  const STAT = {
    none: null,
    approval: ["Approval", "text-warning-foreground", "shield-question-mark"],
    input: ["Input", "text-indigo-600 dark:text-indigo-300", "message-circle-question-mark"],
    request: ["Request", "text-guest-foreground", "user-round"],
    working: ["Working", "text-info-foreground", "loader-circle"],
    waiting: ["Waiting", "text-muted-foreground", "circle-dot-dashed"],
    limited: ["Limited", "text-warning-foreground", "circle-alert"],
    done: ["Done", "text-success-foreground", "circle-check"],
    failed: ["Failed", "text-error-foreground", "circle-alert"],
    woke: ["Woke", "text-warning-foreground", "alarm-clock"],
  };
  P.STAT = Object.keys(STAT);
  const MIX = ["none", "done", "none", "working", "waiting", "none", "done", "approval", "none", "input", "done", "request", "none", "limited", "failed", "woke", "none", "done", "working", "none"];
  const slotOf = (item) => item.querySelector(".group\\/sidebar-status-slot > span:first-child");
  P.setStatus = (item, k) => {
    const slot = slotOf(item); if (!slot) return;
    const st = STAT[k];
    if (!st) { slot.innerHTML = "<time>14h</time>"; return; }
    const tag = k === "woke" ? "button" : "span";
    slot.innerHTML = `<${tag} class="inline-flex items-center gap-1 font-medium ${st[1]}"><svg class="lucide lucide-${st[2]} shrink-0 size-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle></svg>${st[0]}</${tag}>`;
  };
  P.items = () => [...document.querySelectorAll("[data-thread-item]")];
  P.setRows = (n) => {
    document.querySelectorAll("[data-perf-clone]").forEach((e) => e.remove());
    const real = P.items().filter((e) => e.querySelector(":scope > [data-testid=sidebar-row-card]"));
    if (!real.length) return 0;
    const tpl = real[real.length - 1];
    let last = P.items().at(-1);
    for (let i = P.items().length; i < n; i++) {
      const c = tpl.cloneNode(true);
      c.setAttribute("data-perf-clone", "");
      c.setAttribute("data-thread-item", "perf-" + i);
      c.querySelector("[data-testid=sidebar-row-card]")?.removeAttribute("aria-current");
      P.setStatus(c, MIX[i % MIX.length]);
      last.after(c); last = c;
    }
    return P.items().length;
  };
  P.viewport = () => document.querySelector("[data-slot=sidebar-content]")?.closest("[data-slot=scroll-area-viewport]");

  // ---- Frame recorder (rAF intervals on the main thread).
  P.frames = { start() { this.t = []; this.on = true; let last = performance.now(); const f = (t) => { if (!this.on) return; this.t.push(t - last); last = t; requestAnimationFrame(f); }; requestAnimationFrame(f); },
    stop() { this.on = false; const a = this.t.slice(1).sort((x, y) => x - y); const q = (p) => a.length ? a[Math.min(a.length - 1, Math.floor(p * a.length))] : null; return { n: a.length, median: q(0.5), p95: q(0.95), p99: q(0.99), max: a.at(-1) ?? null, long: a.filter((x) => x > 25).length }; } };

  // ---- In-page scenario drivers (return a promise that resolves when done).
  const raf = () => new Promise((r) => requestAnimationFrame(r));
  const wait = (ms) => new Promise((r) => setTimeout(r, ms));
  P.wait = wait;
  P.scrollSweep = async (pxPerFrame = 40) => {
    const v = P.viewport(); if (!v) return "no viewport";
    v.scrollTop = 0; await raf();
    const max = v.scrollHeight - v.clientHeight;
    for (let y = 0; y <= max; y += pxPerFrame) { v.scrollTop = y; await raf(); }
    for (let y = max; y >= 0; y -= pxPerFrame) { v.scrollTop = y; await raf(); }
    return { max };
  };
  P.statusChurn = async (frames = 120, perFrame = 5) => {
    const items = P.items(); let k = 0;
    for (let f = 0; f < frames; f++) {
      for (let j = 0; j < perFrame; j++) { const it = items[(k * 7) % items.length]; P.setStatus(it, P.STAT[k % P.STAT.length]); k++; }
      await raf();
    }
    return { changes: k };
  };
  P.stream = async (ms = 8000) => {
    let md = [...document.querySelectorAll(".chat-markdown")].at(-1);
    if (!md) return "no markdown";
    const p = document.createElement("p"); md.appendChild(p);
    const words = "the kitchen prints a new order line with `code` and **bold** text while the rail keeps moving ".split(" ");
    const t0 = performance.now(); let i = 0;
    while (performance.now() - t0 < ms) { p.append(words[i++ % words.length] + " "); if (i % 40 === 0) { const q = document.createElement("p"); md.appendChild(q); } await wait(33); }
    p.remove(); return { words: i };
  };
  P.fillChat = (n = 60) => {
    const md = [...document.querySelectorAll(".chat-markdown")].at(-1); if (!md) return "no markdown";
    if (!md.querySelector("[data-perf-fill]")) for (let i = 0; i < n; i++) { const p = document.createElement("p"); p.setAttribute("data-perf-fill", ""); p.textContent = "The kitchen prints line " + i + " of a long answer so the conversation can scroll through the dining room wallpaper."; md.appendChild(p); }
    const sc = document.querySelector(".messages-timeline-scroll"); return sc ? sc.scrollHeight - sc.clientHeight : "no scroller";
  };
  // Replica of the Working shelf header (same component as the settled shelf header, working test ids).
  P.addWorkingShelf = () => {
    if (document.querySelector('[data-perf-working-shelf]')) return "exists";
    const src = document.querySelector('[data-testid=sidebar-settled-header]'); if (!src) return "no settled header";
    const c = src.cloneNode(true); c.setAttribute('data-perf-working-shelf', ''); c.setAttribute('data-testid', 'sidebar-working-header');
    const t = c.querySelector('[data-testid=sidebar-settled-shelf-toggle]'); t.setAttribute('data-testid', 'sidebar-working-shelf-toggle'); t.setAttribute('data-sidebar-row', 'shelf:working');
    const lab = t.querySelector(':scope > span:first-child'); lab.textContent = 'Working';
    const first = document.querySelector('[data-perf-clone]') || document.querySelector('[data-thread-item]'); first.before(c); return "added";
  };
  P.sidebarToggle = async (times = 6) => {
    const b = document.querySelector("[data-sidebar=trigger]"); if (!b) return "no trigger";
    for (let i = 0; i < times * 2; i++) { b.click(); await wait(450); }
    return { toggles: times * 2, state: document.querySelector("[data-slot=sidebar]")?.dataset.state };
  };
  const HOSTS = [[document.documentElement, "::after"], [document.body, "::after"], ...["main[data-slot=sidebar-inset]", "[data-workspace-area=conversation]", "[data-workspace-area=composer]"].flatMap((q) => [[document.querySelector(q), "::before"], [document.querySelector(q), "::after"]])];
  P.bubbles = () => HOSTS.filter(([e, p]) => { if (!e) return false; const c = getComputedStyle(e, p); return c.content !== "none" && c.display !== "none" && parseFloat(c.left) > 0 && parseFloat(c.left) < innerWidth && c.positionVisibility !== "hidden"; }).length;
  P.domStats = () => ({ bubbles: P.bubbles(),  nodes: document.querySelectorAll("*").length, items: P.items().length, md: document.querySelectorAll(".chat-markdown").length, dark: document.documentElement.classList.contains("dark"), rewrites: P.appRewrites || 0 });
  // Hover activity in the thread list: hover changes (mouseover) and CSS transitions started (transitionrun).
  P.hc = { ov: 0, tr: 0, props: {} };
  P.hcTake = () => { const o = P.hc; P.hc = { ov: 0, tr: 0, props: {} }; return o; };
  document.addEventListener("mouseover", (e) => { if (e.target.closest?.("[data-thread-item]")) P.hc.ov++; }, true);
  document.addEventListener("transitionrun", (e) => { if (e.target.closest?.("[data-thread-item]")) { P.hc.tr++; P.hc.props[e.propertyName] = (P.hc.props[e.propertyName] || 0) + 1; } }, true);
  window.__perf = P;
  return "ok";
})();
