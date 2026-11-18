#!/bin/zsh
# Diagnostic: idle + 6 status churns + idle, variants none / full / full-noanim, order ABC CBA.
set -u; cd "${0:A:h}"; E=/Users/roger/t3code/.css-perf/bin/electron/Electron.app/Contents/MacOS/Electron
dir=${1:-data/memory-$(date +%Y%m%d-%H%M)}; mkdir -p $dir; out=$dir/samples.jsonl; : > $out
order=(none full full-noanim full-noanim full none); i=0
for v in $order; do i=$((i+1)); { echo "== run $i $v $(date +%T)"; uptime; } >> $dir/system.log
  PLAN=memory $E src/timeline.js $v $i $out > $dir/run-$i-$v.log 2>&1; echo "run $i $v exit $?"; sleep 20; done
