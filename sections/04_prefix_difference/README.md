# Section 4: Prefix Sums And Difference Arrays

## Learning Goals

After this section, you should be able to:

- build prefix sums for constant-time range queries;
- handle inclusive and half-open interval conventions;
- use a difference array for many range updates;
- reconstruct final values from differences;
- count subarrays with a target sum using prefix sums and frequencies.

## Study Order

1. Read `lesson.pdf`, or `lesson.qmd` if the PDF has not been built.
2. Solve the problems in order:
   - `a_range_sum_queries`
   - `b_range_add_final_array`
   - `c_subarray_sum_count`
   - `d_signal_peak` (blind practice: attempt before opening the editorial)
3. Run this section's checker after each problem.
4. Read `editorial.pdf` only after a serious attempt.

## Commands

From the repository root:

```bash
python3 sections/04_prefix_difference/check.py
```

Run one problem:

```bash
python3 tools/judge.py sections/04_prefix_difference/problems/a_range_sum_queries --lang cpp
python3 tools/judge.py sections/04_prefix_difference/problems/a_range_sum_queries --lang py
```

Validate reference solutions:

```bash
CP_TARGET=solution python3 sections/04_prefix_difference/check.py
```

## External Practice Queue

See [`PRACTICE.md`](PRACTICE.md). Their statements are external; this
repository does not copy them.
