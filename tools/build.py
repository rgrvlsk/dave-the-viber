"""Build lite and full theme CSS + JSON from src/. Usage: python3 -I build.py <scratchpad>"""
import json, sys, os, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sprites import S as SPR, svg, uri, grid, path

def multi(art, colors, w_css=None):
    rows, w, h = grid(art)
    body = "".join(f"<path fill='{c}' d='{path(rows, ch)}'/>" for ch, c in colors.items() if path(rows, ch))
    return "url(\"" + uri(f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {w} {h}' shape-rendering='crispEdges'>{body}</svg>") + "\")"

WOOD = """
aaaaaa..........
......aaaa......
..........aaaaaa
bb..............
...bbbbbb.......
................
.......aaaaa....
aaa.........bbbb
"""
WAVES = """
....aaaaaaaa....
..aa........aa..
.a...bbbbbb...a.
a..bb......bb..a
..b...aaaa...b..
.b..aa....aa..b.
b..a........a..b
..a..........a..
"""
TEAR = """
####
.##.
"""
root = sys.argv[1]
tok = {k: "url(\"" + uri(svg(a)[0]) + "\")" for k, a in SPR.items()}
tok["wood"] = multi(WOOD, {"a": "#dcc59c", "b": "#e9d7b3"})
tok["waves"] = multi(WAVES, {"a": "#ffffff0a", "b": "#ffffff05"})
tok["tear"] = "url(\"" + uri(svg(TEAR)[0]) + "\")"
extra_tok_path = os.path.join(root, "src", "extra_sprites.py")
if os.path.exists(extra_tok_path):
    ns = {"multi": multi, "uri": uri, "svg": svg}
    exec(open(extra_tok_path).read(), ns)
    tok.update(ns["TOKENS"])
def fill(css):
    def rep(m):
        k = m.group(1)
        if k not in tok: raise SystemExit("missing token " + k)
        return tok[k]
    return re.sub(r"\{\{(\w+)\}\}", rep, css)
core = fill(open(os.path.join(root, "src/core.css")).read())
extras_p = os.path.join(root, "src/extras.css")
extras = fill(open(extras_p).read()) if os.path.exists(extras_p) else ""
colors = json.load(open(os.path.join(root, "src/colors.json")))
os.makedirs(os.path.join(root, "out"), exist_ok=True)
for name, css, title in [("lite", core, "Pixel Sushi Counter Lite"), ("full", core + "\n" + extras, "Pixel Sushi Counter")]:
    open(os.path.join(root, f"out/{name}.css"), "w").write(css)
    theme = {"version": 1, "name": title, "appearance": "light", **colors, "css": css}
    json.dump(theme, open(os.path.join(root, f"out/{name}.json"), "w"), indent=1, ensure_ascii=False)
    imgs = sum(len(m) for m in re.findall(r"data:[^\"')]+", css))
    print(f"{name}: css {len(css)} chars, data: URIs {imgs} chars")
