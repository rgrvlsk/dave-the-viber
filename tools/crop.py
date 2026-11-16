import sys
from PIL import Image
src, dst, x0, y0, x1, y1 = sys.argv[1], sys.argv[2], *map(int, sys.argv[3:7])
im = Image.open(src); s = im.size[0] / 1280
im.crop((int(x0*s), int(y0*s), int(x1*s), int(y1*s))).save(dst)
