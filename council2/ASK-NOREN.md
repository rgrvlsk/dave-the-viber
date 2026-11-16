# Question for Fable: how would you build the project-coloured noren?

Read-only. Edit nothing, start no agents. Answer in under 450 words.

## The owner's request (Catalan, verbatim)
"Els Noren podrien tenir el color general de la icona del projecte actiu i tenir la icona pixelada (amb un shader?)"
Then: "No sé si aquest approach és el millor. Pregunta-li a Fable com ho faria, basant-nos en el teu disseny original
dels peixos."
= The noren (curtain under the chat header) should take the general colour of the active project's icon and show that
icon pixelated. Base it on the original fish noren design.

## The original fish noren (the base to build on)
- `[data-chat-header]::after`, 36 px tall, under the header; the header reserves the space (margin-bottom: 36px).
- Pixel-art SVG data URI tile 40x18 at 2x (80x36), repeat-x: wooden rod on top, indigo cloth panels (#2a3f73) with
  2-px slits, a cream pixel fish crest per panel, a darker hem band and a scalloped bottom edge.
- Picture: council2/r3-app-light.png (top of the chat area).

## What I tried (picture: council2/noren-dye-attempt.png)
1. Dye: the breadcrumb's project-icon element (`[data-chat-header] nav li:first-child > button > span:first-child`,
   14 px; an emoji span, an <img> favicon, or an SVG monogram depending on the project) moved with position:absolute
   into the noren strip, `scale: 110 3` + `filter: blur(1.5px) saturate(1.8) brightness(1.5)`, under a translucent
   cloth tile. Result: a muddy streaky band; the fish crests are gone; the breadcrumb loses its icon.
2. Crest: the active sidebar ticket's project icon set to position:fixed (top 62px, right 72px, scale 2.25, a 2-px
   pixel-grid mask). It computes to the right place but does not appear (still debugging; its row has no transform,
   filter, mask or content-visibility now).

## Hard CSS facts here
- Theme CSS only (an adopted stylesheet). No JS, no @import, url() only data: or #id (no SVG filter can be
  referenced: no element with an id exists to point at), no external fonts, ≤ 50,000 chars (now ~48,000; lite edition
  ≤ 20,000 does not include the chat). Chromium 152 (anchor positioning, anchor-scope, :has, nth-child(of S), CSS
  nesting, mask-composite, backdrop-filter all available).
- CSS cannot read an image's colours or duplicate an element's rendering (no element()). attr() cannot yield url().
- Two elements show the active project's icon: the header breadcrumb icon (after the sidebar in DOM order) and the
  active sidebar ticket's icon (before it). Anchoring needs the anchor earlier in tree order than the positioned box,
  so the sidebar icon cannot anchor to the header.
- Real pixelation of an emoji/SVG/favicon is not available (no shader); a mask grid or image-rendering: pixelated on
  raster favicons are the only approximations.
- Rows already use the project icon as a big faint pixelated watermark (scale 4, opacity .17, multiply).

## What I want from you
Your recommended approach (one, ranked against at most two alternatives), concrete enough to implement: which
element supplies colour and which supplies the crest, the key CSS properties, what happens for emoji vs favicon vs
monogram projects and for "No project", and what you would drop if the honest answer is "CSS can't do this well".
Say plainly if you think the fish noren should stay as it was and the project colour should live somewhere else.
