"""Friendly checker for Section 2."""

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
    SECTION / "problems" / "a_robot_walk",
    SECTION / "problems" / "b_ticket_split",
    SECTION / "problems" / "c_best_subset",
    SECTION / "problems" / "d_carousel_visits",
]

def main() -> int:
    return run_section_checks(2, PROBLEMS, ROOT)


if __name__ == "__main__":
    raise SystemExit(main())
