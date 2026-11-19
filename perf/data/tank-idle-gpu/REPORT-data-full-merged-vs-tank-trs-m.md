# Test data: tank-trs-m vs full-merged

Runs: 1=full-merged, 2=tank-steps0-m, 3=tank-tr0-m, 4=tank-trs-m, 5=tank-trs-m, 6=tank-tr0-m, 7=tank-steps0-m, 8=full-merged. Medians of 2; diff = median of 2 paired (tank-trs-m − full-merged) with 95% bootstrap CI.

## Whole test

| Metric | full-merged | tank-trs-m | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| cpu.total.s | 4.7 | 6.0 | 1.3 [0.9, 1.7] | 1.28× |
| cpu.renderer.s | 3.3 | 4.6 | 1.3 [0.8, 1.8] | 1.41× |
| cpu.gpu.s | 1.2 | 1.2 | 0.0 [-0.1, 0.1] n.s. | 1.03× |
| cpu.browser.s | 0.2 | 0.1 | -0.0 [-0.0, -0.0] | 0.75× |
| energy.impact.mean | 15.6 | 18.9 | 3.3 [2.8, 3.8] | 1.21× |
| frames.drawn | 480 | 692 | 213 [206, 220] | 1.44× |
| frames.dropped | 64 | 66 | 2 [-5, 9] n.s. | 1.03× |
| mem.renderer.max.MB | 683 | 859 | 176 [155, 197] | 1.26× |
| mem.gpu.max.MB | 95 | 96 | 1 [1, 1] | 1.01× |
| mem.footprint.max.MB | 1,282 | 1,324 | 42 [34, 50] | 1.03× |
| mem.footprint.end.MB | 1,095 | 1,238 | 143 [126, 160] | 1.13× |
| heap.max.MB | 151.3 | 153.6 | 2.3 [-1.6, 6.3] n.s. | 1.02× |
| heap.end.MB | 136.7 | 133.2 | -3.5 [-3.6, -3.3] | 0.97× |
| phases.wall.s | 30.0 | 30.0 | 0.0 [0.0, 0.0] | 1.00× |
| sys.cpu% | 22.9 | 49.2 | 26.3 [4.1, 48.4] | 2.15× |

## cpu.total.ms per phase

| Phase | full-merged | tank-trs-m | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 4,683 | 6,008 | 1,324 [904, 1,745] | 1.28× |

## cpu.%core per phase

| Phase | full-merged | tank-trs-m | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 15.6 | 20.0 | 4.4 [3.0, 5.8] | 1.28× |

## energy.impact per phase

| Phase | full-merged | tank-trs-m | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 15.6 | 18.9 | 3.3 [2.8, 3.8] | 1.21× |

## frames.drawn per phase

| Phase | full-merged | tank-trs-m | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 480 | 692 | 213 [206, 220] | 1.44× |

## frames.dropped per phase

| Phase | full-merged | tank-trs-m | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 64 | 66 | 2 [-5, 9] n.s. | 1.03× |

## raf.p95.ms per phase

| Phase | full-merged | tank-trs-m | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | – | – | – [–, –] n.s. | – |

## style.ms per phase

| Phase | full-merged | tank-trs-m | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 1,247 | 2,670 | 1,424 [840, 2,007] | 2.14× |

## layout.ms per phase

| Phase | full-merged | tank-trs-m | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 48 | 53 | 6 [-0, 11] n.s. | 1.12× |

## mem.renderer.MB per phase

| Phase | full-merged | tank-trs-m | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 616 | 681 | 64 [-18, 147] n.s. | 1.10× |

## mem.gpu.MB per phase

| Phase | full-merged | tank-trs-m | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 93 | 93 | 0 [0, 1] | 1.00× |

## wake.gpu/s per phase

| Phase | full-merged | tank-trs-m | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 127 | 127 | 1 [-0, 1] n.s. | 1.00× |

## hover.changes per phase

| Phase | full-merged | tank-trs-m | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 0 | 0 | 0 [0, 0] n.s. | – |

## hover.transitions per phase

| Phase | full-merged | tank-trs-m | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 0 | 0 | 0 [0, 0] n.s. | – |
