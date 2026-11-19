#!/bin/zsh
# Steady idle cost, window visible: VARIANTS in blocks ABC..CBA (BLOCKS blocks), PLAN=idle, SETTLE_MS=25000 so the
# finite intro animations have ended before the 30 s measurement.
set -u; cd "${0:A:h}"; E=/Users/roger/t3code/.css-perf/bin/electron/Electron.app/Contents/MacOS/Electron
dir=${1:-data/idle-$(date +%Y%m%d-%H%M)}; mkdir -p $dir; out=$dir/samples.jsonl; : > $out
vs=(${=VARIANTS}); order=(); for b in $(seq 1 ${BLOCKS:-2}); do if (( b % 2 )); then order+=($vs); else order+=(${(Oa)vs}); fi; done; i=0
for v in $order; do i=$((i+1)); { echo "== run $i $v $(date +%T)"; uptime; ps -Ao pcpu,comm -r | sed -n 2,6p | cut -c1-90; } >> $dir/system.log
  PLAN=idle SETTLE_MS=25000 $E src/timeline.js $v $i $out > $dir/run-$i-$v.log 2>&1; echo "run $i $v exit $?"; sleep 15; done
