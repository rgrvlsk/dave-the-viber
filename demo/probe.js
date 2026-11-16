(async () => {
  const strip = (h) => h.replace(/<path[^>]*>/g, "<path/>").replace(/src="[^"]*"/g, "src=…").replace(/d="[^"]*"/g, "");
  const out = {};
  const card = document.querySelector('[data-testid="sidebar-row-card"]');
  if (card) {
    const l3 = card.querySelector(":scope > div > div:nth-child(3)");
    out.ticketLine3 = l3 && strip(l3.outerHTML).slice(0, 900);
    out.ticketModelSvgColor = [...card.querySelectorAll("svg")].map((s) => [s.getAttribute("class"), getComputedStyle(s).color, getComputedStyle(s).fill, getComputedStyle(s).filter].join(" | ")).slice(-3);
  }
  const host = document.querySelector('[data-slot="composer-host"]');
  if (host) out.composerModel = [...host.querySelectorAll("button")].map((b) => strip(b.outerHTML).slice(0, 300)).filter((h) => /model|Opus|Haiku|Sonnet|Codex|Multi|fixture/i.test(h)).slice(0, 2);
  out.shelfToggles = [...document.querySelectorAll('[data-testid$="-shelf-toggle"], [data-testid*="shelf"], [data-testid*="snooze"]')].map((e) => e.tagName + " " + e.getAttribute("data-testid") + " | " + e.textContent.trim().slice(0, 20));
  const sn = document.querySelector('[data-sidebar-parent*="snooz"]');
  out.snoozedRow = sn && strip(sn.outerHTML).slice(0, 900);
  const banner = document.querySelector("[data-composer-banner-surface]");
  if (banner) {
    const ind = [...banner.querySelectorAll("*")].filter((e) => { const r = e.getBoundingClientRect(); return r.width >= 12 && r.width <= 22 && Math.abs(r.width - r.height) < 2; });
    out.radioIndicators = ind.slice(0, 3).map((e) => strip(e.outerHTML).slice(0, 300) + " || bg=" + getComputedStyle(e).backgroundColor);
    out.bannerFades = [...banner.querySelectorAll("*")].filter((e) => /gradient/.test(getComputedStyle(e).backgroundImage) || getComputedStyle(e).maskImage !== "none").slice(0, 3).map((e) => e.tagName + " " + (e.className.baseVal ?? e.className).toString().slice(0, 160) + " | bgi=" + getComputedStyle(e).backgroundImage.slice(0, 120) + " | mask=" + getComputedStyle(e).maskImage.slice(0, 80));
  }
  const code = document.querySelector(".chat-markdown-codeblock");
  if (code) out.codeTokens = [...code.querySelectorAll("span[style]")].slice(0, 4).map((s) => s.getAttribute("style"));
  const panels = [...document.querySelectorAll("div")].filter((d) => { const r = d.getBoundingClientRect(); const cs = getComputedStyle(d); return r.left > innerWidth * 0.6 && r.width > 200 && r.width < 500 && parseFloat(cs.borderTopLeftRadius) >= 8; }).slice(0, 2);
  out.rightPanels = panels.map((d) => d.tagName + " " + [...d.attributes].filter((a) => a.name.startsWith("data-") || a.name === "role" || a.name === "aria-label").map((a) => a.name + "=" + a.value).join(" ") + " | cls=" + d.className.toString().slice(0, 160) + " | br=" + getComputedStyle(d).borderTopLeftRadius + " bg=" + getComputedStyle(d).backgroundColor);
  out.url = location.pathname; out.dark = document.documentElement.className;
  return JSON.stringify(out);
})()
