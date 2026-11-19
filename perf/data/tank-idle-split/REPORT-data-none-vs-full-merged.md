# Test data: full-merged vs none

Runs: 1=none, 2=full-merged, 3=tank-final, 4=tank-final-nob, 5=tank-inf, 6=tank-inf, 7=tank-final-nob, 8=tank-final, 9=full-merged, 10=none. Medians of 2; diff = median of 2 paired (full-merged − none) with 95% bootstrap CI.

## Whole test

| Metric | none | full-merged | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| cpu.total.s | 0.8 | 0.7 | -0.1 [-0.2, -0.0] | 0.85× |
| cpu.renderer.s | 0.2 | 0.3 | 0.1 [0.1, 0.1] | 1.41× |
| cpu.gpu.s | 0.3 | 0.2 | -0.1 [-0.2, -0.1] | 0.56× |
| cpu.browser.s | 0.2 | 0.1 | -0.0 [-0.0, -0.0] | 0.74× |
| energy.impact.mean | 3.0 | 2.8 | -0.2 [-1.2, 0.7] n.s. | 0.92× |
| frames.drawn | 98 | 61 | -38 [-63, -12] | 0.62× |
| frames.dropped | 0 | 21 | 21 [20, 22] | – |
| mem.renderer.max.MB | 301 | 428 | 127 [125, 128] | 1.42× |
| mem.gpu.max.MB | 74 | 92 | 18 [14, 21] | 1.24× |
| mem.footprint.max.MB | 1,227 | 1,170 | -57 [-97, -17] | 0.95× |
| mem.footprint.end.MB | 810 | 680 | -130 [-151, -109] | 0.84× |
| heap.max.MB | 145.6 | 139.1 | -6.5 [-12.4, -0.5] | 0.96× |
| heap.end.MB | 133.7 | 133.9 | 0.2 [0.1, 0.3] | 1.00× |
| phases.wall.s | 30.0 | 30.0 | -0.0 [-0.0, -0.0] | 1.00× |
| sys.cpu% | 44.5 | 50.1 | 5.6 [4.4, 6.7] | 1.13× |

## cpu.total.ms per phase

| Phase | none | full-merged | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 782 | 662 | -120 [-193, -48] | 0.85× |

## cpu.%core per phase

| Phase | none | full-merged | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 2.6 | 2.2 | -0.4 [-0.6, -0.2] | 0.85× |

## energy.impact per phase

| Phase | none | full-merged | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 3.0 | 2.8 | -0.2 [-1.2, 0.7] n.s. | 0.92× |

## frames.drawn per phase

| Phase | none | full-merged | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 98 | 61 | -38 [-63, -12] | 0.62× |

## frames.dropped per phase

| Phase | none | full-merged | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 0 | 21 | 21 [20, 22] | – |

## raf.p95.ms per phase

| Phase | none | full-merged | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | – | – | – [–, –] n.s. | – |

## style.ms per phase

| Phase | none | full-merged | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 14 | 0 | -14 [-18, -10] | – |

## layout.ms per phase

| Phase | none | full-merged | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 2 | 4 | 3 [-0, 6] n.s. | 2.51× |

## mem.renderer.MB per phase

| Phase | none | full-merged | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 144 | 307 | 162 [126, 199] | 2.13× |

## mem.gpu.MB per phase

| Phase | none | full-merged | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 64 | 83 | 18 [16, 21] | 1.28× |

## wake.gpu/s per phase

| Phase | none | full-merged | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 67 | 63 | -4 [-4, -4] | 0.95× |

## hover.changes per phase

| Phase | none | full-merged | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 0 | 0 | 0 [0, 0] n.s. | – |

## hover.transitions per phase

| Phase | none | full-merged | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 0 | 0 | 0 [0, 0] n.s. | – |
