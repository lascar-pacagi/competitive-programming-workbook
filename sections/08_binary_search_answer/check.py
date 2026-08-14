"""Friendly checker for Section 8."""

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
    SECTION / "problems" / "a_square_threshold",
    SECTION / "problems" / "b_max_min_distance",
    SECTION / "problems" / "c_minimum_capacity",
    SECTION / "problems" / "d_factory_deadline",
]

def main() -> int:
    return run_section_checks(8, PROBLEMS, ROOT)


if __name__ == "__main__":
    raise SystemExit(main())
