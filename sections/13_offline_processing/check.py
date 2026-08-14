"""Friendly checker for Section 13."""

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
    SECTION / "problems" / "a_coordinate_compression",
    SECTION / "problems" / "b_range_count_at_most",
    SECTION / "problems" / "c_distinct_range_queries",
    SECTION / "problems" / "d_activation_totals",
]

def main() -> int:
    return run_section_checks(13, PROBLEMS, ROOT)


if __name__ == "__main__":
    raise SystemExit(main())
