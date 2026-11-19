# Resource cost: skin d292df3 vs no skin (2026-11-18)

## Result
- The skin costs **+68% CPU** over the whole stress test (50.8 s vs 30.3 s, +20.5 s [18.5, 23.3]) and
  **1.83× the macOS energy impact** (51 vs 28). Renderer and GPU both grow ~1.7×; the browser process does not change.
- **Idle with the window visible is the largest cost:** 50% of a core against 21% (+29 points [23, 32]), 60 frames/s
  against 16. The cause is the 5 infinite animations (`sk-float` sign, `sk-sway` kelp, `sk-swim` koi,
  `sk-rise` bubbles, `sk-screen`). Diagnostic: the same skin without those 5 `@keyframes` idles at 22–24%,
  the same as no skin (239–240 frames vs 238–240).
- **Hidden window:** 6% vs 4% of a core (+3 points [1, 5]). Small, but not zero.
- **Interaction:** +15% to +70% CPU per scenario. Frame p95 does not change in scroll, wheel or hover (~18 ms).
  It gets worse in status changes (50 vs 33 ms), sidebar toggles and resizes (33 vs 18 ms), and appearance switches (167 vs 102 ms).
  The skin drops more frames per run (402 vs 285).
- **Memory:** renderer + GPU start equal (~1.17 GB). Under status changes the skin adds +300 to +450 MB. After 2–3
  rounds of status changes the growth stops (6 rounds: 1.30 → 1.44 GB, then flat), so it is **not a leak**.
  With the animations the memory **is not given back** in idle (1.35 GB at the end, against 0.88 GB without the skin).
  Without the animations it returns to 0.85 GB within ~12 s. Inference: the animations keep the renderer from going
  idle, so Blink does not run its idle memory purge. JS heap is the same (≈ +6 MB at the end).

## Method
- Driver `src/timeline.js` (based on `/Users/roger/t3code/.css-perf` bench.js/page.js, read-only), Electron 44.10.1
  (the same Chromium as T3 Code Nightly), dev server `:7508`, 1440×900 window, DPR 2, the most-used thread open.
- One fresh Electron process per run. 10 runs in ABBA order (none, full, full, none, …): 5 with the skin, 5 without.
  "None" = the theme sheet empty (the app keeps the theme colour roles). "Full" = the installed
  `dave-the-viber.json` CSS (sha256 a2cc87f5…, equal to `out2/full.css` of d292df3), `variants/full-d292df3.css`.
- The stress test, the same in every run: idle 20 s → hidden 10 s → scrollTop sweep @200 tickets → wheel @200 →
  wheel @500 → hover sweep → status churn (600 changes) → synthetic stream 8 s → sidebar ×5 → resize → appearance ×10
  → idle 15 s. 50 tickets unless noted.
- Sampling, the whole run: Electron `getAppMetrics` every 250 ms (CPU % per process, working set, idle wakeups,
  system CPU); CDP `Performance.getMetrics` every 500 ms (JS heap, nodes, style/layout time); macOS `top` every 1 s
  (CPU, energy impact, physical memory per process). Per phase: CPU time per process, light trace (frames
  drawn/dropped, busy time per thread, stage time), rAF frame intervals for interactive phases.
- Statistics: medians of 5; the difference is the median of the 5 adjacent pairs (skin − none) with a 95% bootstrap CI.
- Memory diagnostic (`./run-memory.sh`, `PLAN=memory`): idle 15 s → 6 status churns → idle 20 s; none / full /
  full without the 5 `@keyframes` (`variants/full-noanim-d292df3.css`), 2 runs each, order ABCCBA.

## Limits
- Background noise: Time Machine (`backupd`) and the T3 Code Nightly app ran during the test (`system.log`).
  The ABBA order spreads it over both variants; the CIs include it.
- "Energy impact" is Activity Monitor's estimate, not watts (`powermetrics` needs sudo).
- The memory diagnostic has 2 runs per variant: enough for a 450 MB effect, not for small effects.
- Dev server build (React dev mode). CSS cost does not depend on it; absolute JS numbers would be lower in production.

## Files
- `data/stress-d292df3/samples.jsonl`: every sample of the 10 runs (`kind`: `s`, `cdp`, `top`, `phase`, `meta`, `end`).
- `data/stress-d292df3/REPORT-data.md`, `summary.json`: all metrics per phase and per run. `report.html`: every run as a line.
- `data/memory-d292df3/samples.jsonl`: the memory diagnostic.
- Rerun: `src/pair.js` once (pairing token from `node … src/bin.ts pair --base-dir /tmp/t3code-dev`), then
  `./run.sh data/<dir>`, `python3 -I src/analyze.py data/<dir>`, `python3 -I src/report.py data/<dir>`.

# Hover animations while the list scrolls (2026-11-18)

## Result
- **Chromium updates `:hover` every frame while the list scrolls under a still pointer.** With the skin, 150–500
  row transitions start per scroll phase (mostly the paper's `background-color`, plus `rotate`). With no skin: 0.
- **CSS cannot turn them off only during the scroll:** there is no "is scrolling" state in CSS. Two CSS options measured:
  - **Hover-in delayed 80 ms** (`transition-delay` in the `:hover` rule, so a row that only passes under the pointer
    never straightens): **no gain**. Whole test −1.0 s [−1.8, −0.1] of 33.9 s (−3%); no scroll phase is significant.
  - **No transitions on the rows** (hover still straightens and recolours the ticket, instantly): **−3.5 s [−3.8, −2.6]
    of 33.9 s CPU (−10%)**. GPU −20 to −37% in every scroll phase and in hover. Slow wheel (800 px/s) −22% total CPU
    (6.6 → 4.9 s). Fast wheel and scrollTop: total CPU −4 to −6%, not significant; GPU drop is significant.
- Frame p95 is 18.5–18.7 ms in all three variants: the hover transitions cost CPU/GPU, not smoothness.
- Inference, not measured: the delay does not help because a delayed transition already exists as an animation
  (the `rotate` one on the compositor), so the row is still promoted to its own layer and repainted on the GPU.
- Scale: the skin's idle animations cost +29 points of a core all the time; the hover transitions cost only while
  the pointer is over a scrolling list.

## Method
- `PLAN=scroll` in `src/timeline.js`: idle 5 s → scrollTop sweep @200 → wheel 800 px/s @200 → wheel 4000 px/s @200 →
  wheel 5000 px/s @500 → hover sweep. Before each scroll phase the pointer moves to (150, 420), over the list.
- `page.js` counts `mouseover` and `transitionrun` inside `[data-thread-item]` per phase (`hc` in the phase record).
- `./run-hover.sh`: 15 fresh runs in blocks ABC CBA ABC CBA ABC: A = installed skin, B = `variants/full-hoverdelay-d292df3.css`,
  C = `variants/full-notx-d292df3.css`. `python3 -I src/analyze.py data/hover-d292df3 full <variant>` pairs A with B or C per block.
- Data: `data/hover-d292df3/` (`samples.jsonl`, `summary-full-vs-*.json`, `REPORT-data-full-vs-*.md`).
- Limits: Time Machine and a download client ran during the test (`system.log`); the blocks spread it over the variants.
  Not tested: which of the two transitions (`background-color` or `rotate`) carries the cost.

## Split test: colour fade or rotation?
- 15 more runs, same plan (`B=full-nobgtx C=full-norottx ./run-hover.sh data/hoversplit-d292df3`).
- **No colour fade, spring kept** (`full-nobgtx`): whole test −1.6 s [−2.3, −0.6] of 34.0 s (**−5%**). GPU −25% in
  slow wheel and −20% in hover; the other scroll phases do not change significantly.
- **No rotation, fade kept** (`full-norottx`): whole test +0.2 s [−1.9, +0.3], **no gain**. GPU falls in scroll@200 and
  wheel@500 but rises in slow wheel.
- The cost needs both transitions gone: −3.5 s (−10%) for both against −1.6 s for the fade alone.

# Finite animations (2026-11-18)

## Result
- Change (Roger's choice): the sign, the tank (kelp, koi, bubbles) and Dave's screen play 13-20 s when they appear
  (`sk-float` ×4, `sk-sway` ×6, `sk-swim` ×0.5, `sk-rise` ×2, `sk-screen` ×20), then rest in their first frame. They play
  again while the pointer is over the sign, the counter (footer) or the composer lane. Bubbles rest where they start
  (`background-position-y` = the `from` keyframe), so the end of the intro does not jump.
- Full stress test, 15 runs ABC/CBA (none / d292df3 / finite), `./run-finite.sh data/finite`, `SETTLE_MS=25000`:
  | | No skin | Skin d292df3 | Finite |
  |---|---:|---:|---:|
  | CPU whole test | 29.9 s | 58.1 s | **42.9 s** (−16.0 s [−22.1, −7.0] vs d292df3, −26%) |
  | Energy impact | 25.6 | 58.2 | **38.3** |
  | Idle, visible (% of a core) | 16.8 | 53.7 | **18.3** (vs no skin +1.9 [−2.1, +3.8], n.s.) |
  | Frames drawn, idle 20 s | 320 | 1201 | **317** |
  | Idle after the test | 17.0 | 48.7 | **21.4** |
  | Footprint at end, runs that released memory | 4 of 5 | 0 of 5 | 2 of 5 |
- Intro cost per appearance: 45% of a core for 10 s, 39% for the next 10 s, then 14% (no skin 12-16%): about 5-6 s
  of CPU each time the page or the sidebar footer mounts.
- What remains (finite vs no skin, +12.7 s [9.1, 17.6]) is interaction: scroll and wheel +30 to +46 points of a core,
  hover +15, appearance +18, sidebar +13. Status churn and resize do not differ.
- Memory: the 15 s idle window at the end is short; release depends on when Blink's purge runs. Finite runs ended at
  880-1420 MB, d292df3 runs at 1460-1510 MB.
- Checks: build + validator pass (full 48,809 chars, lite unchanged); `fx/check.js` on :7508: 128 rules, 0 invalid,
  rows without overlap; `getAnimations()` is empty 25 s after load and lists only the hovered element's animations on
  hover. Light vs dark differ in the "SR" project sign colour and a strip at the sidebar edge, the same with d292df3
  (not caused by this change).
- Limits: a download client and Time Machine ran during the test (`system.log`); hover restarts an animation at the point
  of its cycle that the time since it appeared gives (a koi may pop in mid-tank), and leaving snaps it to rest.

## Applied after the split test (Roger's choice)
- Rows lose the colour fade and keep the spring: the source now matches `variants/full-nobgtx-d292df3.css`
  (whole scroll test −1.6 s [−2.3, −0.6], −5%). Not re-measured on top of the finite animations.

# Final build 7a0b011: finite animations + no colour fade (2026-11-18)
- 7a0b011 was the local commit; after the rebase on origin it is fe3acaa, with the same `out2/full.css`.
- 15 runs ABC/CBA, full stress test, `SETTLE_MS=25000` (`C=full-7a0b011 ./run-finite.sh data/final-7a0b011`).

| | No skin | Skin d292df3 | 7a0b011 | 7a0b011 vs d292df3 |
|---|---:|---:|---:|---:|
| CPU whole test | 26.0 s | 48.0 s | **33.9 s** | −14.0 s [−16.1, −13.3], **−29%** |
| Energy impact | 23.4 | 48.0 | **31.2** | −16.8 [−19.8, −14.2] |
| Frames drawn | 2278 | 4736 | **2551** | −2180 |
| Footprint at end | 878 MB | 1429 MB | **878 MB** | −569 [−661, −380]; all 5 runs released |
| Idle visible, % of a core | 17.4 | 45.0 | **19.2** | −26.6 |
| Idle hidden | 1.8 | 7.6 | **3.6** | −3.7 |
| Scroll / wheel | 45–47 | 61–74 | **50–64** | −10 to −11 points |
| Hover | 30.4 | 53.2 | **36.3** | −16.9 |

- Against no skin the skin now costs +7.7 s [7.0, 8.3] (+30%) per test, down from +22 s: interaction only
  (scroll +4 to +20 points of a core, appearance +19, sidebar +9). Frame p95 is the same as d292df3 in every phase.
- Absolute numbers differ between run sets (d292df3 48.0 s here, 58.1 s in `data/finite`); qBittorrent and Time
  Machine ran in both (local `system.log`) at different loads. Compare within one run set only.

# Hover off while the list scrolls (2026-11-19)
Plan `scroll` (pointer over the list), 15 fresh Electron runs per set, blocks ABC/CBA, paired bootstrap CIs.
Base: 389a4bb (`variants/full-389a4bb.css`, finite animations, no colour fade, rotation spring kept).

## Rotation off (`data/norot-389a4bb`)
- `variants/full-norot-389a4bb.css` drops the rows' last transition (rotate/translate spring).
- Whole test −0.7 s [−2.8, 0.6], not significant; GPU −0.9 s [−1.7, −0.8] (−15%). The skin costs +10.4 s over no skin
  here, so the spring is a small part of it. Not applied.

## Scroll flag (`data/busy-389a4bb`, `data/busy2-389a4bb`, `data/final-busy`)
CSS has no "is scrolling" state (`scroll-state(scrolled)` keeps the last direction after the scroll stops). The flag
builds one: a scroll timeline sets `--sk-p` on `[data-slot=sidebar-content]`; its children hold `--sk-pd: var(--sk-p)`
with a 150 ms transition, so the two differ only while the list moves; `--sk-busy: sign(abs(p − pd))` is an
integer (rows restyle only when it flips) and `[data-thread-item] { pointer-events: if(style(--sk-busy:1):none) }`
takes rows out of hit-testing. Chromium then updates no row `:hover` during the scroll.
- Probe (`Input.synthesizeScrollGesture`, 200 rows): during the scroll 0 rows hovered and 0 transitions (before: ~330
  hover changes per phase); hover returns 50–100 ms after the scroll ends; hovering after a scroll gives 102 changes,
  the same as without the flag.
- First version (viewport timeline, `linear both`): −5.6 s [−5.7, −4.5] (−22%).
- A size cut tried with it (`content-visibility: visible` on every attention ticket instead of the 8 anchored ones)
  cost 10 of 104 hover changes and +25 dropped frames in the 500-row wheel phase: off-screen attention tickets kept
  painting and their overflow caught the pointer. Rejected; the minifier change below made room instead.

Final build (flag + minifier change), `A=full-389a4bb B=full-final C=none ./run-hover.sh data/final-busy`:

| | No skin | 389a4bb | Final | Final vs 389a4bb |
|---|---:|---:|---:|---:|
| CPU whole test | 16.2 s | 28.1 s | **21.4 s** | −6.6 s [−7.1, −5.7], **−24%** |
| Renderer | 11.5 s | 19.8 s | 16.7 s | −3.0 [−3.4, −2.4] |
| GPU | 3.7 s | 7.3 s | **3.7 s** | −3.5 [−3.7, −3.1], −48% |
| Energy impact | 36.3 | 65.9 | 53.3 | −12.5 [−13.3, −8.2] |
| Frames dropped | 162 | 129 | 100 | −30 [−41, −22] |
| Row hover changes, wheel@500 | – | 399 | 1 | |
| Hover phase CPU / changes | – | 2.67 s / 104 | 2.69 s / 104 | n.s. / 0 |

- Per scroll phase −25 to −40% CPU; frame p95 unchanged (~18.6 ms). Idle and hover phases do not differ.
- The skin's cost over no skin on this test falls from +11.9 s to +5.2 s [4.4, 5.8]; GPU equals no skin.
- Limits: a click during a scroll, or within 150 ms of its end, lands on the list instead of a row; a change of the
  list height (rows added) also moves `--sk-p` and turns hover off for 150 ms. Browsers without `if()` keep the plain
  hover. Measured only in Electron 44.10.1 (Chromium 152) on this Mac mini.
