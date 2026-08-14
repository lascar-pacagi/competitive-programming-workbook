"""Friendly checker for Section 23."""

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
    SECTION / "problems" / "a_budget_selection",
    SECTION / "problems" / "b_unlimited_training",
    SECTION / "problems" / "c_possible_sums",
    SECTION / "problems" / "d_balanced_split",
]

def main() -> int:
    return run_section_checks(23, PROBLEMS, ROOT)


if __name__ == "__main__":
    raise SystemExit(main())
