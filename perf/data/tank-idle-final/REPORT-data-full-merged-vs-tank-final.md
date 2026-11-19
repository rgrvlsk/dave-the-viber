# Test data: tank-final vs full-merged

Runs: 1=none, 2=full-merged, 3=tank-final, 4=tank-final, 5=full-merged, 6=none. Medians of 2; diff = median of 2 paired (tank-final − full-merged) with 95% bootstrap CI.

## Whole test

| Metric | full-merged | tank-final | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| cpu.total.s | 0.7 | 3.6 | 2.8 [2.4, 3.2] | 4.86× |
| cpu.renderer.s | 0.3 | 2.8 | 2.5 [2.2, 2.8] | 8.13× |
| cpu.gpu.s | 0.2 | 0.5 | 0.4 [0.3, 0.4] | 2.83× |
| cpu.browser.s | 0.1 | 0.1 | -0.0 [-0.0, 0.0] n.s. | 0.95× |
| energy.impact.mean | 3.1 | 11.1 | 8.0 [6.3, 9.7] | 3.59× |
| frames.drawn | 60 | 242 | 182 [181, 182] | 4.00× |
| frames.dropped | 29 | 1 | -28 [-33, -23] | 0.03× |
| mem.renderer.max.MB | 444 | 437 | -7 [-117, 102] n.s. | 0.98× |
| mem.gpu.max.MB | 95 | 86 | -8 [-12, -5] | 0.91× |
| mem.footprint.max.MB | 1,180 | 1,122 | -57 [-60, -54] | 0.95× |
| mem.footprint.end.MB | 642 | 732 | 90 [53, 127] | 1.14× |
| heap.max.MB | 145.4 | 143.2 | -2.1 [-3.5, -0.8] | 0.99× |
| heap.end.MB | 136.2 | 132.6 | -3.6 [-6.1, -1.1] | 0.97× |
| phases.wall.s | 30.0 | 30.0 | 0.0 [0.0, 0.0] n.s. | 1.00× |
| sys.cpu% | 30.0 | 54.1 | 24.1 [5.6, 42.6] | 1.80× |

## cpu.total.ms per phase

| Phase | full-merged | tank-final | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 734 | 3,563 | 2,830 [2,414, 3,245] | 4.86× |

## cpu.%core per phase

| Phase | full-merged | tank-final | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 2.4 | 11.9 | 9.4 [8.0, 10.8] | 4.86× |

## energy.impact per phase

| Phase | full-merged | tank-final | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 3.1 | 11.1 | 8.0 [6.3, 9.7] | 3.59× |

## frames.drawn per phase

| Phase | full-merged | tank-final | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 60 | 242 | 182 [181, 182] | 4.00× |

## frames.dropped per phase

| Phase | full-merged | tank-final | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 29 | 1 | -28 [-33, -23] | 0.03× |

## raf.p95.ms per phase

| Phase | full-merged | tank-final | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | – | – | – [–, –] n.s. | – |

## style.ms per phase

| Phase | full-merged | tank-final | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 0 | 1,034 | 1,034 [891, 1,178] | – |

## layout.ms per phase

| Phase | full-merged | tank-final | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 1 | 1 | 0 [-2, 2] n.s. | 1.17× |

## mem.renderer.MB per phase

| Phase | full-merged | tank-final | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 374 | 351 | -23 [-124, 78] n.s. | 0.94× |

## mem.gpu.MB per phase

| Phase | full-merged | tank-final | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 89 | 81 | -7 [-11, -4] | 0.92× |

## wake.gpu/s per phase

| Phase | full-merged | tank-final | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 63 | 116 | 52 [52, 53] | 1.83× |

## hover.changes per phase

| Phase | full-merged | tank-final | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 0 | 0 | 0 [0, 0] n.s. | – |

## hover.transitions per phase

| Phase | full-merged | tank-final | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 0 | 0 | 0 [0, 0] n.s. | – |
