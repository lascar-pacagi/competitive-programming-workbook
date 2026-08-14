"""Friendly checker for Section 54."""
from __future__ import annotations
import os, subprocess, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from tools.section_checker import run_section_checks

SECTION=Path(__file__).resolve().parent
PROBLEMS=[
    SECTION / "problems" / "a_orientation",
    SECTION / "problems" / "b_segment_intersection",
    SECTION / "problems" / "c_polygon_double_area",
    SECTION / "problems" / "d_interior_lattice_points",
]

def main() -> int:
    return run_section_checks(54, PROBLEMS, ROOT)


if __name__ == "__main__":
    raise SystemExit(main())
