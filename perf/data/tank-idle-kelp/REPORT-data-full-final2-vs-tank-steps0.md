# Test data: tank-steps0 vs full-final2

Runs: 1=full-final2, 2=tank-steps0, 3=tank-stepsk, 4=tank-stepsk, 5=tank-steps0, 6=full-final2. Medians of 2; diff = median of 2 paired (tank-steps0 − full-final2) with 95% bootstrap CI.

## Whole test

| Metric | full-final2 | tank-steps0 | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| cpu.total.s | 5.8 | 7.0 | 1.2 [0.4, 1.9] | 1.20× |
| cpu.renderer.s | 3.8 | 5.0 | 1.2 [0.6, 1.7] | 1.31× |
| cpu.gpu.s | 1.7 | 1.8 | 0.0 [-0.1, 0.2] n.s. | 1.02× |
| cpu.browser.s | 0.2 | 0.2 | -0.0 [-0.1, -0.0] | 0.82× |
| energy.impact.mean | 20.1 | 24.8 | 4.7 [2.6, 6.7] | 1.23× |
| frames.drawn | 477 | 717 | 240 [226, 254] | 1.50× |
| frames.dropped | 60 | 58 | -2 [-4, 0] n.s. | 0.97× |
| mem.renderer.max.MB | 882 | 780 | -102 [-180, -23] | 0.88× |
| mem.gpu.max.MB | 96 | 103 | 8 [4, 12] | 1.08× |
| mem.footprint.max.MB | 1,314 | 1,206 | -108 [-196, -19] | 0.92× |
| mem.footprint.end.MB | 1,030 | 945 | -84 [-260, 91] n.s. | 0.92× |
| heap.max.MB | 143.3 | 149.9 | 6.6 [-3.7, 16.9] n.s. | 1.05× |
| heap.end.MB | 133.6 | 134.0 | 0.4 [-0.1, 1.0] n.s. | 1.00× |
| phases.wall.s | 30.0 | 30.0 | 0.0 [0.0, 0.0] n.s. | 1.00× |
| sys.cpu% | 16.2 | 20.3 | 4.1 [2.9, 5.3] | 1.25× |

## cpu.total.ms per phase

| Phase | full-final2 | tank-steps0 | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 5,805 | 6,972 | 1,167 [414, 1,920] | 1.20× |

## cpu.%core per phase

| Phase | full-final2 | tank-steps0 | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 19.3 | 23.2 | 3.9 [1.4, 6.4] | 1.20× |

## energy.impact per phase

| Phase | full-final2 | tank-steps0 | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 20.1 | 24.8 | 4.7 [2.6, 6.7] | 1.23× |

## frames.drawn per phase

| Phase | full-final2 | tank-steps0 | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 477 | 717 | 240 [226, 254] | 1.50× |

## frames.dropped per phase

| Phase | full-final2 | tank-steps0 | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 60 | 58 | -2 [-4, 0] n.s. | 0.97× |

## raf.p95.ms per phase

| Phase | full-final2 | tank-steps0 | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | – | – | – [–, –] n.s. | – |

## style.ms per phase

| Phase | full-final2 | tank-steps0 | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 1,344 | 2,553 | 1,209 [1,082, 1,336] | 1.90× |

## layout.ms per phase

| Phase | full-final2 | tank-steps0 | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 27 | 27 | 1 [-0, 2] n.s. | 1.03× |

## mem.renderer.MB per phase

| Phase | full-final2 | tank-steps0 | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 782 | 581 | -201 [-287, -115] | 0.74× |

## mem.gpu.MB per phase

| Phase | full-final2 | tank-steps0 | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 93 | 94 | 1 [-2, 4] n.s. | 1.01× |

## wake.gpu/s per phase

| Phase | full-final2 | tank-steps0 | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 126 | 127 | 1 [0, 1] | 1.01× |

## hover.changes per phase

| Phase | full-final2 | tank-steps0 | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 0 | 0 | 0 [0, 0] n.s. | – |

## hover.transitions per phase

| Phase | full-final2 | tank-steps0 | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 0 | 0 | 0 [0, 0] n.s. | – |
