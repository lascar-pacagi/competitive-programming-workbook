# Section 28: DP I Mixed Contest

This section is a mixed contest for the first dynamic programming block. It
does not introduce a separate named algorithm; it asks you to recognize which
state shape fits the statement.

## Category Coverage

| DP category | Problem |
|---|---|
| One-dimensional DP | A. Training Schedule; [H. Sliding Jump Cost](problems/h_sliding_jump_cost/README.md) |
| Knapsack and subset DP | B. Two Carts; [I. Grouped Cargo](problems/i_grouped_cargo/README.md) |
| Grid DP | [E. One Diagonal Path](problems/e_one_diagonal_path/README.md); [J. Minimum Starting Energy](problems/j_minimum_starting_energy/README.md) |
| Interval DP | [F. Matrix Chain](problems/f_matrix_chain/README.md); [K. Last Crystal Removed](problems/k_last_crystal_removed/README.md) |
| Tree DP | C. Prerequisite Tree; [L. Weighted Tree Guards](problems/l_weighted_tree_guards/README.md) |
| Bitmask DP | [G. Hamiltonian Route](problems/g_hamiltonian_route/README.md) |

Circular Exhibition remains an additional one-dimensional boundary-case
problem. H--L form a harder reinforcement set: each changes either the
evaluation order, transition cost, or boundary information compared with the
first representative of its category.

## Study Order

1. Read `lesson.qmd`.
2. Attempt the local exercises:
   - `a_training_schedule`
   - `b_two_carts`
   - `c_prerequisite_tree`
   - `d_circular_exhibition` (blind practice: use its README only)
   - `e_one_diagonal_path`
   - `f_matrix_chain`
   - `g_hamiltonian_route`
   - `h_sliding_jump_cost`
   - `i_grouped_cargo`
   - `j_minimum_starting_energy`
   - `k_last_crystal_removed`
   - `l_weighted_tree_guards`
3. Run the checker:

```bash
python3 sections/28_dp_i_mixed_contest/check.py
```

To test the reference solutions:

```bash
CP_TARGET=solution python3 sections/28_dp_i_mixed_contest/check.py
```

4. Read `editorial.qmd`.
5. Work through `PRACTICE.md`.
