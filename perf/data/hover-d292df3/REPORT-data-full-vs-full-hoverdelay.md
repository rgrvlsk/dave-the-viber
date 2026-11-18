# Test data: full-hoverdelay vs full

Runs: 1=full, 2=full-hoverdelay, 3=full-notx, 4=full-notx, 5=full-hoverdelay, 6=full, 7=full, 8=full-hoverdelay, 9=full-notx, 10=full-notx, 11=full-hoverdelay, 12=full, 13=full, 14=full-hoverdelay, 15=full-notx. Medians of 5; diff = median of 5 paired (full-hoverdelay − full) with 95% bootstrap CI.

## Whole test

| Metric | full | full-hoverdelay | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| cpu.total.s | 33.9 | 33.1 | -1.0 [-1.8, -0.1] | 0.98× |
| cpu.renderer.s | 23.5 | 23.0 | -0.7 [-1.2, 0.4] n.s. | 0.98× |
| cpu.gpu.s | 9.4 | 9.0 | -0.4 [-0.5, -0.2] | 0.96× |
| cpu.browser.s | 1.1 | 1.1 | -0.0 [-0.1, 0.0] n.s. | 0.97× |
| energy.impact.mean | 79.5 | 79.1 | -0.2 [-3.8, 1.1] n.s. | 1.00× |
| frames.drawn | 2,223 | 2,219 | -4 [-13, 7] n.s. | 1.00× |
| frames.dropped | 149 | 143 | -6 [-37, 9] n.s. | 0.96× |
| mem.renderer.max.MB | 1,068 | 1,108 | 33 [-62, 207] n.s. | 1.04× |
| mem.gpu.max.MB | 102 | 101 | 1 [-2, 22] n.s. | 0.99× |
| mem.footprint.max.MB | 1,755 | 1,780 | 26 [-81, 96] n.s. | 1.01× |
| mem.footprint.end.MB | 1,660 | 1,667 | 24 [-61, 85] n.s. | 1.00× |
| heap.max.MB | 152.3 | 152.8 | -4.7 [-17.0, 7.2] n.s. | 1.00× |
| heap.end.MB | 137.6 | 136.0 | -1.5 [-3.4, 1.5] n.s. | 0.99× |
| phases.wall.s | 37.0 | 36.9 | -0.0 [-0.2, 0.1] n.s. | 1.00× |
| sys.cpu% | 43.5 | 38.7 | -1.3 [-11.6, -0.9] | 0.89× |

## cpu.total.ms per phase

| Phase | full | full-hoverdelay | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 2,195 | 2,383 | 45 [-417, 237] n.s. | 1.09× |
| scroll@200 | 7,353 | 7,325 | 32 [-1,200, 1,258] n.s. | 1.00× |
| wheelSlow@200 | 6,553 | 5,551 | -940 [-1,517, 438] n.s. | 0.85× |
| wheel@200 | 3,491 | 3,388 | 43 [-840, 873] n.s. | 0.97× |
| wheel@500 | 10,321 | 10,780 | 720 [-1,156, 1,267] n.s. | 1.04× |
| hover | 3,657 | 3,575 | -69 [-1,571, 210] n.s. | 0.98× |

## cpu.%core per phase

| Phase | full | full-hoverdelay | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 43.9 | 47.7 | 0.9 [-8.3, 4.7] n.s. | 1.09× |
| scroll@200 | 116.5 | 116.0 | -0.4 [-16.5, 17.2] n.s. | 1.00× |
| wheelSlow@200 | 84.5 | 72.1 | -12.4 [-19.0, 6.0] n.s. | 0.85× |
| wheel@200 | 111.6 | 107.8 | 1.6 [-27.6, 27.9] n.s. | 0.97× |
| wheel@500 | 127.0 | 132.3 | 8.8 [-14.1, 16.2] n.s. | 1.04× |
| hover | 55.4 | 53.5 | -1.9 [-21.6, 3.2] n.s. | 0.97× |

## energy.impact per phase

| Phase | full | full-hoverdelay | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 43.5 | 44.0 | 0.5 [-11.8, 5.7] n.s. | 1.01× |
| scroll@200 | 101.1 | 104.8 | 3.6 [-16.3, 16.2] n.s. | 1.04× |
| wheelSlow@200 | 74.6 | 65.7 | -9.8 [-13.2, 0.0] n.s. | 0.88× |
| wheel@200 | 68.9 | 78.4 | 3.0 [-9.7, 14.5] n.s. | 1.14× |
| wheel@500 | 108.8 | 116.2 | 7.8 [-13.0, 18.1] n.s. | 1.07× |
| hover | 53.8 | 49.8 | -1.2 [-11.1, 1.0] n.s. | 0.93× |

## frames.drawn per phase

| Phase | full | full-hoverdelay | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 301 | 300 | 0 [-2, 2] n.s. | 1.00× |
| scroll@200 | 380 | 378 | -2 [-9, 8] n.s. | 0.99× |
| wheelSlow@200 | 465 | 462 | -2 [-4, 1] n.s. | 0.99× |
| wheel@200 | 189 | 189 | 0 [-2, 2] n.s. | 1.00× |
| wheel@500 | 489 | 489 | 0 [-3, 0] n.s. | 1.00× |
| hover | 397 | 399 | 3 [-12, 6] n.s. | 1.01× |

## frames.dropped per phase

| Phase | full | full-hoverdelay | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 5 | 6 | 0 [-12, 2] n.s. | 1.20× |
| scroll@200 | 28 | 27 | -1 [-10, 7] n.s. | 0.96× |
| wheelSlow@200 | 27 | 25 | 0 [-3, 6] n.s. | 0.93× |
| wheel@200 | 18 | 17 | 2 [-14, 6] n.s. | 0.94× |
| wheel@500 | 56 | 56 | 4 [-33, 10] n.s. | 1.00× |
| hover | 6 | 6 | 0 [-8, 2] n.s. | 1.00× |

## raf.p95.ms per phase

| Phase | full | full-hoverdelay | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | – | – | – [–, –] n.s. | – |
| scroll@200 | 18.5 | 18.6 | 0.1 [-0.0, 0.1] n.s. | 1.01× |
| wheelSlow@200 | 18.6 | 18.5 | 0.0 [-0.1, 0.0] n.s. | 0.99× |
| wheel@200 | 18.7 | 18.6 | -0.2 [-16.4, 14.3] n.s. | 0.99× |
| wheel@500 | 18.6 | 18.7 | 0.1 [-15.1, 14.1] n.s. | 1.01× |
| hover | 18.6 | 18.6 | 0.0 [-0.1, 0.0] n.s. | 1.00× |

## style.ms per phase

| Phase | full | full-hoverdelay | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 1,049 | 991 | -43 [-106, 20] n.s. | 0.95× |
| scroll@200 | 2,465 | 2,474 | -104 [-436, 368] n.s. | 1.00× |
| wheelSlow@200 | 1,959 | 1,970 | -56 [-289, 254] n.s. | 1.01× |
| wheel@200 | 1,192 | 1,208 | 158 [-570, 276] n.s. | 1.01× |
| wheel@500 | 3,930 | 4,132 | 330 [-215, 382] n.s. | 1.05× |
| hover | 1,150 | 1,033 | 2 [-513, 157] n.s. | 0.90× |

## layout.ms per phase

| Phase | full | full-hoverdelay | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 5 | 5 | -0 [-1, 1] n.s. | 0.99× |
| scroll@200 | 395 | 404 | 8 [-36, 45] n.s. | 1.02× |
| wheelSlow@200 | 454 | 219 | -214 [-287, -128] | 0.48× |
| wheel@200 | 230 | 202 | 11 [-192, 19] n.s. | 0.88× |
| wheel@500 | 602 | 641 | 80 [-18, 107] n.s. | 1.06× |
| hover | 225 | 220 | -2 [-48, 14] n.s. | 0.98× |

## mem.renderer.MB per phase

| Phase | full | full-hoverdelay | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 564 | 615 | 32 [-197, 453] n.s. | 1.09× |
| scroll@200 | 680 | 678 | 24 [-92, 222] n.s. | 1.00× |
| wheelSlow@200 | 798 | 683 | 50 [-327, 65] n.s. | 0.86× |
| wheel@200 | 614 | 645 | 55 [-268, 446] n.s. | 1.05× |
| wheel@500 | 807 | 822 | -40 [-183, 154] n.s. | 1.02× |
| hover | 572 | 589 | 26 [-209, 502] n.s. | 1.03× |

## mem.gpu.MB per phase

| Phase | full | full-hoverdelay | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 91 | 93 | 3 [-5, 33] n.s. | 1.03× |
| scroll@200 | 98 | 97 | 1 [-3, 26] n.s. | 0.99× |
| wheelSlow@200 | 98 | 96 | -1 [-5, 22] n.s. | 0.98× |
| wheel@200 | 97 | 96 | 2 [-8, 24] n.s. | 0.99× |
| wheel@500 | 95 | 97 | 1 [-1, 24] n.s. | 1.02× |
| hover | 92 | 94 | 1 [-4, 20] n.s. | 1.03× |

## wake.gpu/s per phase

| Phase | full | full-hoverdelay | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 124 | 123 | -4 [-6, 1] n.s. | 1.00× |
| scroll@200 | 129 | 131 | 4 [-8, 8] n.s. | 1.02× |
| wheelSlow@200 | 130 | 130 | -0 [-13, 4] n.s. | 1.00× |
| wheel@200 | 129 | 132 | 8 [-12, 12] n.s. | 1.02× |
| wheel@500 | 129 | 128 | -1 [-3, 2] n.s. | 0.99× |
| hover | 129 | 129 | -0 [-4, 6] n.s. | 1.00× |

## hover.changes per phase

| Phase | full | full-hoverdelay | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 0 | 0 | 0 [0, 0] n.s. | – |
| scroll@200 | 334 | 334 | 0 [0, 0] n.s. | 1.00× |
| wheelSlow@200 | 202 | 125 | -76 [-86, -70] | 0.62× |
| wheel@200 | 124 | 120 | -5 [-10, 2] n.s. | 0.97× |
| wheel@500 | 385 | 389 | 2 [-29, 44] n.s. | 1.01× |
| hover | 104 | 105 | 1 [0, 2] n.s. | 1.01× |

## hover.transitions per phase

| Phase | full | full-hoverdelay | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 0 | 0 | 0 [0, 0] n.s. | – |
| scroll@200 | 345 | 356 | 11 [5, 21] | 1.03× |
| wheelSlow@200 | 408 | 387 | -21 [-28, -9] | 0.95× |
| wheel@200 | 196 | 210 | 14 [-21, 61] n.s. | 1.07× |
| wheel@500 | 441 | 496 | 43 [21, 79] | 1.12× |
| hover | 104 | 104 | 0 [0, 0] n.s. | 1.00× |
