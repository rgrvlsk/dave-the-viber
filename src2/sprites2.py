# v2 pixel art. Runs inside build2.py with multi() and png() in scope.
# The art lives in src2/sprites/<name>.png (1 px per pixel); each palette maps the PNG's colours to the token's colours.
WOOD = "#d8a15f"; WOOD_D = "#a8703a"; OUT = "#3a2414"
PEG_P = {"o": OUT, "w": WOOD, "d": WOOD_D, "m": "#d3dae0", "s": "#6f7b86"}
CLIP_P = {"o": "#3a2408", "h": "#fbe7a6", "w": "#d9a84a", "d": "#8f5f1e", "s": "#060e1a73"}
STEEL_P = {"o": "#0e1620", "h": "#eef3f6", "m": "#a9b4bd", "d": "#5d6872", "s": "#060e1a73"}
BUBBLE_P = {"o": "#10202f", "w": "#fffdf6", "g": "#d9d2c3"}
COUNTER_P = {"h": "#e2a866", "w": "#b9783d", "g": "#a0662f", "s": "#5e3818"}
BASE_P = {"k": "#0e1620", "s": "#c9d1d8", "b": "#8a5a2b", "h": "#b07a40"}
TIP_P = {"k": "#0e1620", "s": "#dfe5ea", "c": "#7d8994"}
# Kitchen wall: glazed tiles (2x2 per sprite), dark grout, lit top-left bevel, glints, one chipped corner.
WALL_P = {"g": "#13253b", "h": "#2b4d74", "t": "#1d3a5a", "u": "#1a3452", "s": "#3a5a7e"}
# Header beam: dark wood, dark enough that muted text on its lightest streak stays above 4.5:1.
BEAM_P = {"h": "#6e4630", "w": "#4a2f1e", "d": "#3e2718", "k": "#2e1d12"}
# Dining-room wallpaper: seigaiha waves. The PNG marks outer rings white, inner rings grey;
# the token paints both in faint white, so the pattern stays low-contrast behind text on any night surface.
SEIG_P = {"a": "#ffffff", "b": "#c0c0c0"}
# Night window over the wall (128x50, shown 2x): navy sky, clouds, stars, moon and reflection, moonlit ridges, shore
# lights, sea, a cherry branch, a wood sill.
NIGHT_P = {"a": "#18243c", "b": "#242448", "c": "#303c60", "s": "#e4d8cc", "g": "#f0cc90", "m": "#e4b460", "f": "#1f2a48",
           "n": "#141a2c", "w": "#3a4870", "p": "#e4106c", "q": "#c8346e", "r": "#483024", "h": "#6e4630", "k": "#2e1d12"}
NOREN_P = {"n": "#2a3f73", "w": "#efe2c8", "d": "#1a2b55", "r": "#8a5a2b"}
DRINKS_P = {"c": "#ffd0e6", "r": "#c83482", "g": "#f0cc90"}
SPECIALS_P = {"c": "#d2faff", "r": "#28aac8", "g": "#f0cc90"}
FISH_P = {"o": "#10202f", "y": "#f08a5d", "w": "#ffd2b8"}
# Footer fish tank: kelp (two sway frames), branch and brain coral, sand, rising bubbles.
WEED_P = {"d": "#245e33", "g": "#3f9a4a", "l": "#7cc96f"}
CORAL_P = {"p": "#e8607a", "h": "#ffa0ac", "s": "#a8344e"}
BRAIN_P = {"y": "#e9b44c", "l": "#ffe08f", "o": "#b8742a"}
SAND_P = {"a": "#d9b77a", "b": "#c49a5c", "c": "#a87d45"}
BUB_P = {"b": "#bff3ff", "w": "#ffffff"}
# The restaurant bar under the chat: wooden stools with a back, and newly drawn fan-art of Dave in his sushi-bar
# outfit (straw hat, pale blue shirt, goatee) behind a laptop with a lit fish. Art is 56x60, displayed at 2x.
STOOL_P = {"k": "#3a2414", "w": "#c58848", "h": "#e2a866", "d": "#8a5a2b"}
DAVE_P = {"a": "#29282f", "b": "#2e211c", "c": "#4a3d38", "d": "#546973", "e": "#554436", "f": "#825965",
          "g": "#9cbbc2", "h": "#a4a5ab", "i": "#acc9d1", "j": "#b0b6c2", "k": "#b59065", "l": "#baf5f7",
          "m": "#e3aa6b", "n": "#f2ebd3", "o": "#fadbab", "p": "#fdc38d", "q": "#fdc994", "r": "#dfa76a",
          "s": "#d8a267", "t": "#cf9c64", "u": "#b6bcc6", "v": "#ebebeb", "w": "#29282f02"}
# Local edition only: the kitchen reacts while agents work (rules in /*bg*/ spans of extras.css).
# Chochin over Dave (14x18 in a 22x26 canvas, shown 2x); lit, it wears a dithered halo (h, i). Unlit: the same
# lantern in dark reds, no halo.
LANTERN_P = {"k": "#2e1d12", "o": "#a8283e", "r": "#e4506a", "R": "#ff8a6a", "Y": "#ffc98a", "W": "#fff0c8", "y": "#e9b44c",
             "h": "#ffc87846", "i": "#ffc87826"}
LANTERN_OFF_P = {"k": "#2e1d12", "o": "#2a0e14", "r": "#4e1626", "R": "#62202e", "Y": "#6e2834", "W": "#7a2e38", "y": "#5e3c14"}
# Its light: a stepped cone in three dithered bands of cream (60x64, 2x) and a glint on the counter's lip (24x3, 2x).
CONE_P = {"a": "#ffdc9622", "b": "#ffdc9614", "c": "#ffdc960a"}
GLINT_P = {"a": "#ffd28a60", "b": "#ffe2a8b0"}
# Service bell on the counter (20x16, 2x). Lit when a thread asks for attention: brass, ding strokes and a cream
# "!" order tag (t, p, X, w), so the state reads without colour. At rest the tag and strokes are gone.
BELL_P = {"k": "#3a2408", "y": "#e9b44c", "Y": "#ffe08f", "W": "#fff6d8", "d": "#8f5f1e",
          "t": "#2e1d12", "p": "#fff3dc", "X": "#7a1e2e", "w": "#fff2c0"}
BELL_OFF_P = {"k": "#3a2408", "y": "#9a7430", "Y": "#c49a46", "W": "#d8b468", "d": "#5e3c14"}
# The noren lit from behind: the slit between panels and the gaps of the fringe glow warm (overlay on noren.png).
NOREN_LIT_P = {"c": "#ffc46e", "e": "#3e5a9a", "f": "#ffb060"}
# The new-thread picture: our bar seen from the quay (320x107, 2x), pixelated from original generated art; the hut
# wears our noren and the moon the header moon's ramp (NIGHT_P g, m). harbour_dark is the hut with its lights out
# (92x46 at art 228,26). A fish crate stands on the picture's sill (22x10).
# The top of the sidebar: the restaurant across the street (Fable's 128x50 drawing after Luna's concept), cut into pieces
# so it follows the sidebar's width: sky, roof, frieze and planks tile; the neon sign and the roof plaque stop at
# 480 CSS px. The lit pieces (tile0-6, halo, fish, chochin) light while agents work. Palettes are their own.
FACADE = ("sky", "stars", "plate0", "plate", "plate0_lit", "plate_lit", "halo1", "halo2", "halo3", "halo4", "roof", "frieze", "planks", "tiles", "sushi", "sushi_lit", "halo_wide", "roof_sign", "fish_l", "fish_r", "chochin", "halo",
          "fishl_lit", "fishr_lit", "chochin_lit") + tuple(f"tile{k}" for k in range(7))
CRATE_P = {"k": "#2e1d12", "d": "#7a5030", "b": "#7f8ea0", "w": "#b07a4a", "s": "#cfd6dc"}
# An unsent draft is a page still on the order pad, with its pencil laid on it (30x6, 2x): eraser, ferrule, gold
# paint, sharpened wood, graphite tip pointing right, and its shade on the paper (s), 1 px right and down.
PENCIL_P = {"k": "#3a2414", "g": "#3a3b44", "w": "#f0cfa0", "v": "#c99a64", "Y": "#ffe08f", "y": "#f2c25c", "d": "#b9862a",
            "m": "#dfe5ea", "n": "#a9b4bd", "o": "#5d6872", "p": "#ee8f9c", "P": "#c05a6c", "s": "#060e1a73"}
def own(name):
    """Palette of imported art: its own colours, each a letter or digit, in colour order."""
    from PIL import Image
    import os, sprites, string
    cols = sorted(c for _, c in Image.open(os.path.join(sprites.SRC, name + ".png")).convert("RGBA").getcolors(4096) if c[3])
    assert len(cols) <= 62, f"{name}.png: {len(cols)} colours"
    return {ch: "#%02x%02x%02x%02x" % c for ch, c in zip(string.ascii_letters + string.digits, cols)}
FISH = png("fish", FISH_P)
PEG = png("peg", PEG_P)
def rot90(art):
    rows = [r for r in art.strip("\n").split("\n")]
    return "\n".join("".join(rows[len(rows) - 1 - y][x] for y in range(len(rows))) for x in range(len(rows[0])))
mask = lambda name: multi(png(name), {"#": None})
# One mask atlas for the status, key, saucepan and bubble icons (12 px wide, 4 empty rows between). Masks centre an icon in
# their box with `calc(box/2 - centre)`; centres: waiting 5, working 19, saucepan 34, settle 49, discard 63,
# failed 74.5, limited 86, draft 101, input 117, request 132, woke 146. Bubbles clip each background layer to an
# 18 px content box, so one slot shows. Approval stays a single image: at 1.5x its 9 rows land on a half device
# pixel, and the atlas offset cannot reproduce the old rounding for every anchor position.
ATLAS = "\n".join(("." * 12 + "\n") * 4 * (i > 0) + png(n).strip("\n") for i, n in enumerate(
    ("waiting", "working", "saucepan", "settle", "discard", "failed", "limited", "draft", "input", "request", "woke")))
# Sprites the local edition takes from the theme image, in atlas order (see `pack` and `relayer` in tools/build2.py).
# "single": one sprite; ("single", rows): with that many more empty rows above it. "strip": a tile for `repeat-x`.
# ("block", rows): a tile for `repeat`, tiled that many rows down. "fill" is cut with a mask-box-image, where a layer
# cannot do it: a mask as large as its box.
# Drinks is first: at the image's origin its offsets stay positive, and Chromium snaps a positive offset to a device
# pixel as it does for a single image (at 1x the sign is centred to a half pixel).
# Night is not here: local's sidebar top is the beam and the restaurant's sign (extras.css), not the night view.
# The bracket sits at the bottom of a row (95 px today, shown at 1x), so it needs more empty rows above.
# Not here, each would change pixels: the status atlas and approval (1.5x in the bubble, half device pixels), wall and
# seigaiha (`repeat` in boxes as tall as the window), bubbles (`repeat-y`).
ATLAS_PLAN = {"drinks": "single", "noren": "strip", "counter": "strip", "sand": "strip", "stool": "strip", "tear": "strip",
              "beam": ("block", 52), "specials": "single", "dave": "single", "peg_h": "single", "peg_shade": "single",
              "bubble": "single", "fish": "single", "fish_l": "single", "clip": "single", "base": "single",
              "weed_s": "single", "weed_a": "single", "coral": "single", "brain": "single", "chef": "fill",
              "bracket": ("single", 120), "harbour": "single", "harbour_dark": "single"}
TOKENS = {
    "atlas": multi(ATLAS, {"#": None}),
    "peg_h": multi(rot90(PEG), PEG_P),
    "peg_shade": multi(rot90(PEG), dict.fromkeys(PEG_P, "#060e1a73")),
    "bubble": multi(png("bubble", BUBBLE_P), BUBBLE_P),
    "counter": multi(png("counter", COUNTER_P), COUNTER_P),
    "peg": multi(PEG, PEG_P),
    "peg_red": multi(PEG, {"o": "#3a1410", "w": "#d4533a", "d": "#93301f", "m": "#d3dae0", "s": "#6f7b86"}),
    "peg_gold": multi(PEG, {"o": "#3a2a0a", "w": "#f2c25c", "d": "#b9862a", "m": "#eef2f5", "s": "#6f7b86"}),
    # Working shelf: a brass clip and a steel rail bracket, each with its shade (s) baked in.
    "clip": multi(png("clip", CLIP_P), CLIP_P),
    "bracket": multi(png("bracket", STEEL_P), STEEL_P),
    "base": multi(png("base", BASE_P), BASE_P),
    "tip": multi(png("tip", TIP_P), TIP_P),
    "wall": multi(png("wall", WALL_P), WALL_P),
    "beam": multi(png("beam", BEAM_P), BEAM_P),
    "night": multi(png("night", NIGHT_P), NIGHT_P),
    "seigaiha": multi(png("seigaiha", SEIG_P), {"a": "#ffffff0c", "b": "#ffffff07"}),
    "noren": multi(png("noren", NOREN_P), NOREN_P),
    "drinks": multi(png("drinks", DRINKS_P), DRINKS_P),
    "specials": multi(png("specials", SPECIALS_P), SPECIALS_P),
    "chef": mask("chef"),
    "fish": multi(FISH, FISH_P),
    "fish_l": multi("\n".join(r[::-1] for r in FISH.split("\n")), FISH_P),
    "weed_a": multi(png("weed_a", WEED_P), WEED_P),
    # The kelp's stem: weed_a without its top 7 rows, which sway on their own layer (weed_b = those rows 2 px left).
    "weed_s": multi("\n".join(png("weed_a", WEED_P).split("\n")[7:]), WEED_P),
    "coral": multi(png("coral", CORAL_P), CORAL_P),
    "brain": multi(png("brain", BRAIN_P), BRAIN_P),
    "sand": multi(png("sand", SAND_P), SAND_P),
    "bubbles": multi(png("bubbles", BUB_P), BUB_P),
    "stool": multi(png("stool", STOOL_P), STOOL_P),
    "dave": multi(png("dave", DAVE_P), DAVE_P),
    "lantern": multi(png("lantern", LANTERN_P), LANTERN_P),
    "lantern_off": multi(png("lantern", LANTERN_P), LANTERN_OFF_P),
    "cone": multi(png("cone", CONE_P), CONE_P),
    "glint": multi(png("glint", GLINT_P), GLINT_P),
    "bell": multi(png("bell", BELL_P), BELL_P),
    "bell_off": multi(png("bell", BELL_P), BELL_OFF_P),
    "noren_lit": multi(png("noren_lit", NOREN_LIT_P), NOREN_LIT_P),
    "crate": multi(png("crate", CRATE_P), CRATE_P),
    "pencil": multi(png("pencil", PENCIL_P), PENCIL_P),
    "harbour": multi(png("harbour", own("harbour")), own("harbour")),
    "harbour_dark": multi(png("harbour_dark", own("harbour_dark")), own("harbour_dark")),
}
TOKENS.update({"facade_" + n: multi(png("facade_" + n, own("facade_" + n)), own("facade_" + n)) for n in FACADE})
# Close-up busts from Roger's supplied pixel grids. Crop the lower torso to fit 100 CSS px at 2x.
for name in ("cobranch", "brancho"):
    palette = own(name)
    TOKENS[name] = multi("\n".join(png(name, palette).splitlines()[:48]), palette)
