# Test data: tank-final-nob vs full-merged

Runs: 1=none, 2=full-merged, 3=tank-final, 4=tank-final-nob, 5=tank-inf, 6=tank-inf, 7=tank-final-nob, 8=tank-final, 9=full-merged, 10=none. Medians of 2; diff = median of 2 paired (tank-final-nob − full-merged) with 95% bootstrap CI.

## Whole test

| Metric | full-merged | tank-final-nob | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| cpu.total.s | 0.7 | 1.8 | 1.2 [1.1, 1.3] | 2.79× |
| cpu.renderer.s | 0.3 | 1.1 | 0.8 [0.7, 0.9] | 3.60× |
| cpu.gpu.s | 0.2 | 0.5 | 0.4 [0.3, 0.4] | 2.94× |
| cpu.browser.s | 0.1 | 0.1 | 0.0 [0.0, 0.0] | 1.14× |
| energy.impact.mean | 2.8 | 6.5 | 3.7 [2.5, 4.9] | 2.34× |
| frames.drawn | 61 | 267 | 206 [181, 231] | 4.38× |
| frames.dropped | 21 | 14 | -8 [-8, -7] | 0.64× |
| mem.renderer.max.MB | 428 | 347 | -81 [-101, -61] | 0.81× |
| mem.gpu.max.MB | 92 | 91 | -0 [-7, 6] n.s. | 1.00× |
| mem.footprint.max.MB | 1,170 | 1,120 | -50 [-68, -33] | 0.96× |
| mem.footprint.end.MB | 680 | 706 | 26 [22, 31] | 1.04× |
| heap.max.MB | 139.1 | 143.2 | 4.1 [3.8, 4.4] | 1.03× |
| heap.end.MB | 133.9 | 133.1 | -0.7 [-1.0, -0.4] | 0.99× |
| phases.wall.s | 30.0 | 30.0 | 0.0 [0.0, 0.0] n.s. | 1.00× |
| sys.cpu% | 50.1 | 48.3 | -1.7 [-3.4, -0.1] | 0.97× |

## cpu.total.ms per phase

| Phase | full-merged | tank-final-nob | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 662 | 1,844 | 1,182 [1,093, 1,271] | 2.79× |

## cpu.%core per phase

| Phase | full-merged | tank-final-nob | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 2.2 | 6.1 | 3.9 [3.6, 4.2] | 2.79× |

## energy.impact per phase

| Phase | full-merged | tank-final-nob | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 2.8 | 6.5 | 3.7 [2.5, 4.9] | 2.34× |

## frames.drawn per phase

| Phase | full-merged | tank-final-nob | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 61 | 267 | 206 [181, 231] | 4.38× |

## frames.dropped per phase

| Phase | full-merged | tank-final-nob | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 21 | 14 | -8 [-8, -7] | 0.64× |

## raf.p95.ms per phase

| Phase | full-merged | tank-final-nob | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | – | – | – [–, –] n.s. | – |

## style.ms per phase

| Phase | full-merged | tank-final-nob | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 0 | 257 | 257 [235, 278] | – |

## layout.ms per phase

| Phase | full-merged | tank-final-nob | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 4 | 15 | 10 [10, 11] | 3.37× |

## mem.renderer.MB per phase

| Phase | full-merged | tank-final-nob | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 307 | 336 | 29 [29, 29] | 1.09× |

## mem.gpu.MB per phase

| Phase | full-merged | tank-final-nob | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 83 | 85 | 2 [-2, 6] n.s. | 1.03× |

## wake.gpu/s per phase

| Phase | full-merged | tank-final-nob | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 63 | 112 | 49 [47, 51] | 1.77× |

## hover.changes per phase

| Phase | full-merged | tank-final-nob | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 0 | 0 | 0 [0, 0] n.s. | – |

## hover.transitions per phase

| Phase | full-merged | tank-final-nob | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 0 | 0 | 0 [0, 0] n.s. | – |
