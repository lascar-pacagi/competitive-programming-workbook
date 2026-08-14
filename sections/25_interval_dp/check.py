"""Friendly checker for Section 25."""

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
    SECTION / "problems" / "a_merge_piles",
    SECTION / "problems" / "b_palindrome_repairs",
    SECTION / "problems" / "c_treasure_balloons",
    SECTION / "problems" / "d_endgame_advantage",
]

def main() -> int:
    return run_section_checks(25, PROBLEMS, ROOT)


if __name__ == "__main__":
    raise SystemExit(main())
