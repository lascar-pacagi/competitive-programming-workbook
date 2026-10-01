# Section 100 Complexity Audit

## Release status

Problems 50--65 were replaced on 2026-09-30. The previous packages were
byte-identical copies of earlier problems (for example, 52 copied 02 and 65
copied 10), published under unrelated titles. The new problems each have an
independent brute-force oracle (`tests/random_cases.py`), C++ and Python
references, and the adversarial maximum-size suite
`tools/stress_finale_50_65.py`.

Problems 31--49 are still adapted from earlier course sections (see
`tools/generate_finale_31_40.py` and `tools/generate_finale_41_50.py`). Their
statements have been rewritten to drop technique hints and to be
self-contained.

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

## Measured Problems 31--40

`tools/stress_finale_31_40.py` forces full FPS lengths, complete subset/XOR
spectra, 50,000-point interpolation, repeated hard semiprime factorization,
maximum discrete-log/modular-root query counts, and 200,000 maximum-argument
multiplicative queries.

| Problem | C++ time / RSS | Python time / RSS | Result |
|---:|---:|---:|---|
| 31 | 0.30 s / 13.5 MiB | 7.54 s / 31.6 MiB | pass |
| 32 | 0.31 s / 14.3 MiB | 11.05 s / 63.6 MiB | pass |
| 33 | 0.07 s / 16.8 MiB | 1.88 s / 59.5 MiB | pass |
| 34 | 0.12 s / 16.0 MiB | 3.14 s / 98.5 MiB | pass |
| 35 | 0.56 s / 25.9 MiB | 27.79 s / 109.0 MiB | pass after correcting limit to 40 s |
| 36 | 0.79 s / 11.7 MiB | 1.88 s / 11.6 MiB | pass |
| 37 | 0.13 s / 11.7 MiB | 0.22 s / 14.6 MiB | pass |
| 38 | 0.24 s / 11.7 MiB | 0.42 s / 14.6 MiB | pass |
| 39 | 0.04 s / 15.5 MiB | 0.45 s / 110.9 MiB | pass |
| 40 | 0.32 s / 13.4 MiB | 4.44 s / 74.1 MiB | pass |

Problem 35 originally rebuilt the same product tree while evaluating the
derivative. Reusing it reduced Python from 30.61 to 27.79 seconds and 112.9 to
109.0 MiB. The algorithm has the intended `O(n log^2 n)` complexity, but the
shared 15-second manifest was not compatible with its promised CPython
reference. Problems 35, Section 89-B, and Section 90-D now use a measured
40-second limit; this is a support-limit correction, not an algorithmic speedup.

## Measured Problems 41--49

`tools/stress_finale_41_50.py` uses 200,000-vertex strict integer convex
polygons, a 200,000-edge regular polygon, a 2,500-point parabola Delaunay
instance, 100,000 distinct sweep coordinates, all 1,024 Steiner masks, the
maximum transfer exponent, a width-15 decomposition state, and (for the
former Problem 50) 100,000 balanced-tree path comparisons.

| Problem | C++ time / RSS | Python time / RSS | Result |
|---:|---:|---:|---|
| 41 | 0.08 s / 17.1 MiB | 0.80 s / 76.5 MiB | pass |
| 42 | 0.89 s / 61.3 MiB | 5.47 s / 141.4 MiB | pass after complexity fix |
| 43 | 0.04 s / 11.8 MiB | 1.75 s / 12.3 MiB | pass |
| 44 | 0.09 s / 15.6 MiB | 1.16 s / 40.9 MiB | pass |
| 45 | 0.09 s / 18.2 MiB | 0.88 s / 81.3 MiB | pass |
| 46 | 0.06 s / 11.7 MiB | 0.28 s / 11.6 MiB | pass |
| 47 | 0.03 s / 11.7 MiB | 0.07 s / 11.5 MiB | pass |
| 48 | 0.02 s / 11.8 MiB | 0.14 s / 11.7 MiB | pass |
| 49 | 0.05 s / 32.2 MiB | 0.16 s / 74.0 MiB | axis test passes; joint bound fixed below |

Problem 42 had two independent complexity defects. C++ chose its binary-search
upper bound with an `O(n^2)` all-pairs scan and took 114.81 seconds. Both
references also sorted an already cyclically ordered convex edge set on every
feasibility check. A bounding-box upper bound plus one initial angular rotation
makes C++ linear per check; a specialized allocation-light cyclic HPI gives the
same bound in Python. The repaired references passed the 25-case independent
geometry oracle as well as the maximum regular-polygon invariant.

Problem 49's measured case independently reaches `t=199,999` and the full
`2^15` state space. It deliberately does not claim that this certifies their
Cartesian product. The implementation is `Theta(t * 2^w)` and stores every
node's map. A valid decomposition can contain about 11,700 branches that each
introduce the same 15-vertex join bag and then join at that bag, requiring
hundreds of millions of map entries. Thus the simultaneous published maxima
are not computationally viable; the constraints need an aggregate state bound
or the implementation must discard child tables and adopt a stronger design.

## Fixes on 2026-09-30

- **Problem 27** asked to print the `k`-th distinct substring itself. For
  `s = a^200000` that is up to 200,000 characters per query, about 40 GB of
  output at the limits (the old stress case only queried `k = 1`). The output
  is now `start length` of the leftmost occurrence, answered in `O(log n)` per
  query from the suffix array. Full profile: 0.19 s C++, 2.1 s Python.
- **Problems 37 and 38** were measured on primes near `10^12` whose group
  order has a huge prime factor. There, every query needs about `2*10^6` hash
  operations. With 50 and 100 queries they took 14.4 s / 25.9 s in C++ and
  17.9 s / 34.6 s in Python, against a 15 s limit. BSGS now stops at its first
  giant-step hit (still minimal), and both statements allow at most 20
  queries. The worst 20-query inputs take 2.5 s / 2.6 s in C++ and
  5.1 s / 5.7 s in Python; outputs are unchanged.
- **Problem 49** regained the aggregate bound `sum(2^|bag|) <= 2*10^6` from
  its source problem, which resolves the incompatible joint maxima described
  above. A width-15 budget case with `t = 199999` nodes and no edges (every
  subset is a state) takes 0.25 s C++ and 0.50 s Python / 205 MiB.

## Next audit stage

1. Keep Python 06, 51, 56, and 63 on the performance-watch list across slower
   machines.
2. Decide whether Problems 31--49, which repeat earlier sections' problems,
   should be replaced like 50--65.
3. Apply this same inventory + oracle + adversary + timing/RSS process to
   Sections 64--99.
