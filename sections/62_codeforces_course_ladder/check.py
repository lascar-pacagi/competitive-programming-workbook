#!/usr/bin/env python3
"""Validate the 50-rung Codeforces ladder and local companion packages."""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from tools.section_checker import run_section_checks


SECTION = Path(__file__).resolve().parent
REQUIRED = (
    "README.md",
    "PRACTICE.md",
    "problem_sheet.qmd",
    "lesson.qmd",
    "editorial.qmd",
    "OFFLINE_COMPANIONS.md",
)
PACKAGE_FILES = (
    "README.md",
    "manifest.json",
    "solve.cpp",
    "solve.py",
    "solution.cpp",
    "solution.py",
    "tests/sample1.in",
    "tests/sample1.out",
    "tests/edge1.in",
    "tests/edge1.out",
    "tests/random_cases.py",
)


def companion_packages() -> list[Path]:
    packages = sorted((SECTION / "problems").glob("[0-9][0-9]_*"))
    if len(packages) != 50:
        raise SystemExit(f"Section 62: expected 50 companion packages, found {len(packages)}")
    return packages


def main() -> int:
    missing = [name for name in REQUIRED if not (SECTION / name).is_file()]
    packages = companion_packages()
    for package in packages:
        missing.extend(str(path.relative_to(SECTION)) for name in PACKAGE_FILES if not (path := package / name).is_file())
    if missing:
        raise SystemExit(f"Section 62: missing {', '.join(missing)}")

    if os.environ.get("CP_TARGET") != "solution":
        print("Section 62: 50 offline companion package contracts are complete.")
        print("Run CP_TARGET=solution python3 sections/62_codeforces_course_ladder/check.py to verify references.")
        return 0

    return run_section_checks(62, packages, ROOT, random_count=6)


if __name__ == "__main__":
    raise SystemExit(main())
