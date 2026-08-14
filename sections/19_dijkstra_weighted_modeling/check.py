"""Friendly checker for Section 19."""

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
    SECTION / "problems" / "a_weighted_route_queries",
    SECTION / "problems" / "b_grid_toll_path",
    SECTION / "problems" / "c_discount_route",
    SECTION / "problems" / "d_even_hop_route",
]

def main() -> int:
    return run_section_checks(19, PROBLEMS, ROOT)


if __name__ == "__main__":
    raise SystemExit(main())
