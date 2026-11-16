Act as a UI relay. Run this script; do not judge or change the theme.

Context: a T3 Code dev server runs on this Mac at http://localhost:7508 (dev home /tmp/t3code-dev). It wears the
custom theme "Pixel Sushi Rail" and has threads from an earlier demo (statuses Approval, Input, Done, Settled,
Snoozed; some threads use the "Replay (dev)" provider, e.g. a Showcase thread with code blocks).
A first relay run failed because aria-ref element references went stale. So in this run:
- NEVER use aria-ref locators. Tag targets with preview_evaluate, then act with preview_act `selector`.
- Tag helper (run in preview_evaluate whenever you need a target; re-run it after every navigation):
  `(()=>{const rows=[...document.querySelectorAll('[data-thread-item]')];const tag=(re,name)=>{const r=rows.find(e=>re.test(e.innerText));if(r){r.setAttribute('data-demo',name);(r.querySelector('a')||r).setAttribute('data-demo-link',name)}return !!r};return {rows:rows.length,approval:tag(/Approval/i,'approval'),input:tag(/Input/i,'input'),showcase:tag(/showcase|code/i,'showcase'),texts:rows.slice(0,12).map(e=>e.innerText.replace(/\s+/g,' ').slice(0,70))}})()`
  Then: hover → preview_act hover selector `[data-demo=approval]`; open → preview_act click selector
  `[data-demo-link=input]`. If a regex finds nothing, read `texts` and adapt the regex once.
- Other stable selectors: search field `input[aria-label="Search threads"]`, clear search
  `[aria-label="Clear thread search"]`, sidebar toggle `[aria-label="Toggle main sidebar"]`, question header
  toggle `[data-pending-user-input-toggle]`, composer editor `[data-slot="composer-host"] [contenteditable="true"]`,
  Settled shelf: the sidebar button whose text starts with "Settled" (tag it the same way).
- Hard rules: do not modify /Users/roger/t3code, ~/.t3/userdata, any theme or settings; do not stop servers;
  do not answer pending questions or approve permission requests; no commits; start no subagents.
  If a step fails twice, skip it, note why, continue.

Script (pause ~2 s on each view; snapshots with preview_snapshot save=true, then copy each PNG to the output name)
1. preview_open http://localhost:7508 (open=false, reuseExistingTab=false). preview_resize 1440x900.
   preview_set_appearance dark. preview_recording_start.
2. Snapshot sidebar top → 01-sidebar-dark.png.
3. Hover the Approval ticket 2 s, snapshot → 02-hover-approval-dark.png; hover the Input ticket 2 s.
4. Open the Showcase thread. Click the composer editor, preview_act type "demo", press Enter. Within 2 s run:
   `(()=>{const b=document.querySelector('[data-slot="composer-host"] button[aria-label*="stop" i]');if(!b)return 'no stop';const c=getComputedStyle(b);return [b.getAttribute('aria-label'),c.backgroundColor,c.borderRadius].join(' | ')})()`
   Record the value; snapshot → 03-working-stop-dark.png. Wait until the turn ends; snapshot → 04-done-dark.png.
   (If sending fails because the thread is read-only, note it and continue.)
5. Open the Input thread. Snapshot → 05-question-dark.png. Click `[data-pending-user-input-toggle]`, snapshot
   → 06-question-collapsed-dark.png, click it again.
6. Open the Settled shelf, scroll the sidebar to the bottom. Snapshot → 07-settled-dark.png. Close the shelf.
7. Type "demo" in the search field, wait 1 s, snapshot → 08-search-dark.png, click clear.
8. Open the Showcase thread, scroll to a code block. Snapshot → 09-code-dark.png.
9. Click the sidebar toggle, snapshot → 10-collapsed-dark.png, click it again.
10. preview_set_appearance light. Repeat steps 2, 5 (first snapshot only), 8 → 01-sidebar-light.png,
    05-question-light.png, 09-code-light.png. preview_recording_stop.
11. Save everything in /tmp/t3code-theme-demo-out/v3/. Convert the recording:
    `ffmpeg -y -i <recording> -vf fps=25 -pix_fmt yuv420p -c:v libx264 /tmp/t3code-theme-demo-out/v3/video.mp4`.
12. Close the preview tab you opened.

Report (under 200 words): each step OK/skipped with reason, the step-4 value, and the list of files in
/tmp/t3code-theme-demo-out/v3/ with sizes.
