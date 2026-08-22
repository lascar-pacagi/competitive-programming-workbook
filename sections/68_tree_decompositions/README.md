# Section 68: Advanced Tree Decompositions

This section decomposes a tree in three different senses: heavy paths for
ordered path products, centroid ancestors for dynamic distance queries, and a
query-specific virtual tree for sparse marked sets. D adds the complementary
small-to-large merging pattern.

| Problem | Main tool |
|---|---|
| A. Path Affine Composition | noncommutative HLD |
| B. Toggle Nearest Beacon | centroid decomposition |
| C. Marked Pair Distances | virtual tree DP |
| D. Subtree Mode Sum | small-to-large map merging |

Run `CP_TARGET=solution python3 sections/68_tree_decompositions/check.py`.
