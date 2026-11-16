# Council brief: "Pixel Sushi Counter v2" (round 4, verification after the owner's new requests)

Read-only review. Do not edit any file. Do not start subagents or other agents. Do not change the app theme.
Context, hard constraints, criteria and return format: council2/BRIEF-R1.md (six scores + overall /10, numbered
findings with severity, evidence and a concrete fix, "what moves it above 9"). Under 650 words.
Previous: R3 Astra 8.9 (open nits: spike rod segments tilt with the paper; lamp pool too wide). Fable R3 did not return.

## The owner's new requests since round 3 (all implemented)
1. "Cordill i pinces a l'esquerra": a twine runs down the left of the wall; each ticket is pegged at its top-left
   corner by a horizontal pixel peg and tilts from it. Rows are ~15 px shorter (title 12, project 40–42, branch 59–60).
2. "Comandes que reclamen atenció → una bombolla com els clients de Dave the Diver, flotant a la dreta enllà del
   separador; el popover de detall la tapa": a white rounded pixel speech bubble with a tail, holding the status sprite
   in its colour, floats past the sidebar's right edge beside the ticket; the stamp leaves that ticket. The sidebar's
   scroller has a fade mask that clips anything inside it (even position:fixed), so each bubble is a page-level
   pseudo-element (html::after, body::after, [data-workspace-area=conversation]::before/::after) placed with anchor
   positioning, one per status kind (Approval, Input, Request, Woke), anchored to the first ticket of that kind via
   :nth-child(1 of …:has()). z-index 30 < popovers 140. Limit (ponytail note): a second ticket with the same status
   keeps its stamp. The Woke stamp stays (it is the dismiss button).
3. "El color dels papers basat en una marca d'aigua amb els colors de la icona": the project icon on line 2 becomes a
   big faint stain on the paper (scale 4, opacity .17, multiply), run through a 2-px pixel shader (full).
4. "Els settled: una vora, sobretot inferior": paper edge + 3 px bottom lip + dark seam + shadow per slip; the spike
   rod stays plumb in front of each slip (only paper tilts), small hole; z-order inverted with
   z-index: calc(1000 - sibling-index()) so each slip lies over the next.
5. "Noren amb la icona del projecte pixelada, com el rètol del negoci (shader)": the fish noren is back; the
   breadcrumb's project mark hangs as the crest of the first panel (in place of its fish), filtered by a real SVG
   pixel shader passed as a data: URL filter (works in Chromium 152): box-average each 3-px cell (feConvolveMatrix),
   sample one pixel per cell (feFlood/feComposite/feTile), dilate to fill the cell, posterize to 5 levels per
   channel (feComponentTransfer discrete) and add a 1-px dark sprite outline. "No project" keeps the fish.

## Evidence (real app, contrast 165)
- r4-app-light.png (OS light), r4-app-dark.png (OS dark), r4-sidebar-bubble-light.png, r4-settled-dark.png,
  r4-shader-crest-and-stains.png (crest enlarged 3x nearest-neighbour + stains), r4-noren-crest-light.png (earlier,
  simpler shader). full: 154 rules = 154 parsed, 0 invalid; lite: 71 = 71. Sizes: full 49,787 / 50,000; lite 19,997.
- Rows: no overlap on hover; title 7.0, project/branch 6.7, stamp 5.6, sprite 6.6; worst-case stain (black at 17 %)
  keeps secondary text ≥ 5.6. Whole-page text scan OS light: only disabled buttons and the aria-hidden stain glyph.

Files: council2/r4-*.png, council2/full.css, council2/lite.css, sources src2/core.css, src2/extras.css,
src2/sprites2.py, tools/build2.py (folder:
/private/tmp/claude-501/-Users-roger--t3-scratch-2026-11-16-crea-un-tema-per-a-365d7a95/a839c0bb-e96e-4e10-8b9f-90dd03059585/scratchpad/).
