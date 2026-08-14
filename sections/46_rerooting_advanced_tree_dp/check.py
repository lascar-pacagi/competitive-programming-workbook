"""Friendly checker for Section 46."""
from __future__ import annotations
import os, subprocess, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from tools.section_checker import run_section_checks

SECTION=Path(__file__).resolve().parent
PROBLEMS=[
    SECTION / "problems" / "a_sum_distances",
    SECTION / "problems" / "b_farthest_node_distance",
    SECTION / "problems" / "c_paths_through_node",
    SECTION / "problems" / "d_forced_independent_set",
]

def main() -> int:
    return run_section_checks(46, PROBLEMS, ROOT)


if __name__ == "__main__":
    raise SystemExit(main())
