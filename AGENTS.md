# Dave the Viber — agent guide

T3 Code theme: a night sushi bar in pixel art (Dave-the-Diver sushi mood, original art only).
Sidebar threads are kitchen order slips hung on a left rail with pegs; settled threads are spiked on a
spindle; the project header is a noren with a restaurant sign. One look in OS light and dark mode.

Owner: Roger (CTO, Tres65). Answer in Catalan, short sentences, result first.
`HANDOFF.md` has the latest state and numbers; read it first. This file has the durable rules.

## Hard rules
- Never publish to any gallery (t3skins.dev, t3themes.com) without asking Roger.
- Never commit or push screenshots, captures or videos to GitHub (Roger, 2026-11-17). Keep them local; `.gitignore`
  blocks images except `src2/sprites/*.png`, `out2/sprites/*.webp` and `out2/local/*.webp` (the sprite atlas). Never `git add -f` an image.
- `private/` holds secrets (the t3skins.dev manage link). It is ignored only by this clone's `.git/info/exclude`:
  never commit, push, copy or quote its contents.
- Never modify `~/.t3/userdata/themes/status-edge.json` or `pixel-sushi.json` (fallbacks).
- Never touch `/Users/roger/t3code` (main checkout) or the Mac mini's `~/.t3/userdata`, except its
  `themes/dave-the-viber.json` and, until it replaces it, `themes/pixel-sushi-rail.json` (installed and active there at Roger's request, 2026-11-17).
  The skin was called Pixel Sushi Rail (themeId, folder and repo `pixel-sushi-rail`) until 2026-11-17.
  Never point a dev server at live userdata.
- Size limits: full ≤ 50,000 chars (galleries), lite ≤ 20,000 chars, local ≤ 100,000 chars (the app's limit since
  2026-11-18), all checked by the build; the validator checks full and lite.
- CSS limits: no `@import`, `image-set()`, `src()`; `url()` only `data:` or `#id`; no `:has()` inside `:has()`.

## Files
| Path | Purpose |
| --- | --- |
| `src2/core.css` | Shared rules. Spans `/*full*/ … /*/full*/` are full-only (may sit inside rules or selector lists). |
| `src2/extras.css` | Full-edition-only rules. |
| `src2/sprites/*.png` | Sprite art, the source: 1 px per pixel, edit in Aseprite. Masks are black on transparent; colour sprites use exactly the colours of their palette. |
| `src2/sprites2.py`, `tools/sprites.py` | Palettes and tokens; `png()` reads the art (needs Pillow), `webp()` encodes lossless WebP → `{{token}}` data URIs. |
| `src2/colors.json` | Colour roles (same for `variants.light`). |
| `tools/build2.py` | Build + minify → `out2/full.{json,css}`, `out2/lite.{json,css}`, `out2/local.css` + `out2/local/dave-the-viber.{json,webp}` (copy-ready pair), and `out2/sprites/*.webp` (the exact sprites the full CSS uses). |
| `tools/t3skins-validate.js` | Gallery validator. |
| `tools/serve.py` | CORS static server on :8765 for the injector. |
| `fx/inject2.js`, `fx/check.js`, `fx/scan.js` | Live injection and in-page checks. |
| `fx/prune2.js` | Per-flag `!important` test: `f(flatCssUrl, [k…])` → ok / needed per flag (paired, synchronous, drift-proof). `fx/prune.js` (older, group bisection) drifts while other threads re-render the sidebar. |
| `fx/bubwatch.js` | Desktop-console watchdog: logs each attention bubble that stops answering a hit test, with the row's state. |
| `fx/cmp.js` | Computed-style A/B/A of two builds on the current page state: `f(urlA, urlB)` → diff, drift. |
| `tools/atlascheck.py`, `tools/localcheck.py` | Local edition: every sprite use as full and as local on one page, to screenshot and diff; json/webp stamp check. |
| `tools/pixcheck.py` | Pixel-sampled contrast from a screenshot + boxes JSON. |
| `tools/atlascheck.py` | Local edition judge: `page <dir>` writes `h.html` + `atlas.webp` (each sprite use as full, class `a`, and as local, class `b`); `diff a.png b.png` counts differing pixels. |
| `final2/` | Last published JSON/CSS + reference captures. |
| `demo/` | `video.mp4` of all dev demo states, PNGs, `verify/`. |
| `LEDGER.md`, `council2/`, `v1/` | History: hillclimb ledger, council briefs, v1 sources. |

## Build, validate, publish
1. Build: `python3 -I tools/build2.py "$PWD"` (project script "Build + validate" also runs the validator on both editions).
   The build is deterministic. It refuses unbalanced braces and nested `:has()`, and asserts sprite pixel coverage.
   The minifier nests consecutive rules that share a selector prefix (`NEST` in `build2.py`, per edition; False = flat).
   It refuses nested output that does not expand to the flat CSS, and any edition over its size limit.
2. Test (next section) before publishing.
3. Publish locally: copy both files of `out2/local/` to `~/.t3/userdata/themes/` (they already carry the themeId
   names), then call `t3_theme_set` with `themeId: "dave-the-viber"` and no
   payload. Verify both server files equal the build, and `python3 -I tools/localcheck.py ~/.t3/userdata/themes`
   (the local CSS ends with `/*atlas <sha>*/` of its image: a .json and .webp from different builds cut wrong sprites). Galleries get `out2/full.json` (no image file travels).
   The local edition is full with most sprites taken from that image (`ATLAS_PLAN` in `src2/sprites2.py`; the build
   rewrites their layers, see `relayer` in `tools/build2.py`); its pixels must equal full's.

## Testing
1. Start `python3 -I tools/serve.py "$PWD"` in the background (project script "Static server :8765").
2. Open the live app in T3's built-in browser (`preview_open`, `open:false`, `reuseExistingTab:false`) and inject
   without publishing:
   `const f=eval(await (await fetch('http://127.0.0.1:8765/fx/inject2.js?'+Date.now())).text()); await f('full')`
3. Eval `fx/check.js`: written rules == parsed rules, 0 invalid, 3-line rows, contrast, hover buttons never over status.
4. Eval `fx/scan.js` for page text contrast. It cannot see gradients: for wall/lamp/wood text use
   `python3 -I tools/pixcheck.py <shot.png> boxes.json`.
5. `preview_set_appearance light` and `dark`: the look must be identical.
6. Refactors: freeze motion
   (`*,*::before,*::after,html::after,body::after{animation:none!important;transition:none!important}`),
   screenshot before/after, PIL pixel diff must be 0. Exception (Roger, 2026-11-17): Chromium dithers every
   `linear-gradient`, even one colour, so the bubble inks may differ by ±1/255 per channel.
7. Question UI: spawn a Haiku child that calls AskUserQuestion (single + multi select), open its thread,
   inject, inspect `[data-composer-banner-surface]`, then `task_cancel` it. Ask Roger not to answer it.
8. All status states: Mac mini dev demo (see `HANDOFF.md` → "Mac mini dev demo"): `ssh rogerflix`, worktree
   `/tmp/t3code-theme-demo`, dev home `/tmp/t3code-dev`, `http://localhost:7508`. Drive its built-in browser with
   a Luna relay (`delegate_task` with the Mac mini `environmentId` and its `t3code` project).
9. Desktop app checks: Luna relay per the `checking-interfaces` skill (bundle id `com.t3tools.t3code`).

## Owner design contracts
- Row: line 1 title alone; line 2 project + status; line 3 branch + model; no wrapping.
  Hover buttons never cover the status. Exception: tickets that call for attention show a bubble beside the ticket.
- Hover only straightens a ticket; no lift. Rail and peg never move.
- Settled slips: inverted z-order (`sibling-index()`), small bottom edge, spiked and aligned on the spindle.
- Done label reads "Dish!" with the hot-dish icon; Working shows a steaming saucepan. Both stamps are static
  (Roger, 2026-11-17: no dish or pot animation).
- Round radios and square checkboxes in questions keep their shape.
- The thread detail popover may cover the bubbles. The sign may cover the first line.
- Text ≥ 4.5:1, icons ≥ 3:1 at Appearance contrast 165; status distinguishable without colour;
  `prefers-reduced-motion` respected; visible keyboard focus.

## Pitfalls (each cost a broken build or a wasted round)
- `!important` is needed only against inline styles, unlayered app rules, app animations and other theme rules:
  app utilities are in `@layer`s and lose to any unlayered theme declaration. Before adding or removing a flag read
  `HANDOFF.md` → "`!important` pruning". Keep it on properties that JS or `animate-*` sets (opacity, transform, size,
  position, display, transition, animation).
- The first screenshot after switching edition (lite ↔ full) misses late-painted content. Inject the same edition
  twice, wait ~3 s, then compare.
- `{{token}}` contains `}}`. Never slice a rule with `index("}")`; edit by exact string replacement.
- The published theme drops a `content` value with a backslash escape (`"A\A B"`), though injection shows it. Verify
  `content` changes in the published theme; break lines with `width: min-content` instead.
- The minifier drops the space before a `{{token}}` (`#18243c {{x}}` becomes `#18243curl(`, invalid). Put the token first.
- Each attention ticket's bubble is its own row's `::before` (`position: fixed` + `position-anchor: auto`); every
  ticket row paints its twine as its background (`--sk-tw`), so `::before` is free. It works only while the row (`li`) has no transform, filter or containment
  (`content-visibility: visible`): any of those makes the row the containing block and the scroller clips the bubble.
  The paper (row card) is rotated, so nothing inside it can host a bubble. A named anchor on the row itself fails;
  `auto` works. Page-level hosts with `nth-child(-n+3 of …)` capped the count (removed 2026-11-19).
- Keep an anchored bubble's `top`/`left` linear in `anchor()` (no `max()`/`min()`/`clamp()`): Chromium can keep the
  layout from when the row was off-screen and add later scrolling at paint time, so a clamped value lands off-screen
  (a row moved by the app's translateY while off-screen lost its bubble until the next layout). Computed `left`/`top`
  read in JS are that stale layout, not the painted place: hit-test at the row instead (`fx/bubwatch.js`).
- An attention row must never get a transform: the app slides moved rows with a WAAPI transform (150 ms), which
  makes the row the bubble's containing block; after it Chromium kept the bubble on the peg or off-screen until a
  later layout. Attention rows carry `transform: none !important` (not while dnd-kit drags: `[style*="transform:"]`;
  every sortable row has `transition: transform` inline) and `anchor(right, -300px)` hides the bubble meanwhile.
- `fx/prune2.js` "ok" covers only the elements on the page. Before dropping a flag, also list the app's unlayered
  rules on that property (`document.styleSheets`, outside `@layer`): one with higher specificity (e.g.
  `.chat-markdown a:not(.chat-markdown-file-link, …)`) wins in states the page does not show.
- Rows use `content-visibility: auto`: a screenshot may show an empty sidebar. Retake it.
- Background preview tabs: an `evaluate` that passes 15 s closes the tab, and `setTimeout` is throttled. Keep each
  evaluate under ~5 s; for long in-page loops yield with a `MessageChannel` kept on `window` and poll.
- Other threads often edit `src2/` and rebuild at the same time. Before a before/after check, copy `src2/` + `tools/`
  to a scratch root and build both versions there (`build2.py <root>` writes `<root>/out2`).
- One look in both OS modes depends on `:root{--lightningcss-light: ;--lightningcss-dark: initial}`, the
  `--contrast-*` tokens and `body{color:var(--contrast-foreground)}`. App `dark:` utilities (provider marks,
  radios) need explicit overrides.
- Search results sit inside `li[role=presentation]`: use descendant selectors.
- The ticket's torn edge is painted, not masked: the card `::after` fills the gaps with #112339 (the shaded wall,
  sampled on screen). If the wall art or `--sk-shade` changes, sample the gap colour again.
- Projects with a favicon render a direct `img`; projects without an icon need the fallback sign.
- Pairing the Mac mini dev server through an SSH tunnel does not work; use a relay on the Mac mini.
- Theme image sprites (local edition): the image is a column atlas, one sprite per row band at x = 0 with empty rows
  between, strips tiled across its whole width. A layer shows one sprite because its box clips the rest, so a sprite
  needs empty rows for the tallest box that uses it (`GAP`, at the sprite's scale), and a sprite in a box as tall as
  the window goes last (night). The build writes the layers (`relayer`): a new `{{token}} <position> / <size>` layer
  moves by adding the token to `ATLAS_PLAN`. Pixels equal the data: URI only when the layer's y offset is a whole
  number of device pixels: Chromium snaps a positive offset (a single image) but not a negative one (the atlas).
  x is always safe (sprites sit at x = 0), and so is the sprite at the image's origin (drinks). That keeps the status
  atlas and approval (1.5x in the bubble) as data: URIs; `repeat` in a window-high box (wall, seigaiha) and
  `repeat-y` (bubbles) stay too. Nothing paints until the app loads the image. Save it as lossless WebP: PNG rounds
  semi-transparent pixels 1/255 differently. Test with `f('local')` (it sets the variable from `out2/local/dave-the-viber.webp`) and
  `python3 -I tools/atlascheck.py page <dir>`: every use as full and as local on one page, to screenshot and diff.
- The minifier deletes `-webkit-mask*` declarations (the app has unprefixed `mask`), except `-webkit-mask-box-image`,
  which has no unprefixed form in Chromium.

## Open items
See `HANDOFF.md` → "Open items" (unverified Stop/separator selectors, remaining size cuts, Mac mini dev
server cleanup, which needs Roger's approval).
