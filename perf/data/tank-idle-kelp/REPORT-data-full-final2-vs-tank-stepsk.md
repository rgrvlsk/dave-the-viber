# Test data: tank-stepsk vs full-final2

Runs: 1=full-final2, 2=tank-steps0, 3=tank-stepsk, 4=tank-stepsk, 5=tank-steps0, 6=full-final2. Medians of 2; diff = median of 2 paired (tank-stepsk − full-final2) with 95% bootstrap CI.

## Whole test

| Metric | full-final2 | tank-stepsk | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| cpu.total.s | 5.8 | 12.9 | 7.1 [6.4, 7.9] | 2.23× |
| cpu.renderer.s | 3.8 | 8.5 | 4.7 [4.5, 4.9] | 2.24× |
| cpu.gpu.s | 1.7 | 4.2 | 2.5 [1.9, 3.0] | 2.41× |
| cpu.browser.s | 0.2 | 0.2 | -0.0 [-0.0, -0.0] | 0.84× |
| energy.impact.mean | 20.1 | 42.7 | 22.5 [20.0, 25.1] | 2.12× |
| frames.drawn | 477 | 1,770 | 1,293 [1,285, 1,301] | 3.71× |
| frames.dropped | 60 | 30 | -30 [-34, -26] | 0.50× |
| mem.renderer.max.MB | 882 | 760 | -122 [-154, -90] | 0.86× |
| mem.gpu.max.MB | 96 | 99 | 3 [-3, 9] n.s. | 1.03× |
| mem.footprint.max.MB | 1,314 | 1,226 | -88 [-97, -80] | 0.93× |
| mem.footprint.end.MB | 1,030 | 1,076 | 47 [-108, 202] n.s. | 1.05× |
| heap.max.MB | 143.3 | 137.1 | -6.2 [-12.8, 0.5] n.s. | 0.96× |
| heap.end.MB | 133.6 | 133.3 | -0.3 [-0.9, 0.2] n.s. | 1.00× |
| phases.wall.s | 30.0 | 30.0 | 0.0 [0.0, 0.0] n.s. | 1.00× |
| sys.cpu% | 16.2 | 20.4 | 4.2 [2.4, 5.9] | 1.26× |

## cpu.total.ms per phase

| Phase | full-final2 | tank-stepsk | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 5,805 | 12,940 | 7,134 [6,395, 7,874] | 2.23× |

## cpu.%core per phase

| Phase | full-final2 | tank-stepsk | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 19.3 | 43.1 | 23.8 [21.3, 26.2] | 2.23× |

## energy.impact per phase

| Phase | full-final2 | tank-stepsk | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 20.1 | 42.7 | 22.5 [20.0, 25.1] | 2.12× |

## frames.drawn per phase

| Phase | full-final2 | tank-stepsk | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 477 | 1,770 | 1,293 [1,285, 1,301] | 3.71× |

## frames.dropped per phase

| Phase | full-final2 | tank-stepsk | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 60 | 30 | -30 [-34, -26] | 0.50× |

## raf.p95.ms per phase

| Phase | full-final2 | tank-stepsk | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | – | – | – [–, –] n.s. | – |

## style.ms per phase

| Phase | full-final2 | tank-stepsk | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 1,344 | 5,186 | 3,842 [3,839, 3,846] | 3.86× |

## layout.ms per phase

| Phase | full-final2 | tank-stepsk | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 27 | 27 | 0 [-1, 1] n.s. | 1.01× |

## mem.renderer.MB per phase

| Phase | full-final2 | tank-stepsk | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 782 | 693 | -88 [-276, 99] n.s. | 0.89× |

## mem.gpu.MB per phase

| Phase | full-final2 | tank-stepsk | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 93 | 96 | 2 [-5, 10] n.s. | 1.03× |

## wake.gpu/s per phase

| Phase | full-final2 | tank-stepsk | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 126 | 125 | -1 [-2, -1] | 0.99× |

## hover.changes per phase

| Phase | full-final2 | tank-stepsk | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 0 | 0 | 0 [0, 0] n.s. | – |

## hover.transitions per phase

| Phase | full-final2 | tank-stepsk | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 0 | 0 | 0 [0, 0] n.s. | – |
