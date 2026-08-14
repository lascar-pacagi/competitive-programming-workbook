"""Friendly checker for Section 5."""

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
    SECTION / "problems" / "a_min_adjacent_gap",
    SECTION / "problems" / "b_rank_table",
    SECTION / "problems" / "c_merge_intervals",
    SECTION / "problems" / "d_compact_team",
]

def main() -> int:
    return run_section_checks(5, PROBLEMS, ROOT)


if __name__ == "__main__":
    raise SystemExit(main())
