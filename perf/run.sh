#!/bin/zsh
# Stress test, skin vs no skin: 10 fresh Electron runs in ABBA order (5 each), continuous sampling.
# Usage: ./run.sh <out-dir>   Needs the dev server on :7508 and ./profile paired (src/pair.js).
set -u; cd "${0:A:h}"; E=/Users/roger/t3code/.css-perf/bin/electron/Electron.app/Contents/MacOS/Electron
dir=${1:-data/run-$(date +%Y%m%d-%H%M)}; mkdir -p $dir; out=$dir/samples.jsonl; : > $out
order=(none full full none none full full none none full); i=0
for v in $order; do
  i=$((i+1))
  { echo "== run $i $v $(date +%T)"; uptime; ps -Ao pcpu,comm -r | sed -n 2,6p | cut -c1-90; } >> $dir/system.log
  $E src/timeline.js $v $i $out > $dir/run-$i-$v.log 2>&1; echo "run $i $v exit $?"
  sleep 20
done
