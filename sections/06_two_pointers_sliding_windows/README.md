# Section 6: Two Pointers And Sliding Windows

## Learning Goals

After this section, you should be able to:

- use two pointers on a sorted array;
- maintain a moving window over nonnegative values;
- explain why each pointer moves only forward;
- count many valid subarrays in one step;
- recognize when negative values break a sliding-window argument.

## Study Order

1. Read `lesson.pdf`, or `lesson.qmd` if the PDF has not been built.
2. Solve the problems in order:
   - `a_sorted_two_sum`
   - `b_longest_bounded_window`
   - `c_count_subarrays_at_most`
   - `d_cover_all_labels` (blind practice)
3. Run this section's checker after each problem.
4. Read `editorial.pdf` only after a serious attempt.

## Commands

From the repository root:

```bash
python3 sections/06_two_pointers_sliding_windows/check.py
```

Run one problem:

```bash
python3 tools/judge.py sections/06_two_pointers_sliding_windows/problems/a_sorted_two_sum --lang cpp
python3 tools/judge.py sections/06_two_pointers_sliding_windows/problems/a_sorted_two_sum --lang py
```

Validate reference solutions:

```bash
CP_TARGET=solution python3 sections/06_two_pointers_sliding_windows/check.py
```

## External Practice Queue

See [`PRACTICE.md`](PRACTICE.md). Their statements are external; this
repository does not copy them.
