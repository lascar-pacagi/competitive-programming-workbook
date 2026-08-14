# Course Section Style

This file records the approved depth for future sections.

## Lesson Standard

Each lesson should be pedagogical, not just a summary. It should normally
include:

1. Motivation from contest pressure.
2. How to recognize the concept from constraints and statement shape.
3. A vocabulary section with precise but gentle definitions.
4. At least two worked examples or traces.
5. Tables, ASCII diagrams, or generated figures when they clarify the idea.
6. C++ and Python implementation notes.
7. Proof habits relevant to the section.
8. Common wrong approaches and why they fail.
9. A local judge workflow section when new tooling or testing style appears.
10. A checklist before submitting.

The lesson should teach the concept, not merely introduce the exercises.

If a local exercise or reference solution requires a data structure, language
library, mathematical tool, or named algorithm that has not already been taught
in the course, the lesson must include a self-contained primer sufficient to
understand and implement that section. Future-only mentions are allowed, but
they must be clearly framed as future tools and not used in required solutions
without explanation.

## Editorial Standard

Each editorial should be detailed enough to upsolve from. It should normally
include, for every local problem:

1. Restatement in simpler terms.
2. Important constraints and traps.
3. Observations leading to the algorithm.
4. A sample walk-through.
5. Algorithm in pseudocode.
6. Correctness proof with invariants, exchange arguments, induction, or case
   analysis as appropriate.
7. Complexity analysis.
8. C++ implementation notes.
9. Python implementation notes.
10. Full C++ solution.
11. Full Python solution when Python is viable.
12. Common wrong answers.
13. Tests that matter.

Each section editorial should end with a testing or stress-testing discussion
and a short "what to carry forward" summary.

If an editorial solution uses a newly introduced tool, include a reminder of
the tool's operations, invariants, indexing conventions, and complexity before
the full code. Do not require the reader to infer a required data structure from
implementation alone.

## Problem Policy

Local exercises should be original or use short local summaries. External
Codeforces, AtCoder, ICPC, and Kattis statements are linked, not copied.

Every mature section should include a balanced external practice queue:

- Codeforces;
- AtCoder;
- ICPC-style or ICPC archive/Kattis problem;
- optional stretch problem.

## Blind Practice Standard

Every technical section should also contain at least one local **blind
exercise** beyond the guided exercises introduced in its lesson. A blind
exercise may require concepts already taught by that section, but the lesson
must not reveal its reduction, state definition, greedy choice, transition, or
algorithmic outline.

Its problem statement must stand on its own. Its editorial must be fully
problem-specific and include the same upsolve material as other local problems:
observations, a worked trace where useful, algorithm, correctness argument,
complexity, implementation traps, and targeted tests. This creates a real
attempt before the explanation while preserving a strong learning path after a
failed attempt.
