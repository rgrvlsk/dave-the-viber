"""Pixel-sampled contrast: for each CSS-px box, background = median of the box's border ring,
foreground = the box pixel with the highest contrast to it. Sees gradients, blends and filters.
Usage: python3 -I pixcheck.py shot.png boxes.json  (boxes: [{"n":name,"r":[x,y,w,h]}])"""
import json, sys, statistics
from PIL import Image
im = Image.open(sys.argv[1]).convert("RGB"); s = im.size[0] / 1280
def lum(c):
    f = lambda v: (v / 255) / 12.92 if v / 255 <= 0.03928 else ((v / 255 + 0.055) / 1.055) ** 2.4
    return 0.2126 * f(c[0]) + 0.7152 * f(c[1]) + 0.0722 * f(c[2])
def ratio(a, b):
    x, y = lum(a), lum(b); return (max(x, y) + 0.05) / (min(x, y) + 0.05)
for b in json.load(open(sys.argv[2])):
    x, y, w, h = [round(v * s) for v in b["r"]]
    ring = [im.getpixel((i, j)) for i in range(x - 2, x + w + 2) for j in (y - 2, y + h + 1)] + \
           [im.getpixel((i, j)) for j in range(y, y + h) for i in (x - 2, x + w + 1)]
    bg = tuple(statistics.median(p[k] for p in ring) for k in range(3))
    px = [im.getpixel((i, j)) for i in range(x, x + w) for j in range(y, y + h)]
    fg = max(px, key=lambda p: ratio(p, bg))
    print(f"{ratio(fg, bg):5.2f}  {b['n'][:40]}  bg={tuple(int(v) for v in bg)} fg={fg}")
