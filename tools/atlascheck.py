"""Judge for the local edition. Usage:
  python3 -I tools/atlascheck.py page <out dir>   writes h.html + atlas.webp: every sprite use as the full edition
      writes it (class a) and as relayer() rewrites it (class b), in boxes of the app's sizes. Serve the folder, open
      h.html in T3's browser, `await go('a')`, screenshot, `await go('b')`, screenshot (go(v, zoom, scrollY); zoom 0.5
      emulates 1x; 'c' = b without the image, the control).
  python3 -I tools/atlascheck.py diff a.png b.png  counts differing pixels; `at(points)` in the page names the cells.
Expected: 0, except the fractional-size koi cell (40.5x26.25, a half device pixel on purpose)."""
import sys, os, shutil, tempfile, io, json, contextlib
if sys.argv[1] == "diff":
    from PIL import Image, ImageChops
    a = Image.open(sys.argv[2]).convert("RGB"); b = Image.open(sys.argv[3]).convert("RGB")
    d = ImageChops.difference(a, b); bbox = d.getbbox()
    if not bbox: sys.exit(print("differing pixels: 0"))
    px = d.load(); g = {}; n = 0
    for y in range(bbox[1], bbox[3]):
        for x in range(bbox[0], bbox[2]):
            if px[x, y] != (0, 0, 0):
                n += 1; c = g.setdefault((x // 96, y // 96), [x / 2, y / 2, 0]); c[2] += 1
    print("differing pixels:", n, "bbox", bbox); sys.exit(print(json.dumps(list(g.values())[:40])))
root, out = os.path.dirname(os.path.dirname(os.path.abspath(__file__))), sys.argv[2]
os.makedirs(out, exist_ok=True)
scratch = tempfile.mkdtemp()
for d in ("src2", "tools"): shutil.copytree(os.path.join(root, d), os.path.join(scratch, d))
src = open(os.path.join(scratch, "tools/build2.py")).read()
sys.argv = ["build2.py", scratch]
B = {"__file__": os.path.join(scratch, "tools/build2.py"), "__name__": "build"}
with contextlib.redirect_stdout(io.StringIO()): exec(compile(src, "build2.py", "exec"), B)
relayer, fill, AT = B["relayer"], B["fill"], B["ATLAS_IMG"]
AT.save(os.path.join(out, "atlas.webp"), lossless=True, exact=True)

cells = []
def cell(name, box, a, b=None):
    """a: declarations as in the source ({{tokens}}); b: the local edition's (default: relayer(a))."""
    i = len(cells)
    cells.append((name, f"#c{i}{{{box}}}\n.a #c{i}{{{fill(a)}}}\n.b #c{i}{{{fill(b if b else relayer(a))}}}\n"))
BB = "box-sizing:border-box;"
for off in ("", "margin-left:.5px;margin-top:.5px;"):
    cell("peg+shade core:128", BB + "width:28px;height:19px;padding-right:10px;" + off,
         "background: {{peg_h}} 0 0 / 26px 16px no-repeat border-box, {{peg_shade}} 2px 3px / 26px 16px no-repeat content-box;")
cell("peg extras:149", "width:26px;height:16px;", "background: {{peg_h}} 0 0 / 26px 16px no-repeat;")
for off in ("0px", "0.25px", "0.5px", "0.75px", "0.33px"):
    cell(f"bubble extras:190 {off}", BB + f"width:40px;height:30px;padding:4px 11px 8px;position:relative;left:{off};top:{off};background-blend-mode:lighten,normal;filter:drop-shadow(2px 2px #060e1a80);",
         "background: linear-gradient(#34468c 0 0) content-box, {{atlas}} 0 -166.5px / 18px auto no-repeat content-box, {{bubble}} center / 40px 30px;")
for w, h in ((220, 70), (233, 81.5), (180.5, 64), (251, 300)):
    cell(f"tear extras:477 {w}x{h}", f"width:{w}px;height:{h}px;background:#fbf3e2;filter:drop-shadow(3px 3px 0 #000);",
         "mask: linear-gradient(#000 0 0) top / 100% calc(100% - 4px) no-repeat, {{tear}} bottom left / 8px 4px repeat-x;")
cell("foot rod core:565", "width:36px;height:32px;",
     "background: linear-gradient(#0e1620 0 0) 14px 9px / 2px 2px no-repeat, linear-gradient(90deg, #0e1620 0 2px, #c9d1d8 2px 4px, #0e1620 4px) 12px 11px / 6px 10px no-repeat, {{base}} 0 20px / 36px 12px no-repeat;")
cell("foot core:701", "width:36px;height:12px;", "background: {{base}} 0 0 / 36px 12px no-repeat;")
for h in (61, 76.5, 91, 95, 140, 200):
    cell(f"bracket extras:326 h{h}", BB + f"width:250px;height:{h}px;padding:4px 4px 5px 20px;", "background: {{bracket}} 2px 100% / 16px 9px no-repeat;")
for w, h in ((19, 15), (38, 30), (28.5, 22.5)):
    cell(f"chef extras:1083 {w}x{h} (mask-box-image)", f"width:{w}px;height:{h}px;background:#5fd4ef;",
         "mask: {{chef}} 0 / 100%;", "-webkit-mask-box-image: {{bg_chef}} / 0;")
for w in (300, 437, 1000.5):
    cell(f"noren extras:378 w{w}", f"width:{w}px;height:36px;", "background: {{noren}} 0 0 / 80px 36px repeat-x;")
for w, h in ((256, 100), (311, 100), (600, 100), (255, 800), (311.5, 1300)):
    cell(f"night core:104 {w}x{h}", f"width:{w}px;height:{h}px;", "background: {{night}} left top / 256px 100px repeat-x;")
cell("clip extras:337", BB + "width:28px;height:19px;padding-right:10px;", "background: {{clip}} 1px 0 / 28px 14px no-repeat;")
for w, h in ((44, 28), (43, 27), (36, 12), (28, 28), (40.5, 26.25)):
    cell(f"fish sign extras:417 {w}x{h}", f"width:{w}px;height:{h}px;", "background: {{fish}} center / 36px 21px no-repeat, #d8a15f !important;")
for w in (300, 301, 322.5):
    cell(f"specials extras:876 w{w}", f"width:{w}px;height:90px;border-bottom:2px dashed #3c4c70;filter:drop-shadow(0 0 5px #28aac8aa);",
         "background: {{specials}} 50% 12px / 150px 64px no-repeat;")
for w in (400, 401, 448.5, 512.25):
    cell(f"drinks extras:923 w{w}", f"width:{w}px;height:120px;box-shadow:inset 0 -2px #a86030;", "background: {{drinks}} 50% / 183px no-repeat #18243c;")
for w in (255, 256, 311, 400, 273.5):
    cell(f"tank extras:1228 w{w}", f"width:{w}px;height:70px;", """background:
      linear-gradient(#11131a 0 0) top / 100% 3px no-repeat,
      linear-gradient(#bff3ffb3 0 0) 0 6px / 100% 1px no-repeat,
      {{weed_s}} left 12px bottom 4px / 14px 30px no-repeat,
      {{weed_s}} 58% calc(100% - 4px) / 14px 30px no-repeat,
      {{weed_s}} right 36px bottom 4px / 14px 30px no-repeat,
      {{coral}} right 8px bottom 6px / 22px 20px no-repeat,
      {{brain}} 34% calc(100% - 6px) / 18px 10px no-repeat,
      {{sand}} left bottom / 16px 8px repeat-x,
      linear-gradient(90deg, #bff3ff59 1px, #0000 0 calc(100% - 1px), #bff3ff59 0),
      linear-gradient(#0000 6px, #006a8c1f 6px, #00587a2e 30px, #00334f8c);""")
    cell(f"weed_a extras:1265 w{w}", f"width:{w}px;height:14px;",
         "background: {{weed_a}} left 12px top 0 / 14px 44px no-repeat, {{weed_a}} 58% 0 / 14px 44px no-repeat, {{weed_a}} right 36px top 0 / 14px 44px no-repeat;")
cell("tank fish extras:1247", "width:624px;height:32px;", "background: {{fish}} 0 0 / 24px 14px no-repeat, {{fish_l}} 600px 18px / 24px 14px no-repeat;")
for w, d in ((700, "1e5px"), (901, "1e5px"), (1200.5, "1e5px"), (640, "-5px")):
    cell(f"dave+stool extras:1335 w{w} d{d}", f"width:{w}px;height:120px;--sk-d:{d};",
         "background: {{dave}} right 14px top 12px / clamp(0px, var(--sk-d), 112px) 120px no-repeat, {{stool}} right 30px bottom -4px / 80px 28px repeat-x;")
for w in (256, 311):
    cell(f"counter extras:1159 w{w}", BB + f"width:{w}px;height:{74 if w == 256 else 150}px;padding:36px 8px 6px;",
         "background: {{counter}} left 0 top 14px / 64px 16px repeat-x, linear-gradient(transparent 30px, #6e4220 30px 32px, #8f5a2b 32px);")
    cell(f"counter extras:1320 w{w}", f"width:{w * 2}px;height:60px;",
         "background: {{counter}} 0 0 / 64px 16px repeat-x, linear-gradient(#0000 16px, #6e4220 0 18px, #b9783d 0);")
for w, h in ((700, 52), (333, 52), (300, 90)):
    cell(f"beam extras:1410 {w}x{h}", f"width:{w}px;height:{h}px;",
         "background: linear-gradient(transparent 50px, #1a110a 0) 0 0 / 100% 52px no-repeat, {{beam}} 0 0 / 64px 52px #4a2f1e;")

html = ["<!doctype html><meta charset=utf-8><title>atlascheck</title><style>",
        "html{image-rendering:pixelated;background:#445}body{margin:0;display:flex;flex-wrap:wrap;gap:6px;padding:6px;align-items:flex-start;align-content:flex-start}",
        "*,*::before,*::after{animation:none!important;transition:none!important}", ".w{flex:none;padding:3px}"]
html += [c[1] for c in cells] + ["</style><body>"]
html += [f'<div class=w data-n="{c[0]}"><div id=c{i}></div></div>' for i, c in enumerate(cells)]
html.append("""<script>
window.go = async (v, zoom, sy) => {
  document.documentElement.style.zoom = zoom || 1;
  if (!window.__u) { const b = await (await fetch('atlas.webp?' + Date.now())).blob(); window.__u = URL.createObjectURL(b);
    const im = new Image(); im.src = window.__u; await im.decode(); }
  document.documentElement.style.setProperty('--theme-background-image', v === 'c' ? 'none' : `url("${window.__u}")`);
  document.documentElement.className = v === 'c' ? 'b' : v;
  document.body.style.paddingBottom = '2000px'; scrollTo(0, sy || 0);
  await new Promise(r => setTimeout(r, 350));
  const vis = []; [...document.querySelectorAll('.w')].forEach((e, i) => { const r = e.getBoundingClientRect(); if (r.top >= 0 && r.bottom <= 1408) vis.push(i); });
  return [v, zoom || 1, scrollY, devicePixelRatio, vis[0], vis[vis.length - 1], document.querySelectorAll('.w').length];
};
window.at = (pts) => { const o = {}; for (const [x, y, n] of pts) { const e = document.elementFromPoint(x, y), w = e && e.closest('.w'), k = w ? w.dataset.n : '?'; o[k] = (o[k] || 0) + n; } return o; };
</script>""")
open(os.path.join(out, "h.html"), "w").write("\n".join(html))
print(len(cells), "cells; atlas", AT.size)
