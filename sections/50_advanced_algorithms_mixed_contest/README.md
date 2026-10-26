# Section 50: Advanced Algorithms Mixed Contest

This contest contains nineteen original local problem packages, A--S.
M--S add a second problem for every technical section between the mixed
contests in sections 42 and 50: sections 43--49 now each have two main
representatives here. Section 41 already has several applications in section
42, including I. Rerooted Subtree Sums and J. Minimum Bottleneck Routes.

All seven new packages have full statements and constraints, C++ and Python
references, untouched public student stubs, fixed edge cases, independent small
randomized oracles, and two maximum-size performance workloads each. The
standard judge runs performance cases as well as fixed and randomized cases.

## Study order

Attempt A--S without opening the editorial. For shorter sessions, use A--F,
G--L, and M--S as three separate rounds. M--S are arranged by source topic,
not by increasing difficulty. L is an optional min-cost-flow extension: it
requires the extra explanation in its editorial and is not counted as one of
the two main problems for section 45.

- [A. DAG Grundy](problems/a_dag_grundy/README.md)
- [B. General CRT](problems/b_general_crt/README.md)
- [C. Fast Fibonacci](problems/c_fast_fibonacci/README.md)
- [D. Fibonacci Range Sum](problems/d_fibonacci_range_sum/README.md)
- [E. Pattern Prefix Matches](problems/e_pattern_prefix_matches/README.md)
- [F. Suffix LCP Queries](problems/f_suffix_lcp_queries/README.md)
- [G. Domino Placement](problems/g_domino_placement/README.md)
- [H. Weighted Tree Distances](problems/h_weighted_tree_distances/README.md)
- [I. Balanced Subset Difference](problems/i_balanced_subset_difference/README.md)
- [J. Monge Partition Table](problems/j_monge_partition_table/README.md)
- [K. Online Line DP](problems/k_online_line_dp/README.md)
- [L. Profitable Disjoint Routes](problems/l_profitable_disjoint_routes/README.md)
- [M. Dial Alignment](problems/m_dial_alignment/README.md)
- [N. Archive Reassembly](problems/n_archive_reassembly/README.md)
- [O. Relay Throughput](problems/o_relay_throughput/README.md)
- [P. Last Alarm](problems/p_last_alarm/README.md)
- [Q. Exact Beacon Codes](problems/q_exact_beacon_codes/README.md)
- [R. Warehouse Blocks](problems/r_warehouse_blocks/README.md)
- [S. Parabolic Signals](problems/s_parabolic_signals/README.md)

<details>
<summary>Coverage map (consult after an independent attempt)</summary>

| Source section | Topic | First problem | Second problem |
|---|---|---|---|
| 43 | String algorithms I | [E. Pattern Prefix Matches](problems/e_pattern_prefix_matches/README.md) | [M. Dial Alignment](problems/m_dial_alignment/README.md) |
| 44 | String algorithms II | [F. Suffix LCP Queries](problems/f_suffix_lcp_queries/README.md) | [N. Archive Reassembly](problems/n_archive_reassembly/README.md) |
| 45 | Flows and matchings | [G. Domino Placement](problems/g_domino_placement/README.md) | [O. Relay Throughput](problems/o_relay_throughput/README.md) |
| 46 | Rerooting and advanced tree DP | [H. Weighted Tree Distances](problems/h_weighted_tree_distances/README.md) | [P. Last Alarm](problems/p_last_alarm/README.md) |
| 47 | Meet-in-the-middle | [I. Balanced Subset Difference](problems/i_balanced_subset_difference/README.md) | [Q. Exact Beacon Codes](problems/q_exact_beacon_codes/README.md) |
| 48 | DP optimization | [J. Monge Partition Table](problems/j_monge_partition_table/README.md) | [R. Warehouse Blocks](problems/r_warehouse_blocks/README.md) |
| 49 | Convex hull trick and Li Chao | [K. Online Line DP](problems/k_online_line_dp/README.md) | [S. Parabolic Signals](problems/s_parabolic_signals/README.md) |

A--D additionally revisit game theory, congruences, and fast recurrences from
earlier phases. L adds the optional min-cost-flow synthesis.

</details>

## Local judge

```bash
python3 sections/50_advanced_algorithms_mixed_contest/check.py
CP_TARGET=solution python3 sections/50_advanced_algorithms_mixed_contest/check.py --keep-going
CP_TARGET=solution python3 sections/50_advanced_algorithms_mixed_contest/check.py --problem m,n,o,p,q,r,s --keep-going
```

Use the editorial to upsolve: it gives the reduction, proof, complexity,
implementation pitfalls, and complete C++ and Python solutions. The source
includes the actual tested reference files, so the displayed code stays in sync.
