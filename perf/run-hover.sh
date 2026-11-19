#!/bin/zsh
# Hover animations while the list scrolls: skin as installed / B / C (default: hover-in delayed 80 ms / no row transitions;
# split test: B=full-nobgtx C=full-norottx, only the colour fade or only the rotation removed).
# PLAN=scroll (pointer over the list), 15 fresh Electron runs in blocks ABC CBA ... (5 each).
set -u; cd "${0:A:h}"; E=/Users/roger/t3code/.css-perf/bin/electron/Electron.app/Contents/MacOS/Electron
dir=${1:-data/hover-$(date +%Y%m%d-%H%M)}; mkdir -p $dir; out=$dir/samples.jsonl; : > $out
A=${A:-full} B=${B:-full-hoverdelay} C=${C:-full-notx}; order=($A $B $C $C $B $A $A $B $C $C $B $A $A $B $C); i=0
for v in $order; do i=$((i+1)); { echo "== run $i $v $(date +%T)"; uptime; ps -Ao pcpu,comm -r | sed -n 2,6p | cut -c1-90; } >> $dir/system.log
  PLAN=scroll $E src/timeline.js $v $i $out > $dir/run-$i-$v.log 2>&1; echo "run $i $v exit $?"; sleep 20; done
