"""Friendly checker for Section 20."""

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
    SECTION / "problems" / "a_binary_weight_routes",
    SECTION / "problems" / "b_conveyor_grid",
    SECTION / "problems" / "c_warp_maze",
    SECTION / "problems" / "d_letter_portals",
]

def main() -> int:
    return run_section_checks(20, PROBLEMS, ROOT)


if __name__ == "__main__":
    raise SystemExit(main())
