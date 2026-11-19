# Test data: tank-inf vs full-merged

Runs: 1=none, 2=full-merged, 3=tank-final, 4=tank-final-nob, 5=tank-inf, 6=tank-inf, 7=tank-final-nob, 8=tank-final, 9=full-merged, 10=none. Medians of 2; diff = median of 2 paired (tank-inf − full-merged) with 95% bootstrap CI.

## Whole test

| Metric | full-merged | tank-inf | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| cpu.total.s | 0.7 | 7.5 | 6.9 [6.6, 7.2] | 11.40× |
| cpu.renderer.s | 0.3 | 5.1 | 4.8 [4.6, 5.0] | 16.82× |
| cpu.gpu.s | 0.2 | 2.2 | 2.1 [2.0, 2.2] | 12.02× |
| cpu.browser.s | 0.1 | 0.1 | 0.0 [0.0, 0.0] | 1.17× |
| energy.impact.mean | 2.8 | 24.8 | 22.0 [20.9, 23.2] | 8.99× |
| frames.drawn | 61 | 1,798 | 1,737 [1,734, 1,740] | 29.48× |
| frames.dropped | 21 | 2 | -18 [-20, -17] | 0.12× |
| mem.renderer.max.MB | 428 | 568 | 140 [115, 165] | 1.33× |
| mem.gpu.max.MB | 92 | 97 | 5 [4, 6] | 1.05× |
| mem.footprint.max.MB | 1,170 | 1,160 | -10 [-50, 30] n.s. | 0.99× |
| mem.footprint.end.MB | 680 | 845 | 165 [156, 174] | 1.24× |
| heap.max.MB | 139.1 | 150.2 | 11.1 [10.4, 11.8] | 1.08× |
| heap.end.MB | 133.9 | 133.2 | -0.7 [-1.2, -0.2] | 1.00× |
| phases.wall.s | 30.0 | 30.0 | 0.0 [0.0, 0.0] n.s. | 1.00× |
| sys.cpu% | 50.1 | 49.1 | -1.0 [-12.1, 10.1] n.s. | 0.98× |

## cpu.total.ms per phase

| Phase | full-merged | tank-inf | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 662 | 7,544 | 6,882 [6,606, 7,158] | 11.40× |

## cpu.%core per phase

| Phase | full-merged | tank-inf | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 2.2 | 25.1 | 22.9 [22.0, 23.9] | 11.40× |

## energy.impact per phase

| Phase | full-merged | tank-inf | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 2.8 | 24.8 | 22.0 [20.9, 23.2] | 8.99× |

## frames.drawn per phase

| Phase | full-merged | tank-inf | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 61 | 1,798 | 1,737 [1,734, 1,740] | 29.48× |

## frames.dropped per phase

| Phase | full-merged | tank-inf | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 21 | 2 | -18 [-20, -17] | 0.12× |

## raf.p95.ms per phase

| Phase | full-merged | tank-inf | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | – | – | – [–, –] n.s. | – |

## style.ms per phase

| Phase | full-merged | tank-inf | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 0 | 2,031 | 2,031 [1,928, 2,134] | – |

## layout.ms per phase

| Phase | full-merged | tank-inf | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 4 | 5 | 1 [-1, 2] n.s. | 1.12× |

## mem.renderer.MB per phase

| Phase | full-merged | tank-inf | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 307 | 467 | 160 [141, 180] | 1.52× |

## mem.gpu.MB per phase

| Phase | full-merged | tank-inf | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 83 | 92 | 9 [7, 11] | 1.11× |

## wake.gpu/s per phase

| Phase | full-merged | tank-inf | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 63 | 123 | 60 [59, 60] | 1.94× |

## hover.changes per phase

| Phase | full-merged | tank-inf | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 0 | 0 | 0 [0, 0] n.s. | – |

## hover.transitions per phase

| Phase | full-merged | tank-inf | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 0 | 0 | 0 [0, 0] n.s. | – |
