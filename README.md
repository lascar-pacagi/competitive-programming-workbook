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
| Master+ mathematics I | 64--66 | Divisor transforms, NTT, and linear recurrences |
| Master+ structures I | 67--69 | Persistence, rollback, and tree decompositions |
| Master+ flow/convex I | 70--72 | Bounded flows, slope trick, and Lagrangian optimization |
| Master+ geometry I | 73--75 | Convex boundaries, Minkowski sums, and geometric sweeps |
| Master+ string structures I | 76--78 | Suffix arrays, automata, LCP, and palindromic trees |
| Master+ graph decomposition | 79--81 | SCCs, Euler trails, low links, block-cut trees, and dominators |
| Master+ dynamic structures | 82--84 | Wavelet matrices, beats, implicit treaps, and dynamic forests |
| Master+ matching/matroids | 85--87 | Hungarian, blossom, cut trees, arborescences, and matroid intersection |
| Master+ polynomial algebra | 88--90 | Formal series, product trees, interpolation, and subset transforms |
| Master+ computational number theory | 91--93 | 64-bit factorization, discrete logarithms, and modular roots |
| Master+ continuous geometry | 94--96 | Half-planes, circle geometry, enclosing disks, and Delaunay structure |
| Master+ frontier DP | 97--99 | Digit automata, profiles, plug DP, Steiner subsets, and treewidth DP |

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

The course currently has 99 sections. Section 61 is the ICPC readiness module,
Sections 62--63 are the Codeforces and AtCoder ladders, and Sections 64--66
begin the master+ extension with multiplicative transforms and polynomial
algorithms. Sections 67--69 continue with persistence, rollback, heavy-light,
centroid, virtual-tree, and small-to-large techniques. Sections 70--72 add
bounded circulation, potential-based min-cost flow, slope trick, exact-count
Lagrangian relaxation, and discrete convex allocation.
Sections 73--75 continue with convex hull compression, rotating calipers,
Minkowski sums, geometric sweeps, union area, and closest-pair geometry.
Sections 76--78 add suffix-array interval geometry, LCP aggregation,
suffix-automaton path and occurrence DP, palindromic trees, and a six-problem
mixed suffix-structures contest.
Sections 79--81 repair the advanced graph-decomposition gap with SCC
condensation, constructive 2-SAT reasoning, directed Euler trails, bridges,
articulation vertices, block-cut trees, and dominators.
Sections 82--84 add value-domain range navigation, segment-tree beats,
editable implicit-treap sequences, link-cut-tree forest paths, and Kruskal
reconstruction trees.
Sections 85--87 add weighted assignment, general-graph matching, Gomory--Hu
cut trees, directed arborescences, and graphic/partition matroid intersection.
Sections 88--90 develop formal power series through Newton iteration, fast
multipoint evaluation and interpolation, Walsh and OR transforms, and ranked
subset convolution.
Sections 91--93 add deterministic 64-bit Miller--Rabin, Pollard--rho,
large-integer multiplicative functions, primitive roots, generalized discrete
logarithms, and Tonelli--Shanks modular square roots.
Sections 94--96 add half-plane intersection, robust circle classification,
randomized minimum enclosing circles, incremental Delaunay triangulation,
empty-circle queries, and Euclidean MST sparsification.
Sections 97--99 finish the extension with digit DP products, broken profiles,
transfer matrices, canonical connectivity labels, Steiner subset DP, and
dynamic programming over nice tree decompositions.

Problem statements are written locally or summarized briefly. External
Codeforces, AtCoder, and ICPC problems are linked instead of copied.
Every required problem in the master+ extension is instead a complete original
local package; external sources are used only for topic and difficulty
calibration. See [`MASTER_PLUS_SOURCES.md`](MASTER_PLUS_SOURCES.md).

Maximum-constraint certification for Sections 64--99 is tracked separately in
[`sections/MASTER_PLUS_COMPLEXITY_AUDIT.md`](sections/MASTER_PLUS_COMPLEXITY_AUDIT.md).
It records adversarial invariants, measured C++/Python time and memory, and any
constraint or support-limit failures; small random-oracle acceptance alone is
not treated as complexity evidence.

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
