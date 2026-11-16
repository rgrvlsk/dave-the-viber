# Council brief: "Pixel Sushi Counter v2" (round 6, final verification)

Read-only review. Do not edit any file. Do not start subagents or other agents. Do not change the app theme.
Context, constraints, criteria, format: council2/BRIEF-R1.md. Round 5: council2/BRIEF-R5.md.
Round 5: Astra 9.1 (no findings), Fable 9.0 ("ship it"). Six scores + overall /10; remaining findings only. Under 450 words.

## Changes since round 5
1. Fable R5 #1 (two rendering languages): the crisp favicon/emoji mark on the sign now sits on a cream printed label
   with a 2-px dark frame (image-rendering: auto). Letter monograms (projects without an icon) sit on a dark lacquer
   plate with a light wood fillet: council2/r6-monogram-sign.png. "No project" keeps the fish.
2. Fable R5 #3: bubble tops clamp at the list's top edge (112 px) instead of 96 px.
3. Fable R5 #2: ponytail note now carries its trigger ("add a host if the owner reports a missed call").
4. Fable R5 #5: lite headroom 19,833 / 20,000 (minifier unquotes plain font names, shortens hex; pixelated hints
   removed where the art is a crispEdges SVG or a mask). Full 49,685 / 50,000. Validator ok for both.
5. Owner requests: sidebar controls are glazed wall tiles (square, bevelled, cream glyph through the 2-px pixel
   shader); the "T3 Code" logo is a small wooden plaque; "Nightly" is a red-ink paper tag tied to it, tilted.
   council2/r6-logo-buttons.png, r6-header-sign-logo.png, r6-app-dark.png (bubbles in that capture come from status
   labels relabelled in the live DOM for testing). Chat wave texture removed for budget.
6. Fable R5 #4 correction: header icons pixel-sampled at ≥ 4.48 (≥ 3:1 required for icons).
Measured: full 163 rules = 163 parsed, lite 70 = 70, 0 invalid; ticket contrast unchanged (title 7.0, project 6.7,
stamp 5.6, sprite 6.6).

Files: council2/r6-*.png, full.css, lite.css, src2/*.css (folder:
/private/tmp/claude-501/-Users-roger--t3-scratch-2026-11-16-crea-un-tema-per-a-365d7a95/a839c0bb-e96e-4e10-8b9f-90dd03059585/scratchpad/).
