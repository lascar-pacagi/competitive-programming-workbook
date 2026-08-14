"""Friendly checker for Section 39."""

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
    SECTION / "problems" / "a_running_median",
    SECTION / "problems" / "b_course_rooms",
    SECTION / "problems" / "c_k_smallest_pair_sums",
    SECTION / "problems" / "d_merge_costs",
]

def main() -> int:
    return run_section_checks(39, PROBLEMS, ROOT)


if __name__ == "__main__":
    raise SystemExit(main())
