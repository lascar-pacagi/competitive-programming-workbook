"""Friendly checker for Section 11."""

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
    SECTION / "problems" / "a_peak_active",
    SECTION / "problems" / "b_covered_length",
    SECTION / "problems" / "c_point_coverage",
    SECTION / "problems" / "d_first_busiest",
]

def main() -> int:
    return run_section_checks(11, PROBLEMS, ROOT)


if __name__ == "__main__":
    raise SystemExit(main())
