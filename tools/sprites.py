"""Pixel sprites as SVG data URIs (crisp at any DPR via shape-rendering=crispEdges).
Each status sprite is one silhouette used as a CSS mask, so its colour is the label colour.
Usage: python3 -I sprites.py <out.json> [preview.html]"""
import json, os, sys, urllib.parse

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "src2", "sprites")

def _rgba(c):
    c = c.lstrip("#")
    return "#" + (c if len(c) == 8 else c + "ff")

def png(name, palette=None):
    """Sprite art from src2/sprites/<name>.png (1 px per pixel) as a text grid for the encoder.
    Without a palette every opaque pixel is "#" (a mask); with one, each colour maps back to its character."""
    from PIL import Image
    im = Image.open(os.path.join(SRC, name + ".png")).convert("RGBA")
    back = {}
    for ch, c in (palette or {}).items():
        back.setdefault(_rgba(c), ch)
    rows = []
    for y in range(im.height):
        r = ""
        for x in range(im.width):
            px = im.getpixel((x, y))
            if px[3] == 0: r += "."
            elif palette is None: r += "#"
            else:
                k = "#%02x%02x%02x%02x" % px
                assert k in back, f"{name}.png: colour {k} at {x},{y} is not in its palette"
                r += back[k]
        rows.append(r)
    return "\n".join(rows)

# Status masks, one silhouette each (the label colour fills it):
# Approval: the service bell on the pass, "chef, please confirm".
# Input: speech bubble with a question mark cut out.
# Request: a guest at the counter (head and shoulders).
# Working: steaming bowl.
# Waiting: hourglass.
# Limited: a tall wooden tag hanging on a nail (kitchen paused).
# Done: nigiri, a slice of fish over a rice block with a nori band.
# Failed: fish bone with tail, ribs and head.
# Woke: kitchen timer with two bells.
# Draft: a pencil, for an order written but not yet sent.
S = {k: png(k) for k in ("approval", "input", "request", "working", "waiting", "limited", "done", "failed", "woke", "draft")}

def grid(art):
    rows = [r for r in art.strip("\n").split("\n")]
    w = max(len(r) for r in rows)
    return [r.ljust(w, ".") for r in rows], w, len(rows)

def _rects(rows, ch, transpose=False):
    """Pixel set of `ch` as rectangles: runs on each line, merged with identical runs on the next lines."""
    if transpose:
        rows = ["".join(r[x] for r in rows) for x in range(len(rows[0]))]
    open_, out = {}, []
    for y, r in enumerate(rows + [""]):
        runs, x = [], 0
        while x < len(r):
            if r[x] == ch:
                s0 = x
                while x < len(r) and r[x] == ch: x += 1
                runs.append((s0, x))
            else:
                x += 1
        nxt = {}
        for run in runs:
            nxt[run] = open_.pop(run, y)
        for (x0, x1), y0 in open_.items():
            out.append((x0, y0, x1 - x0, y - y0))
        open_ = nxt
    if transpose:
        out = [(y0, x0, h, w) for (x0, y0, w, h) in out]
    return out

def _num(v, prev):
    t = str(v)
    return t if (prev == "" or t.startswith("-") or prev[-1].isalpha()) else " " + t

def _emit(rects):
    d, cx, cy = "", None, None
    for x, y, w, h in sorted(rects, key=lambda r: (r[1], r[0])):
        if cx is None:
            mv = "M" + str(x) + _num(y, "M" + str(x))
        else:
            ab = "M" + str(x) + _num(y, "M" + str(x))
            rel = "m" + str(x - cx) + _num(y - cy, "m" + str(x - cx))
            mv = rel if len(rel) < len(ab) else ab
        close = min("h" + str(-w), "H" + str(x), key=len)
        d += mv + "h" + str(w) + "v" + str(h) + close
        cx, cy = x, y + h
    return d

def path(rows, ch="#"):
    want = {(x, y) for y, r in enumerate(rows) for x, c in enumerate(r) if c == ch}
    best = None
    for t in (False, True):
        rects = _rects(rows, ch, t)
        got = {(x0 + i, y0 + j) for x0, y0, w, h in rects for i in range(w) for j in range(h)}
        assert got == want, "rect cover mismatch"
        d = _emit(rects)
        if best is None or len(d) < len(best): best = d
    return best

def _runs(rows, ch, vertical):
    """Pixel set of `ch` as 1-px stroke runs along rows (or columns); shorter than rects for scattered pixels."""
    if vertical:
        rows = ["".join(r[x] for r in rows) for x in range(len(rows[0]))]
    d, cur = "", None
    for y, r in enumerate(rows):
        x = 0
        while x < len(r):
            if r[x] != ch:
                x += 1
                continue
            x0 = x
            while x < len(r) and r[x] == ch: x += 1
            X, Y = (y, x0) if vertical else (x0, y)
            mv = "M" + str(X) + _num(Y, "M" + str(X))
            if cur:
                rel = "m" + str(X - cur[0]) + _num(Y - cur[1], "m" + str(X - cur[0]))
                if len(rel) < len(mv): mv = rel
            d += mv + ("v" if vertical else "h") + str(x - x0)
            cur = (X, Y + x - x0) if vertical else (X + x - x0, Y)
    return d

def doc(rows, w, h, layers):
    """Shortest SVG for `layers` ({char: colour or None for black}): filled rects, or 1-px strokes on a
    viewBox shifted half a pixel so each stroke covers exactly one pixel row (or column)."""
    head = "<svg xmlns='http://www.w3.org/2000/svg' viewBox='{}' shape-rendering='crispEdges'>"
    present = [(ch, c) for ch, c in layers.items() if any(ch in r for r in rows)]
    fill = "".join(f"<path{'' if c is None else f' fill={chr(39)}{c}{chr(39)}'} d='{path(rows, ch)}'/>" for ch, c in present)
    out = [head.format(f"0 0 {w} {h}") + fill]
    for vertical, vb in ((False, f"0 -.5 {w} {h}"), (True, f"-.5 0 {w} {h}")):
        out.append(head.format(vb) + "".join(f"<path stroke='{c or '#000'}' d='{_runs(rows, ch, vertical)}'/>" for ch, c in present))
    return min(out, key=lambda s: len(uri(s))) + "</svg>"

def svg(art):
    rows, w, h = grid(art)
    return doc(rows, w, h, {"#": None}), w, h

def uri(s):
    # Only "#" and "%" must be escaped; "<" and ">" stay raw (accepted by Chromium and the gallery validator).
    return "data:image/svg+xml," + urllib.parse.quote(s, safe=" =:/'(),<>")

def webp(rows, w, h, layers):
    """Lossless WebP data URI for `layers` ({char: colour or None for black}); other characters are transparent.
    About half the size of the SVG for these sprites. The CSS must render it with image-rendering: pixelated
    (set on :root), which in Chromium matches the SVG's crispEdges pixel for pixel."""
    import base64, io
    from PIL import Image
    px = {ch: (0, 0, 0, 255) if c is None else tuple(int(_rgba(c)[i:i + 2], 16) for i in (1, 3, 5, 7)) for ch, c in layers.items()}
    im = Image.new("RGBA", (w, h))
    im.putdata([px.get(ch, (0, 0, 0, 0)) for r in rows for ch in r])
    b = io.BytesIO()
    im.save(b, "WEBP", lossless=True, quality=100, method=6, exact=True)
    return "data:image/webp;base64," + base64.b64encode(b.getvalue()).decode()

if __name__ == "__main__":
    out = {}
    for k, art in S.items():
        s, w, h = svg(art)
        out[k] = {"uri": uri(s), "w": w, "h": h}
    json.dump(out, open(sys.argv[1], "w"), indent=1)
    print({k: len(v["uri"]) for k, v in out.items()}, "total", sum(len(v["uri"]) for v in out.values()))
    if len(sys.argv) > 2:
        cells = "".join(f"<figure><div style=\"width:{v['w']*8}px;height:{v['h']*8}px;background:#2f6b3a;-webkit-mask:url(&quot;{v['uri']}&quot;) 0 0/100% 100%\"></div><div style=\"width:{v['w']*1.5}px;height:{v['h']*1.5}px;background:#222;-webkit-mask:url(&quot;{v['uri']}&quot;) 0 0/100% 100%\"></div><figcaption>{k}</figcaption></figure>" for k, v in out.items())
        open(sys.argv[2], "w").write(f"<!doctype html><style>body{{display:flex;flex-wrap:wrap;gap:16px;font:12px sans-serif;background:#fdf8ec;padding:12px}}figure{{margin:0}}</style>{cells}")
