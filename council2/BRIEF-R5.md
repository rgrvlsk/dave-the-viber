# Council brief: "Pixel Sushi Counter v2" (round 5, verification of the round-4 findings)

Read-only review. Do not edit any file. Do not start subagents or other agents. Do not change the app theme.
Context, hard constraints, criteria and return format: council2/BRIEF-R1.md; round 4: council2/BRIEF-R4.md.
Six scores + overall /10; only findings that remain, with severity and a concrete fix. Under 550 words.
Round 4: Astra 8.9, Fable 8.8. Both asked for: per-kind stamp hiding, evidence with several calling kinds, the
collapsed sidebar, scrolling, budget, validator runs.

## Changes since round 4 (with evidence)
1. Stamp hiding is per kind now (three selectors matching the three per-kind anchors). All thread rows, pinned and
   unpinned, are children of one <ul> (verified in the DOM: pinned header, 2 pinned rows, pinned divider, 93 rows,
   Working and Settled shelves), so :nth-child(1 of …) picks one page-wide winner per kind.
   r5-multi-bubbles.png and r5-sign-and-bubbles.png: Input, Approval and Request at once (two "Done" chips relabelled
   in the live DOM for the test); a second Request keeps its stamp (bottom ticket).
2. Collapsed sidebar: the app slides the rows off-screen without clipping, so anchors-visible keeps the bubbles; the
   theme now hides the hosts with html/body/:root:has([data-slot=sidebar][data-state=collapsed]). Verified:
   r5-sidebar-collapsed.png (0 bubble pixels at the left edge), and they return when expanded.
3. Scrolling: a ticket scrolled out of the list hides its bubble (anchors-visible), r5-scrolled.png; bubble tops are
   clamped with max(96px, …) so a half-scrolled ticket cannot lift its bubble onto the header or the noren.
4. Shop sign: owner's request — the noren crest became a hanging wooden kanban (64×64, framed wood, two cords to the
   noren rod) bigger than the curtain, over the first panel, 48 px from the left so it clears the bubble column; it
   may cover the start of the chat's first line (owner accepted). Owner then asked to drop the pixel shader on the
   sign: the mark is crisp. "No project" keeps the fish. The rod is no longer cut (the patch is gone).
5. Settled: last slip's front rod stops at its hole; stub outline softened; tilts .9/−1.1/.3. Stains opacity .12,
   still through the 2-px shader (now alpha-thresholded, so no soft fringe).
6. Lamp pool 46% × 20%, alpha .30, centre above the top. Pixel-sampled contrast (tools/pixcheck.py, border-ring
   median background vs strongest glyph pixel, so gradients count): r5-pixcheck.txt — title 7.4, Search 7.7, header
   icons ≥ 4.5, footer icons 5.2.
7. Budget and validity: full 48,881 chars (t3skins validator ok), lite 19,998 (validator ok); full 157 rules = 157
   parsed, lite 71 = 71; the build refuses unbalanced braces and nested :has().
8. Hard constraint 1, owner-approved exception: a calling ticket shows its status as the bubble beside it instead of
   a stamp on line 2; the stamp stays in the accessibility tree and the sprite shape still tells the status.

Files: council2/r5-*.png, r5-pixcheck.txt, full.css, lite.css; sources src2/core.css, src2/extras.css,
src2/sprites2.py, tools/build2.py (folder:
/private/tmp/claude-501/-Users-roger--t3-scratch-2026-11-16-crea-un-tema-per-a-365d7a95/a839c0bb-e96e-4e10-8b9f-90dd03059585/scratchpad/).
