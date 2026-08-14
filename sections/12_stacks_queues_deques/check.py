"""Friendly checker for Section 12."""

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
    SECTION / "problems" / "a_next_greater",
    SECTION / "problems" / "b_sliding_window_max",
    SECTION / "problems" / "c_shortest_subarray_at_least",
    SECTION / "problems" / "d_bounded_spread_subarrays",
]

def main() -> int:
    return run_section_checks(12, PROBLEMS, ROOT)


if __name__ == "__main__":
    raise SystemExit(main())
