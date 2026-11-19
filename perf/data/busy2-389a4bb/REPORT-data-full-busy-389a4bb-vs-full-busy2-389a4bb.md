# Test data: full-busy2-389a4bb vs full-busy-389a4bb

Runs: 1=full-389a4bb, 2=full-busy2-389a4bb, 3=full-busy-389a4bb, 4=full-busy-389a4bb, 5=full-busy2-389a4bb, 6=full-389a4bb, 7=full-389a4bb, 8=full-busy2-389a4bb, 9=full-busy-389a4bb, 10=full-busy-389a4bb, 11=full-busy2-389a4bb, 12=full-389a4bb, 13=full-389a4bb, 14=full-busy2-389a4bb, 15=full-busy-389a4bb. Medians of 5; diff = median of 5 paired (full-busy2-389a4bb − full-busy-389a4bb) with 95% bootstrap CI.

## Whole test

| Metric | full-busy-389a4bb | full-busy2-389a4bb | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| cpu.total.s | 19.8 | 20.1 | 0.2 [-34.7, 0.9] n.s. | 1.01× |
| cpu.renderer.s | 15.4 | 15.7 | 0.3 [-33.4, 0.9] n.s. | 1.02× |
| cpu.gpu.s | 3.6 | 3.6 | -0.1 [-1.2, 0.0] n.s. | 0.98× |
| cpu.browser.s | 0.7 | 0.7 | -0.0 [-0.0, 0.0] n.s. | 0.96× |
| energy.impact.mean | 50.5 | 50.1 | 0.7 [-39.9, 0.8] n.s. | 0.99× |
| frames.drawn | 2,067 | 2,049 | -14 [-18, 747] n.s. | 0.99× |
| frames.dropped | 92 | 141 | 48 [-1,790, 53] n.s. | 1.53× |
| mem.renderer.max.MB | 1,184 | 1,177 | -50 [-1,057, 293] n.s. | 0.99× |
| mem.gpu.max.MB | 115 | 119 | 3 [-13, 9] n.s. | 1.04× |
| mem.footprint.max.MB | 1,386 | 1,486 | -40 [-1,608, 414] n.s. | 1.07× |
| mem.footprint.end.MB | 1,347 | 1,415 | -1 [-1,639, 427] n.s. | 1.05× |
| heap.max.MB | 149.2 | 149.9 | 1.2 [-13.5, 12.2] n.s. | 1.00× |
| heap.end.MB | 134.2 | 134.5 | -0.4 [-2.3, 2.0] n.s. | 1.00× |
| phases.wall.s | 36.8 | 37.3 | 0.4 [-15.5, 0.6] n.s. | 1.01× |
| sys.cpu% | 18.3 | 18.3 | -0.4 [-5.6, 19.1] n.s. | 1.00× |

## cpu.total.ms per phase

| Phase | full-busy-389a4bb | full-busy2-389a4bb | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 2,478 | 2,383 | 38 [-393, 103] n.s. | 0.96× |
| scroll@200 | 4,185 | 4,414 | 181 [-19,692, 535] n.s. | 1.05× |
| wheelSlow@200 | 3,486 | 3,537 | 60 [-6,330, 202] n.s. | 1.01× |
| wheel@200 | 1,777 | 1,538 | -239 [-2,148, 191] n.s. | 0.87× |
| wheel@500 | 5,571 | 5,681 | 25 [-3,855, 736] n.s. | 1.02× |
| hover | 2,508 | 2,480 | -84 [-2,746, 2] n.s. | 0.99× |

## cpu.%core per phase

| Phase | full-busy-389a4bb | full-busy2-389a4bb | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 49.5 | 47.6 | 0.8 [-7.9, 2.1] n.s. | 0.96× |
| scroll@200 | 68.1 | 66.6 | -2.1 [-52.5, 2.9] n.s. | 0.98× |
| wheelSlow@200 | 45.5 | 46.2 | 0.7 [-76.4, 2.6] n.s. | 1.02× |
| wheel@200 | 56.6 | 49.1 | -7.5 [-61.0, 6.0] n.s. | 0.87× |
| wheel@500 | 68.7 | 70.0 | 0.2 [-39.0, 9.0] n.s. | 1.02× |
| hover | 37.7 | 37.0 | -1.6 [-34.2, -0.2] | 0.98× |

## energy.impact per phase

| Phase | full-busy-389a4bb | full-busy2-389a4bb | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 47.6 | 49.6 | 0.8 [-4.6, 6.6] n.s. | 1.04× |
| scroll@200 | 64.0 | 67.0 | 2.2 [-48.8, 5.9] n.s. | 1.05× |
| wheelSlow@200 | 41.0 | 41.8 | 1.0 [-51.4, 1.7] n.s. | 1.02× |
| wheel@200 | 41.3 | 44.7 | 3.4 [-25.0, 9.1] n.s. | 1.08× |
| wheel@500 | 62.9 | 63.9 | 0.7 [-30.2, 2.3] n.s. | 1.02× |
| hover | 36.5 | 35.5 | -2.8 [-20.5, 0.3] n.s. | 0.97× |

## frames.drawn per phase

| Phase | full-busy-389a4bb | full-busy2-389a4bb | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 301 | 300 | 0 [-1, 0] n.s. | 1.00× |
| scroll@200 | 361 | 384 | 20 [-38, 26] n.s. | 1.06× |
| wheelSlow@200 | 442 | 433 | -6 [-12, 322] n.s. | 0.98× |
| wheel@200 | 177 | 173 | -1 [-6, 123] n.s. | 0.98× |
| wheel@500 | 458 | 432 | -23 [-26, 355] n.s. | 0.94× |
| hover | 328 | 326 | 1 [-14, 4] n.s. | 0.99× |

## frames.dropped per phase

| Phase | full-busy-389a4bb | full-busy2-389a4bb | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 4 | 5 | 1 [-1, 3] n.s. | 1.25× |
| scroll@200 | 18 | 27 | 8 [-837, 12] n.s. | 1.50× |
| wheelSlow@200 | 16 | 25 | 9 [-365, 11] n.s. | 1.56× |
| wheel@200 | 9 | 13 | 3 [-143, 5] n.s. | 1.44× |
| wheel@500 | 28 | 53 | 23 [-413, 28] n.s. | 1.89× |
| hover | 17 | 20 | 2 [-34, 6] n.s. | 1.18× |

## raf.p95.ms per phase

| Phase | full-busy-389a4bb | full-busy2-389a4bb | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | – | – | – [–, –] n.s. | – |
| scroll@200 | 18.6 | 18.3 | 0.0 [-81.8, 0.1] n.s. | 0.98× |
| wheelSlow@200 | 18.6 | 18.6 | -0.1 [-133.6, 0.3] n.s. | 1.00× |
| wheel@200 | 18.6 | 18.6 | 0.1 [-98.3, 1.3] n.s. | 1.00× |
| wheel@500 | 18.6 | 18.3 | 0.0 [-233.9, 0.2] n.s. | 0.98× |
| hover | 18.5 | 18.6 | -0.1 [-0.2, 0.4] n.s. | 1.01× |

## style.ms per phase

| Phase | full-busy-389a4bb | full-busy2-389a4bb | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 960 | 1,084 | 148 [-48, 188] n.s. | 1.13× |
| scroll@200 | 1,484 | 1,517 | -25 [-16,416, 249] n.s. | 1.02× |
| wheelSlow@200 | 1,306 | 1,259 | -47 [-5,781, 36] n.s. | 0.96× |
| wheel@200 | 574 | 518 | -56 [-2,482, -32] | 0.90× |
| wheel@500 | 2,485 | 2,187 | -300 [-5,913, -179] | 0.88× |
| hover | 512 | 550 | 38 [-149, 76] n.s. | 1.07× |

## layout.ms per phase

| Phase | full-busy-389a4bb | full-busy2-389a4bb | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 4 | 4 | 0 [-0, 1] n.s. | 0.95× |
| scroll@200 | 319 | 340 | -0 [-404, 36] n.s. | 1.07× |
| wheelSlow@200 | 89 | 97 | 9 [-311, 30] n.s. | 1.09× |
| wheel@200 | 122 | 119 | -5 [-35, 23] n.s. | 0.97× |
| wheel@500 | 462 | 506 | 73 [-191, 213] n.s. | 1.09× |
| hover | 232 | 220 | -12 [-387, 61] n.s. | 0.95× |

## mem.renderer.MB per phase

| Phase | full-busy-389a4bb | full-busy2-389a4bb | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 831 | 814 | 20 [-105, 26] n.s. | 0.98× |
| scroll@200 | 919 | 924 | 18 [-502, 256] n.s. | 1.01× |
| wheelSlow@200 | 964 | 1,007 | 50 [-692, 257] n.s. | 1.04× |
| wheel@200 | 1,033 | 1,020 | -13 [-755, 313] n.s. | 0.99× |
| wheel@500 | 1,115 | 1,072 | -43 [-679, 248] n.s. | 0.96× |
| hover | 1,181 | 1,121 | -70 [-314, 275] n.s. | 0.95× |

## mem.gpu.MB per phase

| Phase | full-busy-389a4bb | full-busy2-389a4bb | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 110 | 109 | -1 [-16, 0] n.s. | 0.99× |
| scroll@200 | 113 | 115 | -0 [-13, 11] n.s. | 1.01× |
| wheelSlow@200 | 110 | 118 | 7 [-13, 16] n.s. | 1.07× |
| wheel@200 | 102 | 118 | 9 [-4, 16] n.s. | 1.16× |
| wheel@500 | 104 | 118 | 9 [-7, 15] n.s. | 1.13× |
| hover | 105 | 112 | 7 [-5, 13] n.s. | 1.06× |

## wake.gpu/s per phase

| Phase | full-busy-389a4bb | full-busy2-389a4bb | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 136 | 125 | -12 [-26, 1] n.s. | 0.92× |
| scroll@200 | 126 | 128 | 2 [-4, 4] n.s. | 1.02× |
| wheelSlow@200 | 126 | 127 | 1 [-4, 4] n.s. | 1.00× |
| wheel@200 | 129 | 128 | -1 [-9, 0] n.s. | 0.99× |
| wheel@500 | 129 | 129 | 0 [-3, 14] n.s. | 1.00× |
| hover | 133 | 134 | 0 [-2, 2] n.s. | 1.01× |

## hover.changes per phase

| Phase | full-busy-389a4bb | full-busy2-389a4bb | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 0 | 0 | 0 [0, 0] n.s. | – |
| scroll@200 | 1 | 1 | 0 [0, 0] n.s. | 1.00× |
| wheelSlow@200 | 1 | 1 | 0 [-1, 0] n.s. | 1.00× |
| wheel@200 | 1 | 1 | 0 [-1, 0] n.s. | 1.00× |
| wheel@500 | 1 | 1 | 0 [-2, 0] n.s. | 1.00× |
| hover | 104 | 95 | -9 [-10, -9] | 0.91× |

## hover.transitions per phase

| Phase | full-busy-389a4bb | full-busy2-389a4bb | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 0 | 0 | 0 [0, 0] n.s. | – |
| scroll@200 | 4 | 5 | 1 [1, 1] | 1.25× |
| wheelSlow@200 | 3 | 5 | 2 [-3, 2] n.s. | 1.67× |
| wheel@200 | 3 | 5 | 2 [2, 2] | 1.67× |
| wheel@500 | 3 | 5 | 2 [2, 2] | 1.67× |
| hover | 69 | 70 | 1 [1, 1] | 1.01× |
