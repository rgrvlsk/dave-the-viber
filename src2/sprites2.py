# v2 pixel art. Runs inside build2.py with multi() and png() in scope.
# The art lives in src2/sprites/<name>.png (1 px per pixel); each palette maps the PNG's colours to the token's colours.
WOOD = "#d8a15f"; WOOD_D = "#a8703a"; OUT = "#3a2414"
PEG_P = {"o": OUT, "w": WOOD, "d": WOOD_D, "m": "#d3dae0", "s": "#6f7b86"}
SPIKE_P = {"k": "#0e1620", "s": "#c9d1d8", "p": "#f4ead3", "q": "#c7b58e", "b": "#8a5a2b"}
BUBBLE_P = {"o": "#10202f", "w": "#fffdf6", "g": "#d9d2c3"}
COUNTER_P = {"h": "#e2a866", "w": "#b9783d", "g": "#a0662f", "s": "#5e3818"}
BASE_P = {"k": "#0e1620", "s": "#c9d1d8", "b": "#8a5a2b", "h": "#b07a40"}
TIP_P = {"k": "#0e1620", "s": "#dfe5ea", "c": "#7d8994"}
TILE_P = {"g": "#3a5a7e", "h": "#2b4d74", "t": "#1d3a5a"}
NOREN_P = {"n": "#2a3f73", "w": "#efe2c8", "d": "#1a2b55", "r": "#8a5a2b"}
FISH_P = {"o": "#10202f", "y": "#f08a5d", "w": "#ffd2b8"}
# Footer fish tank: kelp (two sway frames), branch and brain coral, sand, rising bubbles.
WEED_P = {"d": "#245e33", "g": "#3f9a4a", "l": "#7cc96f"}
CORAL_P = {"p": "#e8607a", "h": "#ffa0ac", "s": "#a8344e"}
BRAIN_P = {"y": "#e9b44c", "l": "#ffe08f", "o": "#b8742a"}
SAND_P = {"a": "#d9b77a", "b": "#c49a5c", "c": "#a87d45"}
BUB_P = {"b": "#bff3ff", "w": "#ffffff"}
FISH = png("fish", FISH_P)
PEG = png("peg", PEG_P)
def rot90(art):
    rows = [r for r in art.strip("\n").split("\n")]
    return "\n".join("".join(rows[len(rows) - 1 - y][x] for y in range(len(rows))) for x in range(len(rows[0])))
mask = lambda name: multi(png(name), {"#": None})
TOKENS = {
    "working2": mask("working2"),
    "settle": mask("settle"),
    "discard": mask("discard"),
    "pot_a": mask("pot_a"),
    "pot_b": mask("pot_b"),
    "pot_c": mask("pot_c"),
    "peg_h": multi(rot90(PEG), PEG_P),
    "bubble": multi(png("bubble", BUBBLE_P), BUBBLE_P),
    "spike_open": multi(png("spike_open", SPIKE_P), SPIKE_P),
    "counter": multi(png("counter", COUNTER_P), COUNTER_P),
    "peg": multi(PEG, PEG_P),
    "peg_red": multi(PEG, {"o": "#3a1410", "w": "#d4533a", "d": "#93301f", "m": "#d3dae0", "s": "#6f7b86"}),
    "peg_gold": multi(PEG, {"o": "#3a2a0a", "w": "#f2c25c", "d": "#b9862a", "m": "#eef2f5", "s": "#6f7b86"}),
    "spike": multi(png("spike", SPIKE_P), SPIKE_P),
    "base": multi(png("base", BASE_P), BASE_P),
    "tip": multi(png("tip", TIP_P), TIP_P),
    "tile": multi(png("tile", TILE_P), TILE_P),
    "noren": multi(png("noren", NOREN_P), NOREN_P),
    "fish": multi(FISH, FISH_P),
    "fish_l": multi("\n".join(r[::-1] for r in FISH.split("\n")), FISH_P),
    "weed_a": multi(png("weed_a", WEED_P), WEED_P),
    "weed_b": multi(png("weed_b", WEED_P), WEED_P),
    "coral": multi(png("coral", CORAL_P), CORAL_P),
    "brain": multi(png("brain", BRAIN_P), BRAIN_P),
    "sand": multi(png("sand", SAND_P), SAND_P),
    "bubbles": multi(png("bubbles", BUB_P), BUB_P),
}
