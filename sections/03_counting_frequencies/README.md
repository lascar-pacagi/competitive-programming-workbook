# Section 3: Counting, Frequencies, And Maps

## Learning Goals

After this section, you should be able to:

- choose between a frequency array and a map/dictionary;
- answer count queries after preprocessing;
- handle tie-breaking rules explicitly;
- count pairs with a given sum using frequencies;
- avoid double-counting when order does not matter.

## Study Order

1. Read `lesson.pdf`, or `lesson.qmd` if the PDF has not been built.
2. Solve the problems in order:
   - `a_value_counts`
   - `b_frequency_winner`
   - `c_pair_sum_count`
   - `d_equal_index_pairs` (blind practice: attempt before opening the editorial)
3. Run this section's checker after each problem.
4. Read `editorial.pdf` only after a serious attempt.

## Commands

From the repository root:

```bash
python3 sections/03_counting_frequencies/check.py
```

Run one problem:

```bash
python3 tools/judge.py sections/03_counting_frequencies/problems/a_value_counts --lang cpp
python3 tools/judge.py sections/03_counting_frequencies/problems/a_value_counts --lang py
```

Validate reference solutions:

```bash
CP_TARGET=solution python3 sections/03_counting_frequencies/check.py
```

## External Practice Queue

See [`PRACTICE.md`](PRACTICE.md). Their statements are external; this
repository does not copy them.
