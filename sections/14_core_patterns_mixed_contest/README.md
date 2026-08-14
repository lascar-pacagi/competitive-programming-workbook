# Section 14: Core Patterns Mixed Contest

This section closes Phase 1 with a short mixed set. The main skill is choosing
the right pattern from Sections 8 through 13 under contest pressure.

## Category Coverage

The four original problems form the timed core. One additional local problem
combines the two missing categories.

| Core-pattern category | Problem |
|---|---|
| Binary search on the answer | B. Minimum Split Limit |
| Greedy exchange arguments | D. First Free Slot |
| Greedy invariants and constructive algorithms | [E. Smallest Distinct Subsequence](problems/e_smallest_distinct_subsequence/README.md) |
| Intervals and sweep line | C. Active Colors; D. First Free Slot |
| Stacks, queues, and deques | [E. Smallest Distinct Subsequence](problems/e_smallest_distinct_subsequence/README.md) |
| Offline processing | C. Active Colors |

Complete Window remains useful cumulative review of the preceding foundation
phase, but it is not used as a substitute for either missing Phase 1 category.

## Focused Stack and Greedy Training

After the A--E mixed contest, use these six original exercises as a progressive
training ladder:

| Problem | Main training goal |
|---|---|
| [F. Adjacent Cancellation](problems/f_adjacent_cancellation/README.md) | basic stack state |
| [G. Next Smaller Distance](problems/g_next_smaller_distance/README.md) | monotonic stack |
| [H. Smallest Fixed-Length Subsequence](problems/h_smallest_fixed_subsequence/README.md) | lexicographic monotonic stack |
| [I. Wildcard Parentheses](problems/i_wildcard_parentheses/README.md) | greedy feasibility interval |
| [J. Interval Point Cover](problems/j_interval_point_cover/README.md) | exchange argument |
| [K. Deadline Selection](problems/k_deadline_selection/README.md) | greedy selection with a heap |

Each package contains C++ and Python stubs, references, fixed cases, and
randomized tests with a small brute-force oracle.

## Reinforcement Set

If H, I, or K was difficult, continue with these six original exercises. They
repeat the underlying decisions in new settings rather than duplicating an
existing course problem.

| Problem | Main training goal |
|---|---|
| [L. Smallest After Deletions](problems/l_smallest_after_deletions/README.md) | deletion-budget monotonic stack |
| [M. Required Letter Subsequence](problems/m_required_letter_subsequence/README.md) | lexicographic choice with two feasibility constraints |
| [N. Wildcard Choice Map](problems/n_wildcard_choice_map/README.md) | combine prefix and suffix feasibility |
| [O. Minimum Parenthesis Depth](problems/o_minimum_parenthesis_depth/README.md) | combine balance intervals with binary search |
| [P. Common Deadline](problems/p_common_deadline/README.md) | build the exchange argument behind shortest-first |
| [Q. Event Attendance](problems/q_event_attendance/README.md) | schedule currently available events by urgency |

## Greedy Proof Laboratory

The final six original exercises concentrate on recognizing *why* a greedy
choice is safe. Each uses a different proof shape:

| Problem | Greedy reasoning to practice |
|---|---|
| [R. Coverage Patches](problems/r_coverage_patches/README.md) | fill the first unavoidable gap |
| [S. Advantage Assignment](problems/s_advantage_assignment/README.md) | exchange the cheapest winning match |
| [T. Minimum Refueling](problems/t_minimum_refueling/README.md) | postpone a choice, then take the largest past opportunity |
| [U. Circular Fuel Start](problems/u_circular_fuel_start/README.md) | discard an entire block of impossible candidates |
| [V. Smallest Separated Rearrangement](problems/v_smallest_separated_rearrangement/README.md) | choose lexicographically with an exact completion test |
| [W. Consecutive Grouping](problems/w_consecutive_grouping/README.md) | satisfy an existing obligation before creating a new one |

## Level-Up Set

After R--W, these three original problems combine the section's ideas in less
immediate ways:

| Problem | Main training goal |
|---|---|
| [X. Subarray Minimum Total](problems/x_subarray_minimum_total/README.md) | compress all suffix minima into a monotonic stack of contributions |
| [Y. Maximum Width Ramp](problems/y_maximum_width_ramp/README.md) | discover useful left endpoints, then scan from the opposite direction |
| [Z. Smallest Alternating Partition](problems/z_smallest_alternating_partition/README.md) | minimize groups and handle a lexicographic secondary objective |

## Study Order

1. Read `lesson.qmd`.
2. Attempt the local exercises as a timed set:
   - `a_complete_window`
   - `b_minimum_split_limit`
   - `c_active_colors`
   - `d_first_free_slot` (blind practice: use its README only)
   - `e_smallest_distinct_subsequence`
3. Complete focused exercises F--K in order.
4. Complete reinforcement exercises L--Q. The useful pairs are H then L--M,
   I then N--O, and K then P--Q.
5. Complete the greedy proof laboratory R--W. For each problem, write the
   one-sentence safety argument before opening the editorial.
6. Attempt the level-up set X--Z. For each one, first write the `O(n^2)` or
   backtracking oracle and identify exactly what the optimized state forgets.
7. Run the checker:

```bash
python3 sections/14_core_patterns_mixed_contest/check.py
```

To test the reference solutions:

```bash
CP_TARGET=solution python3 sections/14_core_patterns_mixed_contest/check.py
```

8. Read `editorial.qmd`.
9. Work through `PRACTICE.md`.
