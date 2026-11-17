# Dave the Viber — handoff (2026-11-16)

T3 Code theme by Roger's request: a night sushi bar in pixel art, Dave-the-Diver mood (original art only).
Published and active as "Dave the Viber", **themeId `dave-the-viber`** (file `~/.t3/userdata/themes/dave-the-viber.json`).
Renamed from Pixel Sushi Rail (themeId, folder and repo `pixel-sushi-rail`) on 2026-11-17.
Fallbacks kept untouched: `pixel-sushi` (v1) and Roger's `status-edge` ("Minimalist color edges").
Folder: `/Users/roger/.t3/projects/dave-the-viber/` (call it `$D`). T3 Code project "Dave the Viber" (id `mcp:58b738ca-6192-4af5-a039-e107ef713625`) with scripts "Build + validate" and "Static server :8765". The old scratch path and `~/.t3/projects/pixel-sushi-rail` are symlinks to this folder.

## State
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
  `demo/menus/bar.png`. Not checked: narrow windows (Dave goes behind the pad), right panel open, desktop app.
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
- Unapplied size items (if room is needed): bubble left/top in the shared rule + collapsed-hide var (~−520),
  inline single-use hex vars (−153 full / −90 lite measured, var scope risk), dead rules list, raw `<>` in data URIs
  (~−500, risky). Rejected with numbers: reordering rules to nest more (−418/−159, cascade risk), one merged
  `border-radius:0!important` rule (+753), `[class*=status-slot]` (matches `group-hover/...` utilities).
- The Mac mini dev server is still running; stop it (`kill $(cat /tmp/t3code-theme-dev.pid)`) and remove the
  worktree (`git -C /Users/roger/t3code worktree remove /tmp/t3code-theme-demo`) when no longer needed — ask Roger.
- History: `LEDGER.md` (hillclimb ledger), `council2/BRIEF-R*.md` (council briefs), `v1/` (first theme sources).


## Context controls on the counter (2026-11-17)
- Context strips are absolute below the pad, so they no longer lift the paper off the plank. Controls use dark ink
  on the chat counter's lighter wood front (#b9783d), with opaque icons, a light hover and an ink focus outline.
- Build + both gallery validators pass; lite unchanged; ink/front contrast 5.31:1. No visual check or local install
  in this task yet. Shared Dave-art and aquarium-selector edits belong to another thread and are preserved.
