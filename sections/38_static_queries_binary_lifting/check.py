"""Friendly checker for Section 38."""

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
    SECTION / "problems" / "a_static_range_minimum",
    SECTION / "problems" / "b_static_range_gcd",
    SECTION / "problems" / "c_kth_ancestor",
    SECTION / "problems" / "d_ancestor_minimum",
]

def main() -> int:
    return run_section_checks(38, PROBLEMS, ROOT)


if __name__ == "__main__":
    raise SystemExit(main())
