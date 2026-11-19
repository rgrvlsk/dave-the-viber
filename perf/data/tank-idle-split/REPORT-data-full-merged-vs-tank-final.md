# Test data: tank-final vs full-merged

Runs: 1=none, 2=full-merged, 3=tank-final, 4=tank-final-nob, 5=tank-inf, 6=tank-inf, 7=tank-final-nob, 8=tank-final, 9=full-merged, 10=none. Medians of 2; diff = median of 2 paired (tank-final − full-merged) with 95% bootstrap CI.

## Whole test

| Metric | full-merged | tank-final | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| cpu.total.s | 0.7 | 2.9 | 2.2 [1.9, 2.6] | 4.38× |
| cpu.renderer.s | 0.3 | 2.0 | 1.7 [1.4, 2.0] | 6.69× |
| cpu.gpu.s | 0.2 | 0.7 | 0.5 [0.5, 0.5] | 3.55× |
| cpu.browser.s | 0.1 | 0.1 | 0.0 [-0.0, 0.0] n.s. | 1.08× |
| energy.impact.mean | 2.8 | 10.6 | 7.9 [6.8, 9.0] | 3.85× |
| frames.drawn | 61 | 325 | 264 [191, 337] | 5.33× |
| frames.dropped | 21 | 2 | -20 [-22, -17] | 0.07× |
| mem.renderer.max.MB | 428 | 428 | 1 [-29, 31] n.s. | 1.00× |
| mem.gpu.max.MB | 92 | 89 | -3 [-11, 6] n.s. | 0.97× |
| mem.footprint.max.MB | 1,170 | 1,164 | -6 [-20, 9] n.s. | 1.00× |
| mem.footprint.end.MB | 680 | 791 | 111 [98, 124] | 1.16× |
| heap.max.MB | 139.1 | 153.0 | 13.9 [2.5, 25.2] | 1.10× |
| heap.end.MB | 133.9 | 133.2 | -0.6 [-1.3, -0.0] | 1.00× |
| phases.wall.s | 30.0 | 30.0 | 0.0 [0.0, 0.0] n.s. | 1.00× |
| sys.cpu% | 50.1 | 40.4 | -9.6 [-22.4, 3.2] n.s. | 0.81× |

## cpu.total.ms per phase

| Phase | full-merged | tank-final | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 662 | 2,896 | 2,234 [1,905, 2,563] | 4.38× |

## cpu.%core per phase

| Phase | full-merged | tank-final | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 2.2 | 9.7 | 7.4 [6.3, 8.5] | 4.38× |

## energy.impact per phase

| Phase | full-merged | tank-final | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 2.8 | 10.6 | 7.9 [6.8, 9.0] | 3.85× |

## frames.drawn per phase

| Phase | full-merged | tank-final | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 61 | 325 | 264 [191, 337] | 5.33× |

## frames.dropped per phase

| Phase | full-merged | tank-final | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 21 | 2 | -20 [-22, -17] | 0.07× |

## raf.p95.ms per phase

| Phase | full-merged | tank-final | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | – | – | – [–, –] n.s. | – |

## style.ms per phase

| Phase | full-merged | tank-final | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 0 | 616 | 616 [419, 814] | – |

## layout.ms per phase

| Phase | full-merged | tank-final | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 4 | 1 | -4 [-7, -0] | 0.16× |

## mem.renderer.MB per phase

| Phase | full-merged | tank-final | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 307 | 372 | 65 [36, 95] | 1.21× |

## mem.gpu.MB per phase

| Phase | full-merged | tank-final | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 83 | 83 | -0 [-6, 6] n.s. | 1.00× |

## wake.gpu/s per phase

| Phase | full-merged | tank-final | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 63 | 117 | 53 [51, 55] | 1.84× |

## hover.changes per phase

| Phase | full-merged | tank-final | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 0 | 0 | 0 [0, 0] n.s. | – |

## hover.transitions per phase

| Phase | full-merged | tank-final | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 0 | 0 | 0 [0, 0] n.s. | – |
