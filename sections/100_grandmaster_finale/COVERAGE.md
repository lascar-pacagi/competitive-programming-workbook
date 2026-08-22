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
| 12 | Parametric Quota Cut | Lagrangian relaxation | minimum cut, exact-cardinality recovery | 2500 |
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
| 28 | Interval LCP Aggregates | LCP Cartesian tree | DSU merging, contribution counting | 2400 |
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
| 36 | Factorized Exponent Tower | Pollard--rho | Carmichael recursion, non-coprime exponent handling | 2500 |
| 37 | Modular Root Catalogue | primitive-root coordinates | linear congruences, root enumeration | 2400 |
| 38 | Composite Discrete Log | generalized BSGS | CRT, gcd reduction, minimality | 2500 |
| 39 | Summatory Multiplicative Blocks | floor-quotient decomposition | Moebius inversion, harmonic intervals | 2500 |
| 40 | GCD Convolution Queries | divisor transforms | Moebius inversion, offline frequency updates | 2400 |

## Round V — Geometry, frontiers, and grand synthesis

| No. | Problem | Primary technique | Secondary techniques | Target |
|---:|---|---|---|---|
| 41 | Moving Convex Robots | Minkowski sums | rotating calipers, exact segment distance | 2400 |
| 42 | Safe Radius Region | half-plane intersection | inward offsets, monotone search | 2300 |
| 43 | Circle Network Bottleneck | Delaunay triangulation | Kruskal reconstruction tree, LCA | 2600 |
| 44 | Rectangle Coverage Moments | sweep-line segment tree | multi-coverage lengths, modular integration | 2400 |
| 45 | Offline Dynamic Hull Queries | hull rollback | segment tree over time, tangent queries | 2600 |
| 46 | Digit Language Arithmetic | digit DP | Aho--Corasick, remainders, range subtraction | 2300 |
| 47 | Periodic Connected Tiling | plug DP | canonical labels, transfer exponentiation | 2700 |
| 48 | Prize Steiner Frontier | Steiner subset DP | Lagrangian quota, multi-source Dijkstra | 2600 |
| 49 | Treewidth Connected Cover | nice tree-decomposition DP | connectivity partitions, join correction | 2800 |
| 50 | Chronicle Path Dictionary | tree-path decomposition | persistent suffix intervals, offline order statistics | 2900 |

## Round VI — Synthesis gauntlet

These fifteen problems are synthesis-first. Removing any named component must
break the intended complexity or correctness; a decorative combination does
not qualify.

| No. | Problem | Technique interaction | Why the interaction is essential | Target |
|---:|---|---|---|---|
| 51 | Versioned Path Pattern Census | version tree + HLD + Aho--Corasick failure tree + rollback Fenwick | each version changes active patterns, while each query text is assembled from directed tree-path fragments | 2800 |
| 52 | Temporal Geometric Alliances | segment tree over time + spatial hashing + rollback parity DSU | proximity edges exist only during overlapping lifetimes, and every edge also imposes a parity relation | 2900 |
| 53 | Colored Cut-Tree Summaries | Gomory--Hu tree + virtual trees + small-to-large aggregation | pair min-cuts become path minima, but each query restricts endpoints to a new sparse color set | 2700 |
| 54 | Exact Fleet Circulation | lower-bound min-cost flow + convex marginal costs + Aliens tie handling | feasibility, convex quantity costs, and an exact number of activated routes must be enforced simultaneously | 3000 |
| 55 | Palindromic Paths Through Centroids | centroid decomposition + bidirectional hashing + polynomial convolution | path palindromes split at centroids, and equal-length hash classes must be paired in bulk | 3000 |
| 56 | Congruent Substring Selection | suffix-array intervals + persistent order statistics + CRT | lexical constraints define suffix intervals, positional congruences define CRT classes, and the answer is the k-th surviving occurrence | 2800 |
| 57 | Polynomial Tree Colorings | tree DP + small-to-large polynomial products + NTT | every child contributes a generating polynomial and total degree is too large for quadratic merging | 2800 |
| 58 | Multiplicative Set Partitions | divisor zeta/Moebius transforms + ranked subset convolution | gcd/lcm restrictions act on divisor coordinates while disjoint group formation acts on mask ranks | 3100 |
| 59 | Factorized Recurrence Oracle | Pollard--rho + Carmichael reduction + Bostan--Mori | enormous indices are exponent expressions modulo a recurrence period whose valid reduction depends on factorization and non-coprimality | 3000 |
| 60 | Delaunay Terminal Backbone | Delaunay sparsification + Kruskal reconstruction tree + virtual-tree DP | geometric edges must first be sparsified, bottleneck connectivity compressed, then optimized over query-specific terminal sets | 2900 |
| 61 | Moving Half-Plane Assignment | half-plane intersection + parametric search + Hungarian feasibility | each agent's feasible region changes with time, creating a monotone geometric compatibility graph whose perfect matching decides the answer | 2900 |
| 62 | Historical Rectangle Quantiles | CDQ over time + sweep-line Fenwick + parallel binary search | updates and rectangle restrictions are temporal, while each query asks for an order statistic rather than a count | 3000 |
| 63 | Periodic Forbidden Frontier | Aho--Corasick product automaton + broken-profile DP + sparse matrix exponentiation | every repeated row changes both occupancy and a boundary word automaton, so neither transfer state alone is sufficient | 3100 |
| 64 | Connected Cover On Bags | nice tree-decomposition DP + canonical connectivity partitions + subset convolution at joins | weighted choices must cover edges and form one component, while join nodes require fast partition-compatible merging | 3200 |
| 65 | Temporal Steiner Dictionary | offline version tree + suffix automaton intervals + virtual-tree Steiner DP + persistent counts | each version selects dictionary strings, each query creates terminals from substring occurrences, and only their compressed tree can be processed in time | 3300 |

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
| cross-family synthesis under versioning, geometry, algebra, and separators | 51--65 |

No row is satisfied merely by mentioning a technique. The final editorial must
identify where it enters the algorithm and which invariant or theorem makes
the combination valid.
