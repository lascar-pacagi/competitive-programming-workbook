# Competitive Programming Workbook

This is a long-form, practice-first competitive programming course for people
who already know basic C++ or Python and want a structured path through
Codeforces, AtCoder, and ICPC-style problem solving.

Every section combines explanation, local exercises, automated checking,
randomized tests, and detailed editorials. Start at the beginning or enter at
the phase matching your experience.

## Start the course in two minutes

Clone the repository:

```bash
git clone https://github.com/lascar-pacagi/competitive-programming-workbook.git
```

Open the cloned `competitive-programming-workbook` folder in your editor. No
installation step is needed to begin: Python 3 and either `g++` or Python are
enough to run the first exercise.

Open the first lesson:

`sections/01_complexity_io_constraints/lesson.pdf`

After the lesson, open your first problem:

`sections/01_complexity_io_constraints/problems/a_sum_constraints/README.md`

Create your private starter files from the repository root:

```bash
python3 tools/manage_submissions.py seed
```

Choose one language and write your answer in its private file:

- `.submissions/sections/01_complexity_io_constraints/problems/a_sum_constraints/solve.cpp`
- `.submissions/sections/01_complexity_io_constraints/problems/a_sum_constraints/solve.py`

The seed command creates only missing files and preserves existing attempts.
The checker automatically uses these private files; the public `solve.*`
files remain untouched TODO stubs. When you are ready, test the first problem:

```bash
python3 sections/01_complexity_io_constraints/check.py -p a --lang cpp
```

Replace `cpp` with `py` if you chose Python. Once it passes, continue with
problem B in the same section. Read the editorial only after a serious try.

## When you want more

Everything below is optional for your first session: the full roadmap, extra
checker options, private-submission workflow, debugging, and course-building
tools.

## Course Roadmap

| Phase | Sections | Main topics |
| --- | ---: | --- |
| [Contest foundations](CURRICULUM_PLAN.md#phase-0-contest-foundations) | 1--7 | Complexity, simulation, counting, prefix sums, sorting, two pointers |
| [Core patterns](CURRICULUM_PLAN.md#phase-1-core-patterns) | 8--14 | Binary search, greedy proofs, sweeps, stacks, offline processing |
| [Graphs I](CURRICULUM_PLAN.md#phase-2-graphs-i) | 15--21 | BFS, DFS, DAG DP, DSU/MST, Dijkstra, 0-1 BFS |
| [Dynamic programming I](CURRICULUM_PLAN.md#phase-3-dynamic-programming-i) | 22--28 | Classical, knapsack, grid, interval, tree, and bitmask DP |
| [Number theory and combinatorics](CURRICULUM_PLAN.md#phase-4-number-theory-and-combinatorics) | 29--35 | Modular arithmetic, GCD/LCM, primes, combinatorics, probability |
| [Data structures](CURRICULUM_PLAN.md#phase-5-advanced-data-structures) | 36--42 | Fenwick/segment trees, static queries, heaps, Euler tours, LCA |
| [Advanced algorithms](CURRICULUM_PLAN.md#phase-6-advanced-algorithms) | 43--50 | KMP, tries, rolling hash, suffix automata, flows, tree DP, optimization |
| [Red-coder training](CURRICULUM_PLAN.md#phase-7-red-coder-training) | 51--63 | Invariants, games, geometry, modeling, contest workflow, external ladders |
| [Master+ mathematics I](CURRICULUM_PLAN.md#phase-8-master-mathematics-i) | 64--66 | Divisor transforms, NTT, linear recurrences |
| [Master+ structures and trees I](CURRICULUM_PLAN.md#phase-9-master-structures-and-trees-i) | 67--69 | Persistence, rollback, tree decompositions |
| [Master+ flow and convex optimization I](CURRICULUM_PLAN.md#phase-10-master-flow-and-convex-optimization-i) | 70--72 | Bounded/min-cost flows, slope trick, Lagrangian optimization |
| [Master+ geometry I](CURRICULUM_PLAN.md#phase-11-master-geometry-i) | 73--75 | Convex boundaries, Minkowski sums, geometric sweeps |
| [Master+ string structures I](CURRICULUM_PLAN.md#phase-12-master-string-structures-i) | 76--78 | Suffix arrays/LCP, automata, palindromic trees |
| [Master+ graph decomposition](CURRICULUM_PLAN.md#phase-13-master-graph-decomposition) | 79--81 | SCCs, Euler trails, low links, block-cut trees, dominators |
| [Master+ dynamic structures](CURRICULUM_PLAN.md#phase-14-master-dynamic-data-structures) | 82--84 | Wavelet matrices, beats, implicit treaps, dynamic forests |
| [Master+ matching and matroids](CURRICULUM_PLAN.md#phase-15-master-matching-cuts-and-matroids) | 85--87 | Hungarian, blossom, cut trees, arborescences, matroid intersection |
| [Master+ polynomial algebra](CURRICULUM_PLAN.md#phase-16-master-polynomial-algebra) | 88--90 | Formal series, product trees, interpolation, subset transforms |
| [Master+ computational number theory](CURRICULUM_PLAN.md#phase-17-master-computational-number-theory) | 91--93 | 64-bit factorization, discrete logarithms, modular roots |
| [Master+ geometry II](CURRICULUM_PLAN.md#phase-18-master-geometry-ii) | 94--96 | Half-planes, circles, enclosing disks, Delaunay structure |
| [Master+ frontier DP](CURRICULUM_PLAN.md#phase-19-master-frontier-dynamic-programming) | 97--99 | Digit/profile DP, plug DP, Steiner subsets, treewidth DP |
| [Grandmaster finale](CURRICULUM_PLAN.md#phase-20-grandmaster-finale) | 100 | Sixty-five Master-to-Grandmaster synthesis problems |

The approved long-term structure is in
[`CURRICULUM_PLAN.md`](CURRICULUM_PLAN.md).
The approved depth and writing standard for lessons and editorials is in
[`COURSE_STYLE.md`](COURSE_STYLE.md).

The root-level discovery manual
[`HOW_TO_FIND_IT.qmd`](HOW_TO_FIND_IT.qmd) uses new, course-independent
problems to reconstruct how a solution is found: slow models, failed ideas,
counterexamples, decisive observations, proofs, and validation. It covers the
technical topics of Sections 1--57, with mixed checkpoints omitted; the
curriculum continues through Section 100. Read the illustrated
[HTML manual](HOW_TO_FIND_IT.html) or the [PDF](HOW_TO_FIND_IT.pdf).

To rebuild only this manual, run `make discovery-pdf`. It requires Quarto,
Chromium, and the Python `websocket-client` package. The build renders the
HTML first, then prints it locally to preserve the SVG diagrams and formulas,
with a clickable contents list and PDF bookmarks. `make pdf` uses the same
route for the manual before rendering the section PDFs.

Study the [lazy-propagation appendix](appendices/lazy_propagation/README.md)
immediately after Section 37, before continuing with the later query sections.

Each section contains:

- an illustrated Quarto lesson;
- an editorial PDF with detailed solutions and proofs;
- C++ and Python exercise stubs;
- reference solutions kept beside, but separate from, the stubs;
- local online-judge tests;
- a friendly section checker.

The repository currently contains **100 sections and 689 local problem
packages**, including original offline companions for external contest
ladders. Every section has lesson/editorial sources and rendered PDFs.
Sections 61--63 contain 20 ICPC, 50 Codeforces, and 50 AtCoder ladder rungs,
respectively, alongside their local companions and any additional local tasks.
The official linked tasks remain separate external submissions.

Recent modeling and string practice includes:

- [Section 44](sections/44_string_algorithms_ii/README.md): tries, double
  rolling hashes, suffix automata, and an offline
  [SAM construction visualizer](sections/44_string_algorithms_ii/sam_playground/index.html).
- [Section 45](sections/45_flows_and_matchings/README.md): 14 local problems,
  including ten modeling exercises E-N with indicative difficulty targets from
  1400 to 2500, plus an offline
  [flow/matching visualizer](sections/45_flows_and_matchings/flow_playground/index.html).
- [Section 50](sections/50_advanced_algorithms_mixed_contest/README.md): 19 local
  problems, with two main representatives for each technical section 43--49.

Sections 64--66 begin the master+ extension with multiplicative transforms and
polynomial algorithms. Sections 67--69 continue with persistence, rollback,
heavy-light, centroid, virtual-tree, and small-to-large techniques. Sections 70--72 add
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
dynamic programming over nice tree decompositions. Section 100 is the
Grandmaster Finale: sixty-five original problems, including a final synthesis
gauntlet that combines multiple technique families.

Problem statements are written locally or summarized briefly. External
Codeforces, AtCoder, and ICPC problems are linked instead of copied.
Every required problem in the master+ extension is instead a complete original
local package; external sources are used only for topic and difficulty
calibration. See [`MASTER_PLUS_SOURCES.md`](MASTER_PLUS_SOURCES.md).

Maximum-constraint certification for Sections 64--99 is tracked separately in
[`sections/MASTER_PLUS_COMPLEXITY_AUDIT.md`](sections/MASTER_PLUS_COMPLEXITY_AUDIT.md).
It records adversarial invariants, measured C++/Python time and memory, and any
constraint or support-limit failures; small random-oracle acceptance alone is
not treated as complexity evidence. Section 100 has its own
[`finale complexity audit`](sections/100_grandmaster_finale/COMPLEXITY_AUDIT.md),
which records the measured problem groups, language-specific limits, fixes,
and performance-watch items. Consult the evidence recorded in these audits
when assessing maximum-limit support.

## Requirements and optional setup

- Python 3.11 or newer
- `g++` with C++23 support
- `gdb` (optional, for interactive C++ debugging)
- Quarto and a LaTeX distribution with XeLaTeX to rebuild section PDFs
- Chromium and Python `websocket-client`, in addition to Quarto, to rebuild
  the HTML/SVG discovery manual as a PDF

You do not need a virtual environment or extra packages to solve and test the
first exercises. Contributors who want the development tools can install them
with:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
```

## Checking more exercises

### Keep personal work outside the public course

Keep attempts in the ignored `.submissions/` overlay. Its
directory structure mirrors the course, and the checker selects an overlay
`solve.cpp` or `solve.py` automatically when it exists.

Run the seed command on a fresh checkout and again after new problems are
added. It copies only missing files and never replaces an existing attempt:

```bash
python3 tools/manage_submissions.py seed
```

`migrate` is a maintainer-only operation: it copies public `solve.*` files to
an overlay and resets the public copies to TODO stubs. It now refuses to
overwrite an existing overlay unless `--overwrite` is supplied. Make a backup
first, and prefer a fresh destination:

```bash
python3 tools/manage_submissions.py migrate --destination .submissions-new
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

Most section checkers test C++ and Python and stop at the first failure. Use
`--keep-going` (or `-k`) to test every remaining submission:

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

Sections 61--63 have an additional inventory-validation mode: without
`CP_TARGET=solution`, their checker validates the numbered companion packages.
Use the direct `tools/judge.py` command above to test your own companion
submission. Set `CP_TARGET=solution` on the section checker to run all of its
numbered companion references.

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

Build all section and appendix PDFs, plus the illustrated discovery manual:

```bash
make pdf
```

Build only the discovery manual with `make discovery-pdf`. To rebuild one
section, render its lesson and editorial directly:

```bash
quarto render sections/45_flows_and_matchings/lesson.qmd --to pdf
quarto render sections/45_flows_and_matchings/editorial.qmd --to pdf
```

## Contributing and licensing

See [`CONTRIBUTING.md`](CONTRIBUTING.md) before proposing a statement, test,
or editorial change. Code is available under the MIT License; original course
content is available under CC BY 4.0 as described in
[`LICENSE-CONTENT.md`](LICENSE-CONTENT.md).
