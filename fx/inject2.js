(async (edition) => {
  const B = "http://127.0.0.1:8765/";
  const css = await (await fetch(B + "out2/" + edition + ".css?" + Date.now())).text();
  const colors = await (await fetch(B + "src2/colors.json?" + Date.now())).json();
  const kebab = (k) => k.replace(/[A-Z]/g, (m) => "-" + m.toLowerCase());
  const map = { terminalSelection: "terminal-selection-background" };
  const roles = Object.entries(colors.colors).map(([k, v]) => `--app-theme-${map[k] || kebab(k)}: ${v} !important;`).join("");
  window.__skRoles ||= new CSSStyleSheet();
  window.__skRoles.replaceSync(`:root{${roles}}`);
  const sheets = document.adoptedStyleSheets;
  const theme = sheets.find((s) => s !== window.__skRoles);
  theme.replaceSync(css);
  if (!sheets.includes(window.__skRoles)) document.adoptedStyleSheets = [...sheets, window.__skRoles];
  // The local edition cuts sprites from the theme background image; the app sets this variable from <themeId>.webp.
  if (edition === "local") {
    const img = await (await fetch(B + "out2/local.webp?" + Date.now())).blob();
    document.documentElement.style.setProperty("--theme-background-image", `url("${URL.createObjectURL(img)}")`);
  }
  window.__skCss = css;
  await new Promise((r) => setTimeout(r, 800));
  return { rules: theme.cssRules.length, len: css.length };
})
