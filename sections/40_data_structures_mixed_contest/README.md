# Section 40: Data Structures Mixed Contest

This mixed contest reviews the structures from Sections 36 through 39. The
first six problems form the core. Problems G--L are a progressively harder
second half, so the complete contest has twelve local exercises.

## Category Coverage

| Data-structure category | Problem |
|---|---|
| Fenwick tree | B. List Removals; C. Range Add, Range GCD; D. Salary Queries |
| Segment tree | A. Hotel Queries; C. Range Add, Range GCD; I. Dynamic Maximum Subarray; K. Budget Prefix Search; L. Range Add Threshold Search |
| Static queries and binary lifting | [E. Functional Walk Minimum](problems/e_functional_walk_minimum/README.md) |
| Heaps and priority queues | [F. Mutable Priority Queue](problems/f_mutable_priority_queue/README.md) |
| Progressive synthesis | G. Streaming Room Count through L. Range Add Threshold Search |

Problem C combines two representations of the same changing array. Problem F
introduces stale heap entries and lazy deletion, rather than repeating the
running-median exercise from Section 39.

## Study Order

1. Attempt the core:
   - `a_hotel_queries`
   - `b_list_removals`
   - `c_range_add_range_gcd`
   - `d_salary_queries` (blind practice)
2. Complete the additional coverage problems:
   - `e_functional_walk_minimum`
   - `f_mutable_priority_queue`
3. Continue through G--L in order. Their intended difficulty rises with the
   letter.
4. Run:

```bash
python3 sections/40_data_structures_mixed_contest/check.py
```

To validate the reference solutions:

```bash
CP_TARGET=solution python3 sections/40_data_structures_mixed_contest/check.py
```

5. Read the editorial and work through `PRACTICE.md`.
