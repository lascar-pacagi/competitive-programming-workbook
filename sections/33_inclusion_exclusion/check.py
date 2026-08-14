"""Friendly checker for Section 33."""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from tools.section_checker import run_section_checks

SECTION = Path(__file__).resolve().parent
PROBLEMS = [
    SECTION / "problems" / "a_multiples_union",
    SECTION / "problems" / "b_all_symbols",
    SECTION / "problems" / "c_bounded_candies",
    SECTION / "problems" / "d_seating_without_matches",
]

def main() -> int:
    return run_section_checks(33, PROBLEMS, ROOT)


if __name__ == "__main__":
    raise SystemExit(main())
