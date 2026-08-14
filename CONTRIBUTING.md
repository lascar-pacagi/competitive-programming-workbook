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

Stage course files explicitly and inspect the staged patch:

```bash
git add path/to/changed/course/files
git diff --cached
```

Do not copy complete third-party problem statements or test data unless their
license permits redistribution. Prefer a short original summary and a link to
the official problem.
