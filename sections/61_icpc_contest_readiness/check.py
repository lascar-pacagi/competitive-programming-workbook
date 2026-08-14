"""Validate the Section 61 ICPC ladder and its offline companion packages."""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from tools.section_checker import run_section_checks


SECTION = Path(__file__).resolve().parent
REQUIRED_ARTIFACTS = (
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
    if len(packages) != 20:
        raise SystemExit(f"Section 61: expected 20 companion packages, found {len(packages)}")
    return packages


def main() -> int:
    missing = [name for name in REQUIRED_ARTIFACTS if not (SECTION / name).is_file()]
    packages = companion_packages()
    for package in packages:
        missing.extend(str(path.relative_to(SECTION)) for name in PACKAGE_FILES if not (path := package / name).is_file())
    if missing:
        print(f"Section 61: missing {', '.join(missing)}")
        return 1

    target = os.environ.get("CP_TARGET")
    if target != "solution":
        print("Section 61: 20 offline companion package contracts are complete.")
        print("Run CP_TARGET=solution python3 sections/61_icpc_contest_readiness/check.py to verify references.")
        return 0

    return run_section_checks(61, packages, ROOT, random_count=6)


if __name__ == "__main__":
    raise SystemExit(main())
