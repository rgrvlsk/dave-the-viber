# Test data: tank-final vs full-merged

Runs: 1=full-merged, 2=tank-final, 3=tank-gpub, 4=tank-gpub, 5=tank-final, 6=full-merged. Medians of 2; diff = median of 2 paired (tank-final − full-merged) with 95% bootstrap CI.

## Whole test

| Metric | full-merged | tank-final | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| cpu.total.s | 1.4 | 3.2 | 1.8 [0.7, 2.8] | 2.25× |
| cpu.renderer.s | 0.8 | 2.4 | 1.5 [0.7, 2.4] | 2.86× |
| cpu.gpu.s | 0.3 | 0.6 | 0.2 [0.1, 0.4] | 1.70× |
| cpu.browser.s | 0.2 | 0.1 | -0.0 [-0.1, 0.0] n.s. | 0.85× |
| energy.impact.mean | 6.3 | 10.7 | 4.3 [1.1, 7.6] | 1.69× |
| frames.drawn | 88 | 244 | 156 [138, 174] | 2.78× |
| frames.dropped | 49 | 0 | -48 [-59, -38] | 0.01× |
| mem.renderer.max.MB | 503 | 452 | -51 [-143, 40] n.s. | 0.90× |
| mem.gpu.max.MB | 83 | 90 | 6 [-9, 22] n.s. | 1.08× |
| mem.footprint.max.MB | 1,293 | 1,142 | -150 [-152, -149] | 0.88× |
| mem.footprint.end.MB | 650 | 746 | 96 [25, 166] | 1.15× |
| heap.max.MB | 149.6 | 155.5 | 5.9 [3.3, 8.4] | 1.04× |
| heap.end.MB | 133.8 | 132.6 | -1.1 [-2.0, -0.3] | 0.99× |
| phases.wall.s | 30.0 | 30.0 | 0.0 [0.0, 0.0] n.s. | 1.00× |
| sys.cpu% | 34.3 | 66.4 | 32.1 [-0.1, 64.3] n.s. | 1.93× |

## cpu.total.ms per phase

| Phase | full-merged | tank-final | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 1,410 | 3,174 | 1,765 [724, 2,806] | 2.25× |

## cpu.%core per phase

| Phase | full-merged | tank-final | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 4.7 | 10.6 | 5.9 [2.4, 9.4] | 2.25× |

## energy.impact per phase

| Phase | full-merged | tank-final | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 6.3 | 10.7 | 4.3 [1.1, 7.6] | 1.69× |

## frames.drawn per phase

| Phase | full-merged | tank-final | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 88 | 244 | 156 [138, 174] | 2.78× |

## frames.dropped per phase

| Phase | full-merged | tank-final | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 49 | 0 | -48 [-59, -38] | 0.01× |

## raf.p95.ms per phase

| Phase | full-merged | tank-final | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | – | – | – [–, –] n.s. | – |

## style.ms per phase

| Phase | full-merged | tank-final | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 170 | 801 | 630 [479, 782] | 4.70× |

## layout.ms per phase

| Phase | full-merged | tank-final | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 9 | 1 | -8 [-17, 1] n.s. | 0.12× |

## mem.renderer.MB per phase

| Phase | full-merged | tank-final | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 370 | 298 | -72 [-193, 49] n.s. | 0.81× |

## mem.gpu.MB per phase

| Phase | full-merged | tank-final | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 75 | 79 | 3 [-14, 20] n.s. | 1.04× |

## wake.gpu/s per phase

| Phase | full-merged | tank-final | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 65 | 114 | 49 [48, 49] | 1.75× |

## hover.changes per phase

| Phase | full-merged | tank-final | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 0 | 0 | 0 [0, 0] n.s. | – |

## hover.transitions per phase

| Phase | full-merged | tank-final | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 0 | 0 | 0 [0, 0] n.s. | – |
