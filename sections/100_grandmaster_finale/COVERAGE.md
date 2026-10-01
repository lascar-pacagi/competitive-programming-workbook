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

## Round IV — Algebra and number theory

These problems (and Round V) replaced copies of earlier sections' problems.

| No. | Problem | Key idea | Supporting techniques | Target |
|---:|---|---|---|---|
| 31 | Two-Faction Networks | log of the 2-coloured-graph EGF, halved | sqrt(2) chirp: 2^{k(n-k)} as one convolution | 2900 |
| 32 | Exponential Polynomial Ledger | S(k) = r^k G(k) + c with deg G <= d | finite differences fix c, Lagrange at n mod p | 2800 |
| 33 | Branching Family Census | Newton iteration on T = x phi(T) | power-series inverse, Horner composition | 2800 |
| 34 | Coin Bag Census | log of prod 1/(1-x^w) is a harmonic sum | power-series exponential | 2700 |
| 35 | Staircase Moments | Euclid-like floor-sum recursion for three moments | swapping rows and columns of lattice points | 2800 |
| 36 | Binomial Ledger | factorials with p removed (generalized Lucas) | Legendre valuations, CRT over prime powers | 2700 |
| 37 | Rabbit Cycle | Pisano period as a matrix order | Pollard rho, Frobenius bound p-1 / 2(p+1) / 20 | 2800 |
| 38 | Exclusive Range Ledger | prefix XOR basis keeping the newest vectors | 2^(len - rank), offline sweep | 2600 |
| 39 | Divisor Echo Power | Omega is a derivation of Dirichlet convolution | O(N log N) recurrence, k only mod p | 3000 |
| 40 | Root Census Modulo p | deg gcd(f, x^p - x) | polynomial powering with Barrett reduction | 2800 |

## Round V — Geometry, grids, and subsets

| No. | Problem | Key idea | Supporting techniques | Target |
|---:|---|---|---|---|
| 41 | Sprinkler Coverage Area | Green's theorem over uncovered arcs | containment removal, angular intervals | 2700 |
| 42 | Crystal Hull Surface | incremental 3D convex hull | horizon edges, exact 128-bit orientation | 2800 |
| 43 | Triangle Census Queries | "points below segment" table | slope sweep with dominance counting | 2600 |
| 44 | Polygon Triangulation Count | interval DP over internal diagonals | cone test, proper-intersection test | 2600 |
| 45 | Obstacle Shortcut | visibility graph of corners | exact segment clipping, Dijkstra | 2600 |
| 46 | Lantern Grid | light chasing reduces nm unknowns to m | GF(2) elimination with bitsets | 2600 |
| 47 | Quorum Circle | binary search with an angular sweep | boundary-point normalization | 2700 |
| 48 | Quiet Committee Census | meet in the middle on independent sets | subset DP with optimal-set counting | 2600 |
| 49 | Glacier Cut | binary searches over sorted edge angles | prefix shoelace sums, exact rational crossings | 2700 |

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
| complexity, compression, prefix reasoning, sorting, binary search | all rounds; especially 01, 04, 12, 15, 47, 64 |
| greedy, stacks, heaps, exchange arguments | 07, 13, 17, 19 |
| BFS/DFS, DSU, shortest paths, MST | 02, 07, 10, 16, 43, 48 |
| classical, interval, tree, mask, and game-style DP habits | 03, 17, 19, 30, 44, 48, 61 |
| modular arithmetic, CRT, combinatorics, probability/randomization | 31--40, 53, 57, 59 |
| Fenwick/segment trees, sparse tables, lifting, HLD | 01, 04, 08--10, 21, 25, 44 |
| flows, matching, cuts, matroids, arborescences | 11--20 |
| convex optimization and discrete convexity | 03, 11, 12, 17, 19 |
| suffix structures, automata, hashing, editable sequences | 21--30, 50 |
| persistence, rollback, dynamic forests | 01--05, 08, 10, 29, 56, 62 |
| SCC/low-link/dominator/decomposition proof habits | 07, 14, 16, 18, 49 |
| polynomial algorithms and subset transforms | 06, 26, 30, 31--34, 40, 59, 63 |
| large-integer and multiplicative number theory | 35--40, 57 |
| convex, sweep, circle, and proximity geometry | 41--45, 47, 49, 55, 60 |
| profile, plug, bitset, and subset frontiers | 46, 48, 63 |
| decisive-idea gauntlet across strings, graphs, trees, algebra, and number theory | 50--65 |

No row is satisfied merely by mentioning a technique. The final editorial must
identify where it enters the algorithm and which invariant or theorem makes
the combination valid.
