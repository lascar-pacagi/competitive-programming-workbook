# Contributing

Contributions that improve correctness, clarity, tests, or progression are
welcome.

## Keep personal submissions private

Tracked `solve.cpp` and `solve.py` files are public TODO stubs. Personal work
belongs in `.submissions/` or in an external directory selected with
`CP_SUBMISSIONS_DIR`. Pull requests containing completed student stubs will be
rejected automatically.

Seed a private overlay without replacing existing attempts:

```bash
python3 tools/manage_submissions.py seed
```

## Before opening a pull request

Enable the repository's safety hook once per clone:

```bash
git config core.hooksPath .githooks
```

It prevents a commit if a public `solve.cpp` or `solve.py` is no longer the
standard TODO stub, or if the course has a structural error. Run the same
publication checks manually with:

```bash
make public-check
CP_TARGET=solution python3 path/to/changed/section/check.py --keep-going
```

If a lesson or editorial changed, render its `.qmd` source and inspect the
resulting PDF. New problems must include the six standard package files, at
least one fixed test, and preferably a randomized generator with an independent
small oracle.

For performance-sensitive exercises, also add `tests/stress_cases.py`. Its
command-line contract is `--out-dir DIRECTORY`; write paired `.in` and `.out`
files there. The normal judge runs these cases under the manifest's per-case
time limit, including with `--random-count 0`. Prefer maximum-size adversarial
shapes with expected answers derived independently from the construction. Keep
small random oracle tests as well: large cases check different properties.

`tools/audit_performance_tests.py` inventories actual generated input sizes for
a section range. Its size threshold is a review aid, not proof of TLE coverage.
Run fixed and performance cases against both reference languages with:

```bash
python3 tools/check_performance_tests.py --through 42 --workers 1 --output /tmp/performance-reference-results.json
```

Use one worker when assessing wall-clock limits. Sections 1–41 share explicit
profiles in `tools/course_performance_profiles.json`; their construction oracles
live in the `tools/performance_*.py` modules.

Stage course files explicitly and inspect the staged patch:

```bash
git add path/to/changed/course/files
git diff --cached
```

Do not copy complete third-party problem statements or test data unless their
license permits redistribution. Prefer a short original summary and a link to
the official problem.
