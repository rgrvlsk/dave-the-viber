# Council: defect hunt on the live demo (Pixel Sushi Rail theme)

Read-only. Edit nothing, start no agents, change no theme. Under 700 words.

## What you are looking at
A T3 Code dev build (origin/main b0f0c44d) running on Roger's Mac mini with the theme "Pixel Sushi Rail"
installed, driven through the dev replay scenarios. Folder:
/private/tmp/claude-501/-Users-roger--t3-scratch-2026-11-16-crea-un-tema-per-a-365d7a95/a839c0bb-e96e-4e10-8b9f-90dd03059585/scratchpad/demo/
- 21 PNGs named by view and mode (01-sidebar-dark … 11-code-answer-light), real captures, 1440×900 at 2x.
- video.mp4 (3 min 24 s) and three contact sheets sheet01–03.png (one frame every 6 s, in order) — use the
  sheets; open video frames only if you need motion detail.
- full.css: the theme as published (minified). Readable sources: ../src2/core.css, ../src2/extras.css.
Statuses produced: Approval, Input, Working, Done ("DISH!"), Settled, Snoozed. Not produced by the demo:
Request, Waiting, Limited, Failed, Woke (judge their rules from the CSS only).

## The design (owner-approved; do not re-litigate)
Night sushi bar. Sidebar = blue tiled wall with a twine on the left; each thread is a cream order ticket
pegged to it (red peg pinned, brass peg current), slightly tilted, straightening on hover. Line 1 title,
line 2 project + status stamp, line 3 branch + model. Project icon = faint blurred stain on the paper.
Calling tickets (Approval/Input/Request/Woke) show a customer speech bubble past the sidebar edge instead of
the stamp (first ticket of each kind only). Done = "DISH!" with a steaming bowl; Working = a pot whose lid
dances. Settled = slips pierced on a spike. Search results = pegged slips. Chat: fish noren with a hanging
wooden shop sign showing the project icon (koi for No project), user message = "ORDER · 注文" paper slip,
composer = order pad with a perforated top on a wooden counter; question banner shares the pad's paper,
round radios / square checkboxes kept. Logo = wooden plaque, DEV/Nightly = paper tag, sidebar buttons and
search field = glazed tiles. One look in light and dark OS modes.

## Find defects
Look for anything that looks broken, misaligned, clipped, overlapping, inconsistent with the rest of the
theme, unstyled (default app look left over, e.g. the "Snoozed" shelf header), low contrast, wrong in light
vs dark, or janky in motion. Also check legibility and that hover buttons never cover the status.

## Return
A numbered list, most severe first. Each: severity (blocking / should-fix / nit), where (PNG name + rough
area, or sheet + tile number), what is wrong, and a concrete CSS-level fix (selector idea + property).
Then one line: overall score /10 for how finished the theme looks in this demo.
