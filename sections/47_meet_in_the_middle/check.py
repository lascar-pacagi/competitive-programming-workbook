"""Friendly checker for Section 47."""
from __future__ import annotations
import os, subprocess, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from tools.section_checker import run_section_checks

SECTION=Path(__file__).resolve().parent
PROBLEMS=[
    SECTION / "problems" / "a_count_subset_sums_leq",
    SECTION / "problems" / "b_best_subset_sum_leq",
    SECTION / "problems" / "c_closest_subset_sum",
    SECTION / "problems" / "d_exact_sum_max_items",
]

def main() -> int:
    return run_section_checks(47, PROBLEMS, ROOT)


if __name__ == "__main__":
    raise SystemExit(main())
