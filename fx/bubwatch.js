// Attention-bubble watchdog. Paste in the desktop DevTools console (View > Toggle Developer Tools).
// Each second it hit-tests the centre of every attention bubble (row ::before, position: fixed). A bubble that is
// hidden, clipped, skipped or covered does not answer the hit test; the row's state at that moment is logged.
// Read the log with copy(__bubLog.join('\n')); stop with __bubStop().
(() => {
  window.__bubStop?.();
  const sheet = new CSSStyleSheet();
  sheet.replaceSync('[data-thread-item]::before{pointer-events:auto!important}');
  document.adoptedStyleSheets = [...document.adoptedStyleSheets, sheet];
  const log = (window.__bubLog = []);
  const last = new Map();
  const cbProps = (e) => {
    const s = getComputedStyle(e);
    const k = ['transform', 'translate', 'rotate', 'scale', 'filter', 'backdropFilter', 'perspective'].filter((p) => s[p] !== 'none');
    if (s.contain !== 'none') k.push('contain:' + s.contain);
    if (s.willChange !== 'auto') k.push('wc:' + s.willChange);
    if (s.contentVisibility !== 'visible') k.push('cv:' + s.contentVisibility);
    return k;
  };
  const tick = () => {
    for (const li of document.querySelectorAll('li[data-thread-item]')) {
      const b = getComputedStyle(li, '::before');
      if (b.position !== 'fixed') continue;
      const name = (li.querySelector('[data-testid$=row-card]')?.ariaLabel || '?').slice(0, 30);
      const r = li.getBoundingClientRect();
      const sc = li.closest('[data-slot$=a-viewport]');
      const v = sc?.getBoundingClientRect();
      const inView = v && r.bottom > v.top && r.top < v.bottom;
      // Hit-test where the bubble belongs (the theme's left/top), not its computed left/top: Chromium keeps those at
      // the last layout and applies later scrolling at paint time.
      const x = r.right + 4 + 20, y = Math.max(112, r.top + 6) + 15;
      const hit = document.elementFromPoint(x, y);
      const ok = !inView || hit === li || li.contains(hit);
      const prev = last.get(li);
      if (prev === ok) continue;
      last.set(li, ok);
      if (ok && prev === undefined) continue;
      const chain = [];
      for (let e = li; e; e = e.parentElement) { const c = cbProps(e); if (c.length) chain.push((e.dataset.slot || e.tagName.toLowerCase()) + '[' + c + ']'); }
      const anims = li.getAnimations({ subtree: false }).map((a) => a.playState + ':' + (a.animationName || a.id || 'waapi')).join(',');
      const line = `${new Date().toISOString().slice(11, 19)} ${ok ? 'BACK' : 'MISSING'} ${name} | before L=${b.left} T=${b.top} disp=${b.display} vis=${b.positionVisibility} | row ${r.left | 0},${r.top | 0},${r.right | 0},${r.bottom | 0} scroller ${v ? (v.top | 0) + '-' + (v.bottom | 0) + ' st=' + (sc.scrollTop | 0) : '-'} | style="${li.getAttribute('style') || ''}" anims=${anims || 0} | CB ${chain.join(' ') || 'viewport'} | hit ${hit ? hit.tagName.toLowerCase() + '.' + String(hit.className).slice(0, 40) : 'none'}`;
      log.push(line);
      console.warn('[bubwatch]', line);
    }
  };
  const id = setInterval(tick, 1000);
  window.__bubStop = () => { clearInterval(id); document.adoptedStyleSheets = document.adoptedStyleSheets.filter((s) => s !== sheet); };
  tick();
  return 'bubwatch on: copy(__bubLog.join("\\n")) to read, __bubStop() to stop';
})();
