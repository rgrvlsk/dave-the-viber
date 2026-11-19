# Test data: tank-final vs tank-final-nob

Runs: 1=none, 2=full-merged, 3=tank-final, 4=tank-final-nob, 5=tank-inf, 6=tank-inf, 7=tank-final-nob, 8=tank-final, 9=full-merged, 10=none. Medians of 2; diff = median of 2 paired (tank-final − tank-final-nob) with 95% bootstrap CI.

## Whole test

| Metric | tank-final-nob | tank-final | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| cpu.total.s | 1.8 | 2.9 | 1.1 [0.6, 1.5] | 1.57× |
| cpu.renderer.s | 1.1 | 2.0 | 0.9 [0.6, 1.3] | 1.86× |
| cpu.gpu.s | 0.5 | 0.7 | 0.1 [0.1, 0.1] | 1.21× |
| cpu.browser.s | 0.1 | 0.1 | -0.0 [-0.0, 0.0] n.s. | 0.94× |
| energy.impact.mean | 6.5 | 10.6 | 4.2 [1.9, 6.4] | 1.64× |
| frames.drawn | 267 | 325 | 58 [10, 106] | 1.22× |
| frames.dropped | 14 | 2 | -12 [-15, -9] | 0.11× |
| mem.renderer.max.MB | 347 | 428 | 81 [32, 131] | 1.23× |
| mem.gpu.max.MB | 91 | 89 | -2 [-4, -0] | 0.98× |
| mem.footprint.max.MB | 1,120 | 1,164 | 45 [13, 77] | 1.04× |
| mem.footprint.end.MB | 706 | 791 | 84 [67, 102] | 1.12× |
| heap.max.MB | 143.2 | 153.0 | 9.8 [-1.2, 20.8] n.s. | 1.07× |
| heap.end.MB | 133.1 | 133.2 | 0.1 [-0.8, 1.0] n.s. | 1.00× |
| phases.wall.s | 30.0 | 30.0 | -0.0 [-0.0, 0.0] n.s. | 1.00× |
| sys.cpu% | 48.3 | 40.4 | -7.9 [-19.0, 3.3] n.s. | 0.84× |

## cpu.total.ms per phase

| Phase | tank-final-nob | tank-final | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 1,844 | 2,896 | 1,052 [634, 1,470] | 1.57× |

## cpu.%core per phase

| Phase | tank-final-nob | tank-final | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 6.1 | 9.7 | 3.5 [2.1, 4.9] | 1.57× |

## energy.impact per phase

| Phase | tank-final-nob | tank-final | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 6.5 | 10.6 | 4.2 [1.9, 6.4] | 1.64× |

## frames.drawn per phase

| Phase | tank-final-nob | tank-final | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 267 | 325 | 58 [10, 106] | 1.22× |

## frames.dropped per phase

| Phase | tank-final-nob | tank-final | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 14 | 2 | -12 [-15, -9] | 0.11× |

## raf.p95.ms per phase

| Phase | tank-final-nob | tank-final | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | – | – | – [–, –] n.s. | – |

## style.ms per phase

| Phase | tank-final-nob | tank-final | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 257 | 616 | 360 [141, 579] | 2.40× |

## layout.ms per phase

| Phase | tank-final-nob | tank-final | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 15 | 1 | -14 [-17, -11] | 0.05× |

## mem.renderer.MB per phase

| Phase | tank-final-nob | tank-final | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 336 | 372 | 36 [7, 66] | 1.11× |

## mem.gpu.MB per phase

| Phase | tank-final-nob | tank-final | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 85 | 83 | -2 [-4, -0] | 0.97× |

## wake.gpu/s per phase

| Phase | tank-final-nob | tank-final | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 112 | 117 | 4 [4, 5] | 1.04× |

## hover.changes per phase

| Phase | tank-final-nob | tank-final | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 0 | 0 | 0 [0, 0] n.s. | – |

## hover.transitions per phase

| Phase | tank-final-nob | tank-final | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 0 | 0 | 0 [0, 0] n.s. | – |
