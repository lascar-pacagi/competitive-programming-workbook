"""Friendly checker for Section 48."""
from __future__ import annotations
import os, subprocess, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from tools.section_checker import run_section_checks

SECTION=Path(__file__).resolve().parent
PROBLEMS=[
    SECTION / "problems" / "a_partition_quadratic",
    SECTION / "problems" / "b_window_min_dp",
    SECTION / "problems" / "c_optimal_merge_knuth",
    SECTION / "problems" / "d_bounded_length_max_sum",
]

def main() -> int:
    return run_section_checks(48, PROBLEMS, ROOT)


if __name__ == "__main__":
    raise SystemExit(main())
