# Extra pixel art for the full theme. Runs inside build.py with multi(), svg(), uri() in scope.
WORKING2 = """
..#..#..#...
...#..#..#..
..#..#..#...
............
############
############
.##########.
..########..
....####....
...######...
"""
# Bulldog clip that holds the current order on the pass.
CLIP = """
...kkkkkkkk...
..kssssssssk..
..kswwwwwwsk..
.kkkkkkkkkkkk.
kssssssssssssk
.kkkkkkkkkkkk.
"""
# Noren panel: indigo cloth, white wave crest, split at the right.
NOREN = """
nnnnnnnnnnnn.
nnnnnnnnnnnn.
nnnnwwwwnnnn.
nnnwnnnnwnnn.
nnwnnwwnnwnn.
nnnnwnnwnnnn.
nnnnnnnnnnnn.
nnnnnnnnnnnn.
"""
TOKENS = {
    "working2": 'url("' + uri(svg(WORKING2)[0]) + '")',
    "clip_light": multi(CLIP, {"k": "#5d4636", "s": "#9a7a5c", "w": "#d9c3a3"}),
    "clip_dark": multi(CLIP, {"k": "#0e0d12", "s": "#8b7a68", "w": "#cdb99f"}),
    "noren_light": multi(NOREN, {"n": "#2f3e6e", "w": "#f4ead6"}),
    "noren_dark": multi(NOREN, {"n": "#8a3426", "w": "#f2dcc0"}),
}
