# Section 5: Sorting As A Tool

## Learning Goals

After this section, you should be able to:

- recognize when sorting exposes adjacency or order;
- design and implement custom sort keys;
- handle deterministic tie-breaking;
- merge overlapping intervals after sorting by start point;
- prove why checking adjacent sorted elements can be sufficient.

## Study Order

1. Read `lesson.pdf`, or `lesson.qmd` if the PDF has not been built.
2. Solve the problems in order:
   - `a_min_adjacent_gap`
   - `b_rank_table`
   - `c_merge_intervals`
   - `d_compact_team` (blind practice: use its problem README only)
3. Run this section's checker after each problem.
4. Read `editorial.pdf` only after a serious attempt.

## Commands

From the repository root:

```bash
python3 sections/05_sorting_as_tool/check.py
```

Run one problem:

```bash
python3 tools/judge.py sections/05_sorting_as_tool/problems/a_min_adjacent_gap --lang cpp
python3 tools/judge.py sections/05_sorting_as_tool/problems/a_min_adjacent_gap --lang py
```

Validate reference solutions:

```bash
CP_TARGET=solution python3 sections/05_sorting_as_tool/check.py
```

## External Practice Queue

See [`PRACTICE.md`](PRACTICE.md). Their statements are external; this
repository does not copy them.
