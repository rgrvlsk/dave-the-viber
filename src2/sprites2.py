# v2 pixel art. Runs inside build2.py with multi() and png() in scope.
# The art lives in src2/sprites/<name>.png (1 px per pixel); each palette maps the PNG's colours to the token's colours.
WOOD = "#d8a15f"; WOOD_D = "#a8703a"; OUT = "#3a2414"
PEG_P = {"o": OUT, "w": WOOD, "d": WOOD_D, "m": "#d3dae0", "s": "#6f7b86"}
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
TOKENS = {
    "atlas": multi(ATLAS, {"#": None}),
    "peg_h": multi(rot90(PEG), PEG_P),
    "peg_shade": multi(rot90(PEG), dict.fromkeys(PEG_P, "#060e1a73")),
    "bubble": multi(png("bubble", BUBBLE_P), BUBBLE_P),
    "counter": multi(png("counter", COUNTER_P), COUNTER_P),
    "peg": multi(PEG, PEG_P),
    "peg_red": multi(PEG, {"o": "#3a1410", "w": "#d4533a", "d": "#93301f", "m": "#d3dae0", "s": "#6f7b86"}),
    "peg_gold": multi(PEG, {"o": "#3a2a0a", "w": "#f2c25c", "d": "#b9862a", "m": "#eef2f5", "s": "#6f7b86"}),
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
    "weed_b": multi(png("weed_b", WEED_P), WEED_P),
    "coral": multi(png("coral", CORAL_P), CORAL_P),
    "brain": multi(png("brain", BRAIN_P), BRAIN_P),
    "sand": multi(png("sand", SAND_P), SAND_P),
    "bubbles": multi(png("bubbles", BUB_P), BUB_P),
    "stool": multi(png("stool", STOOL_P), STOOL_P),
    "dave": multi(png("dave", DAVE_P), DAVE_P),
}
