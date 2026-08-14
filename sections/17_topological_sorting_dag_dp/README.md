# Section 17: Topological Sorting And DAG DP

This section teaches how to work with directed acyclic graphs: ordering tasks,
detecting dependency cycles, and doing dynamic programming in topological order.

## Study Order

1. Read `lesson.qmd`.
2. Attempt the local exercises:
   - `a_lexicographic_course_order`
   - `b_longest_dag_path`
   - `c_project_schedule`
   - `d_unique_build_order` (blind practice: use its README only)
3. Run the checker:

```bash
python3 sections/17_topological_sorting_dag_dp/check.py
```

To test the reference solutions:

```bash
CP_TARGET=solution python3 sections/17_topological_sorting_dag_dp/check.py
```

4. Read `editorial.qmd`.
5. Work through `PRACTICE.md`.
