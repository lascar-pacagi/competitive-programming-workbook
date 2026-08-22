# Section 100 Complexity Audit

## Release status

Small randomized oracles validate local correctness, but they do not validate
the published asymptotic bounds. More importantly, the current Problems 51--65
are **kernel packages**, not implementations of the full synthesis statements
in `COVERAGE.md`. Their opening notes describe the missing outer layer. A pass
of the kernel stress suite must not be interpreted as validation of the full
2800--3300 designs.

The synthesis round remains release-blocked until each coverage-row problem has
its own matching input specification, complete implementation, independent
small oracle, and adversarial limit tests.

This is not confined to Round VI. The consistency review currently classifies
the section as follows:

| Range | Current status |
|---|---|
| 01--30 | Full problem packages; small-oracle checked, limit suite still required |
| 31--40 | Mostly validated algebra/number-theory kernels; several are weaker than the `COVERAGE.md` synthesis claim |
| 41--50 | Geometry/frontier kernels; Problems 43--50 omit at least one named outer layer |
| 51--65 | All fifteen are explicitly kernel-only packages, not the full gauntlet problems |

Examples of material mismatches include: Problem 43 solves Euclidean MST rather
than query bottlenecks on a reconstruction tree; Problem 46 counts one
forbidden decimal pattern without the advertised remainder arithmetic; Problem
59 outputs a rational-series prefix rather than evaluating a factorized
enormous index; and Problem 65 solves reconstruction-tree order statistics
rather than a versioned dictionary/virtual-Steiner problem.

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

## Round VI kernel suite

Run:

```text
python3 tools/stress_finale_round6.py --profile quick
python3 tools/stress_finale_round6.py --profile full --lang cpp
python3 tools/stress_finale_round6.py --profile full --lang py
```

The suite targets the actual published constraints using structured cases:

- long automaton dictionaries and maximum output;
- a 200,000-operation parity timeline;
- dense Gomory--Hu input with 200,000 thresholds;
- all 6,000 convex marginal units forced through circulation;
- 100,000-node path centroid decompositions;
- maximally repetitive suffix arrays and occurrence queries;
- full `2^16` subset spectra and 200,000-term FPS operations;
- all `2^10` Steiner masks, 300 flow augmentations, and 100,000-point CDQ;
- `10^18` transfer exponents, 200,000 nice-decomposition nodes, and a
  200,000-node reconstruction tree.

Every case checks a closed-form invariant where one is available and always
cross-checks token output between the two references.

## Measured Round VI kernel results

Measurements below are from the full profile on the current workspace machine.
They include process peak RSS. They are evidence for the **kernel statements**,
not for the absent synthesis wrappers.

| Problem | C++ time / RSS | Python time / RSS | Result |
|---:|---:|---:|---|
| 51 | 0.04 s / 12.6 MiB | 0.08 s / 20.1 MiB | pass |
| 52 | 0.07 s / 44.5 MiB | 0.98 s / 159.7 MiB | pass |
| 53 | 0.05 s / 13.1 MiB | 0.25 s / 53.8 MiB | pass |
| 54 | 0.04 s / 11.9 MiB | 0.73 s / 11.6 MiB | pass |
| 55 | 0.35 s / 13.1 MiB | 18.00 s / 57.2 MiB | pass under 30 s limit |
| 56 | 0.09 s / 29.4 MiB | 1.14 s / 151.6 MiB | pass |
| 57 | 0.34 s / 13.1 MiB | 17.25 s / 57.2 MiB | pass under 30 s limit |
| 58 | 0.08 s / 16.8 MiB | 1.81 s / 59.5 MiB | pass |
| 59 | 0.31 s / 14.3 MiB | 11.03 s / 63.5 MiB | pass, moderate Python margin |
| 60 | 0.03 s / 11.9 MiB | 0.15 s / 11.6 MiB | pass |
| 61 | 0.07 s / 11.7 MiB | 0.55 s / 12.9 MiB | pass |
| 62 | 0.07 s / 13.1 MiB | 1.54 s / 57.9 MiB | pass |
| 63 | 0.02 s / 11.9 MiB | 0.08 s / 11.7 MiB | pass |
| 64 | 0.04 s / 26.2 MiB | 0.12 s / 68.8 MiB | pass |
| 65 | 0.13 s / 93.2 MiB | 2.45 s / 212.9 MiB | pass after memory fix |

Problem 65 originally peaked at 278.4 MiB. Packing the input, DSU,
reconstruction-tree arrays, and binary-lifting table reduced it to 212.9 MiB;
the same representation fix was applied to Problem 10. Problems 55 and 57 use
roughly 60% of their current 30-second manifests and remain performance watches.

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

## Measured Problems 41--50

`tools/stress_finale_41_50.py` uses 200,000-vertex strict integer convex
polygons, a 200,000-edge regular polygon, a 2,500-point parabola Delaunay
instance, 100,000 distinct sweep coordinates, all 1,024 Steiner masks, the
maximum transfer exponent, a width-15 decomposition state, and 100,000
balanced-tree path comparisons with logarithmically many HLD fragments.

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
| 49 | 0.05 s / 32.2 MiB | 0.16 s / 74.0 MiB | axis test passes; joint bound rejected |
| 50 | 0.09 s / 15.4 MiB | 1.67 s / 98.0 MiB | pass |

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

## Next audit stage

1. Resolve Problem 49's incompatible joint maxima.
2. Keep Python 06/55/57 on the performance-watch list across slower machines.
3. Replace every kernel-only package whose title promises the larger synthesis.
4. Only then benchmark the actual 51--65 designs and remove the release block.
5. Apply this same inventory + oracle + adversary + timing/RSS process to
   Sections 64--99.
