# Test data: tank-tr0 vs full-final2

Runs: 1=full-final2, 2=tank-inf, 3=tank-steps, 4=tank-steps0, 5=tank-tr0, 6=tank-tr0, 7=tank-steps0, 8=tank-steps, 9=tank-inf, 10=full-final2. Medians of 2; diff = median of 2 paired (tank-tr0 − full-final2) with 95% bootstrap CI.

## Whole test

| Metric | full-final2 | tank-tr0 | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| cpu.total.s | 4.4 | 11.9 | 7.5 [5.7, 9.3] | 2.70× |
| cpu.renderer.s | 3.0 | 7.7 | 4.7 [3.5, 6.0] | 2.61× |
| cpu.gpu.s | 1.1 | 3.9 | 2.8 [2.2, 3.3] | 3.41× |
| cpu.browser.s | 0.2 | 0.2 | -0.0 [-0.0, -0.0] | 0.90× |
| energy.impact.mean | 15.2 | 41.9 | 26.8 [19.5, 34.1] | 2.77× |
| frames.drawn | 303 | 1,800 | 1,498 [1,320, 1,675] | 5.94× |
| frames.dropped | 52 | 66 | 14 [-11, 39] n.s. | 1.27× |
| mem.renderer.max.MB | 523 | 615 | 92 [-64, 248] n.s. | 1.18× |
| mem.gpu.max.MB | 99 | 103 | 4 [-6, 15] n.s. | 1.04× |
| mem.footprint.max.MB | 1,192 | 1,336 | 144 [123, 165] | 1.12× |
| mem.footprint.end.MB | 740 | 792 | 52 [17, 88] | 1.07× |
| heap.max.MB | 143.0 | 145.9 | 2.8 [-10.9, 16.6] n.s. | 1.02× |
| heap.end.MB | 134.9 | 134.2 | -0.7 [-0.8, -0.5] | 1.00× |
| phases.wall.s | 30.0 | 30.0 | -0.0 [-0.0, 0.0] n.s. | 1.00× |
| sys.cpu% | 23.9 | 16.5 | -7.4 [-17.6, 2.9] n.s. | 0.69× |

## cpu.total.ms per phase

| Phase | full-final2 | tank-tr0 | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 4,405 | 11,878 | 7,474 [5,675, 9,272] | 2.70× |

## cpu.%core per phase

| Phase | full-final2 | tank-tr0 | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 14.7 | 39.6 | 24.9 [18.9, 30.9] | 2.70× |

## energy.impact per phase

| Phase | full-final2 | tank-tr0 | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 15.2 | 41.9 | 26.8 [19.5, 34.1] | 2.77× |

## frames.drawn per phase

| Phase | full-final2 | tank-tr0 | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 303 | 1,800 | 1,498 [1,320, 1,675] | 5.94× |

## frames.dropped per phase

| Phase | full-final2 | tank-tr0 | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 52 | 66 | 14 [-11, 39] n.s. | 1.27× |

## raf.p95.ms per phase

| Phase | full-final2 | tank-tr0 | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | – | – | – [–, –] n.s. | – |

## style.ms per phase

| Phase | full-final2 | tank-tr0 | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 1,051 | 3,437 | 2,386 [1,895, 2,877] | 3.27× |

## layout.ms per phase

| Phase | full-final2 | tank-tr0 | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 23 | 26 | 3 [-1, 7] n.s. | 1.13× |

## mem.renderer.MB per phase

| Phase | full-final2 | tank-tr0 | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 492 | 574 | 82 [-82, 247] n.s. | 1.17× |

## mem.gpu.MB per phase

| Phase | full-final2 | tank-tr0 | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 94 | 102 | 7 [-6, 21] n.s. | 1.08× |

## wake.gpu/s per phase

| Phase | full-final2 | tank-tr0 | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 81 | 126 | 45 [-0, 91] n.s. | 1.56× |

## hover.changes per phase

| Phase | full-final2 | tank-tr0 | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 0 | 0 | 0 [0, 0] n.s. | – |

## hover.transitions per phase

| Phase | full-final2 | tank-tr0 | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 0 | 0 | 0 [0, 0] n.s. | – |
