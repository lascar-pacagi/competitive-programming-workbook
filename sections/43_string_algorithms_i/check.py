"""Friendly checker for Section 43."""

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
    SECTION / "problems" / "a_kmp_occurrences",
    SECTION / "problems" / "b_all_borders",
    SECTION / "problems" / "c_minimal_period",
    SECTION / "problems" / "d_prefix_frequency",
]

def main() -> int:
    return run_section_checks(43, PROBLEMS, ROOT)


if __name__ == "__main__":
    raise SystemExit(main())
