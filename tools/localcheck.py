"""Check that a local-edition theme and its image come from the same build.
Usage: python3 -I tools/localcheck.py <dir with dave-the-viber.json and .webp>  (out2/local, or a T3 themes folder)"""
import hashlib, json, os, re, sys
d = sys.argv[1]
css = json.load(open(os.path.join(d, "dave-the-viber.json")))["css"]
stamp = re.search(r"/\*atlas ([0-9a-f]{12})\*/$", css)
img = hashlib.sha256(open(os.path.join(d, "dave-the-viber.webp"), "rb").read()).hexdigest()[:12]
if not stamp: sys.exit("no atlas stamp in the CSS: not a local-edition build")
if stamp[1] != img: sys.exit(f"MISMATCH: CSS expects image {stamp[1]}, the folder has {img}")
print(f"ok: CSS and image match ({img})")
