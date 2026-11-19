# Test data: tank-stepsk vs tank-steps0

Runs: 1=full-final2, 2=tank-steps0, 3=tank-stepsk, 4=tank-stepsk, 5=tank-steps0, 6=full-final2. Medians of 2; diff = median of 2 paired (tank-stepsk − tank-steps0) with 95% bootstrap CI.

## Whole test

| Metric | tank-steps0 | tank-stepsk | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| cpu.total.s | 7.0 | 12.9 | 6.0 [4.5, 7.5] | 1.86× |
| cpu.renderer.s | 5.0 | 8.5 | 3.5 [2.8, 4.2] | 1.71× |
| cpu.gpu.s | 1.8 | 4.2 | 2.4 [1.7, 3.2] | 2.37× |
| cpu.browser.s | 0.2 | 0.2 | 0.0 [-0.0, 0.0] n.s. | 1.02× |
| energy.impact.mean | 24.8 | 42.7 | 17.9 [13.3, 22.5] | 1.72× |
| frames.drawn | 717 | 1,770 | 1,053 [1,031, 1,075] | 2.47× |
| frames.dropped | 58 | 30 | -28 [-34, -22] | 0.52× |
| mem.renderer.max.MB | 780 | 760 | -20 [-130, 90] n.s. | 0.97× |
| mem.gpu.max.MB | 103 | 99 | -5 [-14, 5] n.s. | 0.95× |
| mem.footprint.max.MB | 1,206 | 1,226 | 19 [-61, 99] n.s. | 1.02× |
| mem.footprint.end.MB | 945 | 1,076 | 132 [111, 152] | 1.14× |
| heap.max.MB | 149.9 | 137.1 | -12.8 [-16.4, -9.1] | 0.91× |
| heap.end.MB | 134.0 | 133.3 | -0.8 [-0.8, -0.7] | 0.99× |
| phases.wall.s | 30.0 | 30.0 | 0.0 [0.0, 0.0] n.s. | 1.00× |
| sys.cpu% | 20.3 | 20.4 | 0.1 [-0.4, 0.7] n.s. | 1.01× |

## cpu.total.ms per phase

| Phase | tank-steps0 | tank-stepsk | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 6,972 | 12,940 | 5,968 [4,475, 7,460] | 1.86× |

## cpu.%core per phase

| Phase | tank-steps0 | tank-stepsk | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 23.2 | 43.1 | 19.9 [14.9, 24.9] | 1.86× |

## energy.impact per phase

| Phase | tank-steps0 | tank-stepsk | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 24.8 | 42.7 | 17.9 [13.3, 22.5] | 1.72× |

## frames.drawn per phase

| Phase | tank-steps0 | tank-stepsk | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 717 | 1,770 | 1,053 [1,031, 1,075] | 2.47× |

## frames.dropped per phase

| Phase | tank-steps0 | tank-stepsk | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 58 | 30 | -28 [-34, -22] | 0.52× |

## raf.p95.ms per phase

| Phase | tank-steps0 | tank-stepsk | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | – | – | – [–, –] n.s. | – |

## style.ms per phase

| Phase | tank-steps0 | tank-stepsk | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 2,553 | 5,186 | 2,633 [2,503, 2,763] | 2.03× |

## layout.ms per phase

| Phase | tank-steps0 | tank-stepsk | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 27 | 27 | -0 [-1, -0] | 0.98× |

## mem.renderer.MB per phase

| Phase | tank-steps0 | tank-stepsk | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 581 | 693 | 112 [11, 214] | 1.19× |

## mem.gpu.MB per phase

| Phase | tank-steps0 | tank-stepsk | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 94 | 96 | 2 [-9, 12] n.s. | 1.02× |

## wake.gpu/s per phase

| Phase | tank-steps0 | tank-stepsk | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 127 | 125 | -2 [-2, -2] | 0.98× |

## hover.changes per phase

| Phase | tank-steps0 | tank-stepsk | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 0 | 0 | 0 [0, 0] n.s. | – |

## hover.transitions per phase

| Phase | tank-steps0 | tank-stepsk | Diff [95% CI] | Ratio |
|---|---:|---:|---:|---:|
| idle | 0 | 0 | 0 [0, 0] n.s. | – |
