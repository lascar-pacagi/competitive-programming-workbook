# Master+ Extension: Source Map

The master+ phase is self-contained. Its local problems, statements, proofs,
implementations, and tests are original course material. External sources are
used to choose coverage and depth, not as a substitute for teaching material.

## Books consulted

- Victor Shoup, *A Computational Introduction to Number Theory and Algebra*:
  arithmetic functions and Mobius inversion; fast polynomial arithmetic;
  linearly generated sequences; finite fields.
- Ronald Graham, Donald Knuth, and Oren Patashnik, *Concrete Mathematics*:
  floor-quotient sums, recurrence manipulation, binomial identities,
  generating functions, and asymptotic cost accounting.
- Herbert Wilf, *generatingfunctionology*:
  formal power series, coefficient extraction, products as combinatorial
  composition, and recurrences represented by rational generating functions.
- Richard Brent and Paul Zimmermann, *Modern Computer Arithmetic*:
  divide-and-conquer multiplication, FFT/NTT structure, modular transforms,
  and the distinction between algebraic operation counts and machine costs.
- Miklos Bona, *A Walk Through Combinatorics*:
  sieve/inclusion-exclusion arguments, ordinary and exponential generating
  functions, and proof by counting the same family in two ways.

The course paraphrases and rebuilds the relevant arguments. It does not copy
book exercises or passages.

## Contest-topic maps consulted

- [USACO Guide Platinum](https://usaco.guide/plat): advanced range queries,
  tree decompositions, geometry, matrix methods, divide-and-conquer DP, and
  sum-over-subsets DP.
- [USACO Guide Advanced](https://usaco.guide/adv): persistent structures,
  segment-tree beats, treaps, advanced graph decompositions,
  lower-bound/min-cost flow, FFT, suffix structures, arithmetic-function
  prefix sums, and matroid intersection.

The first master+ block (Sections 64--66) deliberately starts with the
mathematical dependency chain: divisor transforms, harmonic quotient blocks,
fast polynomial multiplication, and linear recurrences. Later blocks can use
these tools inside data-structure, graph, geometry, and DP problems.

The second block (Sections 67--69) follows the USACO Platinum/Advanced tree and
data-structure map while closing gaps in the existing course: immutable lazy
tags, rollback over time intervals, direction-aware HLD, centroid branch
subtraction, virtual-tree aggregation, and the amortized small-to-large proof.

The third block (Sections 70--72) follows the Advanced guide's
[flow with lower bounds](https://usaco.guide/adv/flow-lb),
[minimum-cost flow](https://usaco.guide/adv/min-cost-flow), and
[slope trick](https://usaco.guide/adv/slope-trick) coverage. It adds the
missing derivations: lower bounds as vertex imbalance, reduced-cost potential
invariants, exact-count Lagrangian pricing with explicit tie handling, and
threshold selection across enormous convex marginal sequences. The flow API
was also compared with the
[AtCoder Library min-cost-flow contract](https://atcoder.github.io/ac-library/production/document_en/mincostflow.html).

The fourth block (Sections 73--75) extends the
[USACO Platinum geometry map](https://usaco.guide/plat) beyond the course's
existing primitive-only geometry section. Its coverage follows the guide's
[exact geometry primitives](https://usaco.guide/plat/geo-pri) and
[range-sweep](https://usaco.guide/plat/range-sweep) progression, then adds
rotating calipers, Minkowski edge merging, convex point location, union-area
segment trees, and the closest-pair packing proof. Floating-point half-plane
intersection is intentionally deferred to a later geometry block so this one
can make every predicate and checker exact.

The fifth block (Sections 76--78) closes the advanced-string gap identified in
the USACO Advanced guide's [suffix-array module](https://usaco.guide/adv/suffix-array)
and [suffix-structure module](https://usaco.guide/adv/string-suffix). It starts
from suffix ordering and LCP interval geometry, then develops suffix automata
as compressed end-position classes and palindromic trees as one-node-per-
palindrome structures. The mixed contest adds offline LCP connectivity,
occurrence-weighted path DP, multi-string suffix-link propagation, and Booth's
linear rotation elimination. Existing Sections 43--44 already introduce KMP,
tries, and basic suffix-automaton counting; this block deliberately focuses on
the missing Master+ applications rather than repeating them.

The sixth block (Sections 79--81) follows the Advanced guide's SCC, BCC/2CC,
Euler-tour, and critical-vertex map. It fills a prerequisite gap left by the
earlier graph introduction: SCC condensation and low-link decompositions are
now derived before being used as black boxes. The block adds edge-ID-safe
bridge detection for multigraphs, block-cut path queries, constructive 2-SAT
reasoning, directed Euler conditions, Robbins' orientation theorem, and
bounded all-path dominator computation. Every optimized reference is compared
with an independent deletion/reachability oracle on tiny graphs.

The seventh block (Sections 82--84) follows the Advanced guide's wavelet-tree,
segment-tree-beats, treap, and link-cut-tree modules, together with the
Platinum guide's Kruskal reconstruction-tree topic. The lessons emphasize the
state boundary behind each structure: value-prefix routing in wavelet levels,
the unique extremal class permitting a beats update, in-order position as an
implicit treap key, and the distinction between represented and auxiliary
trees in a link-cut tree. Random tests compare every operation sequence with a
literal list, array, or adjacency-list forest oracle.

The eighth block (Sections 85--87) extends the earlier bipartite-flow material
to Hungarian primal-dual assignment, Edmonds blossom contraction, Gomory--Hu
cut trees, directed minimum arborescences, and cardinality matroid
intersection. The local exercises deliberately distinguish two-matroid
intersection from superficially similar three-constraint selection, which is
not polynomial in general. Tiny exhaustive oracles enumerate assignments,
matchings, cuts, arborescences, and independent subsets independently of the
optimized references.

The ninth block (Sections 88--90) uses the polynomial and subset-transform
material as calibration for formal power series, product trees, multipoint
evaluation, interpolation, Walsh--Hadamard transforms, subset zeta transforms,
and ranked subset convolution. The treatment derives Newton precision
doubling from its error invariant rather than presenting formulas as recipes.
Independent quadratic coefficient recurrences and exhaustive mask-pair
enumeration test the optimized NTT and transform references on small cases.

The tenth block (Sections 91--93) develops computational number theory beyond
bounded sieve tables: deterministic 64-bit Miller--Rabin, Pollard--rho,
primitive roots, baby-step--giant-step with non-coprime reductions, and
Tonelli--Shanks. Its random tests use independent trial division and exhaustive
power walks on small domains, while fixed cases exercise the large-integer
paths.

The eleventh block (Sections 94--96) extends the earlier exact convex-geometry
material to continuous feasible regions and proximity structure: half-plane
intersection, circle lenses and tangencies, randomized minimum enclosing
circles, incremental Delaunay triangulation, and Delaunay-sparsified Euclidean
MST. Tiny tests use polygon clipping, exhaustive boundary circles, empty-circle
enumeration, and complete-graph Prim as independent oracles.

The twelfth block (Sections 97--99) develops dynamic programming on compressed
boundaries. It combines tight digit states with finite automata, turns row
profiles into transfer matrices, canonicalizes connectivity partitions in
plug DP, and then moves the same boundary principle to terminal-subset and
nice-tree-decomposition DP. The mixed contest uses new product states,
periodic obstacles, forced cells, multi-mask Steiner queries, and a
vertex-cover reduction rather than repeating the teaching statements. Tiny
oracles enumerate integers, tilings, cell subsets, edge subsets, and vertex
subsets independently of the optimized references.
