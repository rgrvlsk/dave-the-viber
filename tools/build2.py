"""Build lite and full theme CSS + JSON from src/. Usage: python3 -I build.py <scratchpad>"""
import json, sys, os, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sprites import S as SPR, uri, grid, png, webp

def multi(art, colors, w_css=None):
    rows, w, h = grid(art)
    return "url(\"" + webp(rows, w, h, colors) + "\")"

WOOD_P = {"a": "#dcc59c", "b": "#e9d7b3"}
WAVES_P = {"a": "#ffffff06", "b": "#ffffff03"}
WOOD = png("wood", WOOD_P)
WAVES = png("waves", WAVES_P)
TEAR = png("tear")
root = sys.argv[1]
tok = {k: multi(a, {"#": None}) for k, a in SPR.items()}
tok["wood"] = multi(WOOD, WOOD_P)
tok["waves"] = multi(WAVES, WAVES_P)
tok["tear"] = multi(TEAR, {"#": None})
for _k, _c in {"approval": "#7a4d00", "input": "#34468c", "request": "#84295f", "woke": "#7a4d00"}.items():
    tok[_k + "_ink"] = multi(SPR[_k], {"#": _c})
def pixel_filter(cells):
    """SVG pixel shader: sample one pixel per cell (flood + tile + composite) and grow it to fill the cell (dilate)."""
    h = cells // 2
    f = (f"<filter id='f' x='0' y='0' width='1' height='1'><feFlood x='{h}' y='{h}' width='1' height='1'/>"
         f"<feComposite width='{cells}' height='{cells}'/><feTile result='a'/><feComposite in='SourceGraphic' in2='a' operator='in'/>"
         f"<feMorphology operator='dilate' radius='{h}'/></filter>")
    return 'url("' + uri("<svg xmlns='http://www.w3.org/2000/svg'>" + f + "</svg>") + '#f")'
tok["tear_paper"] = multi(TEAR, {"#": "#fbf3e2"})
extra_tok_path = os.path.join(root, "src2", "sprites2.py")
if os.path.exists(extra_tok_path):
    ns = {"multi": multi, "png": png}
    exec(open(extra_tok_path).read(), ns)
    tok.update(ns["TOKENS"])
def fill(css):
    def rep(m):
        k = m.group(1)
        if k not in tok: raise SystemExit("missing token " + k)
        return tok[k]
    return re.sub(r"\{\{(\w+)\}\}", rep, css)
core_src = open(os.path.join(root, "src2/core.css")).read()
core = fill(core_src.replace("/*full*/\n", "").replace("/*/full*/\n", ""))
def minify(css, full=False):
    # Lite drops the full-only blocks; full keeps them and only loses the markers.
    css = re.sub(r"/\*/?full\*/", "", css) if full else re.sub(r"/\*full\*/.*?/\*/full\*/", "", css, flags=re.S)
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    css = re.sub(r"\s+", " ", css)
    css = re.sub(r"\s*([{};,])\s*", r"\1", css)
    css = css.replace(";}", "}").replace(" !important", "!important")
    css = re.sub(r"\s*>\s*", ">", css)
    css = re.sub(r'\[([\w-]+)="([A-Za-z_][\w-]*)"\]', r"[\1=\2]", css)
    css = re.sub(r"([{;])(-?-?[\w-]+): ", r"\1\2:", css)
    css = re.sub(r"rgb\((\d+) (\d+) (\d+) / (0?\.\d+)\)", lambda m: "#%02x%02x%02x%02x" % (int(m[1]), int(m[2]), int(m[3]), round(float(m[4]) * 255)), css)
    css = re.sub(r"-webkit-(?:mask[\w-]*|backdrop-filter):(?:[^;{}]|\{\{\w+\}\})*;", "", css)
    css = re.sub(r"(?<=[ :,(])transparent(?=[ ,;)}])", "#0000", css)
    css = re.sub(r"(?<=[ :,])(\d+)0ms\b", lambda m: ("." + m[1] + "s") if len(m[1]) == 2 else m[0], css)
    css = re.sub(r"(?<=[ :,(])0\.(\d)", r".\1", css)
    css = re.sub(r'"((?:[A-Z][a-z]+ ?)+(?: [A-Z]{2,})?(?: [A-Za-z]+)*)"(?=[,;)])', lambda m: m[1] if re.fullmatch(r"[A-Za-z]+( [A-Za-z]+)*", m[1]) else m[0], css)
    css = re.sub(r"#([0-9a-f])\1([0-9a-f])\2([0-9a-f])\3\b", r"#\1\2\3", css)
    css = re.sub(r"\"[^\"]*\"|'[^']*'| / ", lambda m: "/" if m[0] == " / " else m[0], css)  # "a / b" -> "a/b" outside strings
    uses =__import__("collections").Counter(re.findall(r"--sk-[a-z0-9-]+", css))
    names = sorted(uses, key=lambda n: (-uses[n] * len(n), n))  # most chars saved first; name breaks ties, so builds repeat
    for i, n in enumerate(names):
        css = re.sub(re.escape(n) + r"(?![a-z0-9-])", "--k" + "abcdefghijklmnopqrstuvwxyz"[i % 26] + ("" if i < 26 else str(i // 26)), css)
    return css.strip()
lite = fill(minify(core_src))
extras_p = os.path.join(root, "src2/extras.css")
extras_src = open(extras_p).read() if os.path.exists(extras_p) else ""
extras = fill(extras_src)
def balanced(name, css):
    depth = 0
    for i, ch in enumerate(re.sub(r"/\*.*?\*/", "", css, flags=re.S)):
        depth += (ch == "{") - (ch == "}")
        if depth < 0: raise SystemExit(f"{name}: stray '}}' near char {i}")
    if depth: raise SystemExit(f"{name}: {depth} unclosed '{{'")
balanced("core", core); balanced("lite", lite); balanced("extras", extras)
for _n, _c in (("core", core), ("extras", extras)):
    if re.search(r":has\((?:[^()]|\([^()]*\))*:has\(", _c): raise SystemExit(f"{_n}: :has() nested inside :has()")
colors = json.load(open(os.path.join(root, "src2/colors.json")))
os.makedirs(os.path.join(root, "out2"), exist_ok=True)
def strip_notes(css):
    # Keep only the comments that record a known limit (ponytail:) in the published full CSS.
    css = re.sub(r"/\*(?:(?!\*/).)*?\*/\n?", lambda m: m.group(0) if "ponytail:" in m.group(0) else "", css, flags=re.S)
    # One declaration per line, no indentation, no blank lines: readable and inside 50,000.
    css = re.sub(r"\n\s*\n+", "\n", re.sub(r"\n[ \t]+", "\n", css))
    css = re.sub(r"(?m)^(-?-?[a-z][\w-]*): ", r"\1:", css).replace(" {\n", "{\n")
    return css.strip() + "\n"
# ---- CSS nesting: rules in a row that share a selector prefix P become P{&rest{…}…}.
# Rules never move, P is one complex selector without a pseudo-element, so `&` = :is(P) keeps
# specificity and order. The build expands the result and refuses it unless it equals the flat CSS.
NEST = {"lite": True, "full": True}  # False emits flat CSS (fallback if a gallery importer rejects nesting)
LIMIT = {"lite": 20000, "full": 50000}

def _skip(s, i):
    q = s[i]; i += 1
    while s[i] != q: i += 2 if s[i] == "\\" else 1
    return i + 1

def _blocks(s):
    """Top-level (prelude, body) pairs; bodies keep their nested blocks."""
    out, i = [], 0
    while i < len(s):
        j = s.index("{", i); k, d = j + 1, 1
        while d:
            if s[k] in "\"'": k = _skip(s, k); continue
            d += (s[k] == "{") - (s[k] == "}"); k += 1
        out.append((s[i:j], s[j + 1:k - 1])); i = k
    return out

def _split(s, sep=","):
    """Split at sep outside strings, () and []."""
    parts, d, i, start = [], 0, 0, 0
    while i < len(s):
        if s[i] in "\"'": i = _skip(s, i); continue
        d += (s[i] in "([") - (s[i] in ")]")
        if s[i] == sep and d == 0: parts.append(s[start:i]); start = i + 1
        i += 1
    return parts + [s[start:]]

def _cuts(sel):
    """Where a parent prefix may end: before a combinator, a simple selector or a pseudo-element."""
    out, d, i = [], 0, 0
    while i < len(sel):
        ch = sel[i]
        if ch in "\"'": i = _skip(sel, i); continue
        if ch == "\\": i += 2; continue
        if d == 0 and i > 0 and sel[i - 1] not in " >+~(,:":
            if sel.startswith("::", i): out.append(i); break  # the parent never holds a pseudo-element
            if ch in " >+~:[.#": out.append(i)
        d += (ch in "([") - (ch in ")]")
        i += 1
    return out

def _rel(rest):
    if rest == "": return "&"
    if rest[0] in ">+~": return rest
    if rest[0] == " ": return "& " + rest[1:] if rest[1] == ":" else rest[1:]  # bare child = descendant
    return "&" + rest

def _emit(rules):
    out, i = [], 0
    while i < len(rules):
        best = (0, None, i + 1)
        for c in _cuts(rules[i][0][0]):
            P = rules[i][0][0][:c]
            if P.lstrip(">+~& ") == "": continue
            j = i
            while j < len(rules) and all(s.startswith(P) and (s == P or len(P) in _cuts(s)) for s in rules[j][0]): j += 1
            if j - i < 2: continue
            flat = sum(len(",".join(s)) + len(b) + 2 for s, b in rules[i:j])
            saving = flat - len(P) - 2 - len(_kids(rules[i:j], P))
            if saving > best[0]: best = (saving, P, j)
        _, P, j = best
        out.append(",".join(rules[i][0]) + "{" + rules[i][1] + "}" if P is None else P + "{" + _kids(rules[i:j], P) + "}")
        i = j
    return "".join(out)

def _kids(rules, P):
    kids = [([s[len(P):] for s in sels], b) for sels, b in rules]
    head = ""
    if kids[0][0] == [""]: head = kids[0][1] + (";" if len(kids) > 1 else ""); kids = kids[1:]  # declarations first
    return head + _emit([([_rel(s) for s in sels], b) for sels, b in kids])

def _sel(pre):
    # " + " / " ~ " -> "+" / "~" in selectors (values keep their spaces: calc() needs them).
    return [re.sub(r"\"[^\"]*\"|'[^']*'|\s*([+~])\s*", lambda m: m[1] or m[0], s) for s in _split(pre)]

def nest(css):
    out, run = [], []
    def flush():
        if run: out.append(_emit(run)); run.clear()
    for pre, body in _blocks(css):
        if pre.startswith("@"):
            flush(); out.append(pre + "{" + (nest(body) if pre.startswith(("@media", "@supports")) else body) + "}")
        else: run.append((_sel(pre), body))
    flush()
    return "".join(out)

def flatten(css, par=None, out=None):
    """Expand nested CSS into a flat list of (selectors, declarations) and at-rule markers."""
    out = [] if out is None else out
    for pre, body in _blocks(css):
        if pre.startswith("@"):
            out.append((pre,)); flatten(body, par, out) if pre.startswith(("@media", "@supports")) else out.append(body); out.append(("}",)); continue
        sels = _sel(pre)
        if par: sels = [s.replace("&", p) if "&" in s else p + ("" if s[0] in ">+~" else " ") + s for s in sels for p in par]
        k = min([m.start() for m in re.finditer(r"\{", re.sub(r"\"[^\"]*\"|'[^']*'", lambda m: "x" * len(m[0]), body))] or [len(body)])
        decl = body[:body.rfind(";", 0, k) + 1] if k < len(body) else body
        if decl.rstrip(";"): out.append((tuple(sels), decl.rstrip(";")))
        if k < len(body): flatten(body[len(decl):], sels, out)
    return out

for name, css, title in [("lite", lite, "Pixel Sushi Rail Lite"), ("full", fill(minify(core_src + "\n" + extras_src, full=True)), "Pixel Sushi Rail")]:
    flat_len = len(css)
    if NEST[name]:
        nested = nest(css)
        if flatten(nested) != flatten(css): raise SystemExit(f"{name}: nested CSS does not expand to the flat CSS")
        css = nested
    if len(css) > LIMIT[name]: raise SystemExit(f"{name}: {len(css)} chars > limit {LIMIT[name]}")
    open(os.path.join(root, f"out2/{name}.css"), "w").write(css)
    theme = {"version": 1, "name": title, "appearance": "dark", "canvas": colors["canvas"], "accent": colors["accent"], "colors": colors["colors"], "variants": {"light": colors["colors"]}, "css": css}
    json.dump(theme, open(os.path.join(root, f"out2/{name}.json"), "w"), indent=1, ensure_ascii=False)
    imgs = sum(len(m) for m in re.findall(r"data:[^\"')]+", css))
    print(f"{name}: css {len(css)} chars (flat {flat_len}), data: URIs {imgs} chars")
# The exact image of every sprite the full CSS uses, one file per token, to browse in Finder.
sprite_dir = os.path.join(root, "out2/sprites")
os.makedirs(sprite_dir, exist_ok=True)
for f in os.listdir(sprite_dir):
    if f.endswith((".svg", ".webp")): os.remove(os.path.join(sprite_dir, f))
for k, v in tok.items():
    if v in css:
        open(os.path.join(sprite_dir, k + ".webp"), "wb").write(__import__("base64").b64decode(v[len('url("data:image/webp;base64,'):-2]))
