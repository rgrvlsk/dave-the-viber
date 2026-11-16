# Footer proposal (Opus)

## 1. Diagnosis (live page, 255 px sidebar, CSS px)
- Footer box 70 px high: padding 30/8/8. Plank (16 px sprite) is drawn at 16..32, flat #8f5a2b below.
- Buttons sit at 30..62: they overlap the plank's bottom edge by 2 px, so they look jammed under the counter.
  Below them only 8 px of brown, but the front reads as an empty slab because nothing marks the plank's edge.
- Buttons reuse the wall "glazed tile" (blue #24466a). On the wooden front they look like wall tiles that fell off.
- The desktop update button (`li.ml-auto > button.rounded-full.size-8`) keeps the app's round grey style.
- The composer counter (`[data-chat-composer-form]::after`) is a separate counter under the pad; it does not need to align. Unchanged.

## 2. Design
The footer buttons are menu tags hung on the counter front. They use the same recipe as the ticket hover keys:
1 px ink outline, 1-px clipped corners, lit top, shaded bottom, ink glyph. Their colour is slip paper (#fbf3e2), the same as the tickets.
The update button is the same key in gold (#f2c25c), so it calls for attention without a colour of its own.
Layout: wall strip 0..14 (koi at top 0), plank 14..30, a 2 px #6e4220 shadow line under the plank lip, then 6 px gap,
32 px keys, 6 px bottom. Footer is 74 px (+4 px). Gap between keys: 6 px.
States: hover/expanded = warm lamp glow (#ffdf9e cream, #ffe08f gold); pressed = light moves to the bottom and the glyph drops 1 px;
focus-visible = 2 px ink outline inset 5 px.

## 3. CSS (replaces extras.css from "/* The sidebar ends on the wooden counter" up to "/* The pad rests on the counter")
```css
/* The sidebar ends on the wooden counter; a koi swims on the wall strip above it.
   Wall strip 0..14 px, plank 14..30 px, front panel below; the keys hang on the front with 6 px above and below. */
@keyframes sk-swim {
  from { left: -26px; }
  to { left: 100%; }
}
[data-slot="sidebar-footer"] {
  position: relative;
  padding: 36px 8px 6px !important;
  background: var(--sk-wood) left 0 top 14px / 64px 16px repeat-x, linear-gradient(transparent 30px, #6e4220 30px 32px, #8f5a2b 32px) !important;
  image-rendering: pixelated;
  overflow: hidden;
}
[data-slot="sidebar-footer"] > * {
  position: relative;
  z-index: 1;
}
[data-slot="sidebar-footer"] > ul {
  gap: 6px !important;
}
[data-slot="sidebar-footer"] :is(button, a, [data-slot="button"]),
[data-slot="sidebar-footer"] svg {
  color: #fff3dc !important;
  opacity: 1 !important;
}
/* Footer keys are menu tags hung on the counter front: the ticket keys' recipe (1 px ink outline, clipped corners,
   lit top, shaded bottom) in slip paper with an ink glyph. Lamp-lit on hover; pressed, the light moves down.
   The desktop update button is the same key in gold, so it calls for attention. */
[data-slot="sidebar-inner"] [data-slot="sidebar-footer"] li > button:is([data-size="icon"], .size-8):has(> svg) {
  --sk-c: #fbf3e2;
  --sk-h: #ffdf9e;
  width: 32px !important;
  height: 32px !important;
  border-radius: 0 !important;
  color: #241b15 !important;
  background: var(--sk-c) !important;
  box-shadow: inset 0 0 0 1px #241b15, inset 0 -3px #0003, inset 0 2px #fff9;
  clip-path: polygon(0 1px, 1px 1px, 1px 0, calc(100% - 1px) 0, calc(100% - 1px) 1px, 100% 1px, 100% calc(100% - 1px), calc(100% - 1px) calc(100% - 1px), calc(100% - 1px) 100%, 1px 100%, 1px calc(100% - 1px), 0 calc(100% - 1px));
}
[data-slot="sidebar-inner"] [data-slot="sidebar-footer"] li.ml-auto > button:is([data-size="icon"], .size-8):has(> svg) {
  --sk-c: #f2c25c;
  --sk-h: #ffe08f;
}
[data-slot="sidebar-inner"] [data-slot="sidebar-footer"] li > button:is([data-size="icon"], .size-8):is(:hover, [aria-expanded="true"]):has(> svg) {
  background: var(--sk-h) !important;
}
[data-slot="sidebar-inner"] [data-slot="sidebar-footer"] li > button:is([data-size="icon"], .size-8):active:has(> svg) {
  box-shadow: inset 0 0 0 1px #241b15, inset 0 2px #0003;
}
[data-slot="sidebar-inner"] [data-slot="sidebar-footer"] li > button:is([data-size="icon"], .size-8):focus-visible:has(> svg) {
  outline: 2px solid #241b15;
  outline-offset: -5px;
}
[data-slot="sidebar-inner"] [data-slot="sidebar-footer"] li > button:is([data-size="icon"], .size-8) > svg {
  color: #241b15 !important;
  stroke-width: 2.25;
  filter: none;
}
[data-slot="sidebar-inner"] [data-slot="sidebar-footer"] li > button:is([data-size="icon"], .size-8):active > svg {
  translate: 0 1px;
}

[data-slot="sidebar-footer"]::before {
  content: "";
  position: absolute;
  top: 0;
  width: 24px;
  height: 14px;
  background: var(--sk-fish) center / 24px 14px no-repeat;
  opacity: 0.9;
  animation: sk-swim 40s linear infinite;
  pointer-events: none;
}
```
The reduced-motion rule for the koi stays where it is.

## 4. Evidence
Folder: /private/tmp/claude-501/-Users-roger--t3-projects-pixel-sushi-rail/e5e0f080-420b-48f5-9a03-80d224516c2d/scratchpad/opus/
- Before: `before-dark-255.png`. After, idle: `after-idle-dark.png`, `after-idle-light.png`. Pixel diff light vs dark in the footer = 0 (only x 510-512, outside the sidebar).
- States (Pull requests + Update hover via aria-expanded, Usage focus-visible): `after-states-dark.png`, `after-states-light.png`.
- Wide 340 px sidebar: `after-wide340-dark.png` (update key moves right, still in the front band).
- Contrast: ink glyph on cream 15.3:1, on cream hover 13.1:1, on gold 10.2:1, on gold hover 13.1:1. Cream key vs front 5.2:1, gold key vs front 3.5:1.
- Size: real build in a throwaway copy (`proj/`): full CSS 40,040 -> 41,078 (+1,038 chars), full.json 45,332 chars. Validator ok. Lite unchanged (16,540).

## 5. Risks / not tested
- `:active` is only checked by rule reading, not by screenshot.
- Desktop app not tested; update button was faked (CircleArrowUp). The progress-ring and badge variants are not tested. If the ring is not a direct `svg` child, `:has(> svg)` will not match and that state keeps the app style.
- Collapsed (icon) sidebar and the optional footer items (provider pill, architecture warning, undo notice) are not tested. The key rule only matches `li > button` with `data-size=icon` or `.size-8`, so text pills stay unchanged.
- The cream keys are the brightest thing in the footer. If they compete with the tickets, use aged paper (#d9c9a3); ink contrast stays above 10:1.
