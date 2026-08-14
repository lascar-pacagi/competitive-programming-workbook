"""Friendly checker for Section 49."""
from __future__ import annotations
import os, subprocess, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from tools.section_checker import run_section_checks

SECTION=Path(__file__).resolve().parent
PROBLEMS=[
    SECTION / "problems" / "a_dynamic_line_min",
    SECTION / "problems" / "b_quadratic_cht_dp",
    SECTION / "problems" / "c_dynamic_line_max",
    SECTION / "problems" / "d_line_winner",
]

def main() -> int:
    return run_section_checks(49, PROBLEMS, ROOT)


if __name__ == "__main__":
    raise SystemExit(main())
