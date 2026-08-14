"""Friendly checker for Section 6."""

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
    SECTION / "problems" / "a_sorted_two_sum",
    SECTION / "problems" / "b_longest_bounded_window",
    SECTION / "problems" / "c_count_subarrays_at_most",
    SECTION / "problems" / "d_cover_all_labels",
]

def main() -> int:
    return run_section_checks(6, PROBLEMS, ROOT)


if __name__ == "__main__":
    raise SystemExit(main())
