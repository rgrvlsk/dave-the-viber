Act as a UI relay. Run this script exactly; do not judge or change the theme.

Context: a T3 Code dev server runs on this Mac at http://localhost:7508 (dev home /tmp/t3code-dev, worktree
/tmp/t3code-theme-demo). It already wears the custom theme "Pixel Sushi Rail" and already has threads from
an earlier demo (statuses Approval, Input, Working/Done, Settled, Snoozed). The built-in browser is paired with it.

Hard rules
- Do not modify /Users/roger/t3code, ~/.t3/userdata, any theme file or settings. Do not stop any server.
  Do not answer pending questions or approve pending permission requests. No commits. Start no subagents.
- Use only T3's built-in browser tools (preview_*). If a step fails twice, skip it, note why, continue.

Script (viewport 1440x900; pause ~2 s on each view so the video is readable)
1. preview_open http://localhost:7508 (open=false, reuseExistingTab=false). preview_resize 1440x900.
   preview_set_appearance dark. preview_recording_start.
2. Sidebar top with all live tickets. Snapshot save → 01-sidebar-dark.png.
3. Hover two tickets (one Approval, one Input) for 2 s each. Snapshot the first → 02-hover-dark.png.
4. Working + Stop button: open a thread whose model is "Replay (dev)" with scenario "Showcase" (or start a
   new thread: New thread → pick provider "Replay (dev)", model "Showcase"), send the prompt "demo".
   While it streams (Stop button visible at the composer's right), snapshot → 03-working-stop-dark.png.
   Then preview_evaluate:
   `(()=>{const b=document.querySelector('[data-slot="composer-host"] button[aria-label*="stop" i]');if(!b)return 'no stop';const c=getComputedStyle(b);return [b.getAttribute('aria-label'),c.backgroundColor,c.borderRadius].join(' | ')})()`
   and record the value. Let the stream finish (Done state); snapshot → 04-done-dark.png.
5. Open a thread with a pending question (status Input) so the question banner shows. Snapshot →
   05-question-dark.png. Click the banner's header row (button with
   data-pending-user-input-toggle) to collapse it; snapshot → 06-question-collapsed-dark.png; click it again
   to expand.
6. Open the Settled shelf in the sidebar, scroll to the bottom of the shelf. Snapshot → 07-settled-dark.png.
7. Type "sushi" in the sidebar search, wait for results, snapshot → 08-search-dark.png, then clear it.
8. Open a thread with code blocks or a long answer (e.g. the Showcase thread). Snapshot → 09-code-dark.png.
9. Collapse the sidebar, snapshot → 10-collapsed-dark.png, reopen it.
10. preview_set_appearance light. Repeat snapshots of steps 2, 5, 8 → 01-sidebar-light.png,
    05-question-light.png, 09-code-light.png. preview_recording_stop.
11. Put the video and PNGs in /tmp/t3code-theme-demo-out/v2/ (create it). Convert the video to MP4 with
    ffmpeg (H.264, yuv420p, constant 25 fps: `-vf fps=25 -pix_fmt yuv420p`) as video.mp4.
12. preview close the tab you opened.

Report (under 200 words): each step OK/skipped (with reason), the step-4 evaluate value, and the exact list
of files in /tmp/t3code-theme-demo-out/v2/ with sizes.
