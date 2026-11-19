# Test data: tank-inf vs full-final2

Runs: 1=full-final2, 2=tank-inf, 3=tank-steps, 4=tank-steps0, 5=tank-tr0, 6=tank-tr0, 7=tank-steps0, 8=tank-steps, 9=tank-inf, 10=full-final2. Medians of 2; diff = median of 2 paired (tank-inf − full-final2) with 95% bootstrap CI.

## Whole test

| Metric | full-final2 | tank-inf | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| cpu.total.s | 4.4 | 14.3 | 9.9 [7.8, 12.1] | 3.26× |
| cpu.renderer.s | 3.0 | 9.7 | 6.7 [5.1, 8.4] | 3.28× |
| cpu.gpu.s | 1.1 | 4.4 | 3.3 [2.7, 3.8] | 3.85× |
| cpu.browser.s | 0.2 | 0.2 | -0.0 [-0.1, -0.0] | 0.83× |
| energy.impact.mean | 15.2 | 47.8 | 32.6 [24.6, 40.7] | 3.15× |
| frames.drawn | 303 | 1,762 | 1,459 [1,282, 1,636] | 5.82× |
| frames.dropped | 52 | 38 | -14 [-42, 15] n.s. | 0.74× |
| mem.renderer.max.MB | 523 | 858 | 334 [220, 449] | 1.64× |
| mem.gpu.max.MB | 99 | 102 | 3 [0, 6] | 1.03× |
| mem.footprint.max.MB | 1,192 | 1,290 | 98 [44, 153] | 1.08× |
| mem.footprint.end.MB | 740 | 1,134 | 394 [242, 547] | 1.53× |
| heap.max.MB | 143.0 | 148.7 | 5.7 [0.1, 11.2] | 1.04× |
| heap.end.MB | 134.9 | 132.9 | -1.9 [-3.0, -0.9] | 0.99× |
| phases.wall.s | 30.0 | 30.0 | -0.0 [-0.0, 0.0] n.s. | 1.00× |
| sys.cpu% | 23.9 | 19.4 | -4.5 [-14.7, 5.7] n.s. | 0.81× |

## cpu.total.ms per phase

| Phase | full-final2 | tank-inf | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 4,405 | 14,346 | 9,942 [7,757, 12,126] | 3.26× |

## cpu.%core per phase

| Phase | full-final2 | tank-inf | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 14.7 | 47.8 | 33.1 [25.9, 40.4] | 3.26× |

## energy.impact per phase

| Phase | full-final2 | tank-inf | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 15.2 | 47.8 | 32.6 [24.6, 40.7] | 3.15× |

## frames.drawn per phase

| Phase | full-final2 | tank-inf | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 303 | 1,762 | 1,459 [1,282, 1,636] | 5.82× |

## frames.dropped per phase

| Phase | full-final2 | tank-inf | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 52 | 38 | -14 [-42, 15] n.s. | 0.74× |

## raf.p95.ms per phase

| Phase | full-final2 | tank-inf | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | – | – | – [–, –] n.s. | – |

## style.ms per phase

| Phase | full-final2 | tank-inf | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 1,051 | 6,266 | 5,215 [4,123, 6,307] | 5.96× |

## layout.ms per phase

| Phase | full-final2 | tank-inf | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 23 | 28 | 5 [1, 9] | 1.21× |

## mem.renderer.MB per phase

| Phase | full-final2 | tank-inf | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 492 | 783 | 291 [178, 405] | 1.59× |

## mem.gpu.MB per phase

| Phase | full-final2 | tank-inf | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 94 | 101 | 7 [1, 12] | 1.07× |

## wake.gpu/s per phase

| Phase | full-final2 | tank-inf | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 81 | 124 | 43 [-2, 88] n.s. | 1.53× |

## hover.changes per phase

| Phase | full-final2 | tank-inf | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 0 | 0 | 0 [0, 0] n.s. | – |

## hover.transitions per phase

| Phase | full-final2 | tank-inf | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 0 | 0 | 0 [0, 0] n.s. | – |
