"""Shared command-line runner for a section's problem packages."""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path
from typing import Sequence


def select_problems(
    problems: Sequence[Path],
    selectors: Sequence[str] | None,
    parser: argparse.ArgumentParser,
) -> list[Path]:
    """Return problems matching directory names, prefixes, or list positions."""

    if not selectors:
        return list(problems)

    requested = [
        selector.strip().lower()
        for group in selectors
        for selector in group.split(",")
        if selector.strip()
    ]
    if not requested:
        parser.error("--problem requires a non-empty selector")

    selected: set[Path] = set()
    for selector in requested:
        matches: list[Path] = []
        for position, problem in enumerate(problems, 1):
            name = problem.name.lower()
            short_name = name.split("_", 1)[0]
            if selector in {name, short_name, str(position)}:
                matches.append(problem)

        if not matches:
            available = ", ".join(
                f"{problem.name.split('_', 1)[0]} ({problem.name})"
                for problem in problems
            )
            parser.error(
                f"unknown problem {selector!r}; available problems: {available}"
            )
        if len(matches) > 1:
            names = ", ".join(problem.name for problem in matches)
            parser.error(
                f"ambiguous problem selector {selector!r}; matches: {names}"
            )
        selected.add(matches[0])

    return [problem for problem in problems if problem in selected]


def run_section_checks(
    section_number: int,
    problems: Sequence[Path],
    root: Path,
    argv: Sequence[str] | None = None,
    random_count: int = 25,
) -> int:
    """Run the local judge for the requested languages and problem packages."""

    parser = argparse.ArgumentParser(
        description=f"Check the submissions for Section {section_number}."
    )
    parser.add_argument(
        "-k",
        "--keep-going",
        action="store_true",
        help="check every problem/language even after a failure",
    )
    parser.add_argument(
        "--lang",
        choices=("both", "cpp", "py"),
        default="both",
        help="language to check (default: both)",
    )
    parser.add_argument(
        "-p",
        "--problem",
        action="append",
        metavar="SELECTOR",
        help=(
            "check only this problem: use its letter/number or directory name; "
            "may be repeated or comma-separated"
        ),
    )
    parser.add_argument(
        "--gdb",
        metavar="CASE",
        help=(
            "debug one selected C++ problem on this fixed/random case name "
            "or input-file path"
        ),
    )
    parser.add_argument(
        "--step",
        action="store_true",
        help="with --gdb, stop at main for interactive stepping",
    )
    args = parser.parse_args(argv)

    problems = select_problems(problems, args.problem, parser)
    if args.gdb:
        if len(problems) != 1:
            parser.error("--gdb requires exactly one problem selected with --problem")
        if args.lang == "py":
            parser.error("--gdb cannot be used with --lang py")
        command = [
            sys.executable,
            "tools/judge.py",
            str(problems[0]),
            "--lang",
            "cpp",
            "--random-count",
            str(random_count),
            "--gdb",
            "--case",
            args.gdb,
        ]
        if args.step:
            command.append("--step")
        return subprocess.run(command, cwd=root).returncode
    if args.step:
        parser.error("--step requires --gdb")

    languages = ("cpp", "py") if args.lang == "both" else (args.lang,)
    target = os.environ.get("CP_TARGET", "student")
    failures: list[tuple[str, str]] = []
    accepted_languages: dict[Path, list[str]] = {
        problem: [] for problem in problems
    }

    print(
        f"Section {section_number}: checking {target} submissions "
        f"({', '.join(languages)})...\n",
        flush=True,
    )

    for problem in problems:
        for language in languages:
            result = subprocess.run(
                [
                    sys.executable,
                    "tools/judge.py",
                    str(problem),
                    "--lang",
                    language,
                    "--random-count",
                    str(random_count),
                ],
                cwd=root,
            )
            if not result.returncode:
                accepted_languages[problem].append(language)
                continue

            failures.append((problem.name, language))
            if not args.keep_going:
                print(
                    "\nThe checker stopped at the first failure. "
                    "Use --keep-going to check the remaining submissions."
                )
                return result.returncode

    if args.keep_going:
        solved_count = sum(
            bool(passed) for passed in accepted_languages.values()
        )
        print(
            f"\nProblem progress: {solved_count}/{len(problems)} solved "
            "in at least one checked language."
        )
        for problem in problems:
            passed = accepted_languages[problem]
            if passed:
                print(f"- SOLVED: {problem.name} ({', '.join(passed)})")
            else:
                print(f"- NOT SOLVED: {problem.name}")

    if failures:
        print(f"\nFailed submissions: {len(failures)}")
        for problem_name, language in failures:
            print(f"- {problem_name} [{language}]")
        return 1

    print(
        f"\nSection {section_number} complete: "
        "all checked submissions were accepted."
    )
    return 0
