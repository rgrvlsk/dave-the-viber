// Electron main: one stress-test run with continuous resource sampling (time series).
// Usage: electron src/timeline.js <variant:none|full> <run#> <out.jsonl> [url]
// Derived from the CSS cost harness in /Users/roger/t3code/.css-perf (bench.js, page.js); same Electron 44.10.1.
// One fresh Electron process per run, so memory history starts clean each time.
const { app, BrowserWindow, contentTracing } = require("electron");
const fs = require("fs"), path = require("path"), os = require("os"), { spawn } = require("child_process");
const ROOT = path.join(__dirname, "..");
app.setPath("userData", path.join(ROOT, "profile"));
app.commandLine.appendSwitch("disable-renderer-backgrounding");
const [variant, runNo, outFile, url = "http://localhost:7508/"] = process.argv.slice(2);
const FILES = { none: null, full: "variants/full-d292df3.css", "full-noanim": "variants/full-noanim-d292df3.css" };
if (!(variant in FILES)) { console.error("variant must be " + Object.keys(FILES).join("|")); process.exit(2); }
const CSS = FILES[variant] ? fs.readFileSync(path.join(ROOT, FILES[variant]), "utf8") : "";
const PLAN_NAME = process.env.PLAN || "stress";
const out = fs.createWriteStream(path.resolve(outFile), { flags: "a" });
const emit = (o) => out.write(JSON.stringify({ run: +runNo, variant, ...o }) + "\n");
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), variant, runNo, ...a);
process.on("unhandledRejection", (e) => { console.error("FATAL " + (e && e.stack || e)); app.exit(3); });
setTimeout(() => { console.error("FATAL watchdog"); app.exit(5); }, 8 * 60e3).unref();

const LIGHT_CATS = ["toplevel", "devtools.timeline", "disabled-by-default-devtools.timeline.frame", "blink.animations", "viz", "gpu"];
function summarizeTrace(file, t0Wall) {
  const ev = (j => j.traceEvents || j)(JSON.parse(fs.readFileSync(file, "utf8"))); fs.unlinkSync(file);
  const pname = {}, tname = {}; for (const e of ev) if (e.ph === "M") { if (e.name === "process_name") pname[e.pid] = e.args.name; if (e.name === "thread_name") tname[e.pid + ":" + e.tid] = e.args.name; }
  const busy = {}, stage = {}, frames = {}, draw = [];
  for (const e of ev) {
    if (e.ph === "X" && (e.cat || "").split(",").includes("toplevel")) { const th = (pname[e.pid] || "?") + "/" + (tname[e.pid + ":" + e.tid] || "?").replace(/\d+$/, "N"); busy[th] = (busy[th] || 0) + (e.dur || 0) / 1000; }
    if (e.ph === "X" && /devtools\.timeline/.test(e.cat || "")) stage[e.name] = (stage[e.name] || 0) + (e.dur || 0) / 1000;
    if (/devtools\.timeline\.frame/.test(e.cat || "") && e.ph !== "M") { frames[e.name] = (frames[e.name] || 0) + 1; if (e.name === "DrawFrame") draw.push(e.ts); }
  }
  // DrawFrame per second, relative to the first DrawFrame of the phase.
  draw.sort((a, b) => a - b); const fps = []; for (const ts of draw) { const s = Math.floor((ts - draw[0]) / 1e6); fps[s] = (fps[s] || 0) + 1; }
  const r = (o) => Object.fromEntries(Object.entries(o).map(([k, v]) => [k, Math.round(v * 100) / 100]));
  return { busy: r(busy), stage: r(stage), frames, fps: Array.from(fps, (x) => x || 0) };
}

// macOS top, 1 s samples: CPU %, energy impact ("power"), idle wakeups, physical footprint (MEM) per PID.
function startTop(pidMap, t0) {
  const label = Object.fromEntries(Object.entries(pidMap).map(([k, v]) => [String(v), k]));
  const args = ["-l", "0", "-s", "1", "-stats", "pid,cpu,power,idlew,mem"]; for (const p of Object.values(pidMap)) args.push("-pid", String(p));
  const p = spawn("top", args); let buf = "", block = 0;
  const unit = (s) => { const m = s.match(/^([\d.]+)([BKMG]?)/); return m ? +m[1] * { B: 1 / 1048576, K: 1 / 1024, M: 1, G: 1024, "": 1 / 1048576 }[m[2]] : null; };
  p.stdout.on("data", (d) => {
    buf += d; const parts = buf.split(/\n(?=Processes:)/); buf = parts.pop();
    for (const b of parts) {
      block++; if (block === 1) continue; // the first top sample has no CPU delta
      const rows = {}; for (const l of b.split("\n")) { const m = l.trim().match(/^(\d+)\s+([\d.]+)\s+([\d.]+)\s+(\d+)[+-]?\s+(\S+)/); if (m && label[m[1]]) rows[label[m[1]]] = { cpu: +m[2], power: +m[3], idlewTotal: +m[4], memMB: unit(m[5]) }; }
      emit({ kind: "top", t: Date.now() - t0, phase: phase.name, procs: rows });
    }
  });
  return p;
}

let phase = { name: "load" };
app.whenReady().then(async () => {
  const w = new BrowserWindow({ width: 1440, height: 900, x: 40, y: 40, show: true, webPreferences: { backgroundThrottling: false } });
  const dbg = w.webContents.debugger, cdp = (m, p = {}) => dbg.sendCommand(m, p), js = (s) => w.webContents.executeJavaScript(s);
  w.loadURL(url).catch((e) => log("loadURL:", e.code || e.message));
  let ok = false; for (let i = 0; i < 60; i++) { await sleep(500); try { if (await js("document.querySelectorAll('[data-thread-item]').length>0 && document.adoptedStyleSheets.length>0")) { ok = true; break; } } catch {} }
  if (!ok) { console.error("FATAL app did not load (pairing?)"); app.exit(6); }
  w.webContents.setBackgroundThrottling(true); // as DesktopWindow.ts after the first reveal
  await sleep(1500); dbg.attach("1.3"); await cdp("Performance.enable");
  // Open the thread with the most messages (stream target), as bench.js does.
  const n = await js("document.querySelectorAll('[data-thread-item] [data-testid=sidebar-row-card]').length"); let best = { i: 0, md: -1 };
  for (let i = 0; i < n; i++) { await js(`document.querySelectorAll('[data-thread-item] [data-testid=sidebar-row-card]')[${i}].click()`); await sleep(1500); const md = await js("document.querySelectorAll('.chat-markdown').length"); if (md > best.md) best = { i, md }; }
  await js(`document.querySelectorAll('[data-thread-item] [data-testid=sidebar-row-card]')[${best.i}].click()`); await sleep(2000);
  log("inject", await js(fs.readFileSync(path.join(__dirname, "page.js"), "utf8")), "thread", JSON.stringify(best));
  const rules = await js(`__perf.setTheme(${JSON.stringify(CSS)})`);

  const pids = () => { const m = app.getAppMetrics(); return { renderer: w.webContents.getOSProcessId(), gpu: m.find((x) => x.type === "GPU")?.pid, browser: process.pid }; };
  const kindOf = (m) => m.pid === w.webContents.getOSProcessId() ? "renderer" : m.type === "GPU" ? "gpu" : m.type === "Browser" ? "browser" : m.type.toLowerCase();
  const cpuTot = () => os.cpus().reduce((a, c) => { const t = c.times; a.busy += t.user + t.nice + t.sys + t.irq; a.all += t.user + t.nice + t.sys + t.irq + t.idle; return a; }, { busy: 0, all: 0 });
  const t0 = Date.now();
  emit({ kind: "meta", plan: PLAN_NAME, node: process.versions, electron: process.versions.electron, rules, cssChars: CSS.length, pids: pids(), thread: best, startedAt: new Date(t0).toISOString(), loadavg: os.loadavg() });

  // Electron sampler, 250 ms: per-process CPU % (from cumulative CPU time), idle wakeups, working set; system CPU %.
  let prev = null, prevSys = cpuTot(), prevT = performance.now();
  const sample = () => {
    const now = performance.now(), dt = (now - prevT) / 1000, cur = {}, procs = {};
    for (const m of app.getAppMetrics()) { const k = kindOf(m); cur[m.pid] = m.cpu.cumulativeCPUUsage;
      const p = (procs[k] ||= { cpu: 0, wsMB: 0, peakMB: 0, wake: 0 });
      p.cpu += prev && prev[m.pid] !== undefined ? ((m.cpu.cumulativeCPUUsage - prev[m.pid]) / dt) * 100 : 0;
      p.wsMB += m.memory.workingSetSize / 1024; p.peakMB += m.memory.peakWorkingSetSize / 1024; p.wake += m.cpu.idleWakeupsPerSecond; }
    const sys = cpuTot(), sysCpu = ((sys.busy - prevSys.busy) / (sys.all - prevSys.all)) * 100;
    if (prev) emit({ kind: "s", t: Date.now() - t0, phase: phase.name, procs: Object.fromEntries(Object.entries(procs).map(([k, p]) => [k, { cpu: +p.cpu.toFixed(1), wsMB: +p.wsMB.toFixed(1), peakMB: +p.peakMB.toFixed(1), wake: p.wake }])), sysCpu: +sysCpu.toFixed(1), load1: +os.loadavg()[0].toFixed(2) });
    prev = cur; prevSys = sys; prevT = now;
  };
  sample(); const sampler = setInterval(sample, 250);
  // CDP page metrics, 500 ms: heap, DOM nodes, layout objects, cumulative style/layout/task time.
  const KEYS = ["JSHeapUsedSize", "JSHeapTotalSize", "Nodes", "LayoutObjects", "RecalcStyleCount", "RecalcStyleDuration", "LayoutCount", "LayoutDuration", "TaskDuration", "ScriptDuration"];
  const pageMetrics = setInterval(async () => { try { const m = Object.fromEntries((await cdp("Performance.getMetrics")).metrics.map((x) => [x.name, x.value])); emit({ kind: "cdp", t: Date.now() - t0, phase: phase.name, m: Object.fromEntries(KEYS.map((k) => [k, m[k]])) }); } catch {} }, 500);
  const top = startTop({ renderer: pids().renderer, gpu: pids().gpu, browser: pids().browser }, t0);

  const S = {
    idle: async (s) => sleep(s.ms),
    idleHidden: async (s) => { w.hide(); await sleep(s.ms); w.show(); },
    scroll: async () => js("__perf.scrollSweep(80)"),
    wheel: async (s) => { for (const y of [-s.distance, s.distance]) await cdp("Input.synthesizeScrollGesture", { x: 150, y: 420, yDistance: y, speed: s.speed, gestureSourceType: "mouse", preventFling: true }); },
    hover: async () => { for (const dir of [1, -1]) for (let k = 0; k <= 90; k++) { await cdp("Input.dispatchMouseEvent", { type: "mouseMoved", x: 150, y: dir > 0 ? 70 + k * 8 : 790 - k * 8 }); await sleep(16); } await cdp("Input.dispatchMouseEvent", { type: "mouseMoved", x: 900, y: 450 }); await sleep(500); },
    status: async () => js("__perf.statusChurn(120, 5)"),
    stream: async () => js("__perf.stream(8000)"),
    sidebar: async () => js("__perf.sidebarToggle(5)"),
    resize: async () => { for (let i = 0; i < 20; i++) { w.setSize(1440 - i * 22, 900); await sleep(40); } for (let i = 20; i >= 0; i--) { w.setSize(1440 - i * 22, 900); await sleep(40); } },
    appearance: async () => { for (let i = 0; i < 10; i++) { await cdp("Emulation.setEmulatedMedia", { features: [{ name: "prefers-color-scheme", value: i % 2 ? "dark" : "light" }] }); await sleep(300); } await cdp("Emulation.setEmulatedMedia", { features: [] }); },
  };
  // The stress test: the same fixed sequence in every run.
  const PLAN = [
    { name: "idle", id: "idle", ms: 20000, rows: 50 },
    { name: "idleHidden", id: "idleHidden", ms: 10000, rows: 50 },
    { name: "scroll", id: "scroll@200", rows: 200 },
    { name: "wheel", id: "wheel@200", rows: 200, distance: 6000, speed: 4000 },
    { name: "wheel", id: "wheel@500", rows: 500, distance: 20000, speed: 5000 },
    { name: "hover", id: "hover", rows: 50 },
    { name: "status", id: "status", rows: 50 },
    { name: "stream", id: "stream", rows: 50 },
    { name: "sidebar", id: "sidebar", rows: 50 },
    { name: "resize", id: "resize", rows: 50 },
    { name: "appearance", id: "appearance", rows: 50 },
    { name: "idle", id: "idleAfter", ms: 15000, rows: 50 },
  ];
  // Memory diagnostic: is the growth under status churn a leak (keeps rising) or a cache (levels off)?
  const MEMORY = [{ name: "idle", id: "idle", ms: 15000, rows: 50 }, ...Array.from({ length: 6 }, (_, i) => ({ name: "status", id: "status" + (i + 1), rows: 50 })), { name: "idle", id: "idleAfter", ms: 20000, rows: 50 }];
  const STEPS = PLAN_NAME === "memory" ? MEMORY : PLAN;
  await sleep(3000); // baseline settle after the theme switch (recorded as phase "load")
  const snap = () => { const o = {}; for (const m of app.getAppMetrics()) { const k = kindOf(m); o[k] = (o[k] || 0) + m.cpu.cumulativeCPUUsage; } return o; };
  for (const s of STEPS) {
    phase = { name: "gap" };
    const rows = await js(`__perf.setRows(${s.rows})`); await sleep(1200);
    await contentTracing.startRecording({ included_categories: LIGHT_CATS, excluded_categories: ["*"] });
    const useRaf = !/^idle/.test(s.name); if (useRaf) await js("__perf.frames.start()");
    const c0 = snap(), m0 = Object.fromEntries((await cdp("Performance.getMetrics")).metrics.map((x) => [x.name, x.value])), ts = Date.now();
    phase = { name: s.id }; const res = await S[s.name](s); phase = { name: "gap" };
    const te = Date.now(), c1 = snap(), m1 = Object.fromEntries((await cdp("Performance.getMetrics")).metrics.map((x) => [x.name, x.value]));
    const fr = useRaf ? await js("__perf.frames.stop()") : null;
    const tr = summarizeTrace(await contentTracing.stopRecording(path.join(os.tmpdir(), `tl-${process.pid}.json`)));
    const d = (k) => (m1[k] ?? 0) - (m0[k] ?? 0);
    const rec = { kind: "phase", phase: s.id, rows, t0: ts - t0, t1: te - t0, wall: te - ts, res,
      cpuMs: Object.fromEntries(Object.keys(c1).map((k) => [k, Math.round((c1[k] - (c0[k] || 0)) * 1000)])),
      style: { n: d("RecalcStyleCount"), ms: +(d("RecalcStyleDuration") * 1000).toFixed(2) }, layout: { n: d("LayoutCount"), ms: +(d("LayoutDuration") * 1000).toFixed(2) },
      taskMs: +(d("TaskDuration") * 1000).toFixed(2), scriptMs: +(d("ScriptDuration") * 1000).toFixed(2), heapMB: +(m1.JSHeapUsedSize / 1048576).toFixed(2), nodes: m1.Nodes, layoutObjects: m1.LayoutObjects,
      rafFrames: fr, trace: tr, dom: await js("__perf.domStats()") };
    emit(rec);
    const tot = Object.values(rec.cpuMs).reduce((a, b) => a + b, 0);
    log(s.id, "cpu", tot, JSON.stringify(rec.cpuMs), "drawn", tr.frames.DrawFrame || 0, "dropped", tr.frames.DroppedFrame || 0);
  }
  phase = { name: "end" };
  clearInterval(sampler); clearInterval(pageMetrics); top.kill(); await sleep(300);
  emit({ kind: "end", t: Date.now() - t0, loadavg: os.loadavg() }); out.end(); await sleep(300); app.exit(0);
});
