#!/bin/zsh
# Finite animations: no skin / skin d292df3 (infinite) / C (default: skin with the finite intro), full stress test.
# 15 fresh runs in blocks ABC CBA ... (5 each). SETTLE_MS=25000: the intro (<= 20 s) ends before the first idle phase.
set -u; cd "${0:A:h}"; E=/Users/roger/t3code/.css-perf/bin/electron/Electron.app/Contents/MacOS/Electron
dir=${1:-data/finite-$(date +%Y%m%d-%H%M)}; mkdir -p $dir; out=$dir/samples.jsonl; : > $out
A=none B=full C=${C:-full-finite}; order=($A $B $C $C $B $A $A $B $C $C $B $A $A $B $C); i=0
for v in $order; do i=$((i+1)); { echo "== run $i $v $(date +%T)"; uptime; ps -Ao pcpu,comm -r | sed -n 2,6p | cut -c1-90; } >> $dir/system.log
  SETTLE_MS=25000 $E src/timeline.js $v $i $out > $dir/run-$i-$v.log 2>&1; echo "run $i $v exit $?"; sleep 20; done
