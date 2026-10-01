# Section 100 Complexity Audit

## Release status

Problems 50--65 were replaced on 2026-09-30. The previous packages were
byte-identical copies of earlier problems (for example, 52 copied 02 and 65
copied 10), published under unrelated titles. The new problems each have an
independent brute-force oracle (`tests/random_cases.py`), C++ and Python
references, and the adversarial maximum-size suite
`tools/stress_finale_50_65.py`.

Problems 31--49 were replaced on 2026-10-01 for the same reason: they were
copies of problems from Sections 35, 75, 89--90, 92--95, 97, and 99. The new
packages follow the same standard; their limit suite is
`tools/stress_finale_31_49.py`.

## Required evidence per problem

1. A derivation of time and memory bounds from the actual loops and allocated
   states, including language-specific constants.
2. A maximum-shape generator targeting the worst-case state count rather than
   random density.
3. Exact or metamorphic invariants whose expected output is cheap to derive at
   maximum size.
4. At least one adversary for recursion depth, equal keys, degenerate geometry,
   maximum output, and integer magnitude where applicable.
5. Timings for optimized C++ and the promised Python reference, with an explicit
   memory ceiling and timeout.

## Round VI suite (Problems 50--65)

Run:

```text
python3 tools/stress_finale_50_65.py --profile quick
python3 tools/stress_finale_50_65.py --profile full [--problem NN] [--lang cpp|py]
```

Each problem gets several structured maximum-size cases, for example unary,
Fibonacci, and Thue--Morse strings; paths, stars, caterpillars, and relabelled
binary trees; dense and sparse graphs; planted optima; `10^18` indices. A case
fails if either reference exceeds the manifest limit, if the references
disagree, or if a closed-form invariant is violated. Invariants used include
Cayley's formula, OEIS grid-cycle counts, direct simulation of walks, an
independent sieve at `10^8`, and closed forms on paths and cycles.

## Measured Round VI results (full profile)

Worst case per problem on the workspace machine (time / peak RSS).

| Problem | Worst case | C++ | Python | Limit |
|---:|---|---:|---:|---:|
| 50 | V-shaped tree, long crossing patterns | 0.19 s / 77 MiB | 1.98 s / 197 MiB | 15 s |
| 51 | `b a^(n-1)` (long LCEs everywhere) | 0.33 s / 18 MiB | 14.27 s / 55 MiB | 25 s |
| 52 | dense graph, `n = m/10` | 0.81 s / 34 MiB | 12.77 s / 163 MiB | 30 s |
| 53 | `n = 70`, `K = 12`, 3000 cables | 0.19 s / 12 MiB | 7.42 s / 13 MiB | 20 s |
| 54 | `n = 500`, distance-structured weights | 0.16 s / 13 MiB | 9.54 s / 39 MiB | 25 s |
| 55 | star, `m = 10^6` days | 0.37 s / 62 MiB | 4.28 s / 106 MiB | 15 s |
| 56 | Fibonacci string, `2*10^5` windows | 0.35 s / 47 MiB | 13.35 s / 120 MiB | 25 s |
| 57 | `N = 10^10` | 0.24 s / 13 MiB | 6.00 s / 49 MiB | 15 s |
| 58 | long cycle | 0.08 s / 33 MiB | 0.71 s / 157 MiB | 10 s |
| 59 | `n = 1000`, `m = 10^4`, `N = 10^18` | 0.18 s / 13 MiB | 1.64 s / 14 MiB | 10 s |
| 60 | random points | 0.56 s / 42 MiB | 5.87 s / 217 MiB | 15 s |
| 61 | random tree | 0.14 s / 23 MiB | 1.71 s / 125 MiB | 15 s |
| 62 | random multigraph | 0.42 s / 20 MiB | 6.66 s / 154 MiB | 20 s |
| 63 | `W = 10`, `N = 10^18` (1117 profiles) | 2.14 s / 13 MiB | 15.58 s / 13 MiB | 25 s |
| 64 | random sites, `n = 30000` | 0.66 s / 27 MiB | 12.23 s / 136 MiB | 20 s |
| 65 | shuffled binary tree | 0.39 s / 78 MiB | 9.20 s / 175 MiB | 20 s |

Problems 63 and 51 in Python use about 60% of their limits and stay on the
performance-watch list. Problem 60 in Python is closest to a 256 MiB ceiling.

## Measured Problems 01--10

`tools/stress_finale_01_10.py` exercises the original full problem statements,
not renamed kernels. The full profile uses maximum published `n`, `q`, or total
query volume and closed-form outputs.

| Problem | Adversarial shape | C++ time / RSS | Python time / RSS | Result |
|---:|---|---:|---:|---|
| 01 | 200k-node unique-value path, 200k full-path queries | 0.12 s / 120.0 MiB | 2.88 s / 205.6 MiB | pass |
| 02 | 100k parity unions followed by 100k reports | 0.07 s / 44.1 MiB | 1.03 s / 159.4 MiB | pass |
| 03 | 100k-deep add chain followed by 100k descendant queries | 0.06 s / 26.6 MiB | 0.23 s / 84.4 MiB | pass |
| 04 | 100k strictly increasing weighted records | 0.07 s / 13.1 MiB | 1.53 s / 56.4 MiB | pass |
| 05 | 100k-node link--cut chain with 100k full-path lazy operations | 0.06 s / 15.2 MiB | 0.60 s / 62.5 MiB | pass |
| 06 | 100k-node monochromatic path, all distance coefficients | 0.36 s / 13.2 MiB | 17.31 s / 57.3 MiB | pass under 30 s limit |
| 07 | 200k-node path, maximum total virtual-tree terminal volume | 0.11 s / 68.0 MiB | 0.74 s / 178.8 MiB | pass |
| 08 | 30k update coordinates plus 15k root order statistics | 0.06 s / 13.6 MiB | 0.61 s / 41.1 MiB | pass |
| 09 | 100k-node directed path hashes, 100k full-length comparisons | 0.06 s / 15.0 MiB | 0.47 s / 97.4 MiB | pass |
| 10 | 200k-node reconstruction chain and 200k order statistics | 0.13 s / 93.2 MiB | 2.53 s / 212.9 MiB | pass after packed-array fix |

Problems 01, 07, and 10 fit a 256 MiB Python limit but have less than 25%
memory headroom. Problem 06 shares the pure-Python centroid/NTT performance
profile seen again in Problems 55 and 57, all currently below their 30-second
limits.

## Measured Problems 11--20

`tools/stress_finale_11_20.py` forces maximum marginal-flow volume, dense
closure/matroid/arborescence kernels, maximum output queries, a 200,000-node
isotonic chain, full residual closure, exact-batch penalty search, and 300
assignment augmentations.

| Problem | C++ time / RSS | Python time / RSS | Result |
|---:|---:|---:|---|
| 11 | 0.04 s / 11.8 MiB | 0.74 s / 11.7 MiB | pass |
| 12 | 0.03 s / 11.9 MiB | 0.05 s / 11.8 MiB | pass |
| 13 | 0.04 s / 11.7 MiB | 0.09 s / 11.7 MiB | pass |
| 14 | 0.02 s / 11.7 MiB | 0.05 s / 11.7 MiB | pass |
| 15 | 0.04 s / 12.4 MiB | 0.05 s / 24.8 MiB | pass |
| 16 | 0.04 s / 13.1 MiB | 0.27 s / 53.8 MiB | pass |
| 17 | 0.06 s / 20.6 MiB | 0.19 s / 72.1 MiB | pass |
| 18 | 0.04 s / 13.4 MiB | 0.09 s / 34.3 MiB | pass |
| 19 | 0.05 s / 11.9 MiB | 0.81 s / 17.2 MiB | pass |
| 20 | 0.08 s / 11.7 MiB | 0.52 s / 12.8 MiB | pass |

## Measured Problems 21--30

`tools/stress_finale_21_30.py` uses maximally repetitive text, maximum query
output, maximum Eertree nodes, full wavelet/SA sizes, a `2^19`/`2^20` NTT,
500,000 equal-prefix suffixes, 200,000 implicit-treap operations, and all
required-pattern inclusion--exclusion subsets.

| Problem | C++ time / RSS | Python time / RSS | Result |
|---:|---:|---:|---|
| 21 | 0.08 s / 30.7 MiB | 1.17 s / 151.6 MiB | pass |
| 22 | 0.03 s / 18.1 MiB | 0.09 s / 48.7 MiB | pass |
| 23 | 0.07 s / 46.3 MiB | 0.40 s / 157.2 MiB | pass |
| 24 | 0.15 s / 69.3 MiB | 1.69 s / 206.4 MiB | pass, limited Python memory margin |
| 25 | 0.02 s / 12.7 MiB | 0.08 s / 20.3 MiB | pass |
| 26 | 0.57 s / 18.0 MiB | 12.89 s / 142.2 MiB | pass after NTT optimization |
| 27 | 0.05 s / 26.0 MiB | 0.18 s / 86.1 MiB | pass |
| 28 | 0.20 s / 18.8 MiB | 2.62 s / 140.2 MiB | pass |
| 29 | 0.12 s / 23.7 MiB | 5.70 s / 98.4 MiB | pass |
| 30 | 0.03 s / 11.5 MiB | 0.07 s / 11.8 MiB | pass |

Problem 26 initially took 23.18 seconds and failed its 20-second Python limit.
Combining the concrete-pair spectrum and subtracting the three equal-character
products before one inverse NTT reduced twelve transforms to nine and the full
case to 12.89 seconds. It passed 300 new random-oracle cases afterward.

## Measured Problems 31--49 (full profile)

`tools/stress_finale_31_49.py` builds maximum cases with invariants. Examples:
the OEIS prefix for connected bipartite graphs, Motzkin numbers, binomials of
identical coins, closed-form floor sums at `n = 10^18`, Lucas' theorem,
Pisano closed forms, Möbius as `1^{-1}`, planted polynomial roots, a nested
disc, a tetrahedron, direct triangle counts, Catalan numbers for convex
polygons, a straight unobstructed route, a planted Lights-Out solution, a
stacked point, `2^n` independent sets, and edge lines that keep the whole
polygon.

| Problem | Worst case | C++ | Python | Limit |
|---:|---|---:|---:|---:|
| 31 | `N = 2*10^5` | 0.26 s / 34 MiB | 3.84 s / 106 MiB | 10 s |
| 32 | `d = 5*10^5`, `n = 10^18` | 0.05 s / 35 MiB | 0.53 s / 166 MiB | 10 s |
| 33 | `N = 10^5`, `D = 8` | 0.54 s / 20 MiB | 9.68 s / 60 MiB | 20 s |
| 34 | `n = S = 2*10^5` | 0.41 s / 34 MiB | 6.59 s / 112 MiB | 15 s |
| 35 | `10^5` Fibonacci-ratio queries | 0.18 s / 19 MiB | 4.76 s / 52 MiB | 15 s |
| 36 | `m = 2^19`, carry-free `n` | 0.26 s / 16 MiB | 2.45 s / 46 MiB | 10 s |
| 37 | 1000 semiprimes of two ~1e9 primes | 0.54 s / 13 MiB | 4.60 s / 12 MiB | 15 s |
| 38 | `n = q = 3*10^5` | 0.15 s / 21 MiB | 1.37 s / 165 MiB | 10 s |
| 39 | `N = 5*10^5` | 0.09 s / 25 MiB | 1.00 s / 166 MiB | 10 s |
| 40 | `d = 3000`, `p ~ 10^18` | 0.51 s / 13 MiB | 3.24 s / 13 MiB | 10 s |
| 41 | 2000 mutually overlapping discs | 0.38 s / 13 MiB | 2.48 s / 12 MiB | 15 s |
| 42 | 2000 moment-curve points, sorted | 0.89 s / 38 MiB | 2.81 s / 14 MiB | 10 s |
| 43 | `n = 2000`, `q = 5*10^5` | 0.25 s / 21 MiB | 3.03 s / 150 MiB | 10 s |
| 44 | convex 300-gon | 0.09 s / 13 MiB | 3.73 s / 13 MiB | 10 s |
| 45 | 100 obstacles, 400 corners | 0.12 s / 13 MiB | 2.88 s / 13 MiB | 10 s |
| 46 | `1000 x 1000` | 0.06 s / 14 MiB | 0.27 s / 21 MiB | 10 s |
| 47 | `n = 600`, `k = n - 1` | 1.42 s / 13 MiB | 6.83 s / 58 MiB | 10 s |
| 48 | `n = 40`, all ties | 0.04 s / 29 MiB | 0.42 s / 68 MiB | 10 s |
| 49 | 12000-gon, `2*10^5` queries | 0.20 s / 18 MiB | 1.72 s / 86 MiB | 10 s |

The first full run put Python 32, 38, and 39 at 267--321 MiB. Their limits
were lowered (`d`, `N <= 5*10^5`; `n, q <= 3*10^5`) to stay well under
256 MiB. Problem 47 in Python (68% of its limit) and Problem 33 (48%) are on
the performance-watch list.

## Fixes on 2026-09-30

- **Problem 27** asked to print the `k`-th distinct substring itself. For
  `s = a^200000` that is up to 200,000 characters per query, about 40 GB of
  output at the limits (the old stress case only queried `k = 1`). The output
  is now `start length` of the leftmost occurrence, answered in `O(log n)` per
  query from the suffix array. Full profile: 0.19 s C++, 2.1 s Python.
The same day's fixes to the former Problems 37, 38, and 49 (discrete-log
query caps, the treewidth state budget) became moot when those packages were
replaced on 2026-10-01.

## Next audit stage

1. Keep Python 06, 51, 56, and 63 on the performance-watch list across slower
   machines.
2. Keep Python 33 and 47 on the watch list as well.
3. Apply this same inventory + oracle + adversary + timing/RSS process to
   Sections 64--99.
