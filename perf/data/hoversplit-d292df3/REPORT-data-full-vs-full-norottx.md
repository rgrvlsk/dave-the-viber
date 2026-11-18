# Test data: full-norottx vs full

Runs: 1=full, 2=full-nobgtx, 3=full-norottx, 4=full-norottx, 5=full-nobgtx, 6=full, 7=full, 8=full-nobgtx, 9=full-norottx, 10=full-norottx, 11=full-nobgtx, 12=full, 13=full, 14=full-nobgtx, 15=full-norottx. Medians of 5; diff = median of 5 paired (full-norottx − full) with 95% bootstrap CI.

## Whole test

| Metric | full | full-norottx | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| cpu.total.s | 34.0 | 33.9 | 0.2 [-1.9, 0.3] n.s. | 1.00× |
| cpu.renderer.s | 23.3 | 23.8 | 0.8 [-1.3, 1.1] n.s. | 1.02× |
| cpu.gpu.s | 9.4 | 8.7 | -0.5 [-0.9, -0.5] | 0.93× |
| cpu.browser.s | 1.1 | 1.1 | 0.0 [-0.1, 0.0] n.s. | 0.99× |
| energy.impact.mean | 80.5 | 78.3 | -1.7 [-3.3, -0.0] | 0.97× |
| frames.drawn | 2,222 | 2,221 | 0 [-6, 4] n.s. | 1.00× |
| frames.dropped | 159 | 160 | 12 [-47, 26] n.s. | 1.01× |
| mem.renderer.max.MB | 1,054 | 1,077 | -14 [-79, 74] n.s. | 1.02× |
| mem.gpu.max.MB | 102 | 98 | -15 [-26, 0] n.s. | 0.96× |
| mem.footprint.max.MB | 1,762 | 1,723 | -32 [-191, 75] n.s. | 0.98× |
| mem.footprint.end.MB | 1,677 | 1,654 | -9 [-137, 122] n.s. | 0.99× |
| heap.max.MB | 152.0 | 158.6 | 6.6 [-1.9, 13.3] n.s. | 1.04× |
| heap.end.MB | 136.6 | 135.9 | -0.2 [-1.7, 0.3] n.s. | 1.00× |
| phases.wall.s | 37.0 | 37.0 | -0.0 [-0.1, 0.1] n.s. | 1.00× |
| sys.cpu% | 42.0 | 41.4 | 2.7 [-11.5, 5.1] n.s. | 0.98× |

## cpu.total.ms per phase

| Phase | full | full-norottx | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 2,196 | 2,179 | -50 [-332, 262] n.s. | 0.99× |
| scroll@200 | 7,535 | 7,272 | -263 [-994, 139] n.s. | 0.97× |
| wheelSlow@200 | 6,640 | 6,458 | -24 [-206, 440] n.s. | 0.97× |
| wheel@200 | 3,408 | 3,473 | -132 [-593, 753] n.s. | 1.02× |
| wheel@500 | 10,711 | 10,658 | -169 [-785, 1,224] n.s. | 1.00× |
| hover | 3,703 | 3,619 | -32 [-650, 717] n.s. | 0.98× |

## cpu.%core per phase

| Phase | full | full-norottx | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 43.9 | 43.6 | -1.0 [-6.6, 5.2] n.s. | 0.99× |
| scroll@200 | 118.9 | 114.1 | -4.7 [-15.3, 1.6] n.s. | 0.96× |
| wheelSlow@200 | 86.4 | 83.9 | -0.3 [-2.4, 5.5] n.s. | 0.97× |
| wheel@200 | 108.2 | 110.9 | -3.6 [-16.3, 24.5] n.s. | 1.02× |
| wheel@500 | 131.6 | 131.1 | -1.9 [-10.1, 14.5] n.s. | 1.00× |
| hover | 55.5 | 54.7 | -0.5 [-9.2, 10.5] n.s. | 0.98× |

## energy.impact per phase

| Phase | full | full-norottx | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 45.6 | 42.3 | -2.8 [-5.3, 4.6] n.s. | 0.93× |
| scroll@200 | 104.4 | 100.3 | -4.2 [-12.2, 1.4] n.s. | 0.96× |
| wheelSlow@200 | 72.0 | 73.1 | 1.2 [-4.7, 7.8] n.s. | 1.02× |
| wheel@200 | 73.7 | 76.7 | 10.1 [-14.5, 14.3] n.s. | 1.04× |
| wheel@500 | 114.7 | 109.9 | -2.6 [-13.7, 3.9] n.s. | 0.96× |
| hover | 55.1 | 51.6 | -1.7 [-10.8, 1.2] n.s. | 0.94× |

## frames.drawn per phase

| Phase | full | full-norottx | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 300 | 301 | 0 [0, 3] n.s. | 1.00× |
| scroll@200 | 381 | 379 | 2 [-6, 4] n.s. | 0.99× |
| wheelSlow@200 | 463 | 463 | 1 [-2, 3] n.s. | 1.00× |
| wheel@200 | 190 | 189 | -1 [-4, 2] n.s. | 0.99× |
| wheel@500 | 489 | 491 | 2 [-4, 4] n.s. | 1.00× |
| hover | 401 | 398 | -2 [-4, 2] n.s. | 0.99× |

## frames.dropped per phase

| Phase | full | full-norottx | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 5 | 5 | 0 [-1, 4] n.s. | 1.00× |
| scroll@200 | 30 | 28 | 2 [-7, 4] n.s. | 0.93× |
| wheelSlow@200 | 31 | 28 | -3 [-10, 6] n.s. | 0.90× |
| wheel@200 | 18 | 16 | -2 [-9, 11] n.s. | 0.89× |
| wheel@500 | 70 | 74 | 0 [-42, 38] n.s. | 1.06× |
| hover | 7 | 8 | 0 [-3, 8] n.s. | 1.14× |

## raf.p95.ms per phase

| Phase | full | full-norottx | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | – | – | – [–, –] n.s. | – |
| scroll@200 | 18.6 | 18.6 | 0.0 [-0.1, 0.1] n.s. | 1.00× |
| wheelSlow@200 | 18.6 | 18.6 | 0.0 [-0.0, 0.1] n.s. | 1.00× |
| wheel@200 | 18.6 | 18.6 | 0.0 [-0.2, 0.2] n.s. | 1.00× |
| wheel@500 | 18.7 | 33.2 | 1.5 [-1.7, 15.6] n.s. | 1.78× |
| hover | 18.5 | 18.5 | 0.0 [0.0, 0.1] n.s. | 1.00× |

## style.ms per phase

| Phase | full | full-norottx | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 1,023 | 1,079 | 111 [-70, 246] n.s. | 1.05× |
| scroll@200 | 2,560 | 2,391 | -65 [-227, 38] n.s. | 0.93× |
| wheelSlow@200 | 2,107 | 2,204 | 115 [-102, 336] n.s. | 1.05× |
| wheel@200 | 1,142 | 1,161 | -84 [-131, 243] n.s. | 1.02× |
| wheel@500 | 4,085 | 4,049 | -236 [-638, 511] n.s. | 0.99× |
| hover | 1,078 | 1,146 | 112 [17, 278] | 1.06× |

## layout.ms per phase

| Phase | full | full-norottx | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 4 | 5 | 1 [-0, 4] n.s. | 1.17× |
| scroll@200 | 401 | 758 | 361 [181, 429] | 1.89× |
| wheelSlow@200 | 402 | 254 | -202 [-335, -76] | 0.63× |
| wheel@200 | 237 | 311 | 38 [9, 125] | 1.31× |
| wheel@500 | 696 | 1,067 | 332 [49, 641] | 1.53× |
| hover | 273 | 44 | -198 [-309, -130] | 0.16× |

## mem.renderer.MB per phase

| Phase | full | full-norottx | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 693 | 317 | -376 [-659, 118] n.s. | 0.46× |
| scroll@200 | 740 | 714 | -75 [-220, 242] n.s. | 0.96× |
| wheelSlow@200 | 664 | 626 | -160 [-263, 239] n.s. | 0.94× |
| wheel@200 | 549 | 608 | -36 [-269, 292] n.s. | 1.11× |
| wheel@500 | 776 | 711 | -121 [-258, 72] n.s. | 0.92× |
| hover | 713 | 684 | 53 [-419, 514] n.s. | 0.96× |

## mem.gpu.MB per phase

| Phase | full | full-norottx | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 94 | 84 | -23 [-31, -0] | 0.90× |
| scroll@200 | 99 | 96 | -8 [-24, -1] | 0.97× |
| wheelSlow@200 | 98 | 84 | -9 [-24, 0] n.s. | 0.85× |
| wheel@200 | 95 | 82 | -8 [-18, 0] n.s. | 0.86× |
| wheel@500 | 95 | 81 | -8 [-19, 3] n.s. | 0.85× |
| hover | 92 | 85 | -8 [-18, 8] n.s. | 0.92× |

## wake.gpu/s per phase

| Phase | full | full-norottx | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 124 | 123 | -0 [-4, -0] | 1.00× |
| scroll@200 | 131 | 130 | 0 [-36, 16] n.s. | 0.99× |
| wheelSlow@200 | 131 | 129 | -3 [-3, 6] n.s. | 0.99× |
| wheel@200 | 129 | 129 | 0 [-13, 2] n.s. | 1.00× |
| wheel@500 | 130 | 131 | 1 [-1, 5] n.s. | 1.01× |
| hover | 132 | 128 | -4 [-5, 3] n.s. | 0.97× |

## hover.changes per phase

| Phase | full | full-norottx | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 0 | 0 | 0 [0, 0] n.s. | – |
| scroll@200 | 334 | 334 | 0 [0, 0] n.s. | 1.00× |
| wheelSlow@200 | 192 | 118 | -74 [-79, -51] | 0.61× |
| wheel@200 | 126 | 133 | 7 [3, 13] | 1.06× |
| wheel@500 | 379 | 381 | -1 [-1, 57] n.s. | 1.01× |
| hover | 104 | 110 | 6 [5, 6] | 1.06× |

## hover.transitions per phase

| Phase | full | full-norottx | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 0 | 0 | 0 [0, 0] n.s. | – |
| scroll@200 | 343 | 395 | 52 [19, 78] | 1.15× |
| wheelSlow@200 | 395 | 310 | -85 [-104, -77] | 0.78× |
| wheel@200 | 199 | 203 | 5 [-8, 29] n.s. | 1.02× |
| wheel@500 | 434 | 462 | 32 [-60, 84] n.s. | 1.06× |
| hover | 104 | 86 | -18 [-18, -18] | 0.83× |
