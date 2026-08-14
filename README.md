# Competitive Programming Workbook

This is a long-form, practice-first competitive programming course for people
who already know basic C++ or Python and want a structured path through
Codeforces, AtCoder, and ICPC-style problem solving.

Every section combines explanation, local exercises, automated checking,
randomized tests, and detailed editorials. Start at the beginning or enter at
the phase matching your experience.

## Course Roadmap

| Phase | Sections | Main topics |
|---|---:|---|
| Foundations | 1--14 | Complexity, arrays, sorting, greedy, stacks |
| Graphs I | 15--21 | BFS, DFS, DSU, shortest paths |
| Dynamic programming | 22--28 | Classical, grid, interval, tree, and bitmask DP |
| Mathematics | 29--35 | Modular arithmetic, CRT, combinatorics, probability |
| Data structures | 36--42 | Fenwick and segment trees, lifting, advanced queries |
| Advanced algorithms | 43--50 | Strings, flows, tree DP, optimization |
| Contest preparation | 51--63 | Hard techniques, workflow, and contest ladders |

The approved long-term structure is in
[`CURRICULUM_PLAN.md`](CURRICULUM_PLAN.md).
The approved depth and writing standard for lessons and editorials is in
[`COURSE_STYLE.md`](COURSE_STYLE.md).

The root-level discovery manual
[`HOW_TO_FIND_IT.qmd`](HOW_TO_FIND_IT.qmd) uses new, course-independent
problems to reconstruct how a solution is found: slow models, failed ideas,
counterexamples, decisive observations, proofs, and validation. A rendered
copy is available as [`HOW_TO_FIND_IT.pdf`](HOW_TO_FIND_IT.pdf).

Each completed section contains:

- an illustrated Quarto lesson;
- an editorial PDF with detailed solutions and proofs;
- C++ and Python exercise stubs;
- reference solutions kept beside, but separate from, the stubs;
- local online-judge tests;
- a friendly section checker.

The course currently has 63 sections. Section 61 is the ICPC readiness module,
Section 62 is a 50-problem Codeforces ladder, and Section 63 is a 50-problem
AtCoder ladder weighted toward intermediate, advanced, orange, and red tasks.

Problem statements are written locally or summarized briefly. External
Codeforces, AtCoder, and ICPC problems are linked instead of copied.

## Requirements

- Python 3.11 or newer
- `g++` with C++23 support
- `gdb` (optional, for interactive C++ debugging)
- Quarto and a LaTeX distribution to build PDFs

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
```

## Study A Section

### Keep personal work outside the public course

Maintainers can keep attempts in the ignored `.submissions/` overlay. Its
directory structure mirrors the course, and the checker selects an overlay
`solve.cpp` or `solve.py` automatically when it exists.

To preserve current attempts and replace the public copies with clean TODO
stubs, run this once:

```bash
python3 tools/manage_submissions.py migrate
```

When new course problems are added, seed their missing personal files without
overwriting existing attempts:

```bash
python3 tools/manage_submissions.py seed
```

The overlay may instead be an entirely separate private repository:

```bash
CP_SUBMISSIONS_DIR=../CompetitiveProgrammingProgress \
python3 sections/35_math_mixed_contest/check.py --problem g
```

Never add `.submissions/` to the public repository. Before committing course
changes, verify the tracked stubs with:

```bash
git config core.hooksPath .githooks  # once per clone
make public-check
```

The committed pre-commit hook repeats the public stub and structural checks,
so normal course improvements can be staged and pushed without exposing the
overlay.

Read the lesson, solve the problems, then run the checker:

```bash
python3 sections/01_complexity_io_constraints/check.py
```

By default, a section checker tests C++ and Python and stops at the first
failure. Use `--keep-going` (or `-k`) to test every remaining submission:

```bash
python3 sections/01_complexity_io_constraints/check.py --keep-going
```

To work in only one language, combine it with `--lang cpp` or `--lang py`:

```bash
python3 sections/01_complexity_io_constraints/check.py --keep-going --lang cpp
```

To check only one problem, pass its letter or full directory name:

```bash
python3 sections/01_complexity_io_constraints/check.py --problem b
python3 sections/01_complexity_io_constraints/check.py -p b_until_threshold
```

Repeat the option, or separate selectors with commas, to check several:

```bash
python3 sections/01_complexity_io_constraints/check.py -p a,c --lang py
```

The keep-going summary first reports whether each problem was accepted in at
least one checked language, including which language or languages passed. It
then lists every failed problem/language and returns a nonzero exit status if
any checked submission failed.

Run a single problem/language:

```bash
python3 tools/judge.py sections/01_complexity_io_constraints/problems/a_sum_constraints --lang cpp
python3 tools/judge.py sections/01_complexity_io_constraints/problems/a_sum_constraints --lang py
```

## Debug C++ with GDB

Select one problem and one input case. To run until the program exits or
crashes:

```bash
python3 sections/27_bitmask_dp/check.py -p c --gdb sample1
```

At a segmentation fault, useful GDB commands are `bt` (backtrace), `frame N`,
`list`, and `print variable`.

To stop at `main` and step through the program:

```bash
python3 sections/27_bitmask_dp/check.py -p c --gdb sample1 --step
```

Use `next` to execute one source line without entering functions, `step` to
enter a function, `continue` to resume, and `display expression` to print an
expression after every step. The debug build uses symbols, low optimization,
libstdc++ debug checks, and assertions.

The case may be a fixed test name, a random case name printed by the checker,
or an explicit input-file path:

```bash
python3 sections/27_bitmask_dp/check.py -p c --gdb random/case_001
python3 sections/27_bitmask_dp/check.py -p c --gdb /tmp/my_case.in --step
```

The direct equivalent is:

```bash
python3 tools/judge.py sections/27_bitmask_dp/problems/c_inspection_route \
  --lang cpp --gdb --case sample1 --step
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

## Contributing and licensing

See [`CONTRIBUTING.md`](CONTRIBUTING.md) before proposing a statement, test,
or editorial change. Code is available under the MIT License; original course
content is available under CC BY 4.0 as described in
[`LICENSE-CONTENT.md`](LICENSE-CONTENT.md).
