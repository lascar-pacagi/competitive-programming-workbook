"""Friendly checker for Section 4."""

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
    SECTION / "problems" / "a_range_sum_queries",
    SECTION / "problems" / "b_range_add_final_array",
    SECTION / "problems" / "c_subarray_sum_count",
    SECTION / "problems" / "d_signal_peak",
]

def main() -> int:
    return run_section_checks(4, PROBLEMS, ROOT)


if __name__ == "__main__":
    raise SystemExit(main())
