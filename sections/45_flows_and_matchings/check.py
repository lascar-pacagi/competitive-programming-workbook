"""Friendly checker for Section 45."""

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
    SECTION / "problems" / "a_max_flow",
    SECTION / "problems" / "b_bipartite_matching",
    SECTION / "problems" / "c_min_cut_reachable",
    SECTION / "problems" / "d_project_selection",
]

def main() -> int:
    return run_section_checks(45, PROBLEMS, ROOT)


if __name__ == "__main__":
    raise SystemExit(main())
