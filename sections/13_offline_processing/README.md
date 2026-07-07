# Section 13: Offline Processing

Offline processing means reading all queries first, reordering the work to make
it efficient, and then restoring answers to the original query order.

## Study Order

1. Read `lesson.qmd`.
2. Solve the local exercises:
   - `a_coordinate_compression`
   - `b_range_count_at_most`
   - `c_distinct_range_queries`
3. Run the checker:

```bash
python3 sections/13_offline_processing/check.py
```

To test the reference solutions:

```bash
CP_TARGET=solution python3 sections/13_offline_processing/check.py
```

4. Read `editorial.qmd`.
5. Work through `PRACTICE.md`.

