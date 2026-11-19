# Test data: tank-trs-m vs tank-steps0-m

Runs: 1=full-merged, 2=tank-steps0-m, 3=tank-tr0-m, 4=tank-trs-m, 5=tank-trs-m, 6=tank-tr0-m, 7=tank-steps0-m, 8=full-merged. Medians of 2; diff = median of 2 paired (tank-trs-m − tank-steps0-m) with 95% bootstrap CI.

## Whole test

| Metric | tank-steps0-m | tank-trs-m | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| cpu.total.s | 6.7 | 6.0 | -0.7 [-1.0, -0.4] | 0.90× |
| cpu.renderer.s | 4.8 | 4.6 | -0.2 [-0.4, 0.0] n.s. | 0.96× |
| cpu.gpu.s | 1.7 | 1.2 | -0.4 [-0.6, -0.3] | 0.74× |
| cpu.browser.s | 0.2 | 0.1 | -0.1 [-0.1, -0.0] | 0.70× |
| energy.impact.mean | 23.2 | 18.9 | -4.3 [-6.7, -2.0] | 0.81× |
| frames.drawn | 703 | 692 | -10 [-33, 12] n.s. | 0.99× |
| frames.dropped | 66 | 66 | -1 [-4, 2] n.s. | 0.98× |
| mem.renderer.max.MB | 547 | 859 | 312 [193, 431] | 1.57× |
| mem.gpu.max.MB | 94 | 96 | 2 [-6, 10] n.s. | 1.02× |
| mem.footprint.max.MB | 1,217 | 1,324 | 106 [-62, 275] n.s. | 1.09× |
| mem.footprint.end.MB | 971 | 1,238 | 267 [-50, 584] n.s. | 1.27× |
| heap.max.MB | 141.7 | 153.6 | 11.9 [-2.6, 26.3] n.s. | 1.08× |
| heap.end.MB | 132.8 | 133.2 | 0.4 [0.0, 0.8] | 1.00× |
| phases.wall.s | 30.0 | 30.0 | 0.0 [-0.0, 0.0] n.s. | 1.00× |
| sys.cpu% | 21.4 | 49.2 | 27.8 [5.4, 50.3] | 2.30× |

## cpu.total.ms per phase

| Phase | tank-steps0-m | tank-trs-m | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 6,701 | 6,008 | -694 [-1,024, -363] | 0.90× |

## cpu.%core per phase

| Phase | tank-steps0-m | tank-trs-m | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 22.3 | 20.0 | -2.3 [-3.4, -1.2] | 0.90× |

## energy.impact per phase

| Phase | tank-steps0-m | tank-trs-m | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 23.2 | 18.9 | -4.3 [-6.7, -2.0] | 0.81× |

## frames.drawn per phase

| Phase | tank-steps0-m | tank-trs-m | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 703 | 692 | -10 [-33, 12] n.s. | 0.99× |

## frames.dropped per phase

| Phase | tank-steps0-m | tank-trs-m | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 66 | 66 | -1 [-4, 2] n.s. | 0.98× |

## raf.p95.ms per phase

| Phase | tank-steps0-m | tank-trs-m | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | – | – | – [–, –] n.s. | – |

## style.ms per phase

| Phase | tank-steps0-m | tank-trs-m | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 2,289 | 2,670 | 381 [116, 646] | 1.17× |

## layout.ms per phase

| Phase | tank-steps0-m | tank-trs-m | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 51 | 53 | 3 [-2, 7] n.s. | 1.05× |

## mem.renderer.MB per phase

| Phase | tank-steps0-m | tank-trs-m | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 443 | 681 | 238 [175, 301] | 1.54× |

## mem.gpu.MB per phase

| Phase | tank-steps0-m | tank-trs-m | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 90 | 93 | 3 [-6, 12] n.s. | 1.03× |

## wake.gpu/s per phase

| Phase | tank-steps0-m | tank-trs-m | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 126 | 127 | 1 [0, 2] | 1.01× |

## hover.changes per phase

| Phase | tank-steps0-m | tank-trs-m | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 0 | 0 | 0 [0, 0] n.s. | – |

## hover.transitions per phase

| Phase | tank-steps0-m | tank-trs-m | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 0 | 0 | 0 [0, 0] n.s. | – |
