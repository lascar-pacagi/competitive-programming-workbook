# Section 1: Complexity, I/O, And Constraints

## Learning Goals

After this section, you should be able to:

- estimate whether an algorithm fits from input constraints;
- read many test cases safely in C++ and Python;
- choose integer types deliberately;
- run the local judge for both languages;
- separate sample confidence from tested correctness.

## Study Order

1. Read `lesson.pdf`, or `lesson.qmd` if the PDF has not been built.
2. Solve the problems in order:
   - `a_sum_constraints`
   - `b_until_threshold`
   - `c_token_budget`
3. Run this section's checker after each problem.
4. Read `editorial.pdf` only after a serious attempt.

## Commands

From the repository root:

```bash
python3 sections/01_complexity_io_constraints/check.py
```

Run one problem:

```bash
python3 tools/judge.py sections/01_complexity_io_constraints/problems/a_sum_constraints --lang cpp
python3 tools/judge.py sections/01_complexity_io_constraints/problems/a_sum_constraints --lang py
```

Validate reference solutions:

```bash
CP_TARGET=solution python3 sections/01_complexity_io_constraints/check.py
```

## External Practice Queue

See [`PRACTICE.md`](PRACTICE.md). Their statements are external; this
repository does not copy them.
