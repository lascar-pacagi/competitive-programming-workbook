# Section 8: Binary Search On The Answer

## Learning Goals

After this section, you should be able to:

- recognize monotone yes/no predicates;
- write integer binary search without off-by-one errors;
- search for a minimum feasible or maximum feasible answer;
- design feasibility checks;
- choose safe lower and upper bounds.

## Study Order

1. Read `lesson.pdf`, or `lesson.qmd` if the PDF has not been built.
2. Solve the problems in order:
   - `a_square_threshold`
   - `b_max_min_distance`
   - `c_minimum_capacity`
3. Run this section's checker after each problem.
4. Read `editorial.pdf` only after a serious attempt.

## Commands

From the repository root:

```bash
python3 sections/08_binary_search_answer/check.py
```

Run one problem:

```bash
python3 tools/judge.py sections/08_binary_search_answer/problems/a_square_threshold --lang cpp
python3 tools/judge.py sections/08_binary_search_answer/problems/a_square_threshold --lang py
```

Validate reference solutions:

```bash
CP_TARGET=solution python3 sections/08_binary_search_answer/check.py
```

## External Practice Queue

See [`PRACTICE.md`](PRACTICE.md). Their statements are external; this
repository does not copy them.

