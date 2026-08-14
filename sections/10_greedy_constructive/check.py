"""Friendly checker for Section 10."""

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
    SECTION / "problems" / "a_non_decreasing_repairs",
    SECTION / "problems" / "b_bracket_completion",
    SECTION / "problems" / "c_bounded_sum_sequence",
    SECTION / "problems" / "d_pattern_permutation",
]

def main() -> int:
    return run_section_checks(10, PROBLEMS, ROOT)


if __name__ == "__main__":
    raise SystemExit(main())
