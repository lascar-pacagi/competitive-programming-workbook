"""Friendly checker for Section 52."""
from __future__ import annotations
import os, subprocess, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from tools.section_checker import run_section_checks

SECTION=Path(__file__).resolve().parent
PROBLEMS=[
    SECTION / "problems" / "a_nim_winner",
    SECTION / "problems" / "b_subtraction_game",
    SECTION / "problems" / "c_dag_game",
    SECTION / "problems" / "d_multi_subtraction",
]

def main() -> int:
    return run_section_checks(52, PROBLEMS, ROOT)


if __name__ == "__main__":
    raise SystemExit(main())
