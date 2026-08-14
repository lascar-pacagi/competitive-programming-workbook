"""Friendly checker for Section 41."""

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
    SECTION / "problems" / "a_tree_distances",
    SECTION / "problems" / "b_max_edge_path",
    SECTION / "problems" / "c_kth_node_path",
    SECTION / "problems" / "d_weighted_distances",
]

def main() -> int:
    return run_section_checks(41, PROBLEMS, ROOT)


if __name__ == "__main__":
    raise SystemExit(main())
