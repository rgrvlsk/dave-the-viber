# Test data: tank-final vs none

Runs: 1=none, 2=full-merged, 3=tank-final, 4=tank-final, 5=full-merged, 6=none. Medians of 2; diff = median of 2 paired (tank-final − none) with 95% bootstrap CI.

## Whole test

| Metric | none | tank-final | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| cpu.total.s | 0.7 | 3.6 | 2.8 [2.4, 3.3] | 4.91× |
| cpu.renderer.s | 0.2 | 2.8 | 2.6 [2.3, 3.0] | 15.90× |
| cpu.gpu.s | 0.3 | 0.5 | 0.2 [0.1, 0.3] | 1.76× |
| cpu.browser.s | 0.2 | 0.1 | -0.0 [-0.1, 0.0] n.s. | 0.77× |
| energy.impact.mean | 2.5 | 11.1 | 8.6 [7.1, 10.2] | 4.47× |
| frames.drawn | 60 | 242 | 182 [180, 183] | 4.00× |
| frames.dropped | 0 | 1 | 1 [0, 2] n.s. | – |
| mem.renderer.max.MB | 238 | 437 | 199 [146, 252] | 1.84× |
| mem.gpu.max.MB | 75 | 86 | 11 [5, 18] | 1.15× |
| mem.footprint.max.MB | 1,210 | 1,122 | -88 [-121, -54] | 0.93× |
| mem.footprint.end.MB | 796 | 732 | -64 [-77, -51] | 0.92× |
| heap.max.MB | 156.1 | 143.2 | -12.8 [-14.1, -11.6] | 0.92× |
| heap.end.MB | 134.3 | 132.6 | -1.7 [-2.1, -1.2] | 0.99× |
| phases.wall.s | 30.0 | 30.0 | -0.0 [-0.0, 0.0] n.s. | 1.00× |
| sys.cpu% | 58.2 | 54.1 | -4.2 [-16.0, 7.7] n.s. | 0.93× |

## cpu.total.ms per phase

| Phase | none | tank-final | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 725 | 3,563 | 2,838 [2,353, 3,323] | 4.91× |

## cpu.%core per phase

| Phase | none | tank-final | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 2.4 | 11.9 | 9.5 [7.8, 11.1] | 4.91× |

## energy.impact per phase

| Phase | none | tank-final | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 2.5 | 11.1 | 8.6 [7.1, 10.2] | 4.47× |

## frames.drawn per phase

| Phase | none | tank-final | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 60 | 242 | 182 [180, 183] | 4.00× |

## frames.dropped per phase

| Phase | none | tank-final | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 0 | 1 | 1 [0, 2] n.s. | – |

## raf.p95.ms per phase

| Phase | none | tank-final | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | – | – | – [–, –] n.s. | – |

## style.ms per phase

| Phase | none | tank-final | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 0 | 1,034 | 1,034 [891, 1,178] | – |

## layout.ms per phase

| Phase | none | tank-final | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 1 | 1 | 0 [0, 1] n.s. | 1.41× |

## mem.renderer.MB per phase

| Phase | none | tank-final | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 156 | 351 | 195 [155, 236] | 2.25× |

## mem.gpu.MB per phase

| Phase | none | tank-final | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 67 | 81 | 14 [8, 21] | 1.22× |

## wake.gpu/s per phase

| Phase | none | tank-final | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 64 | 116 | 51 [51, 52] | 1.80× |

## hover.changes per phase

| Phase | none | tank-final | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 0 | 0 | 0 [0, 0] n.s. | – |

## hover.transitions per phase

| Phase | none | tank-final | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 0 | 0 | 0 [0, 0] n.s. | – |
