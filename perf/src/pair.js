// Electron main: pair ./profile with the dev server. Usage: electron src/pair.js "<url>pair#token=<token>"
const { app, BrowserWindow } = require("electron"), path = require("path");
app.setPath("userData", path.join(__dirname, "..", "profile"));
app.whenReady().then(async () => {
  const w = new BrowserWindow({ width: 1440, height: 900, show: true });
  w.loadURL(process.argv[2]).catch((e) => console.log("load:", e.code));
  for (let i = 0; i < 40; i++) { await new Promise((r) => setTimeout(r, 500)); try { const n = await w.webContents.executeJavaScript("document.querySelectorAll('[data-thread-item]').length"); if (n) { console.log("paired, threads", n, await w.webContents.executeJavaScript("location.href")); break; } } catch {} }
  app.quit();
});
