"""Friendly checker for Section 3."""

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
    SECTION / "problems" / "a_value_counts",
    SECTION / "problems" / "b_frequency_winner",
    SECTION / "problems" / "c_pair_sum_count",
    SECTION / "problems" / "d_equal_index_pairs",
]

def main() -> int:
    return run_section_checks(3, PROBLEMS, ROOT)


if __name__ == "__main__":
    raise SystemExit(main())
