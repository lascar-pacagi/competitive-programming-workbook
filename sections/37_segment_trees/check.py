"""Friendly checker for Section 37."""

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
    SECTION / "problems" / "a_range_minimum_updates",
    SECTION / "problems" / "b_maximum_subarray_updates",
    SECTION / "problems" / "c_lazy_range_add_sum",
    SECTION / "problems" / "d_first_available",
]

def main() -> int:
    return run_section_checks(37, PROBLEMS, ROOT)


if __name__ == "__main__":
    raise SystemExit(main())
