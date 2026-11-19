# Test data: tank-steps0 vs full-final2

Runs: 1=full-final2, 2=tank-inf, 3=tank-steps, 4=tank-steps0, 5=tank-tr0, 6=tank-tr0, 7=tank-steps0, 8=tank-steps, 9=tank-inf, 10=full-final2. Medians of 2; diff = median of 2 paired (tank-steps0 − full-final2) with 95% bootstrap CI.

## Whole test

| Metric | full-final2 | tank-steps0 | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| cpu.total.s | 4.4 | 9.0 | 4.6 [3.1, 6.1] | 2.04× |
| cpu.renderer.s | 3.0 | 6.5 | 3.6 [2.9, 4.3] | 2.22× |
| cpu.gpu.s | 1.1 | 2.2 | 1.0 [0.2, 1.8] | 1.88× |
| cpu.browser.s | 0.2 | 0.2 | -0.0 [-0.0, 0.0] n.s. | 0.92× |
| energy.impact.mean | 15.2 | 31.1 | 15.9 [9.9, 22.0] | 2.05× |
| frames.drawn | 303 | 690 | 386 [224, 549] | 2.28× |
| frames.dropped | 52 | 76 | 24 [-4, 51] n.s. | 1.45× |
| mem.renderer.max.MB | 523 | 862 | 339 [286, 393] | 1.65× |
| mem.gpu.max.MB | 99 | 105 | 6 [-0, 12] n.s. | 1.06× |
| mem.footprint.max.MB | 1,192 | 1,214 | 22 [17, 27] | 1.02× |
| mem.footprint.end.MB | 740 | 902 | 162 [41, 283] | 1.22× |
| heap.max.MB | 143.0 | 147.4 | 4.4 [0.1, 8.6] | 1.03× |
| heap.end.MB | 134.9 | 133.4 | -1.5 [-3.1, 0.2] n.s. | 0.99× |
| phases.wall.s | 30.0 | 30.0 | -0.0 [-0.0, 0.0] n.s. | 1.00× |
| sys.cpu% | 23.9 | 14.4 | -9.5 [-20.5, 1.6] n.s. | 0.60× |

## cpu.total.ms per phase

| Phase | full-final2 | tank-steps0 | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 4,405 | 8,984 | 4,580 [3,078, 6,081] | 2.04× |

## cpu.%core per phase

| Phase | full-final2 | tank-steps0 | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 14.7 | 29.9 | 15.3 [10.3, 20.3] | 2.04× |

## energy.impact per phase

| Phase | full-final2 | tank-steps0 | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 15.2 | 31.1 | 15.9 [9.9, 22.0] | 2.05× |

## frames.drawn per phase

| Phase | full-final2 | tank-steps0 | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 303 | 690 | 386 [224, 549] | 2.28× |

## frames.dropped per phase

| Phase | full-final2 | tank-steps0 | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 52 | 76 | 24 [-4, 51] n.s. | 1.45× |

## raf.p95.ms per phase

| Phase | full-final2 | tank-steps0 | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | – | – | – [–, –] n.s. | – |

## style.ms per phase

| Phase | full-final2 | tank-steps0 | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 1,051 | 3,767 | 2,716 [2,062, 3,370] | 3.59× |

## layout.ms per phase

| Phase | full-final2 | tank-steps0 | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 23 | 27 | 4 [0, 7] | 1.16× |

## mem.renderer.MB per phase

| Phase | full-final2 | tank-steps0 | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 492 | 708 | 216 [203, 229] | 1.44× |

## mem.gpu.MB per phase

| Phase | full-final2 | tank-steps0 | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 94 | 103 | 9 [-1, 18] n.s. | 1.09× |

## wake.gpu/s per phase

| Phase | full-final2 | tank-steps0 | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 81 | 126 | 45 [0, 89] | 1.56× |

## hover.changes per phase

| Phase | full-final2 | tank-steps0 | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 0 | 0 | 0 [0, 0] n.s. | – |

## hover.transitions per phase

| Phase | full-final2 | tank-steps0 | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 0 | 0 | 0 [0, 0] n.s. | – |
