# Section 42: Advanced Data Structures Mixed Contest

A mixed contest using only techniques taught through section 41. Attempt
A--F as the core set, then G--L for further combinations of established tools.
HLD and persistence are taught later, in sections 68 and 67 respectively.

## Prerequisites and coverage

| Earlier technique | Local exercises |
|---|---|
| Count-guided segment-tree descent (40) | A. Dynamic Order Statistics |
| Lazy propagation (37) | B. Range Assign and Add |
| Sorting, compression, offline sweeps, Fenwick (13, 36) | C. Static Rectangle Count; D. Nested Ranges Count |
| Euler intervals with Fenwick or segment trees (36, 37, 41) | E. Subtree Add, Point Query; F. Dynamic Subtree Maximum |
| Euler intervals with offline counting (13, 36, 41) | G. Subtree Value Count |
| Ordinary insertion-only DSU (18) | H. Incremental Connectivity |
| Euler intervals with lazy propagation (37, 41) | I. Subtree Assign, Add, and Sum; L. Subtree Add, Subtree Maximum |
| Static prefix sums with LCA (4, 41) | J. Static Vertex Path Sums |
| Static sweeps with weighted Fenwick sums (13, 36) | K. Static Weighted Rectangles |

All twelve problems have statements, C++ and Python reference solutions,
fixed examples, random generators with small independent oracles, and
deterministic maximum-size performance tests. H has three adversarial
`n = q = 200000` cases; the other exercises have one each. The standard judge
runs these even when random tests are disabled.

Run `CP_TARGET=solution python3 sections/42_advanced_data_structures_mixed/check.py --keep-going`.
