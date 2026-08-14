"""Friendly checker for Section 30."""

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
    SECTION / "problems" / "a_gcd_lcm_queries",
    SECTION / "problems" / "b_general_inverse",
    SECTION / "problems" / "c_linear_diophantine",
    SECTION / "problems" / "d_clock_offset",
    SECTION / "problems" / "e_merge_congruences",
    SECTION / "problems" / "f_shared_maintenance_window",
]

def main() -> int:
    return run_section_checks(30, PROBLEMS, ROOT)


if __name__ == "__main__":
    raise SystemExit(main())
