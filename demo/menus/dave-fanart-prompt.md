# Dave fan-art sprite

Built-in `image_gen` edit, 2026-11-17. Reference research: Luna Low. The drawing is new fan-art; no game sprite was extracted.

Reference: [official Digital Extra character sheet](https://store.steampowered.com/app/2492320/DAVE_THE_DIVER_Digital_Extra/), SUSHI BAR box. [Direct image](https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/2492320/ss_cd225abae4ce17e3665a96bae547e5698247077e.1920x1080.jpg).

Final asset: `src2/sprites/dave.png`, 56x60, 17 opaque colours and binary alpha. Display size stays 56x60. At 28x30, downsampling lost the eyes and fish. The final conversion trims the generated margin, samples to fit 52x56 with ImageMagick `sample:offset=75x25`, centres on a transparent 56x60 canvas, thresholds alpha at 50%, and quantises without dithering, first to 24 and then 20 colours. Seventeen opaque colours remain. The sampling offset preserves the eyes at native size. The source PNG's exact palette is `DAVE_P`.

Roger's final correction retains the original broad goatee, repairs its uneven side and makes the hair black. Preview: `demo/menus/dave-fanart.png`, enlarged 8x with nearest-neighbour sampling.

## Generation prompt

Use case: precise-object-edit.
Asset type: tiny pixel-art game sprite for a night sushi bar interface.
Image 1 is the edit target, our existing 28 by 30 pixel cook behind a laptop. Image 2 is an official Dave the Diver character sheet used ONLY as reference. The SUSHI BAR box in its lower left is the character identity and restaurant outfit to draw anew.
Replace the man in Image 1 with clearly recognizable fan-art of Dave from Dave the Diver in his SUSHI BAR outfit: very stocky round shoulders and belly, broad rounded warm-skinned face, short dark goatee and moustache, short grey side hair, light straw pork pie hat with dark band and a short flat brim, pale muted sea-blue short-sleeve open-collar shirt and a small magenta undershirt triangle. He is programming, head inclined slightly toward the laptop, both hands just above its keyboard. Remove the existing white/pink headband and dark happi completely.
Keep the existing front-facing silver-grey laptop in the lower foreground with its tiny luminous cyan fish silhouette, a clear fish body with triangular tail. It hides the lower belly. The laptop must not hide the face.
Composition: centered, near-frontal man from head to lower torso behind laptop. Whole sprite fits a 28-column by 30-row logical pixel canvas, the same proportions and outer bounding box as Image 1, hat at top, laptop at bottom. Every logical pixel should be one solid flat square; render this coarse 28x30 artwork at 32x nearest-neighbor enlargement, approximately 896x960 output. No internal details smaller than one logical pixel. IMPORTANT: very coarse genuinely tiny retro game sprite, not detailed pixel illustration.
Style: crisp axis-aligned pixels, no antialiasing, limited 16-color palette, dark brown/navy outlines, warm skin highlights, sea-blue shirt, straw cream hat, grey laptop, icy cyan fish. Transparent background and transparent outer margin, NO checkerboard, NO environment, NO text, NO ground, NO shadow, no extra props. Draw just this one sprite.

## Final correction prompt

Make a minimal correction to this exact original Dave sprite. Preserve the ORIGINAL beard/goatee shape shown in this image: the same broad, long U-shaped rounded goatee surrounding the mouth, same lower chin, same overall size and placement. Do NOT replace it with a small circular ring beard, do NOT shorten it or move it up.
Correct only the uneven outer side of the original goatee: its right-side contour should be tidy and consistent with the left-side contour while keeping this original broad silhouette and the original mouth opening. This is just a one-side contour repair, not a beard redesign.
Make the short hair at his temples and sides of his head black instead of grey, using #181b22 with a restrained charcoal highlight. Keep the goatee dark, with the original broad shape.
Everything else must stay visually identical: original face proportions, eyes, warm skin, straw hat, pale blue shirt, hands, silver laptop with cyan fish, pose, silhouette, transparent margins. Do not regenerate or restyle the body or laptop. Keep coarse crisp axis-aligned pixel art and true transparent background. No new objects or text.
