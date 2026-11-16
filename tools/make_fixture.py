import sys
out = sys.argv[1]
WRAP = "pointer-events-none group-has-[:focus-visible]/sidebar-status-slot:absolute group-has-[:focus-visible]/sidebar-status-slot:right-0 group-has-[:focus-visible]/sidebar-status-slot:opacity-0 group-any-hover/sidebar-row:absolute group-any-hover/sidebar-row:right-0 group-any-hover/sidebar-row:opacity-0 flex items-center self-center justify-self-end tabular-nums text-secondary-label"
ACTIONS = "pointer-events-none absolute inset-y-0 right-0 flex items-stretch opacity-0 has-[:focus-visible]:pointer-events-auto has-[:focus-visible]:static has-[:focus-visible]:opacity-100 group-any-hover/sidebar-row:pointer-events-auto group-any-hover/sidebar-row:static group-any-hover/sidebar-row:opacity-100"
ROW = "group/sidebar-row relative w-full cursor-pointer overflow-hidden rounded-md text-left outline-none select-none focus-visible:ring-2 focus-visible:ring-inset focus-visible:ring-ring bg-transparent text-sidebar-foreground hover:bg-sidebar-row-hover"
SVG = '<svg class="lucide {c}" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{p}</svg>'
CHECK = '<path d="M20 6 9 17l-5-5"/>'; CLOCK = '<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>'; CIRCLE = '<circle cx="12" cy="12" r="10"/>'; BRANCH='<circle cx="6" cy="6" r="3"/><circle cx="6" cy="18" r="3"/><path d="M6 9v6"/>'
STATUS = {"approval":("Approval","text-warning-foreground","shield-question-mark"),"input":("Input","text-indigo-600 dark:text-indigo-300","message-circle-question-mark"),
          "request":("Request","text-guest-foreground","user-round"),"working":("Working","text-info-foreground","circle-dashed"),
          "waiting":("Waiting","text-muted-foreground","circle-dot-dashed"),"limited":("Limited","text-warning-foreground","circle-alert"),
          "done":("Done","text-success-foreground","circle-check"),"failed":("Failed","text-error-foreground","circle-alert"),
          "woke":("Woke","text-warning-foreground","alarm-clock")}
ICON = '<svg class="lucide lucide-{n} shrink-0 size-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/></svg>'
MODEL = '<span class="inline-flex shrink-0 items-center" data-test="model">' + SVG.format(c="size-3.5",p=CIRCLE) + '</span>'
XMARK = '<path d="M18 6 6 18"/><path d="m6 6 12 12"/>'
DISCARD = f'<button type="button" aria-label="Discard draft" class="inline-flex cursor-pointer items-center rounded-md bg-transparent px-1.5 text-xs text-muted-foreground hover:text-foreground">{SVG.format(c="lucide-x size-3.5",p=XMARK)}</button>'
def row(i, title, status, meta=True, project="Status bar demo", active=False, receded=False, draft=False):
    if status == "woke":
        label, cls, icon = STATUS[status]
        inner = f'<button type="button" aria-label="Dismiss Woke notification" class="inline-flex cursor-pointer items-center gap-1 rounded-sm font-medium outline-none hover:underline {cls}">{ICON.format(n=icon)}{label}</button>'
    elif status:
        label, cls, icon = STATUS[status]
        inner = f'<span class="inline-flex items-center gap-1 font-medium {cls}">{ICON.format(n=icon)}{label}</span>'
    else:
        inner = '<time>14h</time>'
    metal = (f'<div class="mt-0.5 flex min-w-0 items-center gap-1.5 text-secondary-label text-xs">'
             f'<span class="flex min-w-0 flex-1"><span class="truncate">feature/very-long-branch-name-for-status-bars</span></span>'
             f'<span aria-hidden class="pointer-events-none ml-auto inline-flex shrink-0 items-center gap-1">{MODEL}</span></div>') if meta else ''
    title_icons = '' if meta else f'<span aria-hidden class="inline-flex shrink-0 items-center gap-1">{MODEL}</span>'
    h = "h-[4.875rem]" if meta else "h-auto"
    return f'''<li data-thread-item="t{i}" class="list-none py-0.5"><div role="button" tabindex="0" data-sidebar-row="t{i}" data-testid="sidebar-row-card"{' aria-current="page"' if active else ''} class="{ROW}{' bg-sidebar-row-active light:ring-1 light:ring-inset light:ring-sidebar-border/70' if active else ''}">
<span class="sr-only">{title}</span>
<div class="relative z-10 {h} px-(--sidebar-row-content-inset) py-(--sidebar-content-inset)">
 <div class="flex h-5 min-w-0 items-center gap-1.5"><span class="size-4 shrink-0 rounded bg-indigo-500/30 text-[9px] text-center">SD</span>
  <span class="min-w-0 flex-1 truncate font-normal text-secondary-label text-xs">{project}</span>
  <span class="group/sidebar-status-slot relative ml-auto flex h-5 min-w-8 shrink-0 items-stretch justify-end text-xs">
   <span class="{WRAP}">{inner}</span>
   <span class="{ACTIONS}">{DISCARD if draft else ''}<button type="button" aria-label="Snooze thread" class="inline-flex h-full cursor-pointer items-center gap-0.5 rounded-md bg-transparent px-1.5 text-xs text-muted-foreground hover:text-foreground">{SVG.format(c="size-3",p=CLOCK)}</button><button type="button" aria-label="Settle thread" class="-mr-1 inline-flex cursor-pointer items-center gap-1 rounded-md bg-transparent px-1.5 text-xs text-muted-foreground hover:text-foreground">{SVG.format(c="size-3.5",p=CHECK)}Settle</button></span>
  </span></div>
 <div class="mt-1 flex min-w-0 items-center gap-1.5"><span aria-hidden class="min-w-0 flex-1 text-start text-sm transition-opacity motion-reduce:transition-none {'font-normal truncate text-foreground/75 group-hover/sidebar-row:text-foreground' if receded else 'font-medium truncate text-foreground'}">{title}</span>{title_icons}</div>
 {metal}
</div></div></li>'''
rows = [row(1,"Animate the onboarding flow for new users","approval",active=True), row(2,"Clarify How to Do It","input"), row(3,"Review the sync PR","request",draft=True),
        row(4,"Fix the flaky login test","working"), row(5,"Wait for CI","waiting"), row(6,"Upgrade Laravel","limited"),
        row(7,"Audit colour tokens for contrast","done"), row(8,"Deploy staging","failed"), row(9,"Remind me about DNS","woke",meta=False),
        row(10,"Clean old branches",None,receded=True),
        row(11,"Read the osxphotos speed-test result on the MacBook (read-only shell relay)","approval",meta=False),
        row(12,"Write the osxphotos speed-test script on the MacBook (shell relay)",None,meta=False,receded=True),
        row(13,"Move the MacBook test outputs to the Trash (shell relay)","working",meta=False)]
html = f'''<!doctype html><html class="{sys.argv[2]}" style="--appearance-contrast-base:100%;--appearance-contrast-boost:65%;--appearance-contrast-border-boost:16.25%"><head><meta charset="utf-8"><link rel="stylesheet" href="app.css"><link rel="stylesheet" href="{sys.argv[3]}">
<style>body{{margin:0;padding:16px;background:var(--background)}} #sb{{width:300px;padding:0!important;background:#e4cfa6}} .dark #sb{{background:#1d1f2e}} body{{background:#f7efdf}} .dark body{{background:#16171f}}</style></head>
<body><div id="sb" data-slot="sidebar" data-app-sidebar class="bg-sidebar text-sidebar-foreground rounded-lg p-2"><div data-slot="sidebar-inner" class="p-2" style="min-height:100%"><ul class="flex flex-col gap-px">{"".join(rows)}</ul></div></div></body></html>'''
open(out,'w').write(html)
