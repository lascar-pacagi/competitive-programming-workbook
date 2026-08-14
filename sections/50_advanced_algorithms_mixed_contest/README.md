# Section 50: Advanced Algorithms Mixed Contest

This contest has twelve self-contained local problem packages. Problems G--L
form its progressively harder final half.

## Category Coverage

| Advanced-algorithm category | Contest problem |
|---|---|
| String algorithms I | [E. Pattern Prefix Matches](problems/e_pattern_prefix_matches/README.md) |
| String algorithms II | [F. Suffix LCP Queries](problems/f_suffix_lcp_queries/README.md) |
| Flows and matchings | [G. Domino Placement](problems/g_domino_placement/README.md) |
| Rerooting and advanced tree DP | [H. Weighted Tree Distances](problems/h_weighted_tree_distances/README.md) |
| Meet-in-the-middle | [I. Balanced Subset Difference](problems/i_balanced_subset_difference/README.md) |
| Divide-and-conquer DP optimization | [J. Monge Partition Table](problems/j_monge_partition_table/README.md) |
| Convex hull trick and Li Chao tree | [K. Online Line DP](problems/k_online_line_dp/README.md) |
| Min-cost flow synthesis | [L. Profitable Disjoint Routes](problems/l_profitable_disjoint_routes/README.md) |

Problems A--D revisit earlier advanced ideas, E--F bridge into Phase 6, and
G--L increase progressively from matching through min-cost flow.

## Study Order

1. Attempt problems A through L as a virtual contest. If you split it, use A--F
   as day one and G--L as the harder day two.
2. Run:

```bash
python3 sections/50_advanced_algorithms_mixed_contest/check.py
```

To validate the reference solutions:

```bash
CP_TARGET=solution python3 sections/50_advanced_algorithms_mixed_contest/check.py
```

3. Use this section's coverage guide and the full reference implementations to
   upsolve each problem.
4. Continue with the external reinforcement in `PRACTICE.md`.
