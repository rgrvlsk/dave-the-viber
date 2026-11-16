# Pixel Sushi Rail — agent guide

T3 Code theme: a night sushi bar in pixel art (Dave-the-Diver sushi mood, original art only).
Sidebar threads are kitchen order slips hung on a left rail with pegs; settled threads are spiked on a
spindle; the project header is a noren with a restaurant sign. One look in OS light and dark mode.

Owner: Roger (CTO, Tres65). Answer in Catalan, short sentences, result first.
`HANDOFF.md` has the latest state and numbers; read it first. This file has the durable rules.

## Hard rules
- Never publish to any gallery (t3skins.dev, t3themes.com) without asking Roger.
- Never modify `~/.t3/userdata/themes/status-edge.json` or `pixel-sushi.json` (fallbacks).
- Never touch `/Users/roger/t3code` (main checkout) or the Mac mini's `~/.t3/userdata`, except its
  `themes/pixel-sushi-rail.json` (installed and active there at Roger's request, 2026-11-17).
  Never point a dev server at live userdata.
- Size limits: full ≤ 50,000 chars, lite ≤ 20,000 chars (checked by the build + validator).
- CSS limits: no `@import`, `image-set()`, `src()`; `url()` only `data:` or `#id`; no `:has()` inside `:has()`.

## Files
| Path | Purpose |
| --- | --- |
| `src2/core.css` | Shared rules. Spans `/*full*/ … /*/full*/` are full-only (may sit inside rules or selector lists). |
| `src2/extras.css` | Full-edition-only rules. |
| `src2/sprites/*.png` | Sprite art, the source: 1 px per pixel, edit in Aseprite. Masks are black on transparent; colour sprites use exactly the colours of their palette. |
| `src2/sprites2.py`, `tools/sprites.py` | Palettes and tokens; `png()` reads the art (needs Pillow), `webp()` encodes lossless WebP → `{{token}}` data URIs. |
| `src2/colors.json` | Colour roles (same for `variants.light`). |
| `tools/build2.py` | Build + minify → `out2/full.{json,css}`, `out2/lite.{json,css}`, and `out2/sprites/*.webp` (the exact sprites the full CSS uses). |
| `tools/t3skins-validate.js` | Gallery validator. |
| `tools/serve.py` | CORS static server on :8765 for the injector. |
| `fx/inject2.js`, `fx/check.js`, `fx/scan.js` | Live injection and in-page checks. |
| `tools/pixcheck.py` | Pixel-sampled contrast from a screenshot + boxes JSON. |
| `final2/` | Last published JSON/CSS + reference captures. |
| `demo/` | `video.mp4` of all dev demo states, PNGs, `verify/`. |
| `LEDGER.md`, `council2/`, `v1/` | History: hillclimb ledger, council briefs, v1 sources. |

## Build, validate, publish
1. Build: `python3 -I tools/build2.py "$PWD"` (project script "Build + validate" also runs the validator on both editions).
   The build is deterministic. It refuses unbalanced braces and nested `:has()`, and asserts sprite pixel coverage.
   The minifier nests consecutive rules that share a selector prefix (`NEST` in `build2.py`, per edition; False = flat).
   It refuses nested output that does not expand to the flat CSS, and any edition over its size limit.
2. Test (next section) before publishing.
3. Publish locally: copy `out2/full.json` to `~/.t3/userdata/themes/pixel-sushi-rail.json`, then call
   `t3_theme_set` with `themeId: "pixel-sushi-rail"` and no payload. Verify the server file equals the build.

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
   screenshot before/after, PIL pixel diff must be 0.
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
- Done label reads "Dish!" with the hot-dish icon; Working shows a pot whose lid dances and steam rises.
- Round radios and square checkboxes in questions keep their shape.
- The thread detail popover may cover the bubbles. The sign may cover the first line.
- Text ≥ 4.5:1, icons ≥ 3:1 at Appearance contrast 165; status distinguishable without colour;
  `prefers-reduced-motion` respected; visible keyboard focus.

## Pitfalls (each cost a broken build or a wasted round)
- `{{token}}` contains `}}`. Never slice a rule with `index("}")`; edit by exact string replacement.
- Bubbles use anchor positioning. Anchors must come before their hosts in tree order (`html::before` fails;
  hosts are `html::after`, `body::after`, `[data-workspace-area=conversation]::before/::after`).
  Fixed elements inside the sidebar are clipped by the scroller mask, so bubbles live outside it.
  Anchored slips need `content-visibility: visible` or they stop painting.
- Rows use `content-visibility: auto`: a screenshot may show an empty sidebar. Retake it.
- Background preview tabs: an `evaluate` that passes 15 s closes the tab, and `setTimeout` is throttled. Keep each
  evaluate under ~5 s; for long in-page loops yield with a `MessageChannel` kept on `window` and poll.
- Other threads often edit `src2/` and rebuild at the same time. Before a before/after check, copy `src2/` + `tools/`
  to a scratch root and build both versions there (`build2.py <root>` writes `<root>/out2`).
- One look in both OS modes depends on `:root{--lightningcss-light: ;--lightningcss-dark: initial}`, the
  `--contrast-*` tokens and `body{color:var(--contrast-foreground)}`. App `dark:` utilities (provider marks,
  radios) need explicit overrides.
- Search results sit inside `li[role=presentation]`: use descendant selectors.
- Projects with a favicon render a direct `img`; projects without an icon need the fallback sign.
- Pairing the Mac mini dev server through an SSH tunnel does not work; use a relay on the Mac mini.

## Open items
See `HANDOFF.md` → "Open items" (unverified Stop/separator selectors, remaining size cuts, Mac mini dev
server cleanup, which needs Roger's approval).
