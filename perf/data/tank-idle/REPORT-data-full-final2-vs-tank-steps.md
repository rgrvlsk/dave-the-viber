# Test data: tank-steps vs full-final2

Runs: 1=full-final2, 2=tank-inf, 3=tank-steps, 4=tank-steps0, 5=tank-tr0, 6=tank-tr0, 7=tank-steps0, 8=tank-steps, 9=tank-inf, 10=full-final2. Medians of 2; diff = median of 2 paired (tank-steps − full-final2) with 95% bootstrap CI.

## Whole test

| Metric | full-final2 | tank-steps | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| cpu.total.s | 4.4 | 14.9 | 10.4 [8.0, 12.9] | 3.37× |
| cpu.renderer.s | 3.0 | 10.1 | 7.1 [6.0, 8.3] | 3.41× |
| cpu.gpu.s | 1.1 | 4.5 | 3.4 [2.1, 4.7] | 3.97× |
| cpu.browser.s | 0.2 | 0.2 | -0.1 [-0.1, -0.0] | 0.78× |
| energy.impact.mean | 15.2 | 50.5 | 35.3 [26.2, 44.5] | 3.33× |
| frames.drawn | 303 | 1,768 | 1,464 [1,287, 1,642] | 5.83× |
| frames.dropped | 52 | 32 | -20 [-47, 8] n.s. | 0.62× |
| mem.renderer.max.MB | 523 | 809 | 286 [231, 342] | 1.55× |
| mem.gpu.max.MB | 99 | 104 | 5 [0, 9] | 1.05× |
| mem.footprint.max.MB | 1,192 | 1,182 | -10 [-41, 22] n.s. | 0.99× |
| mem.footprint.end.MB | 740 | 1,039 | 299 [275, 323] | 1.40× |
| heap.max.MB | 143.0 | 139.3 | -3.7 [-11.2, 3.7] n.s. | 0.97× |
| heap.end.MB | 134.9 | 133.8 | -1.1 [-2.2, 0.1] n.s. | 0.99× |
| phases.wall.s | 30.0 | 30.0 | -0.0 [-0.0, 0.0] n.s. | 1.00× |
| sys.cpu% | 23.9 | 18.7 | -5.1 [-16.0, 5.8] n.s. | 0.79× |

## cpu.total.ms per phase

| Phase | full-final2 | tank-steps | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 4,405 | 14,852 | 10,448 [7,979, 12,916] | 3.37× |

## cpu.%core per phase

| Phase | full-final2 | tank-steps | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 14.7 | 49.5 | 34.8 [26.6, 43.1] | 3.37× |

## energy.impact per phase

| Phase | full-final2 | tank-steps | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 15.2 | 50.5 | 35.3 [26.2, 44.5] | 3.33× |

## frames.drawn per phase

| Phase | full-final2 | tank-steps | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 303 | 1,768 | 1,464 [1,287, 1,642] | 5.83× |

## frames.dropped per phase

| Phase | full-final2 | tank-steps | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 52 | 32 | -20 [-47, 8] n.s. | 0.62× |

## raf.p95.ms per phase

| Phase | full-final2 | tank-steps | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | – | – | – [–, –] n.s. | – |

## style.ms per phase

| Phase | full-final2 | tank-steps | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 1,051 | 6,392 | 5,341 [5,081, 5,602] | 6.08× |

## layout.ms per phase

| Phase | full-final2 | tank-steps | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 23 | 26 | 3 [-1, 7] n.s. | 1.14× |

## mem.renderer.MB per phase

| Phase | full-final2 | tank-steps | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 492 | 774 | 282 [210, 354] | 1.57× |

## mem.gpu.MB per phase

| Phase | full-final2 | tank-steps | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 94 | 103 | 8 [1, 16] | 1.09× |

## wake.gpu/s per phase

| Phase | full-final2 | tank-steps | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 81 | 124 | 43 [-2, 88] n.s. | 1.53× |

## hover.changes per phase

| Phase | full-final2 | tank-steps | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 0 | 0 | 0 [0, 0] n.s. | – |

## hover.transitions per phase

| Phase | full-final2 | tank-steps | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 0 | 0 | 0 [0, 0] n.s. | – |
