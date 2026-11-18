# Test data: full-nobgtx vs full

Runs: 1=full, 2=full-nobgtx, 3=full-norottx, 4=full-norottx, 5=full-nobgtx, 6=full, 7=full, 8=full-nobgtx, 9=full-norottx, 10=full-norottx, 11=full-nobgtx, 12=full, 13=full, 14=full-nobgtx, 15=full-norottx. Medians of 5; diff = median of 5 paired (full-nobgtx − full) with 95% bootstrap CI.

## Whole test

| Metric | full | full-nobgtx | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| cpu.total.s | 34.0 | 32.8 | -1.6 [-2.3, -0.6] | 0.97× |
| cpu.renderer.s | 23.3 | 22.9 | -0.7 [-1.3, -0.0] | 0.98× |
| cpu.gpu.s | 9.4 | 8.6 | -0.7 [-0.9, -0.5] | 0.91× |
| cpu.browser.s | 1.1 | 1.1 | -0.0 [-0.1, -0.0] | 0.97× |
| energy.impact.mean | 80.5 | 77.5 | -3.2 [-6.8, -1.3] | 0.96× |
| frames.drawn | 2,222 | 2,225 | 4 [-2, 12] n.s. | 1.00× |
| frames.dropped | 159 | 135 | -21 [-78, -11] | 0.85× |
| mem.renderer.max.MB | 1,054 | 1,206 | 153 [-21, 182] n.s. | 1.14× |
| mem.gpu.max.MB | 102 | 109 | 1 [-7, 11] n.s. | 1.08× |
| mem.footprint.max.MB | 1,762 | 1,812 | 27 [-66, 145] n.s. | 1.03× |
| mem.footprint.end.MB | 1,677 | 1,665 | 8 [-40, 116] n.s. | 0.99× |
| heap.max.MB | 152.0 | 154.1 | 2.4 [-6.5, 16.7] n.s. | 1.01× |
| heap.end.MB | 136.6 | 135.8 | -0.5 [-3.1, 4.4] n.s. | 0.99× |
| phases.wall.s | 37.0 | 37.0 | 0.1 [-0.0, 0.2] n.s. | 1.00× |
| sys.cpu% | 42.0 | 36.3 | -3.6 [-11.7, -0.8] | 0.86× |

## cpu.total.ms per phase

| Phase | full | full-nobgtx | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 2,196 | 2,205 | -36 [-193, 100] n.s. | 1.00× |
| scroll@200 | 7,535 | 7,749 | -15 [-1,348, 388] n.s. | 1.03× |
| wheelSlow@200 | 6,640 | 5,557 | -1,035 [-1,709, 575] n.s. | 0.84× |
| wheel@200 | 3,408 | 3,466 | -20 [-600, 549] n.s. | 1.02× |
| wheel@500 | 10,711 | 10,810 | 277 [-1,011, 942] n.s. | 1.01× |
| hover | 3,703 | 3,338 | -516 [-698, 45] n.s. | 0.90× |

## cpu.%core per phase

| Phase | full | full-nobgtx | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 43.9 | 44.1 | -0.7 [-3.8, 2.0] n.s. | 1.00× |
| scroll@200 | 118.9 | 121.4 | 0.7 [-18.6, 4.0] n.s. | 1.02× |
| wheelSlow@200 | 86.4 | 71.9 | -13.6 [-22.5, 7.1] n.s. | 0.83× |
| wheel@200 | 108.2 | 109.2 | -1.8 [-17.6, 17.9] n.s. | 1.01× |
| wheel@500 | 131.6 | 129.8 | 2.5 [-11.8, 8.7] n.s. | 0.99× |
| hover | 55.5 | 50.0 | -7.5 [-10.5, -0.2] | 0.90× |

## energy.impact per phase

| Phase | full | full-nobgtx | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 45.6 | 44.4 | -0.7 [-6.1, 6.9] n.s. | 0.97× |
| scroll@200 | 104.4 | 104.2 | -2.2 [-16.7, 5.9] n.s. | 1.00× |
| wheelSlow@200 | 72.0 | 64.6 | -8.2 [-20.6, 8.5] n.s. | 0.90× |
| wheel@200 | 73.7 | 80.1 | 8.6 [-11.1, 16.3] n.s. | 1.09× |
| wheel@500 | 114.7 | 114.3 | -2.7 [-8.4, 5.2] n.s. | 1.00× |
| hover | 55.1 | 50.1 | -8.4 [-10.7, 1.6] n.s. | 0.91× |

## frames.drawn per phase

| Phase | full | full-nobgtx | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 300 | 301 | 0 [-1, 1] n.s. | 1.00× |
| scroll@200 | 381 | 382 | 2 [-10, 7] n.s. | 1.00× |
| wheelSlow@200 | 463 | 464 | 1 [0, 2] n.s. | 1.00× |
| wheel@200 | 190 | 190 | 0 [-2, 2] n.s. | 1.00× |
| wheel@500 | 489 | 490 | 1 [-2, 11] n.s. | 1.00× |
| hover | 401 | 399 | 0 [-4, 6] n.s. | 1.00× |

## frames.dropped per phase

| Phase | full | full-nobgtx | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 5 | 5 | -1 [-1, 0] n.s. | 1.00× |
| scroll@200 | 30 | 31 | 2 [-11, 7] n.s. | 1.03× |
| wheelSlow@200 | 31 | 25 | -5 [-10, 2] n.s. | 0.81× |
| wheel@200 | 18 | 15 | -3 [-10, 4] n.s. | 0.83× |
| wheel@500 | 70 | 53 | -19 [-63, 0] n.s. | 0.76× |
| hover | 7 | 7 | 0 [-4, 5] n.s. | 1.00× |

## raf.p95.ms per phase

| Phase | full | full-nobgtx | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | – | – | – [–, –] n.s. | – |
| scroll@200 | 18.6 | 18.6 | 0.0 [-0.1, 0.1] n.s. | 1.00× |
| wheelSlow@200 | 18.6 | 18.6 | 0.1 [-0.1, 0.1] n.s. | 1.00× |
| wheel@200 | 18.6 | 18.6 | -0.0 [-0.1, 0.2] n.s. | 1.00× |
| wheel@500 | 18.7 | 18.6 | -0.1 [-16.4, 0.0] n.s. | 0.99× |
| hover | 18.5 | 18.5 | 0.0 [0.0, 0.1] n.s. | 1.00× |

## style.ms per phase

| Phase | full | full-nobgtx | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 1,023 | 1,035 | 57 [-20, 138] n.s. | 1.01× |
| scroll@200 | 2,560 | 2,571 | -47 [-364, 306] n.s. | 1.00× |
| wheelSlow@200 | 2,107 | 1,913 | -114 [-330, 47] n.s. | 0.91× |
| wheel@200 | 1,142 | 1,084 | -85 [-108, 124] n.s. | 0.95× |
| wheel@500 | 4,085 | 4,139 | 218 [-735, 403] n.s. | 1.01× |
| hover | 1,078 | 1,120 | 92 [-160, 378] n.s. | 1.04× |

## layout.ms per phase

| Phase | full | full-nobgtx | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 4 | 5 | 0 [-0, 1] n.s. | 1.07× |
| scroll@200 | 401 | 405 | 8 [-91, 40] n.s. | 1.01× |
| wheelSlow@200 | 402 | 404 | -42 [-231, 202] n.s. | 1.00× |
| wheel@200 | 237 | 213 | -27 [-62, 27] n.s. | 0.90× |
| wheel@500 | 696 | 667 | 10 [-275, 264] n.s. | 0.96× |
| hover | 273 | 217 | -38 [-64, 76] n.s. | 0.79× |

## mem.renderer.MB per phase

| Phase | full | full-nobgtx | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 693 | 641 | -214 [-289, 61] n.s. | 0.92× |
| scroll@200 | 740 | 684 | 55 [-151, 137] n.s. | 0.92× |
| wheelSlow@200 | 664 | 823 | 159 [-71, 292] n.s. | 1.24× |
| wheel@200 | 549 | 1,056 | 432 [-188, 643] n.s. | 1.92× |
| wheel@500 | 776 | 1,135 | 330 [-50, 390] n.s. | 1.46× |
| hover | 713 | 1,114 | 436 [-261, 640] n.s. | 1.56× |

## mem.gpu.MB per phase

| Phase | full | full-nobgtx | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 94 | 92 | -6 [-15, 2] n.s. | 0.98× |
| scroll@200 | 99 | 97 | -1 [-8, 1] n.s. | 0.98× |
| wheelSlow@200 | 98 | 100 | 8 [-4, 13] n.s. | 1.02× |
| wheel@200 | 95 | 104 | 12 [4, 17] | 1.09× |
| wheel@500 | 95 | 107 | 11 [3, 20] | 1.13× |
| hover | 92 | 106 | 9 [5, 19] | 1.14× |

## wake.gpu/s per phase

| Phase | full | full-nobgtx | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 124 | 123 | -1 [-8, 1] n.s. | 0.99× |
| scroll@200 | 131 | 131 | 0 [-34, 7] n.s. | 1.00× |
| wheelSlow@200 | 131 | 128 | -3 [-5, 1] n.s. | 0.98× |
| wheel@200 | 129 | 130 | -1 [-16, 2] n.s. | 1.00× |
| wheel@500 | 130 | 129 | -1 [-3, 3] n.s. | 0.99× |
| hover | 132 | 127 | -5 [-8, 0] n.s. | 0.97× |

## hover.changes per phase

| Phase | full | full-nobgtx | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 0 | 0 | 0 [0, 0] n.s. | – |
| scroll@200 | 334 | 334 | 0 [0, 0] n.s. | 1.00× |
| wheelSlow@200 | 192 | 200 | 10 [-7, 15] n.s. | 1.04× |
| wheel@200 | 126 | 131 | 5 [-7, 9] n.s. | 1.04× |
| wheel@500 | 379 | 395 | 15 [-6, 69] n.s. | 1.04× |
| hover | 104 | 104 | 0 [-1, 1] n.s. | 1.00× |

## hover.transitions per phase

| Phase | full | full-nobgtx | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 0 | 0 | 0 [0, 0] n.s. | – |
| scroll@200 | 343 | 58 | -288 [-290, -275] | 0.17× |
| wheelSlow@200 | 395 | 278 | -119 [-128, -109] | 0.70× |
| wheel@200 | 199 | 91 | -104 [-128, -98] | 0.46× |
| wheel@500 | 434 | 119 | -300 [-354, -274] | 0.27× |
| hover | 104 | 69 | -35 [-35, -35] | 0.66× |
