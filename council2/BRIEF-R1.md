# Council brief: "Pixel Sushi Counter v2 — the order rail" (round 1 of 3)

Read-only review. Do not edit any file. Do not start subagents or other agents. Do not change the app theme.

## The owner's request (verbatim, Catalan)
"Vull que utilitzis CSS avançat per canviar profundament l'aspecte. Els ítems laterals haurien realment de semblar
comandes. No hi ha dark o light. Vull fins al nivell de tenir pinces per agafar les comandes. I settled és una punta
amb comandes acabades. Canvia angles, tipografies, fes servir molta creativitat per obtenir una interfície completament
nova que recordi a Dave the Diver, apartat sushi, inclús."
(= deep restyle with advanced CSS; sidebar rows must really look like kitchen orders; one look, no light/dark split;
pegs/clips holding the orders; Settled = a spike with finished orders; change angles and typography; very creative,
fully new UI reminiscent of the sushi-bar part of Dave the Diver — original art only, no copied assets.)

## What was built
- Sidebar = tiled blue kitchen wall at night with a warm lamp glow. Each thread = cream order ticket hanging from a
  wooden clothes-peg on its own steel rail, hand-hung at small angles (-0.7..0.5deg), straightens on hover. Pinned = red
  peg, current = brass peg + akane double frame. Title in a condensed face, table (project) in mono capitals, notes
  (branch) in mono; a printer's dashed rule under the title; torn bottom edge.
- Status = rubber stamp (pixel sprite + uppercase word, -2deg).
- Shelves: WORKING header with a steaming bowl; SETTLED header with a pixel spike holding tickets; expanded settled
  rows are old-paper slips pierced by a steel rod (hole sprite), fanned at ±1deg, with a tip and a wooden base (full).
- One look in both modes: the theme forces the app's light-dark() polyfill switch (--lightningcss-light/dark) to the
  night palette, overrides --contrast-* tokens to mix toward white on night surfaces (toward black on paper), and sets
  identical colour roles for both variants.
- Chat (full only): night dining room with seigaiha waves; indigo noren under the header; user message = paper order
  slip "ORDER · 注文"; composer = cream order pad with perforated top; code = black lacquer tray; chunky 8-bit popups;
  chopstick scrollbars; a pixel fish swims along the sidebar footer.

## Files (folder: /private/tmp/claude-501/-Users-roger--t3-scratch-2026-11-16-crea-un-tema-per-a-365d7a95/a839c0bb-e96e-4e10-8b9f-90dd03059585/scratchpad/)
- council2/r1-sidebar-top-light-hover.png — real app, OS light mode, pointer over "X skins post relay" (buttons on line 3).
- council2/r1-sidebar-settled-dark.png — real app, OS dark mode, Settled shelf expanded (the spike).
- council2/r1-app-dark.png, council2/r1-app-light-hover.png — the full window in each OS mode (they should look the same).
- council2/full.css (41,220 chars), council2/lite.css (19,994 chars, minified; for t3themes.com, sidebar only).
- Readable sources: src2/core.css, src2/extras.css, src2/sprites2.py, src2/colors.json.
- fx/app.css — the app's own CSS (540 KB; grep it, do not read it whole).
Screenshots are 2x; the app's own "Permissions changed" toast and the right panel are not part of the theme.

## Hard constraints (blocking if violated)
1. Row layout: line 1 title alone; line 2 project + status (always line 2); line 3 branch + model. No wrapping, no
   content moving between lines. Hover buttons must not cover the status.
2. Text >= 4.5:1, icons/bars >= 3:1 at the owner's Appearance contrast 165. Status distinguishable without colour.
   prefers-reduced-motion respected; motion gentle. Keyboard focus visible.
3. CSS: no @import, image-set(), src(); url() only data: or #id; images ~30 KB total; no external fonts; no nested :has().
4. Selectors: theme-guide stable selectors plus row hooks ([data-thread-item] > [data-testid="sidebar-row-card"],
   .group\/sidebar-status-slot, status classes, lucide icon classes, aria-labels, [aria-current]) and, new in v2,
   data-testid hooks of the shelves (sidebar-settled-shelf-toggle, sidebar-working-shelf-toggle, sidebar-row-slim,
   sidebar-pinned-divider, sidebar-settled-placeholder) and data-sidebar-parent="shelf:settled". Judge if that is acceptable.

## Measured evidence (real app, contrast 165, both OS modes)
- 123 rules (full) / 65 (lite), all pass CSSStyleSheet.insertRule; t3skins validator ok for both editions.
- Rows: title top 18 px, project/status 46, branch 66 (±1 px from tilt); hover: buttons at 65, label at 44, no overlap.
- Min contrast on tickets: title 7.0, project/branch 6.7, stamp label 5.6, sprite 6.6. Whole-page scan in OS light mode:
  no text under 4.5 except emoji glyphs and diff "−" at 4.45.

## Criteria — score each 1–10, then an overall /10
1. Beautiful  2. Relaxing and cosy  3. Legible  4. Coherent with a sushi restaurant, pixel art and the Dave-the-Diver
sushi-bar mood  5. Faithful to the owner's request (orders, pegs, spike, angles, typography, one look)  6. Valid,
robust CSS (constraints above).

## Return format (under 800 words)
- Scores: six criteria + overall /10.
- Findings: numbered, each with severity (blocking / should-fix / nit), evidence (file:line or what you see in which
  PNG), and a concrete fix. Include every material finding. What would move your overall score above 9?
- Stop when you have looked at the four PNGs and read src2/core.css and src2/extras.css.
