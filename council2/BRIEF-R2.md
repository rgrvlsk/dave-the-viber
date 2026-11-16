# Council brief: "Pixel Sushi Counter v2 — the order rail" (round 2 of 3)

Read-only review. Do not edit any file. Do not start subagents or other agents. Do not change the app theme.
Read council2/BRIEF-R1.md first for the owner's request, the concept, the hard constraints and the criteria. Same
criteria and return format (six criteria + overall /10, numbered findings with severity, evidence, concrete fix,
"what moves it above 9"). This round reviews the changes and the open findings only.

## Round-1 results
Fable Low 6.0, Astra Medium 7.3. Both blocked on the light-mode PNGs: they were empty captures (the preview
captured before content-visibility rows painted; not a CSS defect: the rows were measured present at the time).

## What changed since round 1
1. Evidence: new populated captures in both OS modes. council2/r2-app-light.png (light) and r2-app-dark.png (dark);
   sidebar crops r2-sidebar-light.png / r2-sidebar-dark.png. The light capture predates the noren crest change (item 6).
2. Spike (Settled): slips overlap by 7 px and stack; darker aged paper #d9c9a3 with dimmer titles; uneven widths;
   the rod is drawn in front of each slip above its hole; a pointed tip sits on the shelf placeholder above the first
   slip and the wooden base is on the last slip, so a single item never shares one pseudo-element; bigger header
   sprite with point + 3 skewered slips. council2/r2-settled-light.png.
3. Warmth: square ceramic tiles with lighter grout and highlight; stronger lamp glow (0.28); a pixel wooden counter
   under the sidebar footer and under the composer pad; the koi has its own lane above the footer icons, travels
   0→100% of the footer width, and is hidden under reduced motion.
4. Pegs 16x26 px (were 14x20) and visibly grip the paper; tilts now -1.5 / +1.1 / -0.6 deg; rails darker with a
   thinner highlight; ink tokens now scoped to the paper surfaces only (a renamed testid degrades to the default look).
5. Contrast: diff deletion foreground #ff9a8a (~7:1 on the panel); links salmon #ffb08a; the model mark on tickets is
   forced to the notes ink at opacity 1. Whole-page scan, OS light mode: no text under 4.5 except emoji and two
   disabled buttons ("Open in Kiro", "Commit & push", disabled=true, opacity 0.64; exempt under WCAG 1.4.3).
6. Noren: 36 px tall on a wooden rod, slits between panels, scalloped hem, a pixel fish crest per panel.
   Chat waves halved in contrast.
7. Keyboard: Tab from the search reaches the first ticket; it shows a 2 px dashed ink frame and its Settle button on
   line 3 at once (council2/r2-focus-light.png).
8. Robustness: I found and fixed a build defect (two stray "}" swallowed the reduced-motion block); the build now
   refuses unbalanced braces. Full: 134 rules written = 134 parsed by CSSStyleSheet; lite: 67 = 67. 0 invalid.

## Measured (real app, contrast 165, both OS modes, identical numbers)
- Rows: title 22 px, project/status 50–52, branch 69–70 (±1 px from tilt). Hover: buttons on line 3, no overlap.
- Min contrast on tickets: title 7.0, project/branch 6.7, stamp 5.6, sprite 6.6.
- Sizes: full 46,369 chars; lite 19,978 (minified). t3skins validator ok for both.

## Files
council2/r2-*.png, council2/full.css, council2/lite.css; sources src2/core.css, src2/extras.css, src2/sprites2.py,
src2/colors.json, tools/build2.py (folder: /private/tmp/claude-501/-Users-roger--t3-scratch-2026-11-16-crea-un-tema-per-a-365d7a95/a839c0bb-e96e-4e10-8b9f-90dd03059585/scratchpad/).
Stop when you have looked at the r2 PNGs and read the changed parts of src2/core.css and src2/extras.css. Under 700 words.
