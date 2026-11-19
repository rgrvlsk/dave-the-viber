# Test data: tank-tr0-m vs full-merged

Runs: 1=full-merged, 2=tank-steps0-m, 3=tank-tr0-m, 4=tank-trs-m, 5=tank-trs-m, 6=tank-tr0-m, 7=tank-steps0-m, 8=full-merged. Medians of 2; diff = median of 2 paired (tank-tr0-m − full-merged) with 95% bootstrap CI.

## Whole test

| Metric | full-merged | tank-tr0-m | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| cpu.total.s | 4.7 | 8.1 | 3.5 [2.8, 4.1] | 1.74× |
| cpu.renderer.s | 3.3 | 5.5 | 2.2 [1.9, 2.6] | 1.69× |
| cpu.gpu.s | 1.2 | 2.4 | 1.2 [0.9, 1.5] | 2.00× |
| cpu.browser.s | 0.2 | 0.2 | -0.0 [-0.0, 0.0] n.s. | 0.98× |
| energy.impact.mean | 15.6 | 27.7 | 12.2 [9.8, 14.5] | 1.78× |
| frames.drawn | 480 | 1,800 | 1,321 [1,317, 1,325] | 3.75× |
| frames.dropped | 64 | 64 | 0 [-1, 2] n.s. | 1.01× |
| mem.renderer.max.MB | 683 | 744 | 62 [-193, 316] n.s. | 1.09× |
| mem.gpu.max.MB | 95 | 88 | -7 [-27, 14] n.s. | 0.93× |
| mem.footprint.max.MB | 1,282 | 1,338 | 56 [-132, 245] n.s. | 1.04× |
| mem.footprint.end.MB | 1,095 | 1,082 | -14 [-404, 377] n.s. | 0.99× |
| heap.max.MB | 151.3 | 159.7 | 8.4 [-1.5, 18.3] n.s. | 1.06× |
| heap.end.MB | 136.7 | 133.4 | -3.3 [-3.9, -2.7] | 0.98× |
| phases.wall.s | 30.0 | 30.0 | 0.0 [-0.0, 0.0] n.s. | 1.00× |
| sys.cpu% | 22.9 | 30.7 | 7.8 [6.2, 9.4] | 1.34× |

## cpu.total.ms per phase

| Phase | full-merged | tank-tr0-m | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 4,683 | 8,133 | 3,450 [2,770, 4,130] | 1.74× |

## cpu.%core per phase

| Phase | full-merged | tank-tr0-m | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 15.6 | 27.1 | 11.5 [9.2, 13.8] | 1.74× |

## energy.impact per phase

| Phase | full-merged | tank-tr0-m | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 15.6 | 27.7 | 12.2 [9.8, 14.5] | 1.78× |

## frames.drawn per phase

| Phase | full-merged | tank-tr0-m | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 480 | 1,800 | 1,321 [1,317, 1,325] | 3.75× |

## frames.dropped per phase

| Phase | full-merged | tank-tr0-m | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 64 | 64 | 0 [-1, 2] n.s. | 1.01× |

## raf.p95.ms per phase

| Phase | full-merged | tank-tr0-m | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | – | – | – [–, –] n.s. | – |

## style.ms per phase

| Phase | full-merged | tank-tr0-m | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 1,247 | 2,806 | 1,559 [1,145, 1,972] | 2.25× |

## layout.ms per phase

| Phase | full-merged | tank-tr0-m | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 48 | 54 | 7 [6, 8] | 1.15× |

## mem.renderer.MB per phase

| Phase | full-merged | tank-tr0-m | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 616 | 679 | 62 [-77, 201] n.s. | 1.10× |

## mem.gpu.MB per phase

| Phase | full-merged | tank-tr0-m | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 93 | 86 | -7 [-28, 14] n.s. | 0.92× |

## wake.gpu/s per phase

| Phase | full-merged | tank-tr0-m | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 127 | 127 | 0 [-0, 1] n.s. | 1.00× |

## hover.changes per phase

| Phase | full-merged | tank-tr0-m | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 0 | 0 | 0 [0, 0] n.s. | – |

## hover.transitions per phase

| Phase | full-merged | tank-tr0-m | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 0 | 0 | 0 [0, 0] n.s. | – |
