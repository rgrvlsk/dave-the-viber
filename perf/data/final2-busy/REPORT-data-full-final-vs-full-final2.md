# Test data: full-final2 vs full-final

Runs: 1=full-final, 2=full-final2, 3=none, 4=none, 5=full-final2, 6=full-final, 7=full-final, 8=full-final2, 9=none, 10=none, 11=full-final2, 12=full-final, 13=full-final, 14=full-final2, 15=none. Medians of 5; diff = median of 5 paired (full-final2 − full-final) with 95% bootstrap CI.

## Whole test

| Metric | full-final | full-final2 | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| cpu.total.s | 18.8 | 19.8 | 0.8 [-0.2, 1.3] n.s. | 1.05× |
| cpu.renderer.s | 14.5 | 15.3 | 0.7 [-0.3, 1.1] n.s. | 1.06× |
| cpu.gpu.s | 3.5 | 3.6 | 0.1 [-0.1, 0.3] n.s. | 1.01× |
| cpu.browser.s | 0.7 | 0.7 | 0.0 [-0.0, 0.1] n.s. | 1.03× |
| energy.impact.mean | 47.2 | 48.0 | -0.0 [-2.5, 4.1] n.s. | 1.02× |
| frames.drawn | 2,069 | 2,071 | 0 [-9, 14] n.s. | 1.00× |
| frames.dropped | 96 | 95 | 2 [-1, 16] n.s. | 0.99× |
| mem.renderer.max.MB | 1,209 | 1,161 | -90 [-190, 163] n.s. | 0.96× |
| mem.gpu.max.MB | 117 | 104 | -2 [-31, 4] n.s. | 0.88× |
| mem.footprint.max.MB | 1,607 | 1,627 | 143 [-185, 281] n.s. | 1.01× |
| mem.footprint.end.MB | 1,594 | 1,623 | 109 [-189, 314] n.s. | 1.02× |
| heap.max.MB | 150.2 | 152.3 | 0.7 [-4.4, 30.0] n.s. | 1.01× |
| heap.end.MB | 139.9 | 136.5 | 0.1 [-7.5, 2.6] n.s. | 0.98× |
| phases.wall.s | 36.8 | 36.9 | 0.1 [-0.1, 0.2] n.s. | 1.00× |
| sys.cpu% | 20.8 | 19.5 | -0.0 [-1.8, 6.3] n.s. | 0.94× |

## cpu.total.ms per phase

| Phase | full-final | full-final2 | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 2,180 | 2,316 | 162 [-122, 418] n.s. | 1.06× |
| scroll@200 | 4,154 | 4,363 | 78 [-38, 801] n.s. | 1.05× |
| wheelSlow@200 | 3,296 | 3,211 | 80 [-310, 620] n.s. | 0.97× |
| wheel@200 | 1,723 | 1,822 | 171 [-512, 233] n.s. | 1.06× |
| wheel@500 | 5,083 | 5,243 | 124 [17, 320] | 1.03× |
| hover | 2,322 | 2,417 | 114 [-319, 257] n.s. | 1.04× |

## cpu.%core per phase

| Phase | full-final | full-final2 | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 43.6 | 46.3 | 3.2 [-2.4, 8.3] n.s. | 1.06× |
| scroll@200 | 67.9 | 71.2 | 1.6 [-0.5, 11.6] n.s. | 1.05× |
| wheelSlow@200 | 42.7 | 41.9 | 1.0 [-3.6, 7.7] n.s. | 0.98× |
| wheel@200 | 55.0 | 57.4 | 4.9 [-14.8, 6.3] n.s. | 1.04× |
| wheel@500 | 62.7 | 64.4 | 1.7 [0.0, 3.9] | 1.03× |
| hover | 34.4 | 35.5 | 1.7 [-4.8, 3.8] n.s. | 1.03× |

## energy.impact per phase

| Phase | full-final | full-final2 | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 46.6 | 43.8 | -2.7 [-4.1, 8.6] n.s. | 0.94× |
| scroll@200 | 62.9 | 67.8 | 3.1 [-0.9, 13.1] n.s. | 1.08× |
| wheelSlow@200 | 39.1 | 38.4 | 1.4 [-5.8, 8.1] n.s. | 0.98× |
| wheel@200 | 39.6 | 36.8 | -0.9 [-7.5, 0.7] n.s. | 0.93× |
| wheel@500 | 56.3 | 56.3 | -0.1 [-0.6, 8.6] n.s. | 1.00× |
| hover | 32.8 | 31.6 | -1.6 [-3.6, 5.4] n.s. | 0.96× |

## frames.drawn per phase

| Phase | full-final | full-final2 | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 300 | 301 | 0 [0, 1] n.s. | 1.00× |
| scroll@200 | 360 | 360 | 0 [-3, 5] n.s. | 1.00× |
| wheelSlow@200 | 441 | 441 | -2 [-5, 4] n.s. | 1.00× |
| wheel@200 | 177 | 179 | 2 [-5, 4] n.s. | 1.01× |
| wheel@500 | 458 | 459 | 0 [-4, 3] n.s. | 1.00× |
| hover | 329 | 331 | 4 [-2, 7] n.s. | 1.01× |

## frames.dropped per phase

| Phase | full-final | full-final2 | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 5 | 5 | 1 [-2, 2] n.s. | 1.00× |
| scroll@200 | 17 | 17 | 0 [-1, 7] n.s. | 1.00× |
| wheelSlow@200 | 17 | 17 | 1 [-1, 3] n.s. | 1.00× |
| wheel@200 | 9 | 8 | -1 [-1, 1] n.s. | 0.89× |
| wheel@500 | 28 | 28 | 1 [-1, 4] n.s. | 1.00× |
| hover | 20 | 21 | 1 [0, 2] n.s. | 1.05× |

## raf.p95.ms per phase

| Phase | full-final | full-final2 | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | – | – | – [–, –] n.s. | – |
| scroll@200 | 18.0 | 18.4 | 0.2 [0.1, 0.5] | 1.02× |
| wheelSlow@200 | 18.2 | 18.3 | 0.2 [-0.0, 0.4] n.s. | 1.01× |
| wheel@200 | 18.4 | 17.9 | -0.2 [-0.7, 0.5] n.s. | 0.97× |
| wheel@500 | 18.2 | 18.0 | 0.0 [-0.4, 0.4] n.s. | 0.99× |
| hover | 18.1 | 18.2 | 0.1 [-0.1, 0.6] n.s. | 1.01× |

## style.ms per phase

| Phase | full-final | full-final2 | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 865 | 1,041 | 88 [37, 265] | 1.20× |
| scroll@200 | 1,414 | 1,505 | -6 [-40, 452] n.s. | 1.06× |
| wheelSlow@200 | 1,163 | 1,196 | 29 [-22, 69] n.s. | 1.03× |
| wheel@200 | 518 | 519 | -22 [-29, 5] n.s. | 1.00× |
| wheel@500 | 2,140 | 2,169 | 9 [-22, 72] n.s. | 1.01× |
| hover | 506 | 548 | 21 [-5, 85] n.s. | 1.08× |

## layout.ms per phase

| Phase | full-final | full-final2 | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 4 | 4 | 0 [-0, 4] n.s. | 1.03× |
| scroll@200 | 325 | 347 | 11 [-44, 33] n.s. | 1.07× |
| wheelSlow@200 | 103 | 128 | 0 [-58, 66] n.s. | 1.24× |
| wheel@200 | 145 | 152 | -11 [-28, 86] n.s. | 1.05× |
| wheel@500 | 470 | 511 | 27 [-175, 82] n.s. | 1.09× |
| hover | 219 | 270 | 20 [-100, 155] n.s. | 1.23× |

## mem.renderer.MB per phase

| Phase | full-final | full-final2 | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 808 | 668 | -6 [-313, 30] n.s. | 0.83× |
| scroll@200 | 900 | 728 | 17 [-245, 111] n.s. | 0.81× |
| wheelSlow@200 | 932 | 670 | -149 [-378, 144] n.s. | 0.72× |
| wheel@200 | 939 | 663 | -177 [-385, 264] n.s. | 0.71× |
| wheel@500 | 1,023 | 918 | -247 [-335, 153] n.s. | 0.90× |
| hover | 1,207 | 1,077 | -106 [-503, 345] n.s. | 0.89× |

## mem.gpu.MB per phase

| Phase | full-final | full-final2 | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 109 | 97 | -1 [-22, 2] n.s. | 0.89× |
| scroll@200 | 114 | 102 | -2 [-32, 5] n.s. | 0.89× |
| wheelSlow@200 | 117 | 98 | -2 [-38, 3] n.s. | 0.84× |
| wheel@200 | 111 | 97 | -1 [-38, 3] n.s. | 0.88× |
| wheel@500 | 112 | 99 | -2 [-39, 5] n.s. | 0.88× |
| hover | 114 | 99 | -1 [-39, 2] n.s. | 0.87× |

## wake.gpu/s per phase

| Phase | full-final | full-final2 | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 125 | 124 | -1 [-7, -1] | 0.99× |
| scroll@200 | 126 | 126 | -0 [-7, 2] n.s. | 1.00× |
| wheelSlow@200 | 127 | 126 | -0 [-5, 2] n.s. | 0.99× |
| wheel@200 | 130 | 129 | -0 [-5, 3] n.s. | 0.99× |
| wheel@500 | 130 | 130 | -1 [-5, 2] n.s. | 1.00× |
| hover | 133 | 134 | 0 [-0, 3] n.s. | 1.01× |

## hover.changes per phase

| Phase | full-final | full-final2 | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 0 | 0 | 0 [0, 0] n.s. | – |
| scroll@200 | 1 | 1 | 0 [0, 0] n.s. | 1.00× |
| wheelSlow@200 | 1 | 1 | 0 [0, 0] n.s. | 1.00× |
| wheel@200 | 1 | 1 | 0 [-1, 0] n.s. | 1.00× |
| wheel@500 | 1 | 1 | 0 [0, 0] n.s. | 1.00× |
| hover | 104 | 104 | 0 [-1, 0] n.s. | 1.00× |

## hover.transitions per phase

| Phase | full-final | full-final2 | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 0 | 0 | 0 [0, 0] n.s. | – |
| scroll@200 | 4 | 4 | 0 [0, 0] n.s. | 1.00× |
| wheelSlow@200 | 3 | 3 | 0 [0, 0] n.s. | 1.00× |
| wheel@200 | 3 | 3 | 0 [0, 0] n.s. | 1.00× |
| wheel@500 | 3 | 3 | 0 [0, 0] n.s. | 1.00× |
| hover | 69 | 69 | 0 [0, 0] n.s. | 1.00× |
