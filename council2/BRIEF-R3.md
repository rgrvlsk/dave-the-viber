# Council brief: "Pixel Sushi Counter v2 — the order rail" (round 3 of 3, final)

Read-only review. Do not edit any file. Do not start subagents or other agents. Do not change the app theme.
Context, constraints, criteria and return format: council2/BRIEF-R1.md. Round 2: council2/BRIEF-R2.md.
This final round reviews the changes since round 2 and any finding still open. Give the six scores + overall /10,
then only findings that remain, each with severity and a concrete fix. Under 600 words.

## Round-2 results
Astra Medium 8.4 ("no broader redesign needed"), Fable Low 7.7.

## Changes since round 2 (with evidence)
1. Noren no longer covers text: the chat header now reserves the curtain's 36 px (margin-bottom), so the
   conversation scroller starts at 88 px instead of 52 px; nothing scrolls under the curtain and no glyph shows in
   the slits. r3-app-light.png, r3-app-dark-settled.png.
2. Spike: when Settled is open, the header sprite switches to an "open" spike without a base whose rod runs on
   down into the slips (x-aligned); the wooden base sits under the last slip; the separate list tip was removed.
   Hole reduced to 5 px under the rod. Slips have equal widths again (uneven edge comes only from the tilt), so the
   time column is aligned. r3-settled-dark.png (real), r3-spike-1-and-3.png (cloned real DOM: 1 slip and 3 slips;
   that capture predates the open-spike sprite: it shows the old separate tip, now removed).
3. Mode consistency: a boot stylesheet sets `body{color:#262626}` in OS light mode; the theme now sets
   `body{color:var(--contrast-foreground)}`, so the Automations and other inheriting icons are cream in both modes.
   The PR icon on tickets is pinned to --sk-done on the svg itself: rgb(43,98,54) on #fbf3e2 (~6.6:1) in both modes.
   The composer paperclip uses the notes ink. Icon scan (all visible enabled svg.lucide, opacity-composited, against
   their opaque background): 0 under 3:1. Text scan OS light: 0 under 4.5 except two disabled buttons.
4. Lamp: amber rgb(255 150 60 / .55) pool, smaller ellipse, background-blend-mode: screen.
5. Koi has its own wall-coloured lane above the plank; the sidebar footer is plank + solid wood; the composer
   plank continues as solid wood to the window edge.
6. Reduced-motion override now matches the press selector; no-op clip-path removed; title rule 2 px lower;
   settled project marks at opacity .85.
7. Hover in OS dark mode: r3-hover-dark.png (Settle ✓ on line 3; status stamp stays on line 2).

## Measured (real app, both OS modes)
- full: 135 rules written = 135 parsed, 0 invalid; lite: 69 = 69. Sizes: full 46,533; lite 19,963 (limit 20,000).
- Rows: title 22, project/status 50–52, branch 69–70; hover buttons at 69, labels at 48, no overlap.
- Contrast on tickets: title 7.0, project/branch 6.7, stamp 5.6, sprite 6.6.

## Known limits kept on purpose
- The paper token block appears in core (tickets) and extras (order slip, pad) so lite stays self-contained.
- The base marks the last loaded slip ("Show 25 more" follows), which is the bottom of the visible stack.
- Layout hooks depend on the row's child order (ponytail note at src2/core.css:141).

Files: council2/r3-*.png, council2/full.css, council2/lite.css, src2/*.css (folder:
/private/tmp/claude-501/-Users-roger--t3-scratch-2026-11-16-crea-un-tema-per-a-365d7a95/a839c0bb-e96e-4e10-8b9f-90dd03059585/scratchpad/).
