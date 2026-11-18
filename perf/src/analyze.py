"""Analyze a stress-test run directory: per-phase and whole-run stats, skin vs no skin, plus time series.
Usage: python3 -I src/analyze.py <run-dir>   -> <run-dir>/summary.json, REPORT-data.md, series.json
Runs are in ABBA order, so runs (1,2), (3,4) ... are pairs with one of each variant: paired differences.
"""
import json, random, statistics as st, sys, collections, pathlib

d = pathlib.Path(sys.argv[1])
recs = [json.loads(l) for l in open(d / "samples.jsonl")]
runs = sorted({r["run"] for r in recs})
var = {r["run"]: r["variant"] for r in recs if r["kind"] == "meta"}
phases = collections.defaultdict(dict)  # run -> phase -> rec
for r in recs:
    if r["kind"] == "phase":
        phases[r["run"]][r["phase"]] = r
order = [p["phase"] for p in sorted(phases[runs[0]].values(), key=lambda p: p["t0"])]
samples = collections.defaultdict(list); tops = collections.defaultdict(list); cdps = collections.defaultdict(list)
for r in recs:
    if r["kind"] == "s": samples[r["run"]].append(r)
    elif r["kind"] == "top": tops[r["run"]].append(r)
    elif r["kind"] == "cdp": cdps[r["run"]].append(r)

def mean(a): return st.fmean(a) if a else None
def in_phase(lst, ph): return [x for x in lst if x["phase"] == ph]
def tot_cpu(p): return sum(p["cpuMs"].values())

def phase_metrics(run, ph):
    p = phases[run][ph]; s = in_phase(samples[run], ph); t = in_phase(tops[run], ph)
    fr = p["trace"]["frames"]; raf = p.get("rafFrames") or {}
    pw = [x["procs"].get("renderer", {}).get("power", 0) + x["procs"].get("gpu", {}).get("power", 0) for x in t if x["procs"]]
    return {
        "cpu.total.ms": tot_cpu(p), "cpu.renderer.ms": p["cpuMs"].get("renderer"), "cpu.gpu.ms": p["cpuMs"].get("gpu"), "cpu.browser.ms": p["cpuMs"].get("browser"),
        "cpu.%core": tot_cpu(p) / p["wall"] * 100,
        "energy.impact": mean(pw),
        "frames.drawn": fr.get("DrawFrame", 0), "frames.dropped": fr.get("DroppedFrame", 0),
        "raf.p95.ms": raf.get("p95"), "style.ms": p["style"]["ms"], "layout.ms": p["layout"]["ms"],
        "mem.renderer.MB": mean([x["procs"]["renderer"]["wsMB"] for x in s if "renderer" in x["procs"]]),
        "mem.gpu.MB": mean([x["procs"]["gpu"]["wsMB"] for x in s if "gpu" in x["procs"]]),
        "wake.gpu/s": mean([x["procs"]["gpu"]["wake"] for x in s if "gpu" in x["procs"]]),
        "wake.renderer/s": mean([x["procs"]["renderer"]["wake"] for x in s if "renderer" in x["procs"]]),
        "sys.cpu%": mean([x["sysCpu"] for x in s]), "wall.ms": p["wall"],
    }

def run_metrics(run):
    ps = [phases[run][ph] for ph in order]; s = [x for x in samples[run] if x["phase"] in order]
    t = [x for x in tops[run] if x["phase"] in order and x["procs"]]
    foot = [x["procs"].get("renderer", {}).get("memMB", 0) + x["procs"].get("gpu", {}).get("memMB", 0) for x in tops[run] if x["procs"]]
    heap = [x["m"]["JSHeapUsedSize"] / 1048576 for x in cdps[run]]
    pw = [x["procs"].get("renderer", {}).get("power", 0) + x["procs"].get("gpu", {}).get("power", 0) for x in t]
    return {
        "cpu.total.s": sum(tot_cpu(p) for p in ps) / 1000, "cpu.renderer.s": sum(p["cpuMs"].get("renderer", 0) for p in ps) / 1000,
        "cpu.gpu.s": sum(p["cpuMs"].get("gpu", 0) for p in ps) / 1000, "cpu.browser.s": sum(p["cpuMs"].get("browser", 0) for p in ps) / 1000,
        "energy.impact.mean": mean(pw), "frames.drawn": sum(p["trace"]["frames"].get("DrawFrame", 0) for p in ps),
        "frames.dropped": sum(p["trace"]["frames"].get("DroppedFrame", 0) for p in ps),
        "mem.renderer.max.MB": max(x["procs"]["renderer"]["wsMB"] for x in s), "mem.gpu.max.MB": max(x["procs"]["gpu"]["wsMB"] for x in s),
        "mem.footprint.max.MB": max(foot) if foot else None, "mem.footprint.end.MB": foot[-1] if foot else None,
        "heap.max.MB": max(heap), "heap.end.MB": heap[-1],
        "phases.wall.s": sum(p["wall"] for p in ps) / 1000, "sys.cpu%": mean([x["sysCpu"] for x in s]),
    }

pairs = [(runs[i], runs[i + 1]) for i in range(0, len(runs) - 1, 2)]
def split(m):  # m: run -> value ; returns none list, full list, paired diffs (full - none)
    a = [m[r] for r in runs if var[r] == "none" and m[r] is not None]; b = [m[r] for r in runs if var[r] == "full" and m[r] is not None]
    diffs = []
    for x, y in pairs:
        n, f = (x, y) if var[x] == "none" else (y, x)
        if m[n] is not None and m[f] is not None: diffs.append(m[f] - m[n])
    return a, b, diffs
random.seed(7)
def ci(diffs, k=5000):
    if len(diffs) < 2: return (None, None)
    bs = sorted(st.median(random.choices(diffs, k=len(diffs))) for _ in range(k)); return bs[int(0.025 * k)], bs[int(0.975 * k)]
def stat(m):
    a, b, dd = split(m); lo, hi = ci(dd)
    med_a, med_b = (st.median(a) if a else None), (st.median(b) if b else None)
    return {"none": med_a, "full": med_b, "none.all": a, "full.all": b, "diff": st.median(dd) if dd else None, "ci": [lo, hi],
            "ratio": (med_b / med_a) if med_a else None, "sig": lo is not None and (lo > 0 or hi < 0)}

summary = {"runs": {r: var[r] for r in runs}, "pairs": pairs, "phases": {}, "whole": {}}
for ph in order:
    pm = {r: phase_metrics(r, ph) for r in runs}
    summary["phases"][ph] = {k: stat({r: pm[r][k] for r in runs}) for k in pm[runs[0]]}
rm = {r: run_metrics(r) for r in runs}
summary["whole"] = {k: stat({r: rm[r][k] for r in runs}) for k in rm[runs[0]]}
summary["perRun"] = rm
json.dump(summary, open(d / "summary.json", "w"), indent=1)

# Time series, 1 s buckets per run (all samples kept in samples.jsonl).
series = {"runs": [], "phases": {}}
for r in runs:
    b = collections.defaultdict(lambda: collections.defaultdict(list))
    for x in samples[r]:
        k = x["t"] // 1000; P = x["procs"]
        for name, v in [("cpuRenderer", P.get("renderer", {}).get("cpu")), ("cpuGpu", P.get("gpu", {}).get("cpu")), ("cpuTotal", sum(p["cpu"] for p in P.values())),
                        ("memRenderer", P.get("renderer", {}).get("wsMB")), ("memGpu", P.get("gpu", {}).get("wsMB")), ("sysCpu", x["sysCpu"])]:
            if v is not None: b[k][name].append(v)
    for x in tops[r]:
        if x["procs"]:
            k = x["t"] // 1000; b[k]["energy"].append(x["procs"].get("renderer", {}).get("power", 0) + x["procs"].get("gpu", {}).get("power", 0))
            b[k]["footprint"].append(x["procs"].get("renderer", {}).get("memMB", 0) + x["procs"].get("gpu", {}).get("memMB", 0))
    for x in cdps[r]: b[x["t"] // 1000]["heap"].append(x["m"]["JSHeapUsedSize"] / 1048576)
    keys = sorted(b); series["runs"].append({"run": r, "variant": var[r], "t": keys,
        **{m: [round(st.fmean(b[k][m]), 1) if b[k][m] else None for k in keys] for m in ["cpuRenderer", "cpuGpu", "cpuTotal", "memRenderer", "memGpu", "sysCpu", "energy", "footprint", "heap"]}})
for ph in order:
    series["phases"][ph] = [st.median(phases[r][ph]["t0"] for r in runs) / 1000, st.median(phases[r][ph]["t1"] for r in runs) / 1000]
json.dump(series, open(d / "series.json", "w"))

def f(v, n=0):
    return "–" if v is None else (f"{v:,.{n}f}")
def row(name, s, n=0):
    lo, hi = s["ci"]; r = f"{s['ratio']:.2f}×" if s["ratio"] else "–"
    return f"| {name} | {f(s['none'], n)} | {f(s['full'], n)} | {f(s['diff'], n)} [{f(lo, n)}, {f(hi, n)}]{'' if s['sig'] else ' n.s.'} | {r} |"
L = ["# Stress test data: skin d292df3 vs no skin", "", f"Runs: {', '.join(f'{r}={var[r]}' for r in runs)}. Medians of 5; diff = median of 5 paired (full − none) with 95% bootstrap CI.", "",
     "## Whole stress test", "", "| Metric | No skin | Skin | Diff [95% CI] | Ratio |", "|---|---:|---:|---:|---:|"]
W = summary["whole"]
for k, n in [("cpu.total.s", 1), ("cpu.renderer.s", 1), ("cpu.gpu.s", 1), ("cpu.browser.s", 1), ("energy.impact.mean", 1), ("frames.drawn", 0), ("frames.dropped", 0),
             ("mem.renderer.max.MB", 0), ("mem.gpu.max.MB", 0), ("mem.footprint.max.MB", 0), ("mem.footprint.end.MB", 0), ("heap.max.MB", 1), ("heap.end.MB", 1), ("phases.wall.s", 1), ("sys.cpu%", 1)]:
    L.append(row(k, W[k], n))
for k, n in [("cpu.total.ms", 0), ("cpu.%core", 1), ("energy.impact", 1), ("frames.drawn", 0), ("frames.dropped", 0), ("raf.p95.ms", 1), ("style.ms", 0), ("layout.ms", 0), ("mem.renderer.MB", 0), ("mem.gpu.MB", 0), ("wake.gpu/s", 0)]:
    L += ["", f"## {k} per phase", "", "| Phase | No skin | Skin | Diff [95% CI] | Ratio |", "|---|---:|---:|---:|---:|"]
    for ph in order: L.append(row(ph, summary["phases"][ph][k], n))
open(d / "REPORT-data.md", "w").write("\n".join(L) + "\n")
print("\n".join(L[:22]))
