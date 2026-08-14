"""Friendly checker for Section 18."""

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
    SECTION / "problems" / "a_network_growth",
    SECTION / "problems" / "b_minimum_network",
    SECTION / "problems" / "c_cluster_split",
    SECTION / "problems" / "d_cable_savings",
]

def main() -> int:
    return run_section_checks(18, PROBLEMS, ROOT)


if __name__ == "__main__":
    raise SystemExit(main())
