# Sections 64--99 Complexity Audit

## Scope and acceptance rule

Sections 64--99 contain 168 packages across 36 sections. Every package already
has C++ and Python references plus a small independent random generator. Those
oracles remain useful for local correctness, but they are not complexity
evidence.

A package is complexity-certified only after all of the following exist:

1. a worst-shape generator at every simultaneous published maximum;
2. a cheap exact, conservation, or metamorphic invariant at that size;
3. optimized-C++ and CPython wall-time and peak-RSS measurements;
4. an explicit comparison with the package manifest;
5. a consistency check that the statement, editorial, and implementation solve
   the same problem.

If maxima cannot be combined computationally (for example `t * 2^w` with both
`t` and `w` independently maximal), the package fails until it receives an
aggregate bound. Testing each axis separately is diagnostic evidence, not a
pass.

## Reuse from Section 100

Twenty-six source packages in Sections 64--99 are byte-identical to kernels
already exercised by the Section 100 limit suites. Their measurements can be
inherited while the files remain identical. This includes representative FPS,
subset convolution, interpolation, composite discrete log, convex collision,
Delaunay MST, rectangle sweep, digit DP, transfer-matrix, Steiner, and
tree-decomposition kernels.

Inherited evidence does not certify a stronger story wrapped around a kernel,
and semantic copies with different code are rerun rather than assumed equal.

## Section 64 pilot

Run:

```text
python3 tools/stress_advanced_64.py --profile quick
python3 tools/stress_advanced_64.py --profile full --lang cpp
python3 tools/stress_advanced_64.py --profile full --lang py
```

The full cases use `n=M=200,000`, all `M` distinct values for the LCM sieve,
30 adjacent `10^9` totient-prefix queries, and 30 distinct square-free ranks
between 13 and 100 billion. The invariants are respectively a closed-form pair
count, the `Phi(N)-Phi(N-1)=phi(N)` identity, the prime-exponent formula for
LCM pairs, and the defining rank inequalities checked with a Möbius count.

| Problem | C++ time / RSS | Python time / RSS | Result |
|---|---:|---:|---|
| 64-A GCD Pair Energy | 0.05 s / 12.1 MiB | 0.36 s / 25.0 MiB | pass |
| 64-B Summatory Totient | 0.07 s / 11.7 MiB | 0.85 s / 47.6 MiB | pass |
| 64-C LCM Pair Spectrum | 0.04 s / 12.8 MiB | 0.22 s / 28.1 MiB | pass |
| 64-D Square-Free Rank | 0.77 s / 11.8 MiB | 20.79 s / 16.1 MiB | pass after correcting Python limit |

Section 64-D's original six-second manifest was incompatible with the actual
`O(q sqrt(answer) log answer)` CPython reference: four maximum-rank queries took
3.39 seconds and 30 distinct large ranks took 20.79 seconds. Its manifest is
now 40 seconds. This changes the support contract; it does not improve the
algorithm.

## Sections 65--66

`tools/stress_advanced_65_66.py` forces full `2^ceil(log n)` NTT transforms,
the entire 200,000-coefficient product budget, order-400 and order-1,000
quadratic recurrence reductions at index `10^18`, 50 maximum necklace queries,
30 distinct large totient intervals, all 5,000 graph edges, and a 200,000-term
subset-size spectrum.

| Problem | C++ time / RSS | Python time / RSS | Result |
|---|---:|---:|---|
| 65-A Cyclic Agreement | 0.20 s / 12.2 MiB | 10.92 s / 75.2 MiB | pass; limit raised 12 -> 20 s for headroom |
| 65-B Bounded Sum Product | 0.26 s / 11.8 MiB | 14.30 s / 31.2 MiB | pass after limit correction 8 -> 20 s |
| 65-C Huge Linear Recurrence | 0.04 s / 11.8 MiB | 1.12 s / 11.6 MiB | pass |
| 65-D Recurrence Recovery | 0.14 s / 11.8 MiB | 7.35 s / 11.5 MiB | pass after limit correction 6 -> 12 s |
| 66-A Primitive Necklaces | 0.03 s / 11.9 MiB | 0.12 s / 21.4 MiB | pass |
| 66-B Totient Interval | 0.10 s / 11.7 MiB | 1.46 s / 48.0 MiB | pass |
| 66-C Wildcard Rotation | 0.16 s / 11.9 MiB | 5.09 s / 29.3 MiB | pass |
| 66-D Weighted Compositions | 0.27 s / 11.7 MiB | 14.47 s / 31.1 MiB | pass after limit correction 8 -> 20 s |
| 66-E Black-Box Walks | 0.02 s / 11.8 MiB | 0.09 s / 11.6 MiB | pass |
| 66-F GCD-One Size Spectrum | 0.10 s / 15.1 MiB | 3.58 s / 83.9 MiB | pass |

The bounded-composition answers are checked independently by the bounded-star
inclusion--exclusion formula. The recurrence adversaries use a period-1,000
delta sequence, which has minimal recurrence `x^1000-1`, so the exact future
term is known without duplicating Berlekamp--Massey or Kitamasa.

## Sections 67--69

`tools/stress_advanced_67_69.py` creates maximum persistent-node counts,
misaligned rollback intervals, 200,000-node paths, balanced-tree HLD paths with
many fragments, full centroid-path tables, the maximum aggregate marked-set
volume, and balanced unique-color small-to-large merges.

| Problem | C++ time / RSS | Python time / RSS | Result |
|---|---:|---:|---|
| 67-A Branching Multiset | 0.06 s / 29.5 MiB | 0.56 s / 167.0 MiB | pass |
| 67-B Versioned Range Add | 0.08 s / 102.8 MiB | 0.84 s / 187.7 MiB | pass |
| 67-C Dynamic Connectivity | 0.08 s / 35.6 MiB | 0.78 s / 129.4 MiB | pass |
| 67-D Tree Path K-th | 0.13 s / 79.8 MiB | 2.10 s / 193.9 MiB | pass after packing arrays |
| 68-A Path Affine Composition | 0.11 s / 38.6 MiB | 2.00 s / 197.7 MiB | pass |
| 68-B Toggle Nearest Beacon | 0.15 s / 76.7 MiB | 2.42 s / 166.3 MiB | pass after complexity/memory fixes |
| 68-C Marked Pair Distances | 0.09 s / 38.2 MiB | 0.43 s / 167.7 MiB | pass |
| 68-D Subtree Mode Sum | 0.16 s / 45.2 MiB | 0.43 s / 124.7 MiB | pass |
| 69-A Snapshot Range Rank | 0.08 s / 44.8 MiB | 0.75 s / 208.3 MiB | pass, limited Python memory margin |
| 69-B Seasonal Component Size | 0.08 s / 35.7 MiB | 0.74 s / 127.0 MiB | pass |
| 69-C Route Matrices | 0.16 s / 57.5 MiB | 3.39 s / 219.6 MiB | pass, limited Python memory margin |
| 69-D Beacon Distance Sum | 0.15 s / 89.5 MiB | 2.36 s / 155.8 MiB | pass after complexity/memory fixes |
| 69-E Weighted Marked Pairs | 0.08 s / 38.8 MiB | 0.44 s / 167.8 MiB | pass |
| 69-F Subtree Mode Profile | 0.17 s / 44.5 MiB | 0.40 s / 122.8 MiB | pass |

The two C++ centroid references initialized an `n`-element traversal-parent
array separately for every centroid. On a 200,000-node path this made 68-B take
39.31 seconds and 69-D take 6.37 seconds. Reusable timestamped traversal arrays
reduced both to about 0.15 seconds. Independent random oracles pass afterward.

Python 67-D originally used 406.5 MiB; packed persistent-tree and lifting arrays
reduce it to 193.9 MiB. Packing centroid paths and promptly cancelling lazy
heap deletions reduce 68-B from 425.0 to 166.3 MiB. Packing the three-field
centroid paths in 69-D reduces it from 386.4 to 155.8 MiB. Problems 69-A and
69-C still have less than 20% headroom under a conventional 256 MiB ceiling.

## Sections 70--72

`tools/stress_advanced_70_72.py` exercises dense feasible lower-bound
circulations, the maximum edge and quota budgets, 200 augmenting unit paths,
order-statistic isotonic inputs, all 200,000 separable-convex allocation units,
all 5,000 red-MST edges, and all project marginal arcs. Closed-form flow costs,
profits, isotonic losses, and allocation objectives certify the full-size
answers without invoking a second min-cost-flow or convex optimizer.

| Problem | C++ time / RSS | Python time / RSS | Result |
|---|---:|---:|---|
| 70-A Bounded Circulation | 0.03 s / 11.7 MiB | 0.04 s / 11.7 MiB | pass |
| 70-B Exact-Cost Shipment | 0.03 s / 11.7 MiB | 0.08 s / 11.7 MiB | pass |
| 70-C Quota Assignment | 0.03 s / 12.0 MiB | 0.42 s / 17.2 MiB | pass |
| 70-D Minimum-Cost Bounded Circulation | 0.03 s / 11.7 MiB | 0.05 s / 11.5 MiB | pass |
| 71-A Monotone L1 Repair | 0.05 s / 13.1 MiB | 0.10 s / 27.5 MiB | pass |
| 71-B Exact Red Spanning Tree | 0.03 s / 11.7 MiB | 0.09 s / 11.9 MiB | pass |
| 71-C Massive Convex Allocation | 0.05 s / 15.6 MiB | 0.56 s / 37.3 MiB | pass |
| 71-D Weighted Bounded Isotonic | 0.05 s / 13.5 MiB | 0.16 s / 32.4 MiB | pass |
| 72-A Exam Room Bounds | 0.03 s / 11.9 MiB | 0.05 s / 15.1 MiB | pass |
| 72-B Night Delivery | 0.03 s / 11.7 MiB | 0.08 s / 11.6 MiB | pass |
| 72-C Team Quota Profit | 0.03 s / 11.9 MiB | 0.44 s / 17.3 MiB | pass |
| 72-D Monotone Signal | 0.04 s / 12.9 MiB | 0.08 s / 27.4 MiB | pass |
| 72-E Exact Discount Tree | 0.03 s / 11.9 MiB | 0.10 s / 11.8 MiB | pass |
| 72-F Congested Team Assignment | 0.05 s / 12.3 MiB | 2.14 s / 41.1 MiB | pass |

## Sections 73--75

`tools/stress_advanced_73_75.py` constructs maximum-size primitive convex
polygons, antipodal-diameter and Minkowski-query workloads, 100,000-by-100,000
orthogonal crossing families, maximum rectangle sweeps, a 5,000-point parabola
that forces the intended quadratic triangle scan, and maximum collision,
weighted-crossing, coverage, and point-location query volumes. The full-size
checks use Pick's theorem, antipodal symmetry, translation invariance, product
counts, and closed-form union measures.

| Problem | C++ time / RSS | Python time / RSS | Result |
|---|---:|---:|---|
| 73-A Hull Statistics | 0.06 s / 15.0 MiB | 0.28 s / 53.2 MiB | pass |
| 73-B Farthest Pair | 0.06 s / 15.0 MiB | 0.44 s / 53.4 MiB | pass |
| 73-C Sum Polygon Queries | 0.09 s / 17.0 MiB | 0.83 s / 70.2 MiB | pass |
| 73-D Convex Polygon Distance | 0.06 s / 21.5 MiB | 0.36 s / 151.5 MiB | pass |
| 74-A Orthogonal Crossings | 0.06 s / 28.4 MiB | 0.34 s / 62.4 MiB | pass |
| 74-B Rectangle Union | 0.08 s / 13.2 MiB | 0.80 s / 40.7 MiB | pass |
| 74-C Closest Pair | 0.04 s / 14.2 MiB | 0.52 s / 46.2 MiB | pass |
| 74-D Rectangle Union Perimeter | 0.19 s / 48.3 MiB | 5.31 s / 174.0 MiB | pass; limit raised 8 -> 12 s |
| 75-A Convex Lattice Shield | 0.05 s / 15.2 MiB | 0.32 s / 53.5 MiB | pass |
| 75-B Maximum Triangle | 0.06 s / 11.8 MiB | 5.30 s / 11.5 MiB | pass; limit raised 7 -> 12 s |
| 75-C Robot Collision Translations | 0.08 s / 17.3 MiB | 0.82 s / 76.3 MiB | pass |
| 75-D Weighted Crossings | 0.08 s / 27.3 MiB | 0.34 s / 75.4 MiB | pass |
| 75-E Double-Painted Map | 0.08 s / 15.9 MiB | 1.22 s / 40.8 MiB | pass |
| 75-F Fortress Queries | 0.09 s / 17.7 MiB | 0.89 s / 79.9 MiB | pass |

The isolated reruns of 74-D and 75-B remained at 5.31 and 5.30 seconds. Their
old eight- and seven-second limits left inadequate CPython variance margin, so
both support limits are now 12 seconds. No algorithmic defect was found in
Sections 70--75.

## Sections 76--78

`tools/stress_advanced_76_78.py` forces every suffix-doubling round with unary
strings, maximum query and output volumes, high-state suffix automata, all
200,000 eertree nodes, a 1,000,000-character Booth scan, and a 20-archive case
whose first archive consumes essentially the whole 200,000-character budget.
The checks use exact unary-string formulae, equality metamorphisms, substring
count bounds, and an independently enumerated absent word over a de Bruijn
input.

| Problem | C++ time / RSS | Python time / RSS | Result |
|---|---:|---:|---|
| 76-A Suffix Order And LCP | 0.10 s / 12.1 MiB | 0.91 s / 39.7 MiB | pass |
| 76-B Repeated At Least K Times | 0.10 s / 12.1 MiB | 0.86 s / 40.2 MiB | pass |
| 76-C Pattern Occurrence Queries | 0.10 s / 12.3 MiB | 1.60 s / 41.4 MiB | pass |
| 76-D Disjoint Repeated Substring | 0.10 s / 12.1 MiB | 1.03 s / 39.7 MiB | pass |
| 77-A K-th Distinct Substring | 0.09 s / 64.1 MiB | 0.41 s / 106.5 MiB | pass |
| 77-B Longest Common Substring | 0.07 s / 65.5 MiB | 0.29 s / 85.3 MiB | pass |
| 77-C Palindrome Prefix Profile | 0.05 s / 34.5 MiB | 0.15 s / 85.0 MiB | pass |
| 77-D Shortest Absent Word | 0.03 s / 35.1 MiB | 0.12 s / 69.6 MiB | pass |
| 78-A Minimum Rotation | 0.03 s / 12.6 MiB | 0.14 s / 12.6 MiB | pass |
| 78-B Repetition Spectrum | 0.11 s / 12.1 MiB | 0.93 s / 61.8 MiB | pass |
| 78-C K-th Substring With Multiplicity | 0.05 s / 35.1 MiB | 0.21 s / 87.6 MiB | pass |
| 78-D Common Distinct Substrings | 0.04 s / 34.7 MiB | 0.16 s / 81.8 MiB | pass |
| 78-E Palindrome Frequency Value | 0.03 s / 34.6 MiB | 0.15 s / 80.0 MiB | pass |
| 78-F Multi-Archive Commonality | 0.17 s / 69.3 MiB | 1.37 s / 161.5 MiB | pass |

## Sections 79--81

`tools/stress_advanced_79_81.py` uses maximum-size condensation DAGs and
implication graphs, 200,000-edge Euler tours, reverse-numbered dominator chains
that require the full fixed-point convergence sequence, 200,000-node bridge
trees, nearly 400,000-node block-cut trees with 200,000 queries, and the full
distinct-word length budget. Exact path, SCC-degree, articulation-product,
Euler-order, and dominator-subtree invariants certify the outputs.

| Problem | C++ time / RSS | Python time / RSS | Result |
|---|---:|---:|---|
| 79-A Condensation Profile | 0.05 s / 31.9 MiB | 0.22 s / 106.8 MiB | pass; contradictory `m` bound corrected |
| 79-B Clause Satisfiability | 0.07 s / 45.7 MiB | 0.37 s / 178.3 MiB | pass |
| 79-C Lexicographic Euler Trail | 0.05 s / 12.7 MiB | 0.12 s / 34.8 MiB | pass |
| 79-D Unavoidable Checkpoints | 0.09 s / 11.8 MiB | 1.25 s / 12.4 MiB | pass |
| 80-A Bridge Distance Queries | 0.10 s / 54.5 MiB | 0.56 s / 185.0 MiB | pass |
| 80-B Articulation Pair Damage | 0.07 s / 33.9 MiB | 0.36 s / 178.9 MiB | pass |
| 80-C Mandatory Station Queries | 0.11 s / 59.6 MiB | 1.35 s / 198.1 MiB | pass after memory fix |
| 80-D Two-Edge Connectivity Completion | 0.07 s / 54.5 MiB | 0.35 s / 178.4 MiB | pass |
| 81-A Unique Sink Population | 0.06 s / 31.9 MiB | 0.22 s / 106.9 MiB | pass |
| 81-B Strong Connectivity Repairs | 0.05 s / 31.9 MiB | 0.23 s / 106.8 MiB | pass |
| 81-C Eulerian Word Chain | 0.03 s / 12.2 MiB | 0.05 s / 13.9 MiB | pass |
| 81-D Robbins Orientation | 0.06 s / 28.2 MiB | 0.30 s / 178.5 MiB | pass |
| 81-E Failed Vertex Routes | 0.10 s / 59.6 MiB | 1.31 s / 198.3 MiB | pass after memory fix |
| 81-F Dominator Subtree Queries | 0.10 s / 12.8 MiB | 1.53 s / 30.2 MiB | pass after adding `q <= 200000` |

The Python block-cut references in 80-C and 81-E originally peaked at 256.4
MiB because every binary-lifting ancestor was a separate Python integer.
Packed 32-bit input and ancestor arrays reduce them to 198.1 and 198.3 MiB.
Both modified references pass 101-case independent random-oracle runs. The
source generator carries the same fixes, so regenerating the sections will not
reintroduce them.

Section 81-F previously had no published query bound, making its complexity
contract formally unbounded; it now declares `q <= 200000`. Section 79-A's
simultaneous claims that `m >= 1` and `m` may be zero were replaced by the
intended `0 <= m <= 200000` bound.

## Sections 82--84

`tools/stress_advanced_82_84.py` runs maximum query/output volumes through
full-alphabet wavelet levels, one-extreme-at-a-time segment-tree-beats updates,
repeated whole-array modulo reductions, 200,000 treap splits and merges,
100,000-vertex represented forest paths, and maximum Kruskal reconstruction
trees. Closed-form order statistics, clamp sums, lazy-update totals, path
aggregates, and activation times check every emitted answer.

| Problem | C++ time / RSS | Python time / RSS | Result |
|---|---:|---:|---|
| 82-A Range K-th Value | 0.11 s / 57.1 MiB | 1.15 s / 112.6 MiB | pass |
| 82-B Range Frequency Threshold | 0.11 s / 57.1 MiB | 1.18 s / 109.0 MiB | pass |
| 82-C Range Cap And Sum | 0.08 s / 42.8 MiB | 1.55 s / 115.3 MiB | pass |
| 82-D Range Modulo And Sum | 0.09 s / 18.5 MiB | 2.48 s / 75.4 MiB | pass |
| 83-A Sequence Cut And Paste | 0.15 s / 20.0 MiB | 7.81 s / 98.8 MiB | pass; limit raised 8 -> 12 s |
| 83-B Reversible Range Ledger | 0.12 s / 20.0 MiB | 4.69 s / 76.5 MiB | pass |
| 83-C Dynamic Forest XOR | 0.06 s / 16.1 MiB | 0.60 s / 78.8 MiB | pass |
| 83-D Threshold Component Size | 0.11 s / 62.7 MiB | 0.82 s / 192.9 MiB | pass after memory fix |
| 84-A Quantile Prefix Sum | 0.12 s / 57.1 MiB | 1.34 s / 110.5 MiB | pass |
| 84-B Clamped Terrain | 0.10 s / 42.9 MiB | 2.07 s / 115.2 MiB | pass |
| 84-C Reversible String Hash | 0.13 s / 20.1 MiB | 6.97 s / 77.7 MiB | pass; limit raised 8 -> 12 s |
| 84-D Dynamic Forest Sum | 0.06 s / 16.1 MiB | 0.59 s / 82.3 MiB | pass |
| 84-E Earliest Connection | 0.10 s / 63.5 MiB | 0.86 s / 194.7 MiB | pass after memory fix |
| 84-F Affine Forest Paths | 0.08 s / 16.1 MiB | 0.67 s / 78.1 MiB | pass |

The two treap references remained at 7.81 and 6.97 seconds in a serial rerun,
leaving insufficient variance margin under their former eight-second limits.
Their 12-second limits and the generator's corresponding override now reflect
the measured CPython contract. Packed input arrays reduce 83-D from 214.4 to
192.9 MiB and 84-E from 213.1 to 194.7 MiB; both modified references pass 101
independent random-oracle cases.

## Sections 85--87

`tools/stress_advanced_85_87.py` forces cubic Hungarian tie chains, dense odd
blossom searches, all 200,000 compatibility values, all 79 Gomory--Hu flows
over 1,000-edge multigraphs plus 200,000 queries, every permitted matroid
augmentation, maximum arborescence contraction inputs, and dense deficient
bipartite matching at every bottleneck-search threshold.

| Problem | C++ time / RSS | Python time / RSS | Result |
|---|---:|---:|---|
| 85-A Assignment Cost | 0.06 s / 12.1 MiB | 1.86 s / 12.0 MiB | pass |
| 85-B Forbidden Profit Assignment | 0.06 s / 12.1 MiB | 1.86 s / 12.6 MiB | pass |
| 85-C General Pairing | 0.05 s / 12.6 MiB | 0.89 s / 24.7 MiB | pass |
| 85-D Compatibility Pairing | 0.08 s / 15.5 MiB | 0.72 s / 32.9 MiB | pass after adding input bound |
| 86-A All-Pairs Cut Queries | 0.05 s / 12.6 MiB | 0.19 s / 25.2 MiB | pass |
| 86-B Rainbow Forest | 0.03 s / 11.9 MiB | 0.05 s / 11.6 MiB | pass |
| 86-C Dual Forest | 0.03 s / 11.9 MiB | 0.05 s / 11.7 MiB | pass |
| 86-D Directed Arborescence | 0.02 s / 11.5 MiB | 0.05 s / 11.9 MiB | pass |
| 87-A Bottleneck Assignment | 0.34 s / 13.5 MiB | 9.75 s / 37.1 MiB | pass; limit raised 10 -> 15 s |
| 87-B Roommate Rescue | 0.05 s / 12.7 MiB | 0.82 s / 24.8 MiB | pass after adding input bound |
| 87-C Cut Threshold Pairs | 0.04 s / 12.3 MiB | 0.10 s / 26.8 MiB | pass after adding input bound |
| 87-D Rainbow Spanning Tree | 0.03 s / 11.9 MiB | 0.05 s / 11.8 MiB | pass |
| 87-E Broadcast Backbone | 0.03 s / 11.9 MiB | 0.05 s / 12.2 MiB | pass after adding input bound |
| 87-F Two-Map Forest | 0.03 s / 11.8 MiB | 0.05 s / 11.7 MiB | pass |

The serial bottleneck-assignment adversary takes 9.75 seconds because every
sub-threshold graph is dense but deficient by one job; its old ten-second limit
was not supportable, so the package and generator now use 15 seconds.

Four statements had unbounded input dimensions. They now specify at most
200,000 allowed differences for 85-D, 100,000 edges for 87-B, 1,000 edges for
87-C, and 10,000 edges for 87-E. These are the limits of the source problems
whose kernels the mixed round reuses, and every new simultaneous maximum was
included in the full suite.

## Sections 88--90

`tools/stress_advanced_88_90.py` forces full Newton/NTT precision to 200,000
coefficients, 50,000-point product trees, all `2^20` XOR and `2^22` OR masks,
and every ranked layer of the `2^16` subset convolution. Geometric-series,
formal derivative/integral, constant-polynomial, and transform-identity
invariants certify each maximum-size output.

| Problem | C++ time / RSS | Python time / RSS | Result |
|---|---:|---:|---|
| 88-A Series Inverse | 0.26 s / 13.6 MiB | 8.50 s / 57.9 MiB | pass |
| 88-B Series Logarithm | 0.30 s / 13.5 MiB | 11.23 s / 62.1 MiB | pass |
| 88-C Series Exponential | 0.59 s / 14.5 MiB | 28.85 s / 82.7 MiB | pass; limit raised 15 -> 45 s |
| 88-D Series Square Root | 0.49 s / 14.3 MiB | 16.99 s / 68.7 MiB | pass; limit raised 15 -> 30 s |
| 89-A Multipoint Evaluation | 0.11 s / 16.0 MiB | 3.55 s / 60.8 MiB | pass |
| 89-B Polynomial Interpolation | 0.59 s / 25.7 MiB | 27.70 s / 109.1 MiB | pass |
| 89-C XOR Convolution | 0.11 s / 15.9 MiB | 3.14 s / 82.5 MiB | pass |
| 89-D Subset Convolution | 0.09 s / 16.8 MiB | 1.72 s / 40.3 MiB | pass |
| 90-A Rational Series | 0.31 s / 14.3 MiB | 11.20 s / 62.1 MiB | pass |
| 90-B Connected Series | 0.32 s / 13.6 MiB | 10.86 s / 62.3 MiB | pass |
| 90-C Archive Evaluation | 0.11 s / 16.0 MiB | 3.51 s / 58.4 MiB | pass |
| 90-D Recover Polynomial | 0.58 s / 25.8 MiB | 27.49 s / 109.1 MiB | pass |
| 90-E OR Convolution | 0.45 s / 35.2 MiB | 14.78 s / 125.0 MiB | pass after memory and limit fixes |
| 90-F Disjoint Cover Counts | 0.09 s / 16.9 MiB | 1.72 s / 40.3 MiB | pass |

Serial confirmation left 88-C and 88-D well beyond their original 15-second
contracts, so their generator-backed limits are now 45 and 30 seconds. The
`2^22` Python OR reference originally boxed more than eight million input
values and expanded four million print arguments, peaking at 406.8 MiB.
Packed 32-bit transforms, early input release, and chunked output reduce it to
125.0 MiB. It passes 101 independent random-oracle cases; its measured 14.78
seconds now has a 25-second support limit.

## Sections 91--93

`tools/stress_advanced_91_93.py` uses 100,000 copies of a prime immediately
below `2^64`, 200 balanced 64-bit semiprimes, 63-bit primitive-root and Tonelli
inputs, 100 distinct known discrete logs modulo a prime immediately below
`10^12`, and maximum batch volumes for every mixed application. Factor,
totient, divisor, Carmichael, order, and exponent answers follow directly from
the selected prime factorizations and from the fact that 2 is a primitive root
of the BSGS modulus.

| Problem | C++ time / RSS | Python time / RSS | Result |
|---|---:|---:|---|
| 91-A Prime Or Composite | 0.32 s / 13.9 MiB | 3.26 s / 22.4 MiB | pass |
| 91-B Complete Factorization | 1.83 s / 11.7 MiB | 4.57 s / 11.5 MiB | pass after C++ arithmetic fix |
| 91-C Large Totient | 1.82 s / 11.7 MiB | 4.58 s / 11.6 MiB | pass after C++ arithmetic fix |
| 91-D Large Divisor Statistics | 1.87 s / 11.8 MiB | 4.48 s / 11.8 MiB | pass after C++ arithmetic fix |
| 92-A Smallest Primitive Root | 0.04 s / 11.7 MiB | 0.07 s / 11.8 MiB | pass |
| 92-B Prime Discrete Log | 22.76 s / 52.9 MiB | 28.56 s / 158.8 MiB | pass; limit raised 15 -> 60 s |
| 92-C General Discrete Log | 23.71 s / 52.8 MiB | 35.67 s / 158.9 MiB | pass; limit raised 15 -> 60 s |
| 92-D Modular Square Roots | 0.03 s / 11.8 MiB | 0.06 s / 11.5 MiB | pass |
| 93-A Largest Prime Fragment | 1.92 s / 11.7 MiB | 4.97 s / 11.7 MiB | pass after C++ arithmetic fix |
| 93-B Carmichael Clock | 1.93 s / 11.7 MiB | 4.67 s / 11.7 MiB | pass after C++ arithmetic fix |
| 93-C Multiplicative Order | 1.07 s / 11.8 MiB | 2.51 s / 11.7 MiB | pass after C++ arithmetic fix |
| 93-D Power Congruence | 11.90 s / 52.9 MiB | 14.51 s / 159.1 MiB | pass; limit raised 15 -> 25 s |
| 93-E Quadratic Residue Archive | 0.31 s / 12.0 MiB | 2.17 s / 17.1 MiB | pass |
| 93-F Affine Exponent Meeting | 10.90 s / 53.0 MiB | 14.54 s / 158.9 MiB | pass; limit raised 15 -> 25 s |

The shared C++ Pollard--Rho transition added its random constant after reducing
the square into 64 bits. For moduli near `2^64`, that addition overflowed and a
two-query factorization run did not finish in 120 seconds. Performing the sum
in 128 bits reduces the complete 200-query run to 1.83 seconds. The corrected
generator propagated this kernel to every Section 91--93 C++ reference, and
203 independent factorization/Carmichael oracle cases pass afterward.

At the other extreme, maximum-modulus baby-step giant-step genuinely performs
about two million hash-table steps per query. Full 100-query runs require
22.76--23.71 seconds in C++ and 28.56--35.67 seconds in Python, so both direct
discrete-log limits are now 60 seconds. The 50-query mixed variants are now 25
seconds. All overrides are retained by the source generator.

## Sections 94--96

`tools/stress_advanced_94_96.py` uses 200,000 unsorted half-planes whose
intersection is a known square, 200,000-edge regular convex polygons, maximum
minimum-enclosing-circle inputs, and 2,500 points on a parabola. The parabola
forces the supplied incremental Delaunay implementation's quadratic triangle
scan; its Euclidean MST is the consecutive-point path, giving an independent
closed-form length check. Section 96's six kernels are byte-identical to their
measured Section 94--95 sources.

| Problem | C++ time / RSS | Python time / RSS | Result |
|---|---:|---:|---|
| 94-A Half-Plane Region | 0.10 s / 33.6 MiB | 0.45 s / 134.2 MiB | pass |
| 94-B Circle Overlap | 0.03 s / 11.8 MiB | 0.04 s / 11.6 MiB | pass |
| 94-C Common Tangent Count | 0.03 s / 11.8 MiB | 0.04 s / 11.6 MiB | pass |
| 94-D Largest Inscribed Circle | 0.93 s / 60.0 MiB | 7.74 s / 141.2 MiB | pass after numerical witness fix |
| 95-A Minimum Enclosing Circle | 0.08 s / 18.3 MiB | 0.19 s / 53.9 MiB | pass |
| 95-B Delaunay Radius Sum | 0.05 s / 11.7 MiB | 1.77 s / 11.9 MiB | pass |
| 95-C Euclidean Network | 0.04 s / 11.7 MiB | 1.76 s / 12.3 MiB | pass |
| 95-D Largest Empty Delaunay Circle | 0.04 s / 11.8 MiB | 1.71 s / 12.0 MiB | pass |
| 96-A--F story variants | inherited byte-identically | inherited byte-identically | pass |

The first maximum regular-polygon run exposed a false feasible offset: local
deque closure alone could retain three numerically inconsistent boundaries
and report a radius larger than the polygon's circumradius. The feasibility
test now obtains a candidate corner and verifies it against every shifted edge.
This remains `O(n)` per binary-search step. Both languages pass another 101
independent small inradius-oracle cases after the fix.

## Sections 97--99

`tools/stress_advanced_97_99.py` drives all query counts, digit sums, moduli,
profile widths, heights, terminal masks, and matrix-exponentiation exponents to
their published maxima. Its nice-decomposition adversary simultaneously uses
199,999 nodes, width 15, and about 1.97 million potential states. Closed-form
digit coefficients, impossible maximum sums, complete terminal cliques, and
edgeless-decomposition optima provide exact high-limit answers.

| Problem | C++ time / RSS | Python time / RSS | Result |
|---|---:|---:|---|
| 97-A Digit Sum Range | 0.03 s / 12.1 MiB | 0.12 s / 11.9 MiB | pass after query-amortization fix |
| 97-B Forbidden Decimal Pattern | 0.06 s / 11.8 MiB | 0.29 s / 11.6 MiB | pass |
| 97-C Obstacle Domino Tilings | 0.03 s / 11.7 MiB | 0.09 s / 11.8 MiB | pass |
| 97-D Grid Independent Sets | 0.04 s / 11.7 MiB | 0.36 s / 11.7 MiB | pass |
| 98-A Tower Domino Tilings | 0.03 s / 11.8 MiB | 0.25 s / 11.8 MiB | pass |
| 98-B Connected Cell Sets | 0.06 s / 11.8 MiB | 0.11 s / 11.6 MiB | pass |
| 98-C Terminal Steiner Network | 0.03 s / 11.8 MiB | 0.14 s / 11.7 MiB | pass |
| 98-D Nice-Decomposition Independent Set | 0.25 s / 134.1 MiB | 1.10 s / 157.2 MiB | pass after aggregate-bound fix |
| 99-A Checksum Digit Sum | 0.09 s / 11.8 MiB | 1.18 s / 18.0 MiB | pass after query-amortization fix |
| 99-B Serial Filter | 3.30 s / 11.7 MiB | 6.58 s / 93.9 MiB | pass |
| 99-C Repeating Domino Tower | 0.02 s / 11.7 MiB | 0.07 s / 11.7 MiB | pass |
| 99-D Connected Reserve | 0.06 s / 11.8 MiB | 0.13 s / 11.6 MiB | pass |
| 99-E Terminal Backbone | 0.02 s / 11.8 MiB | 0.13 s / 11.6 MiB | pass |
| 99-F Decomposition Profit | 0.23 s / 134.2 MiB | 1.06 s / 157.2 MiB | pass after aggregate-bound fix |

The former 97-A references rebuilt the same suffix digit-sum DP up to 20,000
times. A single length/sum suffix table now makes each bound scan linear in its
19 digits. Problem 99-A similarly groups queries by modulus, builds one
length/sum/remainder suffix table per distinct modulus, and answers each bound
with tight-prefix lookups. Another 202 independent exhaustive digit-DP cases
pass in both languages.

The treewidth statements previously allowed `t=200000` and width 15 with no
aggregate restriction, which permits billions of states and contradicts the
reference complexity. They now require
`sum(2^|bag|) <= 2000000`; editorials express time in this aggregate budget,
and the full test combines it with the maximum node count. A fixed sample
output mismatch in 99-A was also corrected (`10..20`, digit sum two, divisible
by two contains only 20).

## Course structural audit

Section 62 already contained 50 numbered top-level editorials plus its lettered
companion. The audit tool incorrectly switched to a letters-only heading rule
because the directory uses both prefix styles. Mixed numeric/letter headings
are now recognized, and `python3 tools/audit_course.py` reports no structural
or editorial-specificity issues across all 100 sections.

## Rollout order

The remaining work proceeds in six-section families so shared kernels and
adversaries are measured once and story variants are still checked separately:

1. Sections 64--69: complete;
2. Sections 70--75: complete;
3. Sections 76--81: complete;
4. Sections 82--87: complete;
5. Sections 88--93: complete;
6. Sections 94--99: complete.

The Section 100 release blockers remain independent: inherited kernel evidence
must not be presented as certification of its missing synthesis layers.
