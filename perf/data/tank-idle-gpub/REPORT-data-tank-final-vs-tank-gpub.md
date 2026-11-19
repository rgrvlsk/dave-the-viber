# Test data: tank-gpub vs tank-final

Runs: 1=full-merged, 2=tank-final, 3=tank-gpub, 4=tank-gpub, 5=tank-final, 6=full-merged. Medians of 2; diff = median of 2 paired (tank-gpub − tank-final) with 95% bootstrap CI.

## Whole test

| Metric | tank-final | tank-gpub | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| cpu.total.s | 3.2 | 3.9 | 0.7 [0.4, 1.0] | 1.23× |
| cpu.renderer.s | 2.4 | 2.9 | 0.6 [0.4, 0.7] | 1.24× |
| cpu.gpu.s | 0.6 | 0.7 | 0.1 [0.1, 0.2] | 1.25× |
| cpu.browser.s | 0.1 | 0.2 | 0.0 [-0.0, 0.0] n.s. | 1.06× |
| energy.impact.mean | 10.7 | 13.1 | 2.4 [2.1, 2.7] | 1.23× |
| frames.drawn | 244 | 283 | 40 [35, 44] | 1.16× |
| frames.dropped | 0 | 16 | 15 [15, 15] | 31.00× |
| mem.renderer.max.MB | 452 | 386 | -66 [-108, -23] | 0.85× |
| mem.gpu.max.MB | 90 | 86 | -3 [-5, -2] | 0.96× |
| mem.footprint.max.MB | 1,142 | 1,250 | 108 [79, 137] | 1.09× |
| mem.footprint.end.MB | 746 | 784 | 38 [-11, 86] n.s. | 1.05× |
| heap.max.MB | 155.5 | 155.5 | 0.0 [-4.2, 4.2] n.s. | 1.00× |
| heap.end.MB | 132.6 | 132.9 | 0.3 [0.0, 0.6] | 1.00× |
| phases.wall.s | 30.0 | 30.0 | 0.0 [-0.0, 0.0] n.s. | 1.00× |
| sys.cpu% | 66.4 | 54.4 | -12.0 [-49.7, 25.7] n.s. | 0.82× |

## cpu.total.ms per phase

| Phase | tank-final | tank-gpub | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 3,174 | 3,890 | 715 [441, 989] | 1.23× |

## cpu.%core per phase

| Phase | tank-final | tank-gpub | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 10.6 | 13.0 | 2.4 [1.5, 3.3] | 1.23× |

## energy.impact per phase

| Phase | tank-final | tank-gpub | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 10.7 | 13.1 | 2.4 [2.1, 2.7] | 1.23× |

## frames.drawn per phase

| Phase | tank-final | tank-gpub | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 244 | 283 | 40 [35, 44] | 1.16× |

## frames.dropped per phase

| Phase | tank-final | tank-gpub | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 0 | 16 | 15 [15, 15] | 31.00× |

## raf.p95.ms per phase

| Phase | tank-final | tank-gpub | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | – | – | – [–, –] n.s. | – |

## style.ms per phase

| Phase | tank-final | tank-gpub | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 801 | 990 | 189 [60, 319] | 1.24× |

## layout.ms per phase

| Phase | tank-final | tank-gpub | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 1 | 16 | 15 [14, 16] | 14.08× |

## mem.renderer.MB per phase

| Phase | tank-final | tank-gpub | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 298 | 347 | 49 [-8, 106] n.s. | 1.16× |

## mem.gpu.MB per phase

| Phase | tank-final | tank-gpub | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 79 | 82 | 4 [2, 5] | 1.04× |

## wake.gpu/s per phase

| Phase | tank-final | tank-gpub | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 114 | 116 | 2 [1, 3] | 1.01× |

## hover.changes per phase

| Phase | tank-final | tank-gpub | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 0 | 0 | 0 [0, 0] n.s. | – |

## hover.transitions per phase

| Phase | tank-final | tank-gpub | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 0 | 0 | 0 [0, 0] n.s. | – |
