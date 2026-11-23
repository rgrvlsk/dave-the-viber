"""Build lite and full theme CSS + JSON from src/. Usage: python3 -I build.py <scratchpad>"""
import json, sys, os, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sprites import S as SPR, uri, grid, png, webp

def multi(art, colors, w_css=None):
    rows, w, h = grid(art)
    # Unquoted, MIME-less, unpadded: Chromium sniffs the WebP and accepts base64 without "=" padding.
    return "url(" + webp(rows, w, h, colors).replace("data:image/webp;base64,", "data:;base64,").rstrip("=") + ")"

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
# ---- Local edition: sprites taken from one theme image (`<themeId>.webp` beside the theme file), which the app
# exposes as `--theme-background-image: url("blob:…")`. The image is a column atlas: every sprite sits at x = 0 in its
# own row band, GAP transparent rows from the next, and strips are tiled across the whole width (the least common
# multiple of their tile widths). So a plain background or mask layer shows one sprite: `relayer` keeps the layer's
# position, shifts it up by the sprite's row and sizes the image by the sprite's scale; the box clips the rest and
# `repeat-x` still tiles. {{bg_<name>}} = the image plus mask-box-image slice numbers, for a mask as large as its box.
# ponytail: a sprite's neighbours show in a box taller than GAP rows at the sprite's scale (160 px at 2x, 80 px at 1x).
# Ceiling: today's tallest boxes are 120 px at 2x (Dave, drinks at 3x) and the sidebar footer, 74 px, whose counter
# strip has room until 190 px; trigger: a taller box or a new use in one, then give that sprite more rows (ATLAS_PLAN).
GAP = 80
def _img(k):
    from PIL import Image
    import base64, io
    b64 = tok[k][len("url(data:;base64,"):-1]
    return Image.open(io.BytesIO(base64.b64decode(b64 + "=" * (-len(b64) % 4)))).convert("RGBA")
def pack(plan):
    from PIL import Image
    from math import lcm
    plan = {k: (m,) if isinstance(m, str) else m for k, m in plan.items()}
    ims = {k: _img(k) for k in plan}
    W = lcm(*[ims[k].width for k, m in plan.items() if m[0] in ("strip", "block")])
    place, y = {}, 0
    for k, m in plan.items():
        y += m[1] if m[0] == "single" and len(m) > 1 else 0
        rows = m[1] if m[0] == "block" else ims[k].height
        place[k] = (y, rows); y += rows + GAP
    H = y - GAP
    at = Image.new("RGBA", (W, H))
    for k, (py, rows) in place.items():
        im, w, h = ims[k], ims[k].width, ims[k].height
        for yy in range(py, py + rows, h):
            for xx in range(0, W if plan[k][0] in ("strip", "block") else 1, w):
                at.paste(im.crop((0, 0, w, min(h, py + rows - yy))), (xx, yy))
        if plan[k][0] == "fill": tok["bg_" + k] = f"var(--theme-background-image) {py} {W - w} {H - py - h} 0 fill"
    return at, {k: (plan[k][0], place[k][0], ims[k].size) for k in plan if plan[k][0] != "fill"}
ATLAS_IMG, LAYERS = pack(ns["ATLAS_PLAN"]) if os.path.exists(extra_tok_path) else (None, {})
# The CSS holds offsets into this exact image, so the local CSS ends with a stamp of the image's bytes: a .json and a
# .webp from different builds show wrong cuts everywhere. tools/localcheck.py compares the stamp with the file beside it.
ATLAS_WEBP = b""
if ATLAS_IMG:
    import io, hashlib
    _b = io.BytesIO(); ATLAS_IMG.save(_b, "WEBP", lossless=True, exact=True); ATLAS_WEBP = _b.getvalue()
    ATLAS_STAMP = "/*atlas " + hashlib.sha256(ATLAS_WEBP).hexdigest()[:12] + "*/"
def _num(v):
    return f"{v:.4f}".rstrip("0").rstrip(".") if round(v, 4) else "0"
def _lp(v):
    """A length-percentage as (percent, px)."""
    m = re.fullmatch(r"(?:calc\()?(?:(-?[\d.]+)%)?(?: ([+-]) )?(?:(-?[\d.]+)(?:px)?)?\)?", v)
    if not m or not v: raise SystemExit("atlas: cannot read position " + v)
    return float(m[1] or 0), float(m[3] or 0) * (-1 if m[2] == "-" else 1)
def _position(ts):
    KX, KY = {"left": 0, "center": 50, "right": 100}, {"top": 0, "center": 50, "bottom": 100}
    if len(ts) == 4:  # edge offset edge offset
        at = {e: (K[e], _lp(o)[1] * (-1 if K[e] else 1)) for e, o in (ts[:2], ts[2:]) for K in (KX, KY) if e in K and e != "center"}
        return at.get("left") or at["right"], at.get("top") or at["bottom"]
    a, b = ts if len(ts) == 2 else (ts[0], "center")
    if a in ("top", "bottom") or b in ("left", "right"): a, b = b, a
    return ((KX[a], 0) if a in KX else _lp(a)), ((KY[b], 0) if b in KY else _lp(b))
def _layer(k, text, mask=False):
    """One layer `<position> / <size> <rest>` of sprite k, as the same layer of the theme image. A background layer
    reads the image with a `none` fallback: the app sets the variable after first paint, and an unset var() would void
    the whole declaration (wood, counter and every gradient layer with it). A mask keeps no fallback: a `none` mask
    would show its whole box."""
    kind, y0, (w, h) = LAYERS[k]
    ts = [t for t in _split(text.strip(), " ") if t]
    cut = ts.index("/")
    size = [t for t in ts[cut + 1:cut + 3] if re.match(r"[\d.]|clamp\(|auto$", t)]
    rest = ts[cut + 1 + len(size):]
    m = re.fullmatch(r"(?:clamp\(0px, (.+), )?([\d.]+)px\)?", size[0])  # clamp(0px, x, width): shown or not
    s = float(m[2]) / w
    if len(size) > 1 and size[1] != "auto" and float(size[1][:-2]) != h * s: raise SystemExit(f"atlas: {k} is not scaled evenly")
    rep = ([t for t in rest if "repeat" in t] or [None])[0]
    to = {("single", None): "no-repeat", ("single", "no-repeat"): "no-repeat", ("strip", "repeat-x"): "repeat-x",
          ("block", None): "repeat-x", ("block", "repeat"): "repeat-x", ("block", "repeat-x"): "repeat-x"}.get((kind, rep))
    if not to: raise SystemExit(f"atlas: {k} ({kind}) cannot be a {rep or 'repeat'} layer")
    (xp, xo), (yp, yo) = _position(ts[:cut])
    W, H = ATLAS_IMG.width * s, ATLAS_IMG.height * s
    px = lambda v: _num(v) + "px" * (_num(v) != "0")
    at = lambda p, o: px(o) if not p else f"calc({_num(p)}% {'-' if o < 0 else '+'} {px(abs(o))})" if px(o) != "0" else _num(p) + "%"
    out = ["var(--theme-background-image)" if mask else "var(--theme-background-image, none)", at(xp, xo + xp / 100 * (W - w * s)), at(yp, yo - y0 * s + yp / 100 * (H - h * s)), "/",
           f"clamp(0px, {m[1]}, {_num(W)}px)" if m[1] else _num(W) + "px", _num(H) + "px", to] + [t for t in rest if t != rep]
    return " ".join(out) + " " * text.endswith(" ")
def relayer(css):
    """Local edition: every background or mask layer whose image is an atlas sprite becomes a layer of the theme image.
    A custom property that holds only a sprite (`--sk-fish: {{fish}};`) is followed to its uses and dropped."""
    alias = {m[1]: m[2] for m in re.finditer(r"(--sk-[\w-]+): \{\{(\w+)\}\};", css) if m[2] in LAYERS}
    css = re.sub(r"(--sk-[\w-]+): \{\{\w+\}\};", lambda m: "" if m[1] in alias else m[0], css)
    out, i = [], 0
    for m in re.finditer(r"\{\{(\w+)\}\}|var\((--sk-[\w-]+)\)", css):
        k = m[1] or alias.get(m[2])
        if k not in LAYERS: continue
        j, d = m.end(), 0
        while d or css[j] not in ",;}!": d += (css[j] == "(") - (css[j] == ")"); j += 1
        prop = re.search(r"([\w-]+)\s*:[^;{}]*$", css[:m.start()])
        out += [css[i:m.start()], _layer(k, css[m.end():j], mask=bool(prop) and "mask" in prop[1])]; i = j
    return "".join(out) + css[i:]
def fill(css):
    def rep(m):
        k = m.group(1)
        if k not in tok: raise SystemExit("missing token " + k)
        return tok[k]
    return re.sub(r"\{\{(\w+)\}\}", rep, css)
core_src = open(os.path.join(root, "src2/core.css")).read()
core = fill(core_src.replace("/*full*/\n", "").replace("/*/full*/\n", ""))
# Short names for --sk-* custom properties and anchors: Latin-1 letters (U+00C0-U+00FF without the signs × and ÷), one
# letter for the first 62 names, two after. Valid ident code points that cost 1 of the 50,000 chars (the limit counts
# UTF-16 units, not bytes) and that no app custom property uses. Names compare by code point.
ALPHA = "".join(chr(c) for c in range(0xC0, 0x100) if c not in (0xD7, 0xF7))
def edition(css, full=False, local=False):
    for tag, keep in (("full", full), ("bg", local), ("data", not local)):
        css = re.sub(rf"/\*/?{tag}\*/", "", css) if keep else re.sub(rf"/\*{tag}\*/.*?/\*/{tag}\*/", "", css, flags=re.S)
    return re.sub(r"/\*.*?\*/", "", css, flags=re.S)
def minify(css, full=False, local=False):
    # Lite drops the full-only blocks; full keeps them and only loses the markers. /*data*/ spans (sprites as data:
    # URIs) and /*bg*/ spans (sprites cut from the theme background image) are alternatives: only local keeps bg.
    css = edition(css, full, local)
    css = re.sub(r"\s+", " ", css)
    css = re.sub(r"\s*([{};,])\s*", r"\1", css)
    css = css.replace(";}", "}").replace(" !important", "!important")
    css = re.sub(r"\s*>\s*", ">", css)
    css = re.sub(r'\[([\w-]+)([\^$*~|]?)="(-?[A-Za-z_][\w-]*)"\]', r"[\1\2=\3]", css)
    # Keyframes get one-letter names; whole-name matches only, so --sk-pot-b stays intact.
    for i, n in enumerate(dict.fromkeys(re.findall(r"@keyframes ([\w-]+)", css))):
        css = re.sub(r"(?<![\w-])" + re.escape(n) + r"(?![\w-])", "abcdefghij"[i], css)
    css = re.sub(r"([{;])(-?-?[\w-]+): ", r"\1\2:", css)
    css = re.sub(r"rgb\((\d+) (\d+) (\d+) / (0?\.\d+)\)", lambda m: "#%02x%02x%02x%02x" % (int(m[1]), int(m[2]), int(m[3]), round(float(m[4]) * 255)), css)
    css = re.sub(r"-webkit-(?:mask(?!-box-image)[\w-]*|backdrop-filter):(?:[^;{}]|\{\{\w+\}\})*;", "", css)
    css = re.sub(r"(?<=[ :,(])transparent(?=[ ,;)}!])", "#0000", css)
    css = re.sub(r"(?<=[ :,])(\d+)0ms\b", lambda m: ("." + m[1] + "s") if len(m[1]) == 2 else m[0], css)
    css = re.sub(r"(?<=[ :,(])0\.(\d)", r".\1", css)
    css = re.sub(r'"((?:[A-Z][a-z]+ ?)+(?: [A-Z]{2,})?(?: [A-Za-z]+)*)"(?=[,;)])', lambda m: m[1] if re.fullmatch(r"[A-Za-z]+( [A-Za-z]+)*", m[1]) else m[0], css)
    css = re.sub(r"#([0-9a-f])\1([0-9a-f])\2([0-9a-f])\3\b", r"#\1\2\3", css)
    css = re.sub(r"\"[^\"]*\"|'[^']*'| / ", lambda m: "/" if m[0] == " / " else m[0], css)  # "a / b" -> "a/b" outside strings
    # ") x" -> ")x" in declaration values (not selectors or @media preludes); kept before + and -, which calc() needs
    # spaced, and inside strings and after escapes.
    keep = r"\"(?:[^\"\\]|\\.)*\"|'(?:[^'\\]|\\.)*'|\\.|\{\{\w+\}\}"
    css = re.sub(r"(?<=[{;])([\w-]+:)((?:" + keep + r"|[^;{}\"'\\])*)(?=[;}])", lambda m: m[1] + re.sub(keep + r"|\) (?![-+])", lambda q: ")" if q[0] == ") " else q[0], m[2]), css)
    uses =__import__("collections").Counter(re.findall(r"--sk-[a-z0-9-]+", css))
    names = sorted(uses, key=lambda n: (-uses[n] * len(n), n))  # most chars saved first; name breaks ties, so builds repeat
    for i, n in enumerate(names):
        css = re.sub(re.escape(n) + r"(?![a-z0-9-])", "--" + ALPHA[i % 62] + ("" if i < 62 else ALPHA[i // 62]), css)
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
NEST = {"lite": True, "full": True, "local": True}  # False emits flat CSS (fallback if a gallery importer rejects nesting)
LIMIT = {"lite": 20000, "full": 50000, "local": 100000}  # galleries: 50,000; the app: 100,000

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
    else: out.append(len(sel))  # the whole selector may be the parent (A{x}A>b{y} -> A{x;>b{y}})
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
            if P.lstrip(">+~& ") == "" or "::" in P: continue  # & cannot stand for a pseudo-element
            j = i
            while j < len(rules) and all(s.startswith(P) and (s == P or len(P) in _cuts(s)) for s in rules[j][0]): j += 1
            if j - i < (1 if len(rules[i][0]) > 1 else 2): continue
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

built = {}
for name, css, title in [("lite", lite, "Dave the Viber Lite"), ("full", fill(minify(core_src + "\n" + extras_src, full=True)), "Dave the Viber"),
                         ("local", fill(minify(relayer(edition(core_src + "\n" + extras_src, True, True)), full=True, local=True)), "Dave the Viber")]:
    flat_len = len(css)
    if NEST[name]:
        nested = nest(css)
        if flatten(nested) != flatten(css): raise SystemExit(f"{name}: nested CSS does not expand to the flat CSS")
        css = nested
    css = re.sub(r"::(before|after)\b", r":\1", css)
    if name == "local" and ATLAS_WEBP: css += ATLAS_STAMP
    if len(css) > LIMIT[name]: raise SystemExit(f"{name}: {len(css)} chars > limit {LIMIT[name]}")
    open(os.path.join(root, f"out2/{name}.css"), "w").write(css)
    theme = {"version": 1, "name": title, "appearance": "dark", "canvas": colors["canvas"], "accent": colors["accent"], "colors": colors["colors"], "variants": {"light": colors["colors"]}, "css": css}
    # The local edition is a ready-to-copy pair: the app reads <themeId>.json and <themeId>.webp from its themes folder.
    jp = os.path.join(root, "out2/local/dave-the-viber.json" if name == "local" else f"out2/{name}.json")
    os.makedirs(os.path.dirname(jp), exist_ok=True)
    json.dump(theme, open(jp, "w"), indent=1, ensure_ascii=False)
    imgs = sum(len(m) for m in re.findall(r"data:[^\"')]+", css))
    print(f"{name}: css {len(css)} chars (flat {flat_len}), data: URIs {imgs} chars")
    built[name] = css
# The local edition's theme background image: lossless WebP keeps semi-transparent pixels identical to the data: URIs
# (a PNG atlas rounds them 1/255 differently).
if ATLAS_WEBP: open(os.path.join(root, "out2/local/dave-the-viber.webp"), "wb").write(ATLAS_WEBP); print(f"local image: {ATLAS_IMG.size}, {ATLAS_STAMP}")
# A /*data*/ span may define a custom property that rules outside the span still read: local must not use a variable
# that it no longer defines (an undefined var() voids the whole declaration, e.g. every background layer).
_undef = lambda c: set(re.findall(r"var\((--[^,)]+)", c)) - set(re.findall(r"(--[^:;{}\s()]+):", c))
if _undef(built["local"]) - _undef(built["full"]) - {"--theme-background-image"}:
    raise SystemExit(f"local: undefined custom properties {_undef(built['local']) - _undef(built['full'])}")
css = built["full"]
# The exact image of every sprite the full CSS uses, one file per token, to browse in Finder.
sprite_dir = os.path.join(root, "out2/sprites")
os.makedirs(sprite_dir, exist_ok=True)
for f in os.listdir(sprite_dir):
    if f.endswith((".svg", ".webp")): os.remove(os.path.join(sprite_dir, f))
for k, v in tok.items():
    if v in css:
        b64 = v[len("url(data:;base64,"):-1]
        open(os.path.join(sprite_dir, k + ".webp"), "wb").write(__import__("base64").b64decode(b64 + "=" * (-len(b64) % 4)))
