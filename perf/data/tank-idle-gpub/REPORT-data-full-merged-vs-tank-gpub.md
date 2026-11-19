# Test data: tank-gpub vs full-merged

Runs: 1=full-merged, 2=tank-final, 3=tank-gpub, 4=tank-gpub, 5=tank-final, 6=full-merged. Medians of 2; diff = median of 2 paired (tank-gpub − full-merged) with 95% bootstrap CI.

## Whole test

| Metric | full-merged | tank-gpub | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| cpu.total.s | 1.4 | 3.9 | 2.5 [1.7, 3.2] | 2.76× |
| cpu.renderer.s | 0.8 | 2.9 | 2.1 [1.4, 2.8] | 3.54× |
| cpu.gpu.s | 0.3 | 0.7 | 0.4 [0.3, 0.5] | 2.13× |
| cpu.browser.s | 0.2 | 0.2 | -0.0 [-0.0, -0.0] | 0.90× |
| energy.impact.mean | 6.3 | 13.1 | 6.8 [3.9, 9.7] | 2.07× |
| frames.drawn | 88 | 283 | 196 [173, 218] | 3.23× |
| frames.dropped | 49 | 16 | -34 [-44, -23] | 0.32× |
| mem.renderer.max.MB | 503 | 386 | -117 [-166, -68] | 0.77× |
| mem.gpu.max.MB | 83 | 86 | 3 [-11, 17] n.s. | 1.03× |
| mem.footprint.max.MB | 1,293 | 1,250 | -42 [-73, -12] | 0.97× |
| mem.footprint.end.MB | 650 | 784 | 133 [111, 155] | 1.20× |
| heap.max.MB | 149.6 | 155.5 | 5.9 [-0.9, 12.7] n.s. | 1.04× |
| heap.end.MB | 133.8 | 132.9 | -0.8 [-2.0, 0.3] n.s. | 0.99× |
| phases.wall.s | 30.0 | 30.0 | 0.0 [0.0, 0.0] n.s. | 1.00× |
| sys.cpu% | 34.3 | 54.4 | 20.1 [14.5, 25.6] | 1.59× |

## cpu.total.ms per phase

| Phase | full-merged | tank-gpub | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 1,410 | 3,890 | 2,480 [1,713, 3,247] | 2.76× |

## cpu.%core per phase

| Phase | full-merged | tank-gpub | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 4.7 | 13.0 | 8.3 [5.7, 10.8] | 2.76× |

## energy.impact per phase

| Phase | full-merged | tank-gpub | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 6.3 | 13.1 | 6.8 [3.9, 9.7] | 2.07× |

## frames.drawn per phase

| Phase | full-merged | tank-gpub | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 88 | 283 | 196 [173, 218] | 3.23× |

## frames.dropped per phase

| Phase | full-merged | tank-gpub | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 49 | 16 | -34 [-44, -23] | 0.32× |

## raf.p95.ms per phase

| Phase | full-merged | tank-gpub | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | – | – | – [–, –] n.s. | – |

## style.ms per phase

| Phase | full-merged | tank-gpub | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 170 | 990 | 819 [538, 1,100] | 5.81× |

## layout.ms per phase

| Phase | full-merged | tank-gpub | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 9 | 16 | 6 [-2, 15] n.s. | 1.68× |

## mem.renderer.MB per phase

| Phase | full-merged | tank-gpub | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 370 | 347 | -23 [-87, 41] n.s. | 0.94× |

## mem.gpu.MB per phase

| Phase | full-merged | tank-gpub | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 75 | 82 | 7 [-9, 22] n.s. | 1.09× |

## wake.gpu/s per phase

| Phase | full-merged | tank-gpub | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 65 | 116 | 50 [49, 52] | 1.77× |

## hover.changes per phase

| Phase | full-merged | tank-gpub | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 0 | 0 | 0 [0, 0] n.s. | – |

## hover.transitions per phase

| Phase | full-merged | tank-gpub | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 0 | 0 | 0 [0, 0] n.s. | – |
