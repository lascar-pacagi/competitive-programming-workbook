# Competitive Programming Course

This repository is a long-form, code-driven competitive programming course in
the style of the neighboring Collatz course. It is designed for a programmer
who already knows C++ and Python and wants a balanced path through
Codeforces, AtCoder, and ICPC-style problem solving.

The approved long-term structure is in
[`CURRICULUM_PLAN.md`](CURRICULUM_PLAN.md).
The approved depth and writing standard for lessons and editorials is in
[`COURSE_STYLE.md`](COURSE_STYLE.md).

Each completed section contains:

- an illustrated Quarto lesson;
- an editorial PDF with detailed solutions and proofs;
- C++ and Python exercise stubs;
- reference solutions kept beside, but separate from, the stubs;
- local online-judge tests;
- a friendly section checker.

The course currently has 61 sections. Section 61 is the final ICPC readiness
module: complete it with a team after the capstone, then repeat its virtual
contest and postmortem protocol.

Problem statements are written locally or summarized briefly. External
Codeforces, AtCoder, and ICPC problems are linked instead of copied.

## Requirements

- Python 3.11 or newer
- `g++` with C++17 support
- Quarto and a LaTeX distribution to build PDFs

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
```

## Study A Section

Read the lesson, solve the problems, then run the checker:

```bash
python3 sections/01_complexity_io_constraints/check.py
```

Run a single problem/language:

```bash
python3 tools/judge.py sections/01_complexity_io_constraints/problems/a_sum_constraints --lang cpp
python3 tools/judge.py sections/01_complexity_io_constraints/problems/a_sum_constraints --lang py
```

Validate supplied reference solutions:

```bash
CP_TARGET=solution python3 sections/01_complexity_io_constraints/check.py
```

Run all available section checkers:

```bash
python3 tools/check_all.py
```

Audit the complete course structure and flag editorials that need a deeper
pedagogical rewrite:

```bash
python3 tools/audit_course.py
```

## Build PDFs

```bash
make pdf
```
