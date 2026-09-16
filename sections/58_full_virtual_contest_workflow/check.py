"""Friendly checker for Section 58."""
from __future__ import annotations
import os, subprocess, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from tools.section_checker import run_section_checks

SECTION=Path(__file__).resolve().parent
PROBLEMS=[
    SECTION / "problems" / "a_scoreboard_rank",
    SECTION / "problems" / "b_split_workload",
    SECTION / "problems" / "c_quick_mst_decision",
    SECTION / "problems" / "d_circular_contest_run",
]

def main() -> int:
    return run_section_checks(58, PROBLEMS, ROOT)


if __name__ == "__main__":
    raise SystemExit(main())
