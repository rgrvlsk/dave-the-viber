# Dave the Viber — handoff (2026-11-16)

T3 Code theme by Roger's request: a night sushi bar in pixel art, Dave-the-Diver mood (original art only).
Published and active as "Dave the Viber", **themeId `dave-the-viber`** (file `~/.t3/userdata/themes/dave-the-viber.json`).
Renamed from Pixel Sushi Rail (themeId, folder and repo `pixel-sushi-rail`) on 2026-11-17.
Fallbacks kept untouched: `pixel-sushi` (v1) and Roger's `status-edge` ("Minimalist color edges").
Folder: `/Users/roger/.t3/projects/dave-the-viber/` (call it `$D`). T3 Code project "Dave the Viber" (id `mcp:58b738ca-6192-4af5-a039-e107ef713625`) with scripts "Build + validate" and "Static server :8765". The old scratch path and `~/.t3/projects/pixel-sushi-rail` are symlinks to this folder.

## State
- Skin vs no skin, resource cost (2026-11-18, Roger: "same stress test 5 times with and without skin, all consumption
  history"). Own harness in `perf/` (see `perf/REPORT.md`; drives `/Users/roger/t3code/.css-perf`'s Electron 44.10.1
  read-only; profile `perf/profile` is paired with :7508 and git-ignored). 10 fresh runs ABBA, d292df3 full vs empty sheet:
  CPU 50.8 vs 30.3 s per test (+68%), energy impact 1.83x, idle visible 50% vs 21% of a core (60 vs 16 fps).
  The idle cost is all from the 5 infinite animations (float, sway, swim, rise, screen): without their @keyframes idle =
  no skin. Memory: status changes add +300-450 MB that levels off (no leak) but stays while the animations run;
  without them it is released in ~12 s. Raw samples: `perf/data/*/samples.jsonl`.
- Hover while scrolling (2026-11-18, Roger: "remove the list's hover animations during scroll?"). Chromium updates :hover
  every frame under a still pointer: 150-500 row transitions per scroll phase. CSS has no scrolling state. 15 runs ABC/CBA:
  80 ms hover-in delay = no gain (-3%); no row transitions = -10% CPU over the scroll test, GPU -20..-37%, slow wheel -22%.
  Frame p95 unchanged (18.6 ms). Split: no colour fade alone -5%, no rotation alone 0. Skin not changed.
- Finite animations (2026-11-18, Roger chose it): sign, tank and Dave's screen play 13-20 s on appearance, then rest;
  they play again on hover of the sign, the counter or the composer lane. 15 runs ABC/CBA: CPU 58.1 -> 42.9 s (-26%),
  idle visible 54% -> 18% of a core (no skin 17%). Installed in `~/.t3/userdata/themes/dave-the-viber.json` on the
  Mac mini; `t3_theme_set` was denied (thread without full access), so it shows after a reload or a theme switch.
  `perf/REPORT.md`.
- Rows: no colour fade on hover (Roger's choice after the split test: -5% CPU, the 320 ms spring stays).
- One look in both modes: the header monogram ("SR") was the app's amber-600 / dark:amber-400; now #fbbf24. The sidebar
  edge was the app's sidebar ink at 10% light / 8% dark; now 8%. Open: the 1 px under that edge still paints
  (24,35,54) in light and (20,32,51) in dark, max 6/255; every layer there is transparent and body is the same colour.
- Card council (2026-11-17, Roger: "simplify the cards in chars and performance"; Council Fable Low + Astra Medium,
  1 round, blind). Applied what Roger chose: (1) the 8 attention bubbles stand still (`sk-bob`, its 8 delays and its
  reduced-motion entry removed; REPORT-ideas B1: the bob on an anchored box cost 740 ms layout per 8 s); (2) no
  brass peg on the current ticket (the akane frame already marks it; red pinned peg kept); (3) Snooze/Settle/Discard
  appear at once after the 300 ms hover delay and go at once on leave (no slide, no `--sk-kx/--sk-kt`, no span
  clip-path). Kept by Roger: the 10% status tint, the stain blur, all 8 bubbles. Full 49,322 -> 48,181 (-1,141),
  lite 14,986 -> 14,572 (-414). Dev demo :7508: check.js 0 invalid, l3Lost 0, no overlap; frozen pixel diff vs
  6f0ac45 = only the current ticket's peg (+ the composer caret); hover: keys visible, translate none, below the status.
  Not checked: OS light (no colour change), desktop app. Council patches: /private/tmp/council-cards-12964 (Fable),
  /private/tmp/council-cards-M3AY0n (Astra). Fixed 2026-11-18 (pre-existing since the first
  version): the Woke ticket showed its WOKE stamp and its bubble at once; the stamp-hiding rule now lists the Woke
  anchor row too (full +89). Dev demo: stamp clipped, bubble shown, check.js 0 invalid.
  Active since 2026-11-18 on the Mac mini and the MacBook (d292df3, full.json SHA-256 a2cc87f5…eb20; MacBook backup
  `themes/dave-the-viber.json.bak-2026-11-18`).
- Row `drop-shadow` measured (2026-11-17, Mac mini harness `/Users/roger/t3code/.css-perf`, plans `shadow-3f0d021`
  and `listshadow-3f0d021`, 5 reps, 50/200/500 tickets, results in `data/*-3f0d021.md`). Without the row shadow:
  hover GPU -206 ms [102, 304] and -162 [129, 197] per run (two runs), wheel@500 CPU -447 [326, 790] and -215
  [29, 666]; idle, status, wheel@200 n.s.; dropped frames and p95 unchanged (energy, not jank). All card filters
  (shadow + red peg + stain blur): wheel@500 -477 [369, 932]. Tried: ONE drop-shadow on the list `ul` instead of one
  per row (+54 chars): tickets pixel-identical (settled header/stack gain a shadow), rail hit-test OK, but it is
  WORSE when scrolling: wheel@500 GPU +244 ms [144, 274], wheel@200 +106 [63, 145] (the big filtered surface
  re-renders every scroll frame). Rejected. Not tried: a tilted `linear-gradient` shadow on the row (loses the torn
  edge in the shadow and snaps on hover).
- Painted torn edge (2026-11-18, Roger: "find another way to simulate the torn paper"; applied and installed).
  The card has no mask: its `::after` (3 px, 1 px past the paper with `overflow: clip` + `overflow-clip-margin: 1px`)
  paints the tear gaps in #112339, the shaded wall measured on screen; the shadows are the card's `box-shadow`
  (`--sk-shade` #060e1a73, also on the current ticket), the twine's `box-shadow`, and a baked peg shadow sprite
  `peg_shade` (alpha WebP) clipped to the peg box's content box so it falls only on the wall. No row `filter`.
  Frozen pixel diff vs 8f8a7c5: peg and untilted tickets equal; tilted tickets differ only in edge antialiasing; the
  2 px of shadow under the teeth is straight (was toothed). check.js 0 invalid, l3Lost 0. Harness (`paint-3f0d021`):
  hover GPU -249 ms [158, 393], wheel@500 main -314 [37, 1042], status CPU +132 [6, 276] (the extra ::after per
  ticket, ~0.2 ms per change). Full 48,181 -> 48,477, lite 14,572 -> 14,868.
- Specials model picker (2026-11-18, Roger chose mockup C "Specials neon" of three, then "the chef's stamp should be
  a round chef seal with a thumbs-up", "CHEF in letters, not the hat", "a bit smaller", "more like a pixel badge: a
  thumbs-up with CHEF under it", "a closed fist is fine, smaller, not rotated", "badge at 50%", "the check on the left, floating, for levels and models", "remove the pink neon" frame that marked the
  cursor in the model list but the choice in the HEAT column). The model picker popover is the kitchen's night-navy specials board, the drinks
  menu's sister: a 90 px header with `src2/sprites/specials.png` (75x32, `SPECIALS_P`: Brush Script "Specials", cyan
  ring, "(chef's choice)" in the 3x9 hand font), a TONIGHT neon label, pink neon kbd prices, a darker
  provider rail with cyan rings, a pink ALLERGENS ribbon, a "HEAT" effort column with glowing amber pips, and a footer
  line "Prices in tokens. May contain traces of slop. Ask Theo about the full allergen list." The shared dish-line
  rules read `--sk-lead`, `--sk-price`, `--sk-ring` (defaults keep the cream combobox look elsewhere: branch, font
  pickers). The koi short-list rule is gone. The default effort level carries `src2/sprites/chef.png` (19x15 mask drawn at
  final size: a closed-fist thumbs-up over "CHEF" in the 3x5 font, cut out of a chamfered cyan plate) at 1x (19x15
  px, 2x2 device px per pixel), unrotated, centred on the 32 px row and anchored 40 px from its right
  edge (a checked "Extra High" default with its check ends at 109 of 175 px; the badge spans 116-135), with a cyan glow; it replaces the "CHEF RECOMMENDS" text (the
  backslash pitfall no longer applies here). Two Luna Low imagegen passes could not reduce a thumbs-up to the grid; the
  grid is hand-drawn. The selected model and level carry their check in a 24 px left gutter
  (`.lucide-check` absolute at 6 px), so names and levels share one column. The cursor is the gold frame of every menu (the global pink brush is
  cancelled inside the picker, no 6 px text jump); the choice is the check only. Full 49,815 -> 49,739 (lite 14,529 unchanged). check.js 0 invalid; scan.js no contrast failure in
  the popup; light vs dark picker crop identical except the search caret blink. Verified in the published theme after
  a reload without injection. Previous live file: `final2/published-before-2026-11-18-specials.json`.
- Size pass for the Specials model picker (2026-11-18, Council: Fable Low + Sol High). Full 49,793 -> 48,735
  (-1,058), lite 15,009 -> 14,529; with the uncommitted Specials picker on top full is 49,815 (50,186 UTF-8
  bytes; a gallery that counts bytes would refuse it). Measured in order (full/lite):
  - `)` space dropped in declaration values; kept before `+`/`-`, in strings (with escaped quotes), after `\`
    (-85/-31).
  - 8 shorter attribute matches `$=row-card`, `$=w-slim`, `^=sidebar-draft-i`, `$=ned-divider`, `$=t-strip`,
    `$=b-text`, `$=a-viewport`, `$=m-content` (-397/-225). The live DOM and the app's JS bundle hold no other
    value with these ends; `ned-` because a future `settled-divider` would match `d-divider`.
  - 3 single-use hex vars inlined, unused `--sk-line` dropped (-64/-17); `:not(:first-child)` ->
    `:nth-child(n+2)` (-33/-33); `transparent` -> `#0000` before `!` (-12).
  - `--sk-*` short names: 62-letter alphabet (-121/-17), then Latin-1 letters without the `k` (`--À`…`--ÿ`;
    62 one-letter names, the rest two letters) (-346/-157). The validator and the app count UTF-16 units, not
    bytes (full is 49,101 UTF-8 bytes). The app's own sanitizer (`ko`, copied from the bundle) drops no
    declaration of the new build.
  - Rejected by the Council (future-app collision): `[class*=p\/sidebar-s]` for `.group\/sidebar-status-slot`
    (-216; a new `group/sidebar-s…` class would move bubbles), `$=r-host`, `$=r-footer` (`editor-footer` would
    get z-index 1000), `$=r-inner`/`$=r-inset` (`drawer-*`), `^=conv`, `$=w-card`. Also rejected: dropping the
    flags on `.chat-markdown a`, `.chat-markdown :not(pre)>code` and settings-group. `fx/prune2.js` said ok, but
    unlayered app rules with higher specificity win without them (`.chat-markdown a:not(.chat-markdown-file-link,
    …)`, `.user-message-markdown :not(pre)>code`, `[data-provider-detail] [data-slot=settings-group]`); the
    tested page held only file links. Sprites are already minimal (cwebp -z 9 saves 0 bytes).
  - Proof vs HEAD: CSSOM `cssText` of every rule equal (326 full, 90 lite) except 7 full / 2 lite rules whose
    values are equal after substitution (inlined hex, `#0000`);
    computed style 0 diffs (custom properties and renamed anchor names excluded) in conversation (dark, light),
    model picker, command palette, Settings, question banner; frozen pixel diff 0 in conversation and Settings,
    banner 397 px all in the app's "Working for 2m 18s" timer. check.js 0 invalid, l3Lost 0, no overlap.
  - Not checked live: Mac mini status demo, slim rows, draft indicator, context strip, Stop, terminal drawer
    (CSSOM only), and the published theme (not published in this pass).
- Chef stamp (2026-11-18): the published theme never showed "CHEF RECOMMENDS" (only a pink sliver under Low).
  The served CSS loses `content:"CHEF\A RECOMMENDS"` although the theme file holds it and the injected build works.
  Now `content:"CHEF RECOMMENDS"` + `display:block; width:min-content` (two lines, no escape); verified in the
  published theme after a reload. Full 49,779 -> 49,793. Previous live file: `final2/published-before-2026-11-18-stamp.json`.
- Drinks menu (2026-11-18, Roger: the project picker "should be a drinks menu", icons much bigger, shortcuts as
  prices, WebP lettering "Drinks (pick your poison)", then "hero header" and "stack vertically"). Scope: the command
  palette submenu with a Back button and two-line rows (`:has([aria-label=Back]):has([role=option] .flex-col)`), i.e.
  "New thread in…"; Change theme / appearance and the root palette are unchanged (checked live). The popup `::before`
  is a 120 px navy hero with `src2/sprites/drinks.png` (61x29, `DRINKS_P`: neon core, pink ring, gold subtitle; the
  script is macOS Brush Script 26 px rendered without antialiasing plus a 1 px ring, the subtitle a hand-drawn 3x9
  font) at 3x; max-height 34rem so the list keeps its rows; the "Projects" label is hidden. Icons 32 px, a dotted
  leader from the title to the shortcut, the shortcut a granat pixel-type price aligned with line 1. The legend-list
  re-measures the rows (no overlap). Full 48,741 -> 49,779 (WebP 436 chars). check.js 0 invalid, l3Lost 0;
  dark == light on the card (only the caret differs, max 7/255). PUBLISHED locally; previous live file:
  `final2/published-before-2026-11-18-drinks.json`. Pitfall: the minifier drops the space in `#color {{token}}`;
  put the token first.
- Size cut for the drinks menu (2026-11-18, Roger: HANDOFF options 1 and 2 + Council). Full 49,881 -> 48,741
  (-1,140 = flags -526 + shared values -614), lite 14,986 -> 15,009; with the drinks menu block full is 49,779.
  Option 2 was already done (atlas, 6db2d13), so the second cut is shared values as custom properties: `--sk-peg`
  holds the whole peg layer, `--sk-tear` the two-layer slip mask, new `--sk-cut` (1 px notched polygon), `--sk-foot`
  ({{base}}), `--sk-bb` (footer bubbles layer). `--sk-notch`/`--sk-base` were taken: check a new name with
  `rg -- --sk-<name> src2` first (a collision broke every `--contrast-*` token in a first draft; cmp.js caught it).
  `!important` prune: 52 flags removed (popups, tooltip, switch/select, Usage, search results, user bubble, code
  radius, changed-files card, footer buttons, all 9 content-visibility flags: the app sets it only through
  `@layer utilities .[content-visibility:auto]`, no inline style). `fx/prune.js` drifted in this run: the sidebar
  re-renders while other threads run (baseDrift 47), so every group read "needed". Use `fx/prune2.js` (paired
  per-flag test, synchronous, only elements the rule matches) and `fx/cmp.js` (HEAD vs new, whole page).
  Proof, cmp.js, computed style of every element + ::before/::after (custom properties excluded), drift 0: equal in
  the observed states: thread view (dark and OS light), changed-files card, composer focus, model picker, project
  combobox, context menu, select popup, settings dialog (General, Providers), command palette, /usage, thread search,
  tooltip, footer hover, row hover + key-button hover, keyboard focus, settled shelf open; lite 0 differences. The
  only difference: one anchor name renamed by the minifier (--ke2 -> --kg2 on both anchor-name and position-anchor).
  No real `menu-popup` could be opened; its only competitors (`.dropdown-glass`, the `:focus` ring) are in
  `@layer utilities`/`base`, so they lose to a normal theme declaration. Frozen screenshots 0 px (thread view with
  DISH stamps, model picker card). check.js 0 invalid, l3Lost 0, no overlap; the validator passes on both editions.
  Council (Fable Low, Sol High), round 1: both "go with changes", asked for menu/select/command-palette states before
  removing the popup flags; round 2: both "commit with changes". Sol still preferred restoring 82-85, 89-90 and the 7
  unseen content-visibility flags (full 48,871); kept removed on the layer evidence above.
  Not checked: question UI banner (no removed flag or new variable touches it), attention bubbles other than Input
  (computed style of the hosts equal), Mac mini demo, desktop app. If a colour, radius, shadow or a bubble "goes
  away" in one state, put `!important` back on that declaration.
- Settled stack under the water + spike foot (2026-11-17, Roger): the settled slips (z 1000 - sibling-index(), up to
  999) painted over the fish tank, because the footer had z 22 in the same stacking context (sidebar-container); this
  predates today's changes (seen in e04711c). Footer z 22 -> 1000. Closed settled header: the rod stands on its foot
  again ({{base}} at the box bottom, x 0..36 with the rod at 12); open: no foot, the rod runs down (rod x 23 = slips 23).
  Full 49,176 -> 49,322, lite 14,843 -> 14,986. Previous live file: `final2/published-before-2026-11-17-tankz.json`.
- Spike tip (2026-11-17, Roger: the settled header should be only the spike's point, smaller): the header ::before
  is a 2 px tip on the rod drawn with two gradients in the rod colours (no sprite), level with the label; open, the
  rod runs down to the slips (x 23 = slips' rod x 23, measured). The box keeps 32 px, so the header does not move.
  SETTLED text now starts where WORKING does. `spike`/`spike_open` sprites and SPIKE_P removed. Full 49,381 -> 49,176,
  lite 14,904 -> 14,843. check.js 0 invalid. Previous live file: `final2/published-before-2026-11-17-spiketip.json`.
- Saucepan + static stamps (2026-11-17, Roger: remove the dish and pot animations; Working = a saucepan, "cassó").
  `sk-steam` and `sk-dish` are gone (keyframes, animation rules, their reduced-motion entries). Working and the working
  shelf show `src2/sprites/saucepan.png` (12x12, H1: two steam wisps, flat rim, 1 px handle rising in three steps),
  hand-drawn from Luna Low imagegen references after Roger rejected a traditional pot, blue flames, knife/maki/toque.
  `pot_b` left the mask atlas: icons after it moved 16 rows up (12 px scale) / 24 px (bubbles, 1.5x); proof: new
  atlas == old atlas minus rows 44-59 with the saucepan in rows 28-39. Full 49,998 -> 49,381; lite 14,926 -> 14,904.
  Live inject: check.js 0 invalid, l3Lost 0, no overlap; Input bubble icon and the saucepan stamp checked on screen.
  Not checked live: keys on hover, Failed/Limited/Draft/Request/Woke stamps (covered by the atlas proof), desktop app.
- Idea 3 (2026-11-17, published): content-visibility visible only on anchored attention rows; perf reports on the
  Mac mini in `/Users/roger/t3code/.css-perf/` (REPORT.md, REPORT-032c3f5.md, REPORT-ideas.md).
- "MAIN COURSE" leaked (2026-11-17, Roger): since 6db2d13 the label rule was a top-level `[role="listbox"]::before`,
  so every listbox (command palette, selects) showed it. It is now nested in the picker popup rule. Live: command
  palette listbox `::before` content none, picker "MAIN COURSE". Full 49,997 (3 free). PUBLISHED locally.
- Allergen ribbon (2026-11-17, Roger: "Millora-ho" on the provider rail). The ALLERGENS label floated at the rail's
  foot, far from the badges, with the shared brush padding (right 16px) pushing it off-centre. It is now the
  `::after` of the rail's flex column (`.min-h-full`), so it follows the last badge in flow: `flex: 1` makes it a
  ribbon down to the foot, `margin: 0 auto` centres it, own padding (`!important` against the shared rule), label at
  the top (`text-align: end` in `sideways-lr`), swallowtail end. Full 49,995 (5 free). check.js 0 invalid,
  l3Lost 0; white on pink 5.0:1. PUBLISHED locally.
- Picker council fixes (2026-11-17, Roger: "/impeccable council" on a screenshot, then "7 punts + koi gran"). Council
  Fable Low + Sol High (plan-pace routes), blind to each other. Fixed: (1) the "Default" label is a visible
  `span + span` when another level is chosen and `.sr-only` only when it is chosen, so the stamp now targets
  `> span + span` with `position: absolute` (10px, -12deg); (2) Silom's V read "UIBER": the sign uses `Phosphate,
  var(--sk-pixel)`; (3) the chosen level's check is `order: 1` (after the label), so all pips end at one x;
  (4) the hidden favourite toggle (24px) sat between leader and price: it is now `order: 1` in the actions box, after
  the price; (5) the build collapses double spaces inside strings and `\25C6 ` eats one space, so the sign was
  lopsided: literal "◆" (also in "◆ SIDES"); (6) the app's selected-tab bar `[data-model-picker-selected-indicator]`
  is hidden (the gold disc marks the tab); (7) footer toggle groups are printed boxes, the active one inked in;
  plus the house koi 72×42 in the list's empty corner while the list has fewer than 5 options.
  Rejected from the council: badge before the name (menus list allergens after the dish), shrinking the popup
  (app-owned height), dropping the check. Known: when Medium (default) is chosen, the stamp covers its check; the
  brush still marks the choice. Full 49,625 → 49,985 (15 free), lite unchanged. Live inject: check.js 0 invalid,
  scan.js nothing under 4.5 in the picker, picker light == dark 0 px. The list is virtualised (each option in its own
  wrapper), so the koi guard counts wrappers: koi with 2 and 4 options, none with 5. Not checked: DPR 1, desktop app. PUBLISHED locally; previous live file `final2/published-before-2026-11-17-council.json`.
- Menu-card model picker + mask atlas (2026-11-17, Roger: "B, but even more exaggerated … make it pop"; size via a
  council of Fable Low + Astra Medium at Roger's request). The picker is the house's printed menu: paper with a
  perforated top, the restaurant's own sign "◆ VIBER AGENTS ◆" with the house koi (not the game's sign), "MAIN COURSE"
  dish lines (name, provider mark as a round allergen badge, dotted leader, shortcut as the price in #a01e55), the
  provider column as the "ALLERGENS" key, "◆ SIDES" for reasoning (leaders, 1-6 pips via sibling-index(), chosen on
  the brush), the app's hidden "Default" shown as a rubber stamp "CHEF RECOMMENDS", and Roger's foot note "Prices in
  tokens. May contain traces of slop. Ask Theo about the full allergen list." No text under 4.5 in the picker.
  Mask atlas (`atlas` in src2/sprites2.py): 12 icons (waiting, working, pot_a, pot_b, settle, discard, failed,
  limited, draft, input, request, woke), 12 px wide, 4 empty rows between; masks use `var(--sk-m, var(--sk-atlas)) 0
  calc(box/2 - var(--sk-y))`; bubbles clip each background layer to an 18 px content box (Fable's method; my first
  claim that bubbles could not use an atlas was wrong). Approval stays its own image (half-device-pixel tie at 1.5x).
  Full 48,762 → 49,625, lite 15,609 → 14,931. Proof vs HEAD: bubbles and main view 0 px; sidebar 36 device px differ
  on the edges of three tilted stamps (a 1 px grey halo on the steam is gone): ACCEPTED by Roger as a known deviation
  from the pixel-diff-0 rule. check.js 0 invalid, l3Lost 0. Not checked: light vs dark for the new picker, DPR 1,
  approval/request/woke bubbles live (only Input was on screen), desktop app.
  `!important` pruning in picker and Settings states found ~14 flags safe beyond the static guard (~140 chars), not
  applied (method: flat build, flag k in out2 = k-th source flag except the two dropped -webkit-backdrop-filter).
- Picker fixes (2026-11-17, Roger's screenshot): "Show more" is a text span where a model row has its mark, so it
  got the 24 px dark plate and wrapped. The plate now needs a mark (`span:first-child:has(svg)`). The chosen
  reasoning level's label has `margin-right: auto`, so its check and pips stay at the right edge like the other
  rows. Full 48,762 (1,238 free), lite unchanged. Live inject: plate gone, label 72 px on one line, 5.9:1+ ink on
  the row; pips of all 6 levels end at the same x. Both validators pass. PUBLISHED locally 2026-11-17 with the
  `!important` pruning below (Roger approved); previous live file: `final2/published-before-2026-11-17-prune.json`.
- `!important` pruning (2026-11-17, Fable, at Roger's request "fix everything"): 74 of 197 flags removed from
  `src2/core.css` (26) and `src2/extras.css` (48). Full 49,513 → 48,749 (1,251 free), lite 15,859 → 15,609.
  Why it is safe: the app puts Tailwind in `@layer`s and the theme is an unlayered adopted stylesheet, so a normal
  theme declaration already beats every layered utility. A flag is still needed against inline styles, the app's
  ~230 unlayered rules, app animations, and other theme rules.
  Method: `fx/prune.js` on a flat build (`NEST` False) removes flags in groups in the live page and keeps every flag
  whose removal changes any computed standard property of any element or ::before/::after (104 of 110 testable
  flags passed; 87 flags sit in rules that match nothing on the test page and were kept untested). Then a static
  guard kept 30 more: every flag on opacity, transform, translate, scale, rotate, width/height, inset, position,
  display, visibility, pointer-events, transition, animation, overflow (JS and `animate-*` set those). For the
  rest, each competing theme or unlayered app rule on the same property family that can hit the same element
  (state pseudo-classes and state attributes stripped) must lose by specificity and order alone: 0 conflicts.
  Proof, HEAD build vs pruned build: computed style equal on 3,720 elements + pseudo-elements in dark, in light,
  for lite, and with the model picker open (3,842 elements); frozen screenshot pixel diff 0 outside the caret
  (66 px blink, same as two shots of one build); check.js 0 invalid, l3Lost 0, no overlap; both validators pass.
  Not checked: hover/focus states by screenshot, dialogs, Settings, question UI, Mac mini status demo, desktop app.
  Known limit: a flag removed from a rule that later also matches an element with an inline style or a JS
  animation on that property will lose to it; if a colour, radius, padding or shadow "comes back" in one state, put
  `!important` back on that declaration. Screenshot pitfall found: the first shot after switching
  edition (lite ↔ full) misses the pad and popup text; inject the same edition twice before comparing.
- Model picker as the house menu + build size passes (2026-11-17, Roger chose proposals 1, 2, 3, 5; size ideas from a
  Fable Low consult at Roger's request). Build (tools/build2.py): data URIs are `url(data:;base64,…)` unquoted,
  MIME-less and unpadded; `^= $= *= ~= |=` values unquoted; @keyframes renamed to one letter (whole-name match);
  single rules with a shared-prefix selector list nest; `::before/::after` → `:before/:after`. Dead
  `[data-thread-details-card]{border-radius;box-shadow}` removed. Full 49,414 → 48,393, lite 16,234 → 15,859, with
  no source change in the look: computed style of all 3,721 elements + ::before/::after equal (custom properties
  excluded, URIs and keyframe names normalised), frozen screenshot pixel diff 0, out2/sprites/*.webp byte-equal.
  Picker (extras.css, after the kbd rule): key caps for shortcuts; model rows framed with the mark on a dark plate,
  the row under the cursor named on the pink brush (`--sk-brush`, now shared with section labels); the Reasoning
  header a navy band "◆ REASONING" in Silom gold; level pips 1-6 via `sibling-index()`; the chosen level on the brush.
  Full 49,513 (487 free). check.js 0 invalid, l3Lost 0; no text under 4.5 inside the picker; picker body light ==
  dark (differences only at its bottom edge over the pad, cause not isolated). Unknown: whether gallery importers
  accept MIME-less data URIs. Reserve idea from Fable: a mask atlas (~−550 est.).
- Sprite derivations (2026-11-17, Roger chose A+B+C): Dish's 2nd frame and the pot's 4th frame are the mirrored
  sprite (`scale: -1 1` in `sk-dish` / `sk-steam`); `working2.png` and `pot_c.png` removed. The bubble inks are
  the status masks under a `lighten`-blended ink rectangle (18x18 px, inside the white body); the four `*_ink`
  tokens are removed. Full 49,881 → 49,414 (−467); lite 16,183 → 16,234 (+51, three masks became vars). Isolated
  test with real sprites at DPR 2: mirror frames 0 px at 4 phases; inks ±1/255 (Chromium dithers gradients;
  exception recorded in AGENTS.md). Live inject: 125/125 rules, 0 invalid, l3Lost 0, Input bubble ink correct.
  Not checked: light vs dark, DPR 1, Working/Dish rows live (none open). Not published.
  Rejected after measuring: fish mirror (CSS cannot flip one background layer; `fish_l` is already derived in the
  build), kelp trunk/top split (`weed_b` = `weed_a` with the top 7 rows 2 px left, but 3 more layers cost more
  than the ~48 chars saved), spike = open spike + foot (−55 full, +108 lite). Each WebP data URI has ~100 chars of
  fixed cost, so splitting sprites into parts loses; removing whole tokens wins.
- Dave seated (2026-11-17): Roger edited the original PNG in Affinity. His exported 56x60 PNG is used unchanged;
  the palette includes the colours and partial-alpha pixel in his export. The laptop is drawn 12px lower at 2x so
  its base touches the counter; this keeps its screen position while placing Dave lower behind it. Full 49,708;
  lite 16,183. Activated locally on the MacBook; installed JSON equals the build, SHA-256 f9340f118761bd2bc6f1bfad624b98b56607fb6cf53abb9b3b13f23d5a4fc987.
  Both validators pass; source PNG and WebP match at every visible pixel. The edited sprite has not been checked
  visually in the app. Aquarium bubbles fix and desktop titlebar are included.
- Earlier Dave fan-art (2026-11-17; superseded by the seated edit above): newly drawn from the official Digital
  Extra character sheet's SUSHI BAR poses, found by Luna Low. Straw hat, pale blue shirt, broad build and goatee;
  programming behind a silver laptop with a cyan fish. Roger kept the original broad goatee, with its uneven side
  corrected, and asked for black hair. `src2/sprites/dave.png` is now 56x60, 17 opaque colours,
  binary alpha; `DAVE_P` matches it. The old 28x30 reduction lost the eyes and fish. CSS and the displayed 56x60
  size stay unchanged. Integrated with `textures-backgrounds` at 3ae1ad5 on main: the desktop titlebar and collapsed
  bubble size cut are included. Committed full 49,636; working full 49,684 with the pending aquarium selector fix;
  lite unchanged at 16,183. Built-in imagegen prompt and conversion
  notes: `demo/menus/dave-fanart-prompt.md`. Build and both validators pass; lossless WebP matches the PNG.
  NOT activated: the installed theme still has the prior sprite. No new browser or desktop check for this sprite.
  The bar capture below shows the prior artwork. Sprite preview: `demo/menus/dave-fanart.png`.
  The pending aquarium selector fix and its rebuilt `out2/` remain unstaged for their owner. Main contains the
  generated Dave image and desktop titlebar rules. No active theme change during this integration.
- Restaurant bar (2026-11-17, Roger: the bottom bar is the restaurant counter, same height as the sidebar's, the pad
  stays down in a new thread too, stools, Dave at the right behind a laptop with a lit fish). extras.css "The
  restaurant bar": `.chat-composer-lane` gets `position: relative; padding-bottom: 40px`; its `::after` is the counter
  (plank + front, 60 px, the sidebar footer's recipe, so plank y 740..756 = the sidebar's); its `::before` is
  everything behind the bar (Roger: stools never in front, always behind): stool backs (`stool`, 16x14 spindle backs,
  2x, every 80 px, 4 px hidden under the plank) and Dave (`dave`, 28x30, 2x, right 38 px; an ORIGINAL character, not
  the game's: white headband with a pink stripe, indigo happi, laptop lid with a lit fish) with a screen-glow
  flicker (`sk-screen`, off under reduced motion). The composer area's own `::before/::after` are bubble hosts, so the
  bar must not use them. New thread: `[data-chat-composer-overlay]` `align-items: flex-end` (was centred); the
  context strip (checkout / branch / access) rests on the plank with a night background over the stool backs.
  Pad bottom on the plank: thread 741, new thread strip bottom 740. Last message stays above the pad. Light == dark
  0 px on the bar band; check.js 0 invalid, l3Lost 0. Full 48,629 (flat 55,482); lite unchanged. Capture
  `demo/menus/bar.png`. Stools tile from the right edge (one hidden behind Dave), so narrowing slides them behind
  the pad. The app pushes the pad left by `--chat-lane-inset-end` (276 px at 1280, 0 at 1240); Dave and his glow get
  width 0 when the gap right of the pad is under 120 px (`--sk-d` clamp; checked 1280/1240 shown, 1228/1120 hidden).
  Full 49,913: 87 chars left. Not checked: right panel open, desktop app.
- House menu card (2026-11-17, Roger: "personalitza la interfície i els menús amb els colors, formes i tipografia
  d'aquestes captures", 4 screenshots of a pixel sushi-bar game UI; mood, palette and shapes only, no copied art).
  NOT published yet. extras.css "Controls: the house menu card":
  menus, popovers, comboboxes, selects and the command palette are cream cards (#ece2d4) with a 2 px copper border
  (#a86030), dark outline and pixel shadow; the card re-inks the app tokens (`--contrast-*`, success/warning/error/diff)
  so all children follow. Highlighted row = 2 px gold inset (#e4b460); checks pink. Section labels (`*-label`) are
  pink brush strokes (#c8346e, white); dialog titles a gold ribbon. Dialogs and the thread details card: navy #283246
  board, copper frame + gold hairline. Primary buttons hot pink #e4106c (white 5.7:1); switches square, pink when on,
  gold ring; select triggers recessed; settings group cards #303c54; tooltips navy tag with a gold edge.
  Type: `--sk-pixel` = Silom (macOS), Krungthep, then `--sk-round` (no font embedding: `src()` is banned).
  All popups and toggles have square corners. Full 40,323 → 43,607 (flat 49,687: a flat build plus the textures
  thread will exceed 50,000); lite unchanged. Checked: check.js 0 invalid / l3Lost 0 / no overlap; scan.js no new text
  under 4.5 (details card disabled buttons were 3.96 before and are unchanged); light == dark inside popups and
  settings except pre-existing gaps (left settings nav/fish tank, identical in the HEAD build). Captures `demo/menus/`.
  Not checked: alert dialogs with a real title + primary button (none reachable without a destructive action),
  desktop app, Windows/Linux fonts.
  Merged with the textures branch (2026-11-17): the Settings dialog keeps the seigaiha wallpaper (the navy board fill
  excludes `[aria-label=Settings]`); group cards sit on it. Combined check: check.js 0 invalid / l3Lost 0; Settings
  light == dark except the pre-existing left-nav/fish-tank gaps. PUBLISHED locally 2026-11-17 (previous live file
  `final2/published-before-2026-11-17-menus.json`).
  Settings tank fix: the fish tank pseudo-elements are scoped to `sidebar-inner`, so Settings' side nav (its own empty
  `sidebar-footer`) keeps only the wood counter; its last items are no longer covered. Full 44,763.
  Breadcrumb (Roger: "posa el breadcrumb també en silom"): `[data-chat-header] [data-slot=workspace-breadcrumb-text]`
  uses `--sk-pixel`; the header's buttons keep `--sk-round`. Full 44,823 (flat 50,973). check.js 0 invalid, l3Lost 0.
  Usage (Roger: "també caldria estilitzar el usage"; `/usage` is `dialog-popup[aria-label=Usage]`): seigaiha wallpaper
  like Settings, limit cards #303c54, Silom numbers and header crumbs, each meter (`button[aria-label*=left]`) a
  recessed track whose fill (the part left, provider colour inline) shows as 6 px lit segments with 2 px gaps (`mask`; Roger preferred these to 10 px), the pace
  mark a 4 px pink pin, reset chips navy tags with a gold edge, the pressed view toggle pink. Light == dark 0 px in
  the dialog; check.js 0 invalid. Cost/Tokens views not seen: this connection has no diagnostics access. Full 45,469
  (flat 51,803). Capture `demo/menus/usage.png`.
  Changed-files card (Roger: "needs to be stylized and opaque"; `[data-changed-files-state]`, sticky
  `[data-changed-files-header]`): opaque navy board #283246, 3 px copper border, dark outline, 6 px drop shadow
  (fits the 4 px gap inside the lane's `overflow-x: clip`); header #1c2436 with a gold top hairline and copper
  bottom rule, title in Silom gold; square rows, hover #303c54 + 1 px gold edge. File-type icons get a per-mode
  inline colour from the app (light-mode CSS icon 1.9:1, image 2.6:1 on navy), so all are gold `!important`.
  Text ≥ 5.39:1, icons ≥ 3.9:1; light == dark on the card (only diff: the swinging sign); sticky header hides rows;
  check.js 0 invalid, l3Lost 0. Full 45,975. PUBLISHED locally 2026-11-17 (previous live file
  `final2/published-before-2026-11-17-changedfiles.json`). Not checked: hover contrast of folder names on #303c54 by pixel.
- Textures and backgrounds (2026-11-17, branch `textures-backgrounds`, NOT published; Roger: "patterns/textures i imatges
  de fons per a la resta de la interfície … i també el fons de la barra lateral"): sprites `wall` (32x32, four glazed
  tiles with grout, bevel, glints, a chipped corner; replaces `tile`, shown at 64 px), `seigaiha` (24x12 wave scales in
  3-5% white, 48x24 px) and `beam` (32x26 dark wood, 64x52 px). Wall in core.css (both editions; Settings' side nav
  shares it in full, under a 30% inset shade). extras.css "Textures and backgrounds": seigaiha wallpaper (fixed to the
  window, so it lines up across panes) on the conversation, the right panel, the Settings dialog, the empty/loading
  timeline (`[data-timeline-loading]` made transparent) and the changed-files sticky header; the chat header and the
  right panel's tab bar are one wood beam. Full 40,286 → 41,326 (+1,040); lite 15,253 → 15,337 (+84).
  Pixel contrast (tools/pixcheck.py, median ring / brightest ring pixel): header 4.86 / ≥4.7 (the "/" separator; the
  beam's light streak was darkened to `#4f321f` for it), conversation 5.97 / 5.34, panel 6.57 / 5.74, wall labels
  9.57 / 5.87, Settings nav 6.68 / 5.53 (4.33 before the shade), empty state 7.33. Light == dark: 0 px on every textured
  surface. check.js full + lite: 0 invalid, l3Lost 0, no overlap. Captures `demo/textures/`.
  Night window (2026-11-17, Roger: night landscape at the top of the sidebar, behind the logo): sprite `night`
  (128x26, 14 colours, shown 256x52, repeat-x): navy sky with dithered bands, stars, moon and its broken reflection,
  moonlit ridges, sea, shore lights, a cherry branch top right, and a wood sill level with the chat header's beam.
  core.css (both editions) on `[data-slot=sidebar-inner] > div > div:first-child` (the 52 px top bar). +659 chars in
  each edition: full 41,985, lite 15,996 (flat 19,190). Toggle icon on the sky 9.28:1 (brightest ring pixel); light ==
  dark 0 px; check.js 0 invalid, l3Lost 0 in full and lite. Capture `demo/textures/sidebar-night-window.png`.
  Moved into the artwork slot (Roger: "posa'l a lloc"; Environment identification = nightly): the app draws its own
  `.sidebar-stage-backdrop` only for built-in palettes (`sidebarArtwork: true`); a custom CSS theme always falls back
  to the "Nightly" pill (`Et()` in useSettings). So the window now covers the slot itself: `night` is 128x50 (256x100
  px) on `[data-slot=sidebar-inner] > div:first-child`, top bar + search row, sill under the search row.
  Search (full only): rests as a glazed magnifier tile (28 px, 2 px margins keep the 32 px row, list top stays 100);
  the invisible input covers the tile, so click/Tab/shortcut focus it; focus or a query opens the recessed field, an
  empty blur folds it back. Magnifier 8.90:1. Full 42,761 (flat 49,143: the flat fallback is nearly full), lite 16,146.
  Logo (Roger: "treu el rètol de fusta … blanc eteri, flotant en el cel"): no plaque; white `#fbfaff` with a moonlit
  halo (two drop-shadows) and a 2 px drift (`sk-float`, 3.2 s alternate; off under reduced motion), focus outline
  cream. "Code" 12.33:1 on the sky (6.70 against the halo's brightest pixel); light == dark 0 px. Full 42,941
  (flat 49,348).
  Rebased on main 7de285d (house menu card, rename, Usage, changed-files board): full 47,590 nested (flat 54,403;
  a flat build no longer fits 50,000), lite 16,183. check.js 0 invalid / l3Lost 0; scan.js only the decorative ticket
  stains; light == dark 0 px in sidebar and header. PUBLISHED locally 2026-11-17 as `dave-the-viber` (server file =
  build, sha256 fb876c81…); previous live file `final2/published-before-2026-11-17-nightwindow.json` (= main's build).
  At 02:38 another thread published main f377750 (ORDER header fix) over it; main was then fast-forwarded to this
  branch (91b8af1, pushed to GitHub) and republished: live = main build, sha256 f89ff65e…, full 47,637, with both
  changes; previous live file `final2/published-before-2026-11-17-nightwindow2.json`. Public captures: only
  `night-sprite-4x.png` and a crop of the sidebar top above the tickets (no thread titles); the 7 captures of the
  first textures commit were already public and show real thread titles.
  History purge (2026-11-17 03:25, Roger): OCR (macOS Vision, full image + 3x tiles) found client names / real
  thread titles in 114 screenshots (council2, demo, demo/frames, demo/v2, demo/verify, demo/menus, demo/textures,
  final2, v1/final). Each got its private text pixelated (same path and size), re-OCR finds none of the terms;
  `git filter-repo --blob-callback` rewrote main, force-pushed with lease (3188acb -> 194e680; only PNG blobs
  differ). Local main moved with `reset --keep` (other threads' WIP intact), Mac mini clone reset + gc. GitHub may
  keep old commits reachable by SHA until its GC; no forks. Tool scripts: scratchpad only.
  Desktop titlebar (Roger: logo closer to the collapser, centred between it and the moon; history keys after the
  moon): rules keyed on `[aria-label="Go back"]` (desktop only), +622 chars. Real desktop app (relay capture):
  icon 98.5-111, "T3 Code" 118-173.5, moon ~183-203, keys 214.5+. Web unchanged (logo x 52). Full 49,789 of
  50,000. PUBLISHED locally; previous live file `final2/published-before-2026-11-17-desktopbar.json`.
  Size cut (Roger chose the measured cuts): the 8 collapsed-sidebar bubble selectors became one `--sk-bub: none`
  on `:root:has(collapsed sidebar)` read by the hosts' `display` (-597, full 49,192). Computed display/left/top of
  all 8 hosts equal old vs new, open and collapsed; check.js 0 invalid. The "raw <> in data URIs" item is obsolete
  (no SVG URIs since the WebP pass); single-use hex vars (~-150) not applied (scope risk, small gain).
  Not done: the terminal (the web preview cannot open it; xterm paints its own `#11131a`). The fish tank in Settings'
  side nav was fixed on main (scoped to `sidebar-inner`). Found, not mine: the thread details card's muted rows are 3.55-4.08:1 (same before and after).
- Open ticket off the peg (2026-11-17, Roger: "el ticket obert separat de l'agulla, desplaçat a la dreta, sortint una
  mica de la barra lateral"; published locally, previous live file `final2/published-before-2026-11-17-offpeg.json`):
  the current ticket gets `translate: 20px 0` (320 ms, same curve as rotate), so it leaves the peg (12 px gap) and its
  right edge sits at 263 px, 8 px past the 255 px sidebar. To avoid the clip, the sidebar scroll root gets
  `overflow: visible` and the viewport `margin-right: -12px; padding-right: 12px` (ticket column width unchanged, no
  horizontal scroll). Only under `[data-state=expanded]`: a collapsed offcanvas sidebar showed 7 px of the slip at the
  screen's left edge. The app's resize rail (`sidebar-rail`, 247..263 px, z 20) took clicks on the slip's last 16 px,
  so the open slip's row gets `z-index: 21`; that needs the scroller's mask removed (a mask is a stacking context; it
  was a 12 px bottom fade under the fish tank, diff = only that band), and the footer gets `z-index: 22` (extras.css)
  so the open slip still scrolls into the water. Hit test on the live file: 0 px of the slip lost to the rail.
  Checked: check.js 0 invalid, l3Lost 0, no hover overlap; light == dark on the ticket (0 px; the app's own sidebar
  border differs, alpha 0.10 vs 0.08, before this change too); bubble follows the ticket. Side effect: the open
  slip's drop shadow falls 1-2 px over the next peg. Not checked: desktop app, mobile sheet sidebar.
  Roger: only the first recent overhung, the others were clipped. Cause: rows have `content-visibility: auto`
  (paint containment clips to the row); only bubble rows had `visible`. The open row now gets `visible !important`.
  Checked on a non-bubble 5th row: clipped at 247 px before, paper to 263 px after; check.js 0 invalid, l3Lost 0.
- Sync + Mac mini (2026-11-17): this folder is a public GitHub repo, https://github.com/rgrvlsk/dave-the-viber
  (`demo/video.mp4` is git-ignored, 64 MB). Clone on the Mac mini: `~/.t3/projects/dave-the-viber`. The full edition is
  installed in the Mac mini's main T3 Code, still as `~/.t3/userdata/themes/pixel-sushi-rail.json` (older build). Pending: install it as
  `dave-the-viber.json`, activate it there and remove the old file once the CSS perf job below finishes (it measures this skin).
  A Claude Opus High thread on the Mac mini (project t3code) profiles the CSS cost; its work and `REPORT.md` go to
  `/Users/roger/t3code/.css-perf/` on the Mac mini (untracked via `.git/info/exclude`).
- Model mark sync (2026-11-16, Roger: on 2-line tickets the model icon moved out of sync with the keys; published locally
  as a full publish from src2/, so the fish tank is live too; previous live file `final2/published-before-2026-11-16-modelsync.json`):
  the base rule for the absolute model mark (core.css, "With no meta line") had specificity (0,5,4), above the hover
  rule (0,5,3), so its `140ms ease-in` transition also ran on hover (no 300 ms delay, other curve). Fix: wrap
  `:not(:has(...))` in `:where()` → (0,4,3). Live check: hover mark transition = keys transition
  (`0.18s cubic-bezier(0.2,0.9,0.3,1) 0.3s`), leave both 140ms ease-in; check.js 0 invalid, l3Lost 0.
  Leave curve (Roger: "la tornada no és fluïda"): mark and keys were in sync, but `140ms ease-in` stopped at
  full speed (5.5 px in the last 20 ms). Now leave = `160ms cubic-bezier(0.2,0.9,0.3,1)` (entry curve), keys hide at
  160 ms; last 20 ms = 0.1 px, gap mark–key 21 px in every step (paused WAAPI stepping, background tab paints no
  frames). Previous live file: `final2/published-before-2026-11-16-leavecurve.json`.
- Fish tank (2026-11-16, Roger: "peixera amb algues, bombolles i coralls"; published locally with the model mark sync): the footer's wall
  strip is now an aquarium 70 px tall (`sidebar-footer::before` tank: lacquer rim + gold edge, surface line, 3 kelp
  in two sway frames via discrete `--sk-w1/--sk-w2` keyframes, branch + brain coral, sand; `::after` life: koi there
  and back (`fish_l` = mirrored token) and 3 bubble columns, `background-position-x/-y` keyframes). It rises 56 px over
  the ticket list (footer `overflow: hidden` removed), so tickets scroll into the water; `sidebar-content` gets
  56 px bottom padding so the last ticket rests above it. Water tint is dark cyan (darkening keeps contrast better
  than a mid blue): read project ink at the surface 4.80:1 (mid-blue tint gave 4.10). Deeper text (kelp/sand zone)
  goes below 4.5 by design. Light == dark (0 px). check.js 0 invalid, l3Lost 0. Full 37,225 → 39,748 chars; lite
  unchanged. Sprites `weed_a/b`, `coral`, `brain`, `sand`, `bubbles` in `src2/sprites/`. Preview `demo/fishtank.png`.
  Unverified: reduced motion (fish parks off-screen, bubbles freeze), desktop app, narrow/collapsed sidebar.
- Weights (2026-11-16, Roger): ticket titles bold 700; unread keep the full ink, read fade to `--sk-read`
  (65%, 75% on kraft: the 4.5:1 floor; hover/focus give the full ink back). Project line roman 400.
  Live title 5.05 cream / 5.02 kraft. Live file is a hotfix (`final2/hotfix-weights.json` = the pre-change
  live file + these rules appended), because `src2/` also holds another thread's unpublished hover-key
  transitions. The next full publish from `src2/` carries these rules. Previous live file:
  `final2/published-before-2026-11-16-weights.json`.
- Paper tint (2026-11-16 22:30, published locally 2026-11-16 together with the nesting and WebP passes): tickets with a coloured stamp
  get 10% of the stamp ink on their paper (`--sk-t` set by `:has()` in extras.css, `--sk-bg` in core.css; hover now
  sets `--sk-paper`). Grey Waiting and no-status tickets stay cream. Full-only (+643 chars; lite +39).
  Checked: Dish! #e6e4d1, Input #e7e2d9, pinned Input #c8aa86; project text ≥ 5.55, stamp 5.64; light == dark.
- Timer (2026-11-16 22:00): the status timer (`span[aria-hidden]` after the label) has `text-transform: none`,
  so the stamp reads "WORKING 26s". Previous live file: `final2/published-before-2026-11-16-timer.json`.
- Full edition `out2/full.json` / `full.css`: **45,469 chars** nested, 51,803 flat (OVER the limit if a flat build is ever needed) (limit 50,000, for t3skins.dev).
- Lite edition `out2/lite.json` / `lite.css`: **15,374 chars** nested, 18,568 flat (limit 20,000, for t3themes.com). Sidebar only.
- CSS nesting (2026-11-16 21:45): the minifier nests consecutive rules with a shared selector prefix, never reorders
  them, and refuses output that does not expand to the flat CSS. With `--sk-notch`/`--sk-plank`/`--sk-board` and
  `a / b` → `a/b`, on the same sources: full 44,260 → 38,521, lite 19,682 → 16,540. Proof: Chrome CSSOM leaf rules
  equal; computed style of all ~4,250 elements + ::before/::after equal (full dark+light, lite dark); pixel diff 0 in
  dark and light for both editions; `fx/check.js` 0 invalid (it now checks nested blocks at every depth). App filter
  `xi()` keeps nested rules (Electron 44 / Chrome 152). Unknown: whether the t3themes.com / t3skins.dev importers
  accept nesting; set `NEST[edition] = False` for a flat build (flat sizes are printed; lite flat has ~300 left).
- Bubbles (2026-11-16 22:00): every ticket that needs you gets a bubble, not only the first of each kind
  (Roger: a 2nd Input ticket kept its stamp). 8 page-level hosts: Approval and Input ×3 (`html::after`,
  `body::after`, `main[data-slot=sidebar-inset]::before/::after`, `[data-workspace-area=composer]::before/::after`),
  Request and Woke ×1 (conversation `::before/::after`). A 4th ticket of one kind keeps its stamp. Hosts with
  no anchor are NOT hidden by `position-visibility`: the `-300px` anchor fallback parks them off-screen (keep it).
  Ink centred on the white body (`50% calc(50% - 2px)`; it sat 5 px low and touched the bottom edge).
  Full 40,564 css chars; lite 16,579 (only var renames shift). Previous live file:
  `final2/published-before-2026-11-16-bubbles.json`.
  Missing bubble report (2026-11-17, Roger's screenshot: an Input ticket with no bubble and no stamp). The stamp is
  hidden on the first 3 tickets of a kind whether or not the bubble paints, so a failed bubble leaves no signal.
  Not reproduced: with tickets in the viewport, Input bubbles 1–3 (incl. the composer host with a question open)
  paint. Cause unknown. Roger chose to keep only the bubble; investigate when it repeats. Then capture at once:
  screenshot, sidebar scrollTop and collapsed state, ticket index of that kind, open thread, and the host's
  computed `display` / `left` / `top` / `position-anchor`.
- Footer (2026-11-16 22:30, council Opus + Sol, Opus design chosen): wall strip 0..14 px (koi), plank 14..30 + 2 px
  shadow, keys on the brown front with 6 px above/below (footer 70 → 74 px; before, the keys overlapped the plank by 2 px).
  Footer keys are slip-paper pixel keys (ink glyph 15.3:1, hover lamp `#ffdf9e`); the desktop update button
  (`li.ml-auto > button.size-8`, not a menu-button) is the same key in gold (10.2:1) with a square ink dot.
  Cream focus ring 2 px outside. Light == dark (0 px in the footer). Full +1,202 chars (json 46,026). Not tested in
  the desktop app: real update states (progress ring, downloaded badge), other footer pills.
  Previous live file: `final2/published-before-2026-11-16-footer.json`. Sol's alternative (brass keys on the wall,
  counter at the bottom): `council2/footer-sol.md`.
- Key hitbox (2026-11-16 22:50): the keys span gets `z-index: 31`. Before, line-3 content painted over the keys and
  took the clicks: on no-branch rows the absolute model mark (its hover padding covers the keys) and the app's
  `z-30` model span. Hit test (`elementFromPoint`, 1-px grid, real hover): Settle 155/396 → 320/320 px. `check.js`:
  0 invalid, no overlap, l3Lost 0. Previous live file: `final2/published-before-2026-11-16-hitbox.json`.
- Hover keys (2026-11-16 21:40): Snooze/Settle/Discard are pixel keys in the peg colours (gold/green/red, 1-px
  outline, clipped corners, bevel, ink sprites `woke`/`settle`/`discard`; icon contrast 5.5–10.2). Line 3 no longer
  hides anything on hover: it gets `padding-inline-end: var(--sk-actions)`, so the branch truncates and the PR number
  and model mark move left (before, PR rows lost the PR number: line 3 starts with an empty span there). The
  no-branch model mark moves left the same way. `fx/check.js` reports `l3Lost` per row (0 expected; old CSS gave 6).
  Previous live file: `final2/published-before-2026-11-16-keys.json`.
  Keys slide (2026-11-16 22:05, Roger): keys centred on line 3 (wrapper `margin-top` removed; key, PR and model
  centres all at 66.8 px). After 300 ms the keys slide in from the paper edge (`translate: var(--sk-kx)`, wrapper
  `clip-path: inset(0 -0.3125rem 0 0)`) on the same 180 ms curve as the line-3 padding, so they push the PR and model
  marks with a constant 7 px gap (measured per frame); out: 140 ms ease-in, then hidden. Focus/menu: instant.
  `--sk-kx`/`--sk-kt` are the key offset/transition; `--sk-t` is the unrelated status tint.
  Published locally 2026-11-16 ~22:05 from the current sources (a 22:00 publish by another session had dropped the
  slide; that file is `final2/published-before-2026-11-16-slide.json`). Parallel sessions: rebuild from sources
  right before publishing, and diff the live file against the build first.
- Pinned tickets (2026-11-16 21:30): kraft paper `#d9b585` (hover `#e2c398`, edge `#b08a58`), the app's
  `svg[aria-label=Pinned]` hidden, notes ink 82% (read title 5.02:1, project 6.33:1). Status stamps keep a cream
  label via `--sk-stamp` (stamp 6.78:1). Pixel diff vs old build: only pinned rows change; light == dark.
  Previous live file: `final2/published-before-2026-11-16-kraft.json`.
- data: URI pass (2026-11-16 20:35): sprites 9,538 → 7,961 chars in full (4,131 → 3,721 lite). Each sprite takes the
  shortest of filled rects or 1-px strokes on a half-pixel-shifted viewBox (`sprites.doc`); `<`/`>` stay unescaped;
  `woke` lives once in `--sk-i-woke` (it was emitted 3×: the minifier's `-webkit-mask` drop missed `{{token}}` values,
  now fixed). Pixel diff of all 35 tokens × 5 scales × bg/mask, old vs new: 0 px. Reference render: `final2/sprites.png`.
  Previous live file: `final2/published-before-2026-11-16-uri.json`.
- WebP pass (2026-11-16, after the nesting pass): sprites are lossless WebP (`sprites.webp()`), rendered with
  `image-rendering: pixelated` on `:root` (inherited) and `auto` back on `img, video, canvas`; the per-rule pixelated
  lines and the `[data-workspace-area=conversation] *{auto}` reset are gone. Full 41,782 → 36,749, lite 16,590 → 14,291.
  Unrotated sprites match the SVG pixel for pixel (5 scales, bg + mask). On tilted slips the SVG was resampled smoothly;
  WebP stays crisp (~9.5k px differ on the live sidebar: tear edges, status icons, peg 1 row). check.js equal before/after.
  Unverified: Safari/Firefox. Baseline: scratchpad `pre-webp/`.
  PUBLISHED locally 2026-11-16 together with the nesting pass and the paper tint (Roger approved);
  previous live file: `final2/published-before-2026-11-16-webp.json`.
- Both pass `node tools/t3skins-validate.js out2/<edition>.json`. Nothing published to any gallery (Roger's rule).
- Last council (defect hunt on the live demo): Astra 7.5, Fable 7.0 → fixes applied; earlier design rounds R6:
  Fable 9.1, Astra 9.2. Fable's size pass applied (items 1, 3, 4, 5); pixel diff before/after = 0.

## Video and captures
- `demo/v2/` (2026-11-16, after all fixes): video.mp4 (2 min 46 s, 1440 px) + 12 PNGs + sheet.png, recorded via the tunnel.
- `demo/video.mp4` (3 min 24 s) + 21 PNGs: T3 Code dev (origin/main b0f0c44d) on the Mac mini with the theme,
  dev-replay scenarios. Recorded BEFORE the defect fixes. Contact sheets `demo/sheet01-03.png`.
- `demo/verify/*.png`: after the fixes (question + Snoozed dark, hover dark, code light).
- `final2/`: latest published JSON/CSS plus reference captures (sign, search results, pot frames, question).
- States the dev demo produces: Approval, Input, Working, Done ("DISH!"), Settled, Snoozed. Not produced:
  Request, Waiting, Limited, Failed, Woke (tested earlier on the live app by relabelling status chips in the DOM).

## Source layout and build
- `src2/core.css`: shared rules (lite = core minus `/*full*/ … /*/full*/` spans, which may sit inside rules or
  selector lists). `src2/extras.css`: full only. `{{token}}` = sprite data URI; art in `src2/sprites/*.png`
  (read by `png()`), palettes/tokens in `src2/sprites2.py` and `tools/sprites.py`; exact output images in `out2/sprites/*.webp`. `src2/colors.json`: roles (same for light and dark variants).
- Build: `python3 -I tools/build2.py $D` → `out2/` (deterministic since 2026-11-16 20:15: vars renamed by chars saved, name as tie-break). The build minifies both editions (no comments, vars renamed
  `--sk-*`→`--kX`, rgb()→hex8, unquoted attrs/fonts, drops `-webkit-mask*`), and REFUSES unbalanced braces and
  `:has()` nested in `:has()`. Sprite paths are merged rectangles; the build asserts pixel coverage.
- Careful when editing with scripts: `{{token}}` contains `}}`, so never slice a rule with `index("}")`
  (it broke the CSS twice); replace exact strings instead.
- Publish: write `out2/full.json` to `~/.t3/userdata/themes/dave-the-viber.json`, then
  `t3_theme_set themeId: "dave-the-viber"` (no theme payload). Verify the server file equals the build.

## How to test (do all before publishing)
1. Static server for the folder: `python3 -I tools/serve.py $D` in the background (CORS, port 8765).
2. Open the live app in T3's built-in browser: `preview_open http://127.0.0.1:3773/<env>/<thread>` (open=false,
   reuseExistingTab=false). Load the injector and inject without publishing:
   `const f=eval(await (await fetch('http://127.0.0.1:8765/fx/inject2.js?'+Date.now())).text()); await f('full')`
   (also emulates the colour roles). Then:
   - `fx/check.js` (eval it): parse count (written == parsed), 0 invalid, 3-line layout per row, contrast
     (title ≥ 7.0, project 6.7, stamp 5.6, sprite 6.6 today), hover buttons never overlap the status.
   - `fx/scan.js`: whole-page text contrast; it cannot see gradients, so for the wall/lamp/wood use
     `python3 -I tools/pixcheck.py <screenshot.png> boxes.json` (pixel-sampled, border-ring background).
   - OS light vs dark: `preview_set_appearance light|dark`; the look must be identical.
   - Pixel diff for refactors: freeze motion with an extra sheet
     `*,*::before,*::after,html::after,body::after{animation:none!important;transition:none!important}`,
     screenshot old vs new, compare with PIL (expect 0 differing pixels).
   - Screenshots sometimes capture before content-visibility rows paint: retake if the sidebar is empty.
3. Pending question UI: spawn a Haiku child that calls AskUserQuestion once (single + multi select), open its
   thread in the preview, inject, inspect `[data-composer-banner-surface]`, then `task_cancel` it. Ask Roger
   not to answer it.
4. Desktop app checks: Luna relay per the `checking-interfaces` skill (bundle id `com.t3tools.t3code`);
   a look script lives in the old scratchpad pattern (getAXStateAndScreenshot → files).
5. Mac mini dev demo (all replay states): `ssh rogerflix` is the Mac mini (linked env "Mac mini de Roger",
   id fa3bab2b-…, project `t3code` id `mcp:d285ab1c-407a-4efb-85a3-5ddb6366a403`).
   - Worktree `/tmp/t3code-theme-demo` (detached origin/main), dev home `/tmp/t3code-dev`, server
     `http://localhost:7508` (started with `vp run dev --home-dir /tmp/t3code-dev`, pid in /tmp/t3code-theme-dev.pid).
   - Update the theme there: `scp out2/full.json rogerflix:/tmp/t3code-dev/userdata/themes/dave-the-viber.json`
     then `ssh rogerflix 'cd /tmp/t3code-theme-demo/apps/server && export PATH="$HOME/.local/share/vite-plus/bin:$PATH"
     && node --experimental-strip-types src/bin.ts theme set dave-the-viber --base-dir /tmp/t3code-dev'`.
   - Its built-in browser is already paired; drive it with a Luna relay on the Mac mini (delegate_task with
     target.environmentId + projectId) running preview_* tools; copy captures to /tmp/t3code-theme-demo-out and
     `scp` them back. Pairing from this Mac through an SSH tunnel did not complete (token consumed, cookie on
     localhost); `node … src/bin.ts pair --base-dir /tmp/t3code-dev` mints a fresh 5-minute token if needed.
   - Do not touch /Users/roger/t3code (main checkout) or the Mac mini's ~/.t3/userdata.
   - BEST WAY (works, 2026-11-16): drive it from THIS Mac. Tunnel in the background:
     `ssh -N -o ExitOnForwardFailure=yes -L '127.0.0.1:7508:[::1]:7508' rogerflix` (quote the brackets in zsh),
     mint a token (`… src/bin.ts pair --base-dir /tmp/t3code-dev --ttl 10m`), then `preview_open
     http://localhost:7508/pair#token=…` with profileId "incognito". Full access: Stop shows, prompts can be sent.
     Three Luna relays on the Mac mini failed (stale aria refs, no shell, appearance error); do not use relays.

## Owner rules (keep)
- Row layout: line 1 title alone; line 2 project + status; line 3 branch + model; no wrapping; hover buttons never
  cover the status. Approved exception: calling tickets show the status as a bubble beside the ticket.
- Text ≥ 4.5:1, icons ≥ 3:1 at Appearance contrast 165; status distinguishable without colour; reduced motion
  respected; visible keyboard focus; no @import/image-set()/src(); url() only data:/#id; no nested :has().
- One look in light and dark OS modes. Round radios and square checkboxes in questions must keep their shape.
- Hover only straightens tickets (no lift). The thread detail popover covers the bubbles (wanted).
- Roger answers in Catalan, short sentences, result first. Ask before any gallery publication.

## Open items
- Ticket move to the Working shelf shows a clipped remainder/jump (app animation; left alone).
- Breadcrumb emoji is part of the project name (CSS cannot remove it).
- Unapplied size items (if room is needed; applied 2026-11-18 size pass for Specials, see State): the ~40
  non-guarded `!important` flags whose rules match nothing in the tested states (Stop, terminal drawer, dialog
  title, primary buttons, header monogram/favicon variants, focus outline, question banner); `opacity: 0.17` in
  core.css is dead in full (-12 with a lite-only marker); raw `<>` in data URIs (~-500, risky). Sprites are already
  minimal lossless WebP. Rejected with numbers: reordering rules to nest more
  (-418/-159, cascade risk), one merged `border-radius:0!important` rule (+753), `[class*=status-slot]` and
  `[class*=p\/sidebar-s]` (match other `group/...` classes), suffix matches on generic names (`r-host`,
  `r-footer`, `r-inner`, `r-inset`, `w-card`, `^=conv`).
- The Mac mini dev server is still running; stop it (`kill $(cat /tmp/t3code-theme-dev.pid)`) and remove the
  worktree (`git -C /Users/roger/t3code worktree remove /tmp/t3code-theme-demo`) when no longer needed — ask Roger.
- History: `LEDGER.md` (hillclimb ledger), `council2/BRIEF-R*.md` (council briefs), `v1/` (first theme sources).


## Context controls on the counter (2026-11-17)
- Context strips are absolute below the pad, so they no longer lift the paper off the plank. Controls use dark ink
  on the chat counter's lighter wood front (#b9783d), with opaque icons, a light hover and an ink focus outline.
- Build + both gallery validators pass; lite unchanged; ink/front contrast 5.31:1. Activated on Roger's MacBook
  after approval. Desktop capture confirms the paper touches the plank and the visible context controls are dark.
  Built-in browser: existing thread and blank draft both have pad bottom = plank top, y 840 at 1440x900.
  Draft shows Current checkout, main and Full access in dark ink; all fit at 900x700 too. Bar and context-control
  bands have 0 differing pixels between light and dark captures. Test tabs closed; no prompt sent.
  The rewritten change commit is 194e680 (formerly c598606). Concurrent titlebar/bubble publishes preserved;
  latest installed CSS validated at 49,192 chars. Private QA captures stay outside the public repository.
