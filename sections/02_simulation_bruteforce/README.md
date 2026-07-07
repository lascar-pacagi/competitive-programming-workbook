# Section 2: Simulation And Brute Force

## Learning Goals

After this section, you should be able to:

- simulate a process exactly as described;
- identify when exhaustive search is small enough;
- choose loop bounds from constraints;
- avoid off-by-one and state-update mistakes;
- use brute force as both a solution and a testing oracle.

## Study Order

1. Read `lesson.pdf`, or `lesson.qmd` if the PDF has not been built.
2. Solve the problems in order:
   - `a_robot_walk`
   - `b_ticket_split`
   - `c_best_subset`
3. Run this section's checker after each problem.
4. Read `editorial.pdf` only after a serious attempt.

## Commands

From the repository root:

```bash
python3 sections/02_simulation_bruteforce/check.py
```

Run one problem:

```bash
python3 tools/judge.py sections/02_simulation_bruteforce/problems/a_robot_walk --lang cpp
python3 tools/judge.py sections/02_simulation_bruteforce/problems/a_robot_walk --lang py
```

Validate reference solutions:

```bash
CP_TARGET=solution python3 sections/02_simulation_bruteforce/check.py
```

## External Practice Queue

See [`PRACTICE.md`](PRACTICE.md). Their statements are external; this
repository does not copy them.

