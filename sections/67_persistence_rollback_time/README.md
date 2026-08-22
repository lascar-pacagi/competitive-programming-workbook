# Section 67: Persistence, Rollback, And Time

This master+ section studies two ways to revisit the past without copying the
entire state. A and B use immutable versions; C uses rollback while a segment
tree organizes time intervals. D is the blind exercise.

| Problem | Main tool |
|---|---|
| A. Branching Multiset | persistent frequency segment tree |
| B. Versioned Range Add | persistent lazy segment tree |
| C. Dynamic Connectivity | rollback DSU and segment tree over time |
| D. Tree Path K-th | four persistent prefix roots and LCA |

Run `CP_TARGET=solution python3 sections/67_persistence_rollback_time/check.py`.
