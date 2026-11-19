# Test data: tank-steps0-m vs full-merged

Runs: 1=full-merged, 2=tank-steps0-m, 3=tank-tr0-m, 4=tank-trs-m, 5=tank-trs-m, 6=tank-tr0-m, 7=tank-steps0-m, 8=full-merged. Medians of 2; diff = median of 2 paired (tank-steps0-m − full-merged) with 95% bootstrap CI.

## Whole test

| Metric | full-merged | tank-steps0-m | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| cpu.total.s | 4.7 | 6.7 | 2.0 [1.3, 2.8] | 1.43× |
| cpu.renderer.s | 3.3 | 4.8 | 1.5 [0.8, 2.3] | 1.47× |
| cpu.gpu.s | 1.2 | 1.7 | 0.5 [0.5, 0.5] | 1.40× |
| cpu.browser.s | 0.2 | 0.2 | 0.0 [0.0, 0.0] | 1.06× |
| energy.impact.mean | 15.6 | 23.2 | 7.7 [4.8, 10.5] | 1.49× |
| frames.drawn | 480 | 703 | 224 [208, 239] | 1.47× |
| frames.dropped | 64 | 66 | 3 [-1, 7] n.s. | 1.05× |
| mem.renderer.max.MB | 683 | 547 | -136 [-276, 4] n.s. | 0.80× |
| mem.gpu.max.MB | 95 | 94 | -1 [-9, 7] n.s. | 0.99× |
| mem.footprint.max.MB | 1,282 | 1,217 | -64 [-225, 96] n.s. | 0.95× |
| mem.footprint.end.MB | 1,095 | 971 | -124 [-458, 210] n.s. | 0.89× |
| heap.max.MB | 151.3 | 141.7 | -9.5 [-20.1, 1.0] n.s. | 0.94× |
| heap.end.MB | 136.7 | 132.8 | -3.9 [-4.1, -3.6] | 0.97× |
| phases.wall.s | 30.0 | 30.0 | 0.0 [0.0, 0.0] n.s. | 1.00× |
| sys.cpu% | 22.9 | 21.4 | -1.5 [-1.9, -1.2] | 0.93× |

## cpu.total.ms per phase

| Phase | full-merged | tank-steps0-m | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 4,683 | 6,701 | 2,018 [1,267, 2,769] | 1.43× |

## cpu.%core per phase

| Phase | full-merged | tank-steps0-m | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 15.6 | 22.3 | 6.7 [4.2, 9.2] | 1.43× |

## energy.impact per phase

| Phase | full-merged | tank-steps0-m | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 15.6 | 23.2 | 7.7 [4.8, 10.5] | 1.49× |

## frames.drawn per phase

| Phase | full-merged | tank-steps0-m | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 480 | 703 | 224 [208, 239] | 1.47× |

## frames.dropped per phase

| Phase | full-merged | tank-steps0-m | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 64 | 66 | 3 [-1, 7] n.s. | 1.05× |

## raf.p95.ms per phase

| Phase | full-merged | tank-steps0-m | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | – | – | – [–, –] n.s. | – |

## style.ms per phase

| Phase | full-merged | tank-steps0-m | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 1,247 | 2,289 | 1,043 [724, 1,362] | 1.84× |

## layout.ms per phase

| Phase | full-merged | tank-steps0-m | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 48 | 51 | 3 [2, 4] | 1.07× |

## mem.renderer.MB per phase

| Phase | full-merged | tank-steps0-m | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 616 | 443 | -174 [-193, -155] | 0.72× |

## mem.gpu.MB per phase

| Phase | full-merged | tank-steps0-m | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 93 | 90 | -2 [-12, 7] n.s. | 0.98× |

## wake.gpu/s per phase

| Phase | full-merged | tank-steps0-m | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 127 | 126 | -0 [-1, -0] | 1.00× |

## hover.changes per phase

| Phase | full-merged | tank-steps0-m | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 0 | 0 | 0 [0, 0] n.s. | – |

## hover.transitions per phase

| Phase | full-merged | tank-steps0-m | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 0 | 0 | 0 [0, 0] n.s. | – |
