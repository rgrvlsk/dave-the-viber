# Hillclimb: Pixel Sushi v2 — "order rail" redesign

## Goal
Deep redesign of the pixel-sushi T3 Code theme (themeId pixel-sushi) with advanced CSS:
- sidebar rows look like real kitchen order tickets hanging from clips (pinces) on a rail;
- the Settled area is a spike (punxa) with finished orders;
- one single look, not a light/dark pair ("No hi ha dark o light": same restaurant in both modes);
- new angles (slight ticket tilt), new typography (system stacks only), Dave-the-Diver-like
  sushi-bar mood (original art, no copied assets).
Keep Roger's earlier contracts: row layout (title / project+status / branch+model), contrast
165 (text >=4.5, icons >=3), status shape-distinguishable, reduced motion, visible focus,
CSS limits (<=50k, no @import/image-set/src(), url only data:/#id, no external fonts, no nested :has).

## Metric
Council score /10 from the two plan-pace sage routes (sage-claude Fable Low, sage-codex Astra Medium),
3 rounds. Measured by delegate_task with brief + PNGs + CSS. Hard checks by fx/check.js in the real app.

## Target
Both council members > 9/10 overall in the last round; check.js: 0 invalid rules, layout 3 lines,
no overlap, contrast targets met.

## Backlog (ranked)
1. Inventory real DOM for settled section/rows and sidebar group headers (theme guide + live app).
2. Unified palette (mode-independent) + rail + clips per ticket + tilt angles.
3. Settled = spike with stacked finished tickets.
4. Typography system: condensed sans headers, mono receipt body, tabular numerals.
5. Chat area: menu board header, counter, order pad composer in new style.
6. Council round 1 → fixes → round 2 → fixes → round 3.
7. Lite edition (<20k) rebuilt from the new core; t3skins validator.
8. Publish once as pixel-sushi version 2, screenshots.

## Irreversible / needs Roger
- Publishing to any gallery (never).
- Revoking pairing connections not created here.
Publishing the theme via t3_theme_set: authorized by the original request (publish once at the end).

## Limits
One preview tab at a time; council children read-only, max 2 in parallel.

## Ledger
- 16:55 | items 1-4 | v2 built: wall, rails, pegs, tilt, stamps, spike, unified look via --lightningcss-dark switch | check.js 0 invalid, 3 lines, contrast min 5.6 | decision: "No hi ha dark o light" read as one look in both modes (veto-able) | next: council R1
- 17:27 | council R1 | Fable 6/10; Astra held 40 min by pace-gate (Codex reading 3 h old, child held before its first model request so it could never refresh it) | fix: one `codex exec -m gpt-6-luna` call refreshed the reading, gate now go | next: apply R1 fixes (done in part), wait Astra
- 17:33 | Roger: option A sent to rgrstack thread; pace-gate turned OFF here (override) | next: wait Astra R1
- 17:55 | R1 fixes (Fable 6.0, Astra 7.3): spike stack, tip/base split, pegs 16x26, tilts ±1.5, warm tiles+counter, noren fish, rails darker, waves halved, diff #ff9a8a, brace guard in build (found 2 stray braces) | check: 134/134 rules, contrast min 5.6, lite 19,978 | next: council R2 running
- 18:10 | Astra R2 8.4: noren reserved (header margin 36), body boot colour override, PR + paperclip icons, settled marks .85, aligned rod, open-spike sprite; icon scan light: 0 enabled icons <3:1 | next: Fable R2
- 18:25 | Fable R2 7.7 fixes: warm amber pool (screen blend), equal slip widths, koi lane, wood to edge, PR svg pinned (6.6:1 both modes), RM selector | icon scan 0 <3:1, text scan clean | next: council R3 running
- 19:05 | Roger requests: left twine + side pegs (rows ~15px shorter), project-icon watermark stain, customer bubbles (page-level anchored hosts per status kind; scroller mask clips anything inside the sidebar), settled slip lip+seam, noren dye (pending Fable advice) | full 48,773 / lite 19,988 | Astra R3 8.9 | next: Fable noren answer, then council R4
- 19:45 | noren = fish + project crest (Fable option 1); real SVG pixel shader via data: URL filter (avg/sample/dilate/posterize/outline) on crest (3px) and stains (2px); settled z inverted (sibling-index); council R4 launched | full 49,787 / lite 19,997
- 20:05 | Fable R3 (late) 8.4: lamp contrast (pixel-sampled now: title 7.4, search 7.7, icons ≥4.5), footer svg cream (5.2), composer tray -10px, settled tilts .9/-1.1/.3; sign hangs from rod (Roger OK covering first line); build refuses nested :has; new tools/pixcheck.py
- 20:35 | R4 Astra 8.9 / Fable 8.8 fixes: per-kind stamp hiding, collapsed-sidebar hide via :root:has(data-state=collapsed), scroll clamp, last rod, stains .12 + alpha threshold, lamp 46%x20%; sign pixel shader dropped (Roger) | full 48,881 / lite 19,998, validator ok both | next: council R5
- 20:55 | Astra R5 9.1 (no findings). Roger: sidebar buttons → glazed tiles + pixel-shaded icons; logo → wooden plaque; Nightly → paper tag; monogram signs on lacquer plate; chat waves dropped for budget; breadcrumb emoji is part of the project name (not removable in CSS) | full 49,663 / lite 19,998 | next: Fable R5
- 21:10 | Fable R5 9.0 'ship it', Astra R5 9.1: sign label plate, clamp 112, ponytail trigger, lite headroom 19,833, full 49,685, validator ok | council R6 (final) launched
- 21:25 | DONE: council R6 Fable 9.1 / Astra 9.2 (both 'ship it'); published themeId pixel-sushi-rail (file written, server CSS identical, switched with t3_theme_set); live app: 163 rules, roles applied, light = dark | queued for Roger: none irreversible; optional: gallery publication (never without asking)
- 22:00 | Roger batch: tile icons crisp (8.9:1), search recessed tile, card-only hover lift, spike rod unified (k-s-k 6px, 2x sprites, pixel-aligned), settled ellipsis later, sign works for favicon <img> (cords on header::before), composer icons crisp + ink send tile, question banner on paper (shell glass vars), update tag + 8-frame spinner, simple stain shader, pegs tinted by hue-rotate (-1.2k) | republished pixel-sushi-rail: live 168 rules | full 49,837 / lite 19,872
- 22:05 | hover: no lift, only straighten (Roger) | republished, full 49,600
- 22:30 | full minified (no comments, per Roger) 45k; stain shader → blur(.75px) op .2; search results as pegged paper slips (role=option in [aria-label=Thread search results]) with ink accents | republished 46,681 / lite 19,872
- 22:45 | sign missing in desktop = No-project thread by design; now No project shows the koi on a paper label (desktop checked via Luna relay screenshot) | republished 46,996
- 23:00 | Done → 'Dish!' + steaming bowl; Working → pot with dancing lid (3 frames, 1.2s, stops under reduced motion) | republished 46,723 / lite 19,948
- 23:25 | question banner: every composer layer squared, no glass, banner frame removed (one paper sheet) — verified with a pending Haiku question | republished 46,939 | waiting: Mac mini t3code-dev discovery, Fable pot
- 23:45 | Fable cute pot (face, rocking lid, steam) | radios/checkboxes keep their shape | republished 47,178 / lite 19,941 | Mac mini: t3code-dev = dev home dir (vp run dev --home-dir /tmp/t3code-dev) + dev-replay-agent scenarios
- 23:55 | pot without face (stockpot), Dish! steam animates again | republished 47,705 / lite 19,909
- 00:00 | Mac mini (ssh rogerflix) demo job launched: Sol Medium, worktree /tmp/t3code-theme-demo, dev home /tmp/t3code-dev, theme /tmp/pixel-sushi-rail.json, output /tmp/t3code-theme-demo-out | next: fetch video+PNGs via scp, council (Fable+Astra) on them, fix defects
- 00:40 | defect council (Astra 7.5, Fable 7.0) fixes: light-mode code (invert pre), brass rims, provider marks ink (fill-black/dark:fill-white), radios paper, banner scrollbar hidden, snoozed shelf + pegged snoozed slips, details card square, read titles ink, pad icons opaque, noren offset; skipped: tooltip over bubble (owner wants it) | verified on Mac mini dev | republished 49,619 / lite 19,916
- 01:05 | Fable size pass applied (items 1,3,4,5 + minifier): full 49,619→43,379, lite 19,916→17,768, pixel diff 0, 190/190 rules | then snoozed time ink, Stop tile (unverified selector), banner perforation divider | republished 43,681 / lite 17,768
- 01:15 | handoff: work copied to ~/.t3/scratch/2026-11-16-crea-un-tema-per-a-365d7a95/pixel-sushi-rail (HANDOFF.md); new thread launched; this thread settled
- 20:15 | folder moved to ~/.t3/projects/pixel-sushi-rail (symlink at old scratch path), T3 project "Pixel Sushi Rail" created | build made deterministic (renaming had hash-random ties) | banner separator rule removed: the slot is the inline "·" of the collapsed question header, not a divider (rule drew a stub and pushed the dot down; verified live) | republished 43,441 / lite 17,757, check.js 0 invalid, contrast unchanged | Mac mini dev updated; video v2 relay (Luna Low) launched, includes Stop check
- 20:25 | Stop verified live on Mac mini dev ("Stop generation", #9c2f27, radius 0, 32x32) | video v2 recorded from this Mac through an SSH tunnel + fresh pairing (3 Luna relays failed) → demo/v2/ | light = dark confirmed | note: the header actions panel (env/Open in Zed/Select ref/Commit) is unthemed dark glass
- 20:40 | fix: project stain hit the app's "Unsent draft" marker (span[role=img], first child of line 2 when a thread has a client-side draft), so the project icon showed inline at full opacity. Stain selector now `:is(:first-child:not([role=img]), [role=img]:first-child + *)` (same 96/96 matches without a draft); draft marker → pencil stamp (sprite `draft`, approval ink, 6.58:1) | check.js 0 invalid, 194 rules | full 43,441→44,296 / lite 17,757→18,516 | republished pixel-sushi-rail (live = build)
- 20:55 | Roger: draft marker moves next to the status stamp and reads "DRAFT": joins the shared stamp rules (pencil sprite, ink, `content: "Draft" / ""`), `order: 1`; status slot and later siblings `order: 2` (no change without a draft) | check.js 0 invalid, 194 rules, 0 overlaps; DRAFT 12.57:1 | full 44,345 / lite 18,564 | republished
- 21:05 | project icon: `favicon.svg` (the theme's FISH koi, generated from src2/sprites2.py colours) set as faviconPath; projectIcon emoji 🍥 cleared (projectIcon wins over favicon in the app) | verified on the chat-header sign
- 21:40 | noren: tiles start at the left divider (`{{noren}} 0 0`, was `30px top`, which left a 26 px cut panel at the left). Source in src2/extras.css; published as a one-string patch on the live file (another thread was editing core/extras), backup final2/published-before-2026-11-16-noren.json
