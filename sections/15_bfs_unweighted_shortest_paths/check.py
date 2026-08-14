"""Friendly checker for Section 15."""

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
    SECTION / "problems" / "a_connected_groups",
    SECTION / "problems" / "b_unweighted_routes",
    SECTION / "problems" / "c_grid_rescue_path",
    SECTION / "problems" / "d_nearest_station",
]

def main() -> int:
    return run_section_checks(15, PROBLEMS, ROOT)


if __name__ == "__main__":
    raise SystemExit(main())
