# Section 100 Coverage Matrix

Section 100 is a sixty-five-problem Master-to-Grandmaster finale. Every problem is
new and self-contained. The point is not to repeat one exercise from every
earlier section: each problem has a primary technique and deliberately combines
it with one or more earlier tools.

The implementation status is tracked separately from this design. A problem is
part of the published section only after its statement, fixed tests, randomized
oracle, C++ reference, Python reference where viable, and full editorial have
all been validated.

## Round I — Time, versions, and trees

| No. | Problem | Primary technique | Secondary techniques | Target |
|---:|---|---|---|---|
| 01 | Temporal Path Median | persistent value trees | LCA, root inclusion--exclusion, binary search on values | 2100 |
| 02 | Bipartite Timeline | rollback parity DSU | segment tree over time, counting components | 2100 |
| 03 | Versioned Convex DP | rollback Li Chao tree | version-tree DFS, discrete coordinates, identity tie-breaking | 2300 |
| 04 | Historical Rectangle Selection | CDQ divide and conquer | Fenwick tree, coordinate compression, optimal-solution counting | 2300 |
| 05 | Dynamic Forest Ledger | link--cut tree | lazy affine path updates, path aggregates | 2400 |
| 06 | Colored Distance Census | centroid decomposition | polynomial convolution, inclusion--exclusion | 2500 |
| 07 | Virtual Tree Firewall | virtual trees | LCA path minima, lexicographic weighted tree DP | 2300 |
| 08 | Subtree Order Laboratory | Euler tours | offline Fenwick-of-Fenwick allocation, dynamic order statistics | 2300 |
| 09 | Ancestral Pattern Index | heavy--light decomposition | bidirectional double hashes, chunked LCP search | 2400 |
| 10 | Kruskal Time Machine | reconstruction tree | persistent segment tree, offline threshold queries | 2400 |

## Round II — Optimization, flows, matching, and cuts

| No. | Problem | Primary technique | Secondary techniques | Target |
|---:|---|---|---|---|
| 11 | Bounded Convex Shipping | min-cost circulation | lower bounds, convex marginal edges, potentials | 2400 |
| 12 | Quota Project Portfolio | Lagrangian relaxation | minimum cut, exact-cardinality recovery | 2500 |
| 13 | Rainbow Bottleneck Forest | matroid intersection | threshold monotonicity, graphic and partition oracles | 2500 |
| 14 | Rooted Broadcast Choice | directed arborescence | super-root modeling, cycle contraction | 2400 |
| 15 | Pairing Under Thresholds | general matching | offline threshold search, blossom feasibility | 2400 |
| 16 | All-Pairs Cut Statistics | Gomory--Hu tree | tree path minima, offline aggregation | 2300 |
| 17 | Isotonic Tree Labels | slope trick | small-to-large heap merging, tree DP | 2500 |
| 18 | Circulation Repair Queries | bounded circulation | residual reachability, sensitivity certificates | 2500 |
| 19 | Convex Resource Schedule | Aliens trick | convex-hull DP, exact-count tie handling | 2600 |
| 20 | Laminar Assignment | weighted assignment | segment-tree compression, dual potentials | 2500 |

## Round III — Strings and sequences

| No. | Problem | Primary technique | Secondary techniques | Target |
|---:|---|---|---|---|
| 21 | Persistent Text Occurrences | suffix array intervals | persistent segment tree, range order statistics | 2300 |
| 22 | Multi-Archive Common Substrings | generalized suffix automaton | occurrence propagation, per-string minima | 2400 |
| 23 | Palindromic Range Census | palindromic tree | offline Fenwick sweeps, failure links | 2500 |
| 24 | Lexicographic Substring Laboratory | suffix array and LCP | Cartesian trees, wavelet queries | 2500 |
| 25 | Dynamic Pattern Ledger | Aho--Corasick automaton | failure-tree Euler tour, Fenwick activation | 2400 |
| 26 | Cyclic Match Convolution | NTT convolution | string encoding, wildcard correction | 2300 |
| 27 | Distinct Substring Rank | suffix automaton path DP | lexicographic unranking, capped counting | 2300 |
| 28 | Suffix Pair Affinity | LCP Cartesian tree | DSU merging, contribution counting | 2400 |
| 29 | Editable Palindrome Rope | implicit treap | forward/reverse hashes, lazy reversal | 2500 |
| 30 | Forbidden Superstring Count | automaton product | matrix exponentiation, inclusion--exclusion | 2400 |

## Round IV — Algebra and computational number theory

| No. | Problem | Primary technique | Secondary techniques | Target |
|---:|---|---|---|---|
| 31 | Connected Structure Series | formal logarithm/exponential | NTT, combinatorial decomposition | 2400 |
| 32 | Rational Recurrence Samples | linear recurrences | Bostan--Mori, multipoint evaluation | 2500 |
| 33 | Subset Partition Spectrum | ranked subset convolution | zeta/Moebius transforms, generating functions | 2500 |
| 34 | XOR Walk Spectrum | Walsh--Hadamard transform | exponentiation in transform space | 2300 |
| 35 | Polynomial Constraint Recovery | interpolation | product trees, derivative evaluation | 2400 |
| 36 | Universal Exponent Clock | Pollard--rho | Carmichael recursion, non-coprime exponent handling | 2500 |
| 37 | Modular Root Catalogue | primitive-root coordinates | linear congruences, root enumeration | 2400 |
| 38 | Composite Discrete Log | generalized BSGS | CRT, gcd reduction, minimality | 2500 |
| 39 | Summatory Multiplicative Blocks | floor-quotient decomposition | Moebius inversion, harmonic intervals | 2500 |
| 40 | GCD Convolution Queries | divisor transforms | Moebius inversion, offline frequency updates | 2400 |

## Round V — Geometry, frontiers, and grand synthesis

| No. | Problem | Primary technique | Secondary techniques | Target |
|---:|---|---|---|---|
| 41 | Moving Convex Robots | Minkowski sums | rotating calipers, exact segment distance | 2400 |
| 42 | Safe Radius Region | half-plane intersection | inward offsets, monotone search | 2300 |
| 43 | Fibre Network Length | Delaunay triangulation | Kruskal reconstruction tree, LCA | 2600 |
| 44 | Double-Covered Area | sweep-line segment tree | multi-coverage lengths, modular integration | 2400 |
| 45 | Hull Membership Queries | hull rollback | segment tree over time, tangent queries | 2600 |
| 46 | Digit Language Arithmetic | digit DP | Aho--Corasick, remainders, range subtraction | 2300 |
| 47 | Periodic Domino Tower | plug DP | canonical labels, transfer exponentiation | 2700 |
| 48 | Terminal Backbone Frontier | Steiner subset DP | Lagrangian quota, multi-source Dijkstra | 2600 |
| 49 | Decomposition Vertex Cover | nice tree-decomposition DP | connectivity partitions, join correction | 2800 |
| 50 | Chronicle Path Dictionary | Aho--Corasick run down a tree | fail-tree Euler ranges, offline root-path Fenwick counts, KMP across the LCA | 2800 |

## Round VI — Grandmaster gauntlet

These problems are new packages (Problems 50--65 previously repeated earlier
kernels).  Each one needs a decisive idea on top of the machinery practised in
Rounds I--V; the statements do not name it.

| No. | Problem | Key idea | Supporting techniques | Target |
|---:|---|---|---|---|
| 51 | Echo Census | runs theorem via Lyndon arrays under both letter orders | hashing LCE, at most `p` distinct squares per run and multiple | 3000 |
| 52 | Tariff Revision Network | offline dynamic MST by divide and conquer | contraction of forced edges, reduction of useless edges | 3000 |
| 53 | Spanning Weight Spectrum | matrix-tree theorem with polynomial edge weights | evaluation at many points, Lagrange interpolation | 2700 |
| 54 | Fleet Pairing | weighted general matching (primal--dual blossoms) | dual adjustments, blossom expansion | 3300 |
| 55 | Monsoon Diameter | paths as points; upper envelope of all path vectors | binarization, edge-centroid decomposition, Minkowski sums of hulls | 3200 |
| 56 | Window Substring Census | last-occurrence counting on the suffix-link tree | suffix automaton, link-cut access colouring, range-add Fenwick | 3200 |
| 57 | Prime Power Xor Sum | Min_25 sieve | Lucy prime sums, least-prime-factor recursion | 3000 |
| 58 | Critical Link Audit | dominator tree of the edge-subdivided graph | Lengauer--Tarjan with path compression | 2700 |
| 59 | Walk Count Oracle | hidden linear recurrence of `e_s^T A^N e_t` | Berlekamp--Massey, Bostan--Mori | 2800 |
| 60 | Taxicab Backbone | Manhattan MST with O(n) octant candidates | Fenwick sweeps, small-to-large offline bottleneck queries | 2800 |
| 61 | Cavern Descent | Li Chao trees merged up a rooted tree | line containers, amortized merging | 2700 |
| 62 | Window Component Census | newest-edge spanning forest in a link--cut tree | replaced-edge indices, offline Fenwick counting | 3000 |
| 63 | Periodic Loop Frontier | plug DP generating terms of a hidden recurrence | bracket profiles, Berlekamp--Massey, Bostan--Mori | 3100 |
| 64 | Beacon Placement | binary search with 2-SAT | segment-tree implication graph, iterative Tarjan | 2800 |
| 65 | Temporal Steiner Span | union of root paths by recency | HLD chain stacks, colour Fenwick, range LCA by DFS order | 3000 |

## Course-wide coverage

The sixty-five problems cover every major technique family from Sections 1--99:

| Earlier material | Finale problems |
|---|---|
| complexity, compression, prefix reasoning, sorting, binary search | all rounds; especially 01, 04, 12, 15, 42 |
| greedy, stacks, heaps, exchange arguments | 07, 13, 17, 19, 35 |
| BFS/DFS, DSU, shortest paths, MST | 02, 07, 10, 16, 43, 48 |
| classical, interval, tree, mask, and game-style DP habits | 03, 17, 19, 30, 33, 46--49 |
| modular arithmetic, CRT, combinatorics, probability/randomization | 31--40, randomized 43 |
| Fenwick/segment trees, sparse tables, lifting, HLD | 01, 04, 08--10, 21, 25, 44 |
| flows, matching, cuts, matroids, arborescences | 11--20 |
| convex optimization and discrete convexity | 03, 11, 12, 17, 19 |
| suffix structures, automata, hashing, editable sequences | 21--30, 50 |
| persistence, rollback, dynamic forests | 01--05, 08, 10, 29, 45 |
| SCC/low-link/dominator/decomposition proof habits | 07, 14, 16, 18, 49 |
| polynomial algorithms and subset transforms | 06, 26, 30--35, 40, 47 |
| large-integer and multiplicative number theory | 36--40 |
| convex, sweep, circle, and proximity geometry | 41--45 |
| digit, profile, plug, Steiner, and treewidth frontiers | 46--49 |
| decisive-idea gauntlet across strings, graphs, trees, algebra, and number theory | 50--65 |

No row is satisfied merely by mentioning a technique. The final editorial must
identify where it enters the algorithm and which invariant or theorem makes
the combination valid.
