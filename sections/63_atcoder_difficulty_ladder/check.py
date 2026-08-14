#!/usr/bin/env python3
"""Validate Section 63's 50 AtCoder companion packages."""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from tools.section_checker import run_section_checks


SECTION = Path(__file__).resolve().parent
PACKAGE_FILES = (
    "README.md", "manifest.json", "solve.cpp", "solve.py",
    "solution.cpp", "solution.py", "tests/sample1.in", "tests/sample1.out",
    "tests/edge1.in", "tests/edge1.out", "tests/random_cases.py",
)


def main() -> int:
    packages = sorted((SECTION / "problems").glob("[0-9][0-9]_*"))
    if len(packages) != 50:
        raise SystemExit(f"Section 63: expected 50 packages, found {len(packages)}")
    missing = [
        str((package / name).relative_to(SECTION))
        for package in packages
        for name in PACKAGE_FILES
        if not (package / name).is_file()
    ]
    if missing:
        raise SystemExit("Section 63: missing " + ", ".join(missing))
    if os.environ.get("CP_TARGET") != "solution":
        print("Section 63: 50 offline companion package contracts are complete.")
        print("Run with CP_TARGET=solution to verify all references.")
        return 0
    return run_section_checks(63, packages, ROOT, random_count=6)


if __name__ == "__main__":
    raise SystemExit(main())
