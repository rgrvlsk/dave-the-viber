# Test data: full-merged vs none

Runs: 1=none, 2=full-merged, 3=tank-final, 4=tank-final, 5=full-merged, 6=none. Medians of 2; diff = median of 2 paired (full-merged − none) with 95% bootstrap CI.

## Whole test

| Metric | none | full-merged | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| cpu.total.s | 0.7 | 0.7 | 0.0 [-0.1, 0.1] n.s. | 1.01× |
| cpu.renderer.s | 0.2 | 0.3 | 0.2 [0.1, 0.2] | 1.95× |
| cpu.gpu.s | 0.3 | 0.2 | -0.1 [-0.1, -0.1] | 0.62× |
| cpu.browser.s | 0.2 | 0.1 | -0.0 [-0.1, -0.0] | 0.81× |
| energy.impact.mean | 2.5 | 3.1 | 0.6 [0.4, 0.8] | 1.25× |
| frames.drawn | 60 | 60 | 0 [-1, 1] n.s. | 1.00× |
| frames.dropped | 0 | 29 | 29 [23, 35] | – |
| mem.renderer.max.MB | 238 | 444 | 206 [150, 263] | 1.87× |
| mem.gpu.max.MB | 75 | 95 | 20 [10, 30] | 1.27× |
| mem.footprint.max.MB | 1,210 | 1,180 | -30 [-67, 6] n.s. | 0.97× |
| mem.footprint.end.MB | 796 | 642 | -154 [-178, -130] | 0.81× |
| heap.max.MB | 156.1 | 145.4 | -10.7 [-13.3, -8.1] | 0.93× |
| heap.end.MB | 134.3 | 136.2 | 2.0 [-0.1, 4.0] n.s. | 1.01× |
| phases.wall.s | 30.0 | 30.0 | -0.0 [-0.0, 0.0] n.s. | 1.00× |
| sys.cpu% | 58.2 | 30.0 | -28.2 [-58.6, 2.1] n.s. | 0.52× |

## cpu.total.ms per phase

| Phase | none | full-merged | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 725 | 734 | 8 [-61, 78] n.s. | 1.01× |

## cpu.%core per phase

| Phase | none | full-merged | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 2.4 | 2.4 | 0.0 [-0.2, 0.3] n.s. | 1.01× |

## energy.impact per phase

| Phase | none | full-merged | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 2.5 | 3.1 | 0.6 [0.4, 0.8] | 1.25× |

## frames.drawn per phase

| Phase | none | full-merged | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 60 | 60 | 0 [-1, 1] n.s. | 1.00× |

## frames.dropped per phase

| Phase | none | full-merged | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 0 | 29 | 29 [23, 35] | – |

## raf.p95.ms per phase

| Phase | none | full-merged | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | – | – | – [–, –] n.s. | – |

## style.ms per phase

| Phase | none | full-merged | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 0 | 0 | 0 [0, 0] n.s. | – |

## layout.ms per phase

| Phase | none | full-merged | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 1 | 1 | 0 [-2, 2] n.s. | 1.20× |

## mem.renderer.MB per phase

| Phase | none | full-merged | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 156 | 374 | 218 [158, 279] | 2.40× |

## mem.gpu.MB per phase

| Phase | none | full-merged | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 67 | 89 | 22 [11, 32] | 1.32× |

## wake.gpu/s per phase

| Phase | none | full-merged | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 64 | 63 | -1 [-1, -1] | 0.98× |

## hover.changes per phase

| Phase | none | full-merged | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 0 | 0 | 0 [0, 0] n.s. | – |

## hover.transitions per phase

| Phase | none | full-merged | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 0 | 0 | 0 [0, 0] n.s. | – |
