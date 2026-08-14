# Section 11: Intervals And Sweep Line

This section teaches event-based thinking for interval problems: when to sort
endpoints, how to order ties, how to accumulate length between coordinates, and
how to answer point queries while preserving original order.

## Study Order

1. Read `lesson.qmd`.
2. Solve the local exercises:
   - `a_peak_active`
   - `b_covered_length`
   - `c_point_coverage`
   - `d_first_busiest` (blind practice: use its README only)
3. Run the checker:

```bash
python3 sections/11_intervals_sweep_line/check.py
```

To test the reference solutions:

```bash
CP_TARGET=solution python3 sections/11_intervals_sweep_line/check.py
```

4. Read `editorial.qmd`.
5. Work through `PRACTICE.md`.
