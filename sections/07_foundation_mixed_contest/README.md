# Section 7: Foundation Mixed Contest

## Learning Goals

After this section, you should be able to:

- choose among simulation, counting, prefix sums, sorting, and sliding windows;
- read a statement and identify the controlling constraint;
- combine two foundation techniques in one solution;
- write deterministic tie-breaking logic;
- use brute-force oracles to test small cases.

## Category Coverage

| Foundation category | Contest problem |
|---|---|
| Simulation and brute force | [E. Circular Patrol](problems/e_circular_patrol/README.md) |
| Counting, frequencies, and maps | A. Inventory Cleanup |
| Prefix sums and difference arrays | B. Peak Load; D. Balanced Break |
| Sorting as a tool | A. Inventory Cleanup |
| Two pointers and sliding windows | C. Best Study Streak |

Circular Patrol is the local blind-practice representative for explicit state
simulation. Problem D remains useful exhaustive candidate checking with a
maintained prefix state.

## Study Order

1. Treat the section as a short virtual contest.
2. Attempt the problems before reading the lesson or editorial:
   - `a_inventory_cleanup`
   - `b_peak_load`
   - `c_best_study_streak`
   - `d_balanced_break` (blind practice: use its problem README only)
   - `e_circular_patrol`
3. Run this section's checker after each accepted-looking solution.
4. Read `lesson.pdf` for contest workflow and technique selection.
5. Read `editorial.pdf` to upsolve missed problems.

## Commands

From the repository root:

```bash
python3 sections/07_foundation_mixed_contest/check.py
```

Run one problem:

```bash
python3 tools/judge.py sections/07_foundation_mixed_contest/problems/a_inventory_cleanup --lang cpp
python3 tools/judge.py sections/07_foundation_mixed_contest/problems/a_inventory_cleanup --lang py
```

Validate reference solutions:

```bash
CP_TARGET=solution python3 sections/07_foundation_mixed_contest/check.py
```

## External Practice Queue

See [`PRACTICE.md`](PRACTICE.md). Their statements are external; this
repository does not copy them.
