"""Compact report for T3's html_render: per-variant median line + min-max band, runs aligned on phase boundaries.
Usage: python3 -I src/inline.py <stress-dir> <memory-dir> <out.html>
"""
import json, sys, collections, statistics as st, bisect

def load(d):
    recs = [json.loads(l) for l in open(f"{d}/samples.jsonl")]
    var = {r["run"]: r["variant"] for r in recs if r["kind"] == "meta"}
    ph = collections.defaultdict(list)
    for r in recs:
        if r["kind"] == "phase": ph[r["run"]].append(r)
    return recs, var, ph

def aligned(d, metrics):
    recs, var, ph = load(d)
    names = [p["phase"] for p in sorted(ph[next(iter(ph))], key=lambda p: p["t0"])]
    canon = {n: (st.median(p["t0"] for r in ph for p in ph[r] if p["phase"] == n), st.median(p["t1"] for r in ph for p in ph[r] if p["phase"] == n)) for n in names}
    knots = {}
    for r in ph:
        k = [(0, 0)]
        for p in sorted(ph[r], key=lambda p: p["t0"]): k += [(p["t0"], canon[p["phase"]][0]), (p["t1"], canon[p["phase"]][1])]
        knots[r] = k
    def warp(r, t):
        k = knots[r]; i = bisect.bisect_right([x for x, _ in k], t) - 1
        if i >= len(k) - 1: return k[-1][1] + (t - k[-1][0])
        (a, A), (b, B) = k[i], k[i + 1]; return A + (t - a) / (b - a) * (B - A) if b > a else A
    buck = collections.defaultdict(lambda: collections.defaultdict(lambda: collections.defaultdict(list)))  # metric -> variant -> sec -> [run means]
    per = collections.defaultdict(list)
    for x in recs:
        if x["kind"] not in ("s", "top", "cdp") or x["run"] not in knots: continue
        for m, f in metrics.items():
            v = f(x)
            if v is not None: per[(m, x["run"], int(warp(x["run"], x["t"]) // 2000) * 2)].append(v)
    for (m, r, s), vs in per.items(): buck[m][var[r]][s].append(st.fmean(vs))
    out = {}; end = max(b for a, b in canon.values()) / 1000  # drop teardown samples after the last phase
    for m, bv in buck.items():
        out[m] = {}
        for v, secs in bv.items():
            ks = [k for k in sorted(secs) if k <= end]; out[m][v] = [[k, round(min(secs[k])), round(st.median(secs[k])), round(max(secs[k]))] for k in ks]
    return out, {n: [round(a / 1000, 1), round(b / 1000, 1)] for n, (a, b) in canon.items()}

tp = lambda key: (lambda x: (x["procs"].get("renderer", {}).get(key, 0) + x["procs"].get("gpu", {}).get(key, 0)) if x["kind"] == "top" and x["procs"] else None)
M = {"cpu": lambda x: round(sum(p["cpu"] for p in x["procs"].values()), 1) if x["kind"] == "s" else None, "energy": tp("power"), "mem": tp("memMB")}
stress, sph = aligned(sys.argv[1], M)
memo, mph = aligned(sys.argv[2], {"mem": tp("memMB"), "cpu": M["cpu"]})
S = json.load(open(f"{sys.argv[1]}/summary.json"))
bars = {p: [round(v["cpu.total.ms"]["none"]), round(v["cpu.total.ms"]["full"])] for p, v in S["phases"].items()}
W = {k: [S["whole"][k][x] for x in ("none", "full", "diff")] + [S["whole"][k]["ci"]] for k in ("cpu.total.s", "energy.impact.mean", "mem.footprint.end.MB", "frames.drawn")}
W["idle%"] = [S["phases"]["idle"]["cpu.%core"][x] for x in ("none", "full", "diff")] + [S["phases"]["idle"]["cpu.%core"]["ci"]]
data = {"stress": stress, "sph": sph, "memo": memo, "mph": mph, "bars": bars, "W": W}

html = r"""<style>
.v{--n:#3987e5;--f:#d95926;--a:#1baf7a;--g:var(--border);--i2:var(--muted-foreground);font:13px/1.45 var(--font-sans)}
.v .tiles{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:8px;margin-bottom:12px}
.v .t{background:var(--card);border-radius:var(--radius);padding:10px 12px}.v .t b{display:block;font-size:18px;font-variant-numeric:tabular-nums}.v .t span{color:var(--i2);font-size:12px}
.v .lg{display:flex;flex-wrap:wrap;gap:14px;color:var(--i2);font-size:12px;margin:4px 0 8px}.v .lg i{display:inline-block;width:14px;height:3px;border-radius:2px;vertical-align:middle;margin-right:5px}
.v .c{position:relative;background:var(--card);border-radius:var(--radius);padding:10px 12px 6px;margin:8px 0}.v h3{font-size:12px;font-weight:600;margin:0 0 2px;color:var(--i2)}
.v svg{display:block;width:100%;height:auto;overflow:visible}.v svg text{fill:var(--i2);font-size:10px}
.v .tip{position:absolute;pointer-events:none;background:var(--popover);color:var(--popover-foreground);border:1px solid var(--border);border-radius:6px;padding:5px 8px;font-size:12px;display:none;white-space:nowrap;font-variant-numeric:tabular-nums;z-index:2}
</style><div class="v">
<div class="tiles" id="tl"></div>
<div class="lg"><span><i style="background:var(--n)"></i>Sense skin (5 execucions)</span><span><i style="background:var(--f)"></i>Skin d292df3 (5)</span><span>línia = mediana · ombra = mín–màx</span></div>
<div id="ch"></div></div>
<script>
const D=__DATA__,C={none:"var(--n)",full:"var(--f)","full-noanim":"var(--a)"},N={none:"Sense skin",full:"Skin","full-noanim":"Skin sense animacions"};
const f=(v,n=0)=>v==null?"–":(+v).toLocaleString("ca",{maximumFractionDigits:n,minimumFractionDigits:n,useGrouping:false});
const T=(lab,k,n,u,x)=>{const [a,b,d,ci]=D.W[k];return `<div class="t"><span>${lab}</span><b>${f(b,n)}${u} vs ${f(a,n)}${u}</b><span>${x||(d>0?"+":"")+f(d,n)+u} [${f(ci[0],n)}, ${f(ci[1],n)}] · ${f(b/a,2)}×</span></div>`};
document.getElementById("tl").innerHTML=T("CPU per prova sencera","cpu.total.s",1," s")+T("CPU en repòs visible","idle%",0,"%")+T("Impacte energètic mitjà","energy.impact.mean",0,"")+T("Memòria al final","mem.footprint.end.MB",0," MB");
function chart(title,series,phases,unit,h=170){
  const el=document.createElement("div");el.className="c";el.innerHTML=`<h3>${title}</h3><svg viewBox="0 0 700 ${h+30}"></svg><div class="tip"></div>`;document.getElementById("ch").append(el);
  const svg=el.querySelector("svg"),tip=el.querySelector(".tip"),L=34,R=696,T0=16,B=h;const all=Object.values(series).flat();
  const xm=Math.max(...all.map(p=>p[0])),ym=Math.max(...all.map(p=>p[3]))*1.05;const X=t=>L+(R-L)*t/xm,Y=v=>B-(B-T0)*v/ym;let g="";
  Object.entries(phases).forEach(([p,[a,b]],i)=>{g+=`<rect x="${X(a)}" y="${T0}" width="${Math.max(1,X(b)-X(a))}" height="${B-T0}" fill="var(--foreground)" fill-opacity=".05"/>`;g+=`<text x="${(X(a)+X(b))/2}" y="${i%2?T0-2:T0-9}" text-anchor="middle">${p.replace("idleHidden","amagada").replace("idleAfter","repòs 2").replace(/^idle$/,"repòs").replace("appearance","aparença")}</text>`});
  for(let i=0;i<=4;i++){const v=ym*i/4;g+=`<line x1="${L}" x2="${R}" y1="${Y(v)}" y2="${Y(v)}" stroke="var(--g)"/><text x="${L-4}" y="${Y(v)+3}" text-anchor="end">${f(v)}</text>`}
  for(let t=0;t<=xm;t+=20)g+=`<text x="${X(t)}" y="${B+13}" text-anchor="middle">${t}s</text>`;
  for(const [v,pts] of Object.entries(series)){g+=`<path d="M${pts.map(p=>X(p[0]).toFixed(1)+","+Y(p[3]).toFixed(1)).join("L")}L${pts.slice().reverse().map(p=>X(p[0]).toFixed(1)+","+Y(p[1]).toFixed(1)).join("L")}Z" fill="${C[v]}" fill-opacity=".18"/>`;
    g+=`<path d="M${pts.map(p=>X(p[0]).toFixed(1)+","+Y(p[2]).toFixed(1)).join("L")}" fill="none" stroke="${C[v]}" stroke-width="2" stroke-linejoin="round"/>`}
  g+=`<line class="xl" y1="${T0}" y2="${B}" stroke="var(--i2)" stroke-dasharray="2 2" visibility="hidden"/><rect class="hit" x="${L}" y="${T0}" width="${R-L}" height="${B-T0}" fill="transparent"/>`;svg.innerHTML=g;
  const hit=svg.querySelector(".hit"),xl=svg.querySelector(".xl");
  hit.onpointermove=e=>{const p=new DOMPoint(e.clientX,e.clientY).matrixTransform(svg.getScreenCTM().inverse());const t=Math.round((p.x-L)/(R-L)*xm);xl.setAttribute("x1",X(t));xl.setAttribute("x2",X(t));xl.setAttribute("visibility","visible");
    const ph=Object.entries(phases).find(([k,[a,b]])=>t>=a&&t<=b);tip.innerHTML=`<b>${t} s</b>${ph?" · "+ph[0]:""}`+Object.entries(series).map(([v,pts])=>{const q=pts.reduce((m,x)=>Math.abs(x[0]-t)<Math.abs(m[0]-t)?x:m);return `<br><span style="color:${C[v]}">■</span> ${N[v]}: ${f(q[2])+" "+unit}`}).join("");
    const rc=el.getBoundingClientRect();tip.style.display="block";tip.style.left=Math.min(e.clientX-rc.left+12,rc.width-190)+"px";tip.style.top=(e.clientY-rc.top-50)+"px"};
  hit.onpointerleave=()=>{tip.style.display="none";xl.setAttribute("visibility","hidden")};
}
const ord=o=>Object.fromEntries(["none","full","full-noanim"].filter(k=>o[k]).map(k=>[k,o[k]]));
chart("CPU de l'app, % d'un nucli (renderer + GPU + browser)",ord(D.stress.cpu),D.sph,"%");
chart("Impacte energètic (macOS top, renderer + GPU)",ord(D.stress.energy),D.sph,"");
chart("Memòria física renderer + GPU (MB)",ord(D.stress.mem),D.sph,"MB");
chart("Diagnòstic memòria: 6 tandes de canvis d'estat seguides (MB) · verd = skin sense animacions",ord(D.memo.mem),D.mph,"MB");
chart("Diagnòstic: CPU de l'app (%) · verd = skin sense les 5 animacions infinites",ord(D.memo.cpu),D.mph,"%");
(()=>{const el=document.createElement("div");el.className="c";el.innerHTML="<h3>CPU per fase, s (mediana de 5) · sense skin → skin</h3><svg viewBox='0 0 700 190'></svg>";document.getElementById("ch").append(el);
 const ps=Object.entries(D.bars),L=34,B=160,T0=14,bw=(700-L)/ps.length,ym=Math.max(...ps.flat(2).filter(Number.isFinite))*1.1,Y=v=>B-(B-T0)*v/ym;let g="";
 for(let i=0;i<=4;i++){const v=ym*i/4;g+=`<line x1="${L}" x2="700" y1="${Y(v)}" y2="${Y(v)}" stroke="var(--g)"/><text x="${L-4}" y="${Y(v)+3}" text-anchor="end">${f(v/1000,1)}</text>`}
 ps.forEach(([p,[a,b]],i)=>{const x=L+i*bw+bw*.12,w=bw*.36;g+=`<rect x="${x}" y="${Y(a)}" width="${w}" height="${B-Y(a)}" rx="3" fill="var(--n)"><title>${p} sense skin: ${f(a/1000,2)} s</title></rect><rect x="${x+w+2}" y="${Y(b)}" width="${w}" height="${B-Y(b)}" rx="3" fill="var(--f)"><title>${p} skin: ${f(b/1000,2)} s</title></rect>`;
  g+=`<text x="${x+w}" y="${Y(Math.max(a,b))-4}" text-anchor="middle" style="fill:var(--foreground)">${f(b/a,1)}×</text><text x="${x+w}" y="${B+12}" text-anchor="middle">${p.replace("idleHidden","amagada").replace("idleAfter","repòs 2").replace(/^idle$/,"repòs").replace("appearance","aparença").replace("sidebar","barra")}</text>`});
 el.querySelector("svg").innerHTML=g})();
</script>"""
open(sys.argv[3], "w").write(html.replace("__DATA__", json.dumps(data, separators=(",", ":"))))
print(len(html), "chars template;", sys.argv[3])
