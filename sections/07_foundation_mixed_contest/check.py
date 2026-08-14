"""Friendly checker for Section 7."""

from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from tools.section_checker import run_section_checks


SECTION = Path(__file__).resolve().parent
PROBLEMS = [
    SECTION / "problems" / "a_inventory_cleanup",
    SECTION / "problems" / "b_peak_load",
    SECTION / "problems" / "c_best_study_streak",
    SECTION / "problems" / "d_balanced_break",
    SECTION / "problems" / "e_circular_patrol",
]

def main() -> int:
    return run_section_checks(7, PROBLEMS, ROOT)


if __name__ == "__main__":
    raise SystemExit(main())
