"""Friendly checker for Section 32."""

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
    SECTION / "problems" / "a_choose_queries",
    SECTION / "problems" / "b_rearrange_letters",
    SECTION / "problems" / "c_distribute_candies",
    SECTION / "problems" / "d_separated_lineup",
]

def main() -> int:
    return run_section_checks(32, PROBLEMS, ROOT)


if __name__ == "__main__":
    raise SystemExit(main())
