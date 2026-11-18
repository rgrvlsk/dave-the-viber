"""Build a self-contained HTML report from <run-dir>/summary.json and series.json.
Usage: python3 -I src/report.py <run-dir>  -> <run-dir>/report.html
"""
import json, sys, pathlib
d = pathlib.Path(sys.argv[1])
data = {"summary": json.load(open(d / "summary.json")), "series": json.load(open(d / "series.json"))}
html = r"""<!doctype html><html lang="ca"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Consum skin vs no-skin</title>
<style>
:root{color-scheme:light;--bg:#fcfcfb;--panel:#f4f3f0;--ink:#0b0b0b;--ink2:#52514e;--ink3:#7a7975;--grid:#e4e2dc;--band:#efede8;--s1:#2a78d6;--s2:#eb6834}
@media (prefers-color-scheme:dark){:root:not([data-theme=light]){color-scheme:dark;--bg:#1a1a19;--panel:#232321;--ink:#f0efec;--ink2:#c3c2b7;--ink3:#8f8e86;--grid:#33332f;--band:#262624;--s1:#3987e5;--s2:#d95926}}
:root[data-theme=dark]{color-scheme:dark;--bg:#1a1a19;--panel:#232321;--ink:#f0efec;--ink2:#c3c2b7;--ink3:#8f8e86;--grid:#33332f;--band:#262624;--s1:#3987e5;--s2:#d95926}
body{margin:0;background:var(--bg);color:var(--ink);font:14px/1.45 ui-sans-serif,system-ui,-apple-system,sans-serif}
main{max-width:1100px;margin:0 auto;padding:24px 16px 64px}
h1{font-size:22px;margin:0 0 4px}h2{font-size:16px;margin:32px 0 8px}p.sub{color:var(--ink2);margin:0 0 16px}
.legend{display:flex;gap:16px;color:var(--ink2);font-size:13px;margin:8px 0}.legend i{display:inline-block;width:16px;height:2px;vertical-align:middle;margin-right:6px}
.tiles{display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:8px}
.tile{background:var(--panel);border-radius:8px;padding:10px 12px}.tile b{display:block;font-size:20px;font-variant-numeric:tabular-nums}.tile span{color:var(--ink2);font-size:12px}
.chart{position:relative;background:var(--panel);border-radius:8px;padding:8px 8px 4px;margin:8px 0}
.chart h3{font-size:13px;margin:2px 4px 4px;color:var(--ink2);font-weight:600}
svg{display:block;width:100%;height:auto;overflow:visible}svg text{fill:var(--ink3);font-size:10px}
.tip{position:absolute;pointer-events:none;background:var(--bg);border:1px solid var(--grid);border-radius:6px;padding:6px 8px;font-size:12px;display:none;white-space:nowrap;font-variant-numeric:tabular-nums;z-index:2}
table{border-collapse:collapse;width:100%;font-variant-numeric:tabular-nums;font-size:13px}th,td{padding:4px 8px;border-bottom:1px solid var(--grid);text-align:right}th:first-child,td:first-child{text-align:left}
th{color:var(--ink2);font-weight:600}.ns{color:var(--ink3)}.wrap{overflow-x:auto}
</style></head><body><main>
<h1>Consum de recursos: skin Dave the Viber vs sense skin</h1>
<p class="sub" id="sub"></p>
<div class="legend"><span><i style="background:var(--s1)"></i>Sense skin</span><span><i style="background:var(--s2)"></i>Skin d292df3 (full)</span></div>
<div class="tiles" id="tiles"></div>
<h2>Sèries temporals (cada línia = una execució; bandes = fases)</h2><div id="charts"></div>
<h2>CPU per fase (mediana de 5, renderer + GPU + browser)</h2><div class="chart"><svg id="bars"></svg></div>
<h2>Taula per fase</h2><div class="wrap"><table id="tbl"></table></div>
</main><div class="tip" id="tip"></div>
<script>
const D=__DATA__;const S=D.summary,R=D.series;const C={none:"var(--s1)",full:"var(--s2)"};const NAME={none:"Sense skin",full:"Skin"};
const fmt=(v,n=0)=>v==null?"–":v.toLocaleString("ca",{maximumFractionDigits:n,minimumFractionDigits:n});
document.getElementById("sub").textContent=`5 execucions amb skin i 5 sense, ordre ABBA, Electron 44.10.1 (com T3 Code Nightly), servidor dev :7508. Diferència = mediana de 5 parelles (skin − sense) amb IC 95% bootstrap.`;
const W=S.whole;const tile=(k,lab,n,u)=>{const s=W[k];return `<div class="tile"><span>${lab}</span><b>${fmt(s.full,n)} vs ${fmt(s.none,n)}${u}</b><span>${s.ratio?fmt(s.ratio,2)+"×":""} · dif ${fmt(s.diff,n)} [${fmt(s.ci[0],n)}, ${fmt(s.ci[1],n)}]${s.sig?"":" n.s."}</span></div>`};
document.getElementById("tiles").innerHTML=[tile("cpu.total.s","CPU total per prova",1," s"),tile("cpu.gpu.s","CPU GPU",1," s"),tile("energy.impact.mean","Impacte energètic (mitjana)",1,""),tile("frames.drawn","Frames dibuixats",0,""),tile("mem.footprint.max.MB","Memòria màx. (renderer+GPU)",0," MB"),tile("heap.end.MB","JS heap al final",0," MB")].join("");
const tip=document.getElementById("tip");
function line(id,title,key,unit){
  const el=document.createElement("div");el.className="chart";el.innerHTML=`<h3>${title}</h3><svg viewBox="0 0 1000 200"></svg>`;document.getElementById("charts").append(el);
  const svg=el.querySelector("svg"),L=40,Rr=995,T=18,B=180;const xs=R.runs.flatMap(r=>r.t),ys=R.runs.flatMap(r=>r[key].filter(v=>v!=null));
  const xmax=Math.max(...xs),ymax=Math.max(...ys)*1.05||1;const X=t=>L+(Rr-L)*t/xmax,Y=v=>B-(B-T)*v/ymax;let g="";
  Object.entries(R.phases).forEach(([p,[a,b]],i)=>{g+=`<rect x="${X(a)}" y="${T}" width="${Math.max(1,X(b)-X(a))}" height="${B-T}" fill="var(--band)"/>`;if(X(b)-X(a)>18||i%2==0)g+=`<text x="${(X(a)+X(b))/2}" y="${T-5}" text-anchor="middle">${p}</text>`});
  for(let i=0;i<=4;i++){const v=ymax*i/4;g+=`<line x1="${L}" x2="${Rr}" y1="${Y(v)}" y2="${Y(v)}" stroke="var(--grid)"/><text x="${L-4}" y="${Y(v)+3}" text-anchor="end">${fmt(v)}</text>`}
  for(let t=0;t<=xmax;t+=30)g+=`<text x="${X(t)}" y="${B+14}" text-anchor="middle">${t}s</text>`;
  for(const r of R.runs){let dd="";r.t.forEach((t,i)=>{const v=r[key][i];if(v==null)return;dd+=(dd?"L":"M")+X(t).toFixed(1)+","+Y(v).toFixed(1)});g+=`<path d="${dd}" fill="none" stroke="${C[r.variant]}" stroke-width="1.5" stroke-opacity=".6" stroke-linejoin="round"/>`}
  g+=`<line id="x${id}" y1="${T}" y2="${B}" stroke="var(--ink3)" stroke-dasharray="2 2" visibility="hidden"/><rect x="${L}" y="${T}" width="${Rr-L}" height="${B-T}" fill="transparent" id="h${id}"/>`;svg.innerHTML=g;
  const hit=svg.querySelector("#h"+id),xl=svg.querySelector("#x"+id);
  hit.addEventListener("pointermove",e=>{const pt=svg.createSVGPoint();pt.x=e.clientX;pt.y=e.clientY;const p=pt.matrixTransform(svg.getScreenCTM().inverse());const t=Math.round((p.x-L)/(Rr-L)*xmax);
    xl.setAttribute("x1",X(t));xl.setAttribute("x2",X(t));xl.setAttribute("visibility","visible");
    const ph=Object.entries(R.phases).find(([k,[a,b]])=>t>=a&&t<=b);const med=v=>{const a=R.runs.filter(r=>r.variant==v).map(r=>r[key][r.t.indexOf(t)]).filter(x=>x!=null).sort((a,b)=>a-b);return a.length?a[a.length>>1]:null};
    tip.innerHTML=`<b>${t} s</b>${ph?" · "+ph[0]:""}<br><span style="color:${C.full}">■</span> Skin ${fmt(med("full"),1)} ${unit}<br><span style="color:${C.none}">■</span> Sense ${fmt(med("none"),1)} ${unit}`;
    tip.style.display="block";const rc=el.getBoundingClientRect();tip.style.left=Math.min(e.clientX-rc.left+12,rc.width-170)+"px";tip.style.top=(e.clientY-rc.top+el.offsetTop-40)+"px"});
  hit.addEventListener("pointerleave",()=>{tip.style.display="none";xl.setAttribute("visibility","hidden")});
}
line(1,"CPU total de l'app (% d'un nucli; renderer+GPU+browser+utility)","cpuTotal","%");
line(2,"CPU renderer (%)","cpuRenderer","%");line(3,"CPU GPU (%)","cpuGpu","%");
line(4,"Impacte energètic macOS top (renderer+GPU)","energy","");
line(5,"Memòria física renderer+GPU (top MEM, MB)","footprint","MB");
line(6,"Working set renderer (MB)","memRenderer","MB");line(7,"JS heap usat (MB)","heap","MB");
line(8,"CPU del sistema sencer (% de 10 nuclis; soroll de fons)","sysCpu","%");
// Grouped bars per phase.
(()=>{const svg=document.getElementById("bars"),ph=Object.keys(S.phases),L=40,T=10,B=170,Wd=960;svg.setAttribute("viewBox","0 0 1000 200");
 const v=ph.map(p=>S.phases[p]["cpu.total.ms"]);const ymax=Math.max(...v.flatMap(s=>[s.none,s.full]))*1.08;const Y=x=>B-(B-T)*x/ymax;const bw=Wd/ph.length;let g="";
 for(let i=0;i<=4;i++){const y=ymax*i/4;g+=`<line x1="${L}" x2="${L+Wd}" y1="${Y(y)}" y2="${Y(y)}" stroke="var(--grid)"/><text x="${L-4}" y="${Y(y)+3}" text-anchor="end">${fmt(y/1000,1)}s</text>`}
 ph.forEach((p,i)=>{const s=S.phases[p]["cpu.total.ms"],x=L+i*bw+bw*0.15,w=bw*0.33;
  for(const [k,dx] of [["none",0],["full",w+2]]){const h=B-Y(s[k]);g+=`<rect x="${x+dx}" y="${Y(s[k])}" width="${w}" height="${h}" rx="3" fill="${C[k]}"><title>${p} · ${NAME[k]}: ${fmt(s[k]/1000,2)} s CPU</title></rect>`}
  g+=`<text x="${x+w}" y="${B+13}" text-anchor="middle">${p}</text><text x="${x+w}" y="${Y(Math.max(s.none,s.full))-4}" text-anchor="middle" style="fill:var(--ink2)">${s.ratio?fmt(s.ratio,1)+"×":""}</text>`});
 svg.innerHTML=g})();
// Table.
(()=>{const K=[["cpu.total.ms","CPU ms",0],["cpu.gpu.ms","GPU ms",0],["energy.impact","Energia",1],["frames.drawn","Frames",0],["frames.dropped","Perduts",0],["raf.p95.ms","p95 frame ms",1],["style.ms","Estil ms",0],["layout.ms","Layout ms",0]];
 let h="<tr><th>Fase</th>"+K.map(k=>`<th>${k[1]}<br>sense → skin</th>`).join("")+"</tr>";
 for(const [p,m] of Object.entries(S.phases))h+=`<tr><td>${p}</td>`+K.map(([k,,n])=>{const s=m[k];return `<td class="${s.sig?"":"ns"}">${fmt(s.none,n)} → ${fmt(s.full,n)}${s.sig?"":" ·"}</td>`}).join("")+"</tr>";
 document.getElementById("tbl").innerHTML=h+`<tr><td colspan="9" class="ns" style="text-align:left">· = diferència no significativa (IC 95% inclou 0)</td></tr>`})();
</script></body></html>"""
open(d / "report.html", "w").write(html.replace("__DATA__", json.dumps(data)))
# Inline variant for T3's html_render: no page background, theme variables for surfaces and ink.
inline = html.replace(":root{color-scheme:light;--bg:#fcfcfb;--panel:#f4f3f0;--ink:#0b0b0b;--ink2:#52514e;--ink3:#7a7975;--grid:#e4e2dc;--band:#efede8;",
    ":root{--bg:var(--popover);--panel:var(--card);--ink:var(--foreground);--ink2:var(--muted-foreground);--ink3:var(--muted-foreground);--grid:var(--border);--band:color-mix(in srgb,var(--foreground) 6%,transparent);--x:")
inline = inline.replace("body{margin:0;background:var(--bg);color:var(--ink);", "body{margin:0;").replace("main{max-width:1100px;margin:0 auto;padding:24px 16px 64px}", "main{padding:0}")
inline = inline.replace('<h1>Consum de recursos: skin Dave the Viber vs sense skin</h1>', '')
inline = __import__("re").sub(r"@media \(prefers-color-scheme:dark\)\{[^\n]*\n:root\[data-theme=dark\]\{[^\n]*\n", "", inline)
open(d / "report-inline.html", "w").write(inline.replace("__DATA__", json.dumps(data)))
print(d / "report.html")
