"""Friendly checker for Section 34."""

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
    SECTION / "problems" / "a_expected_prize",
    SECTION / "problems" / "b_first_success",
    SECTION / "problems" / "c_coupon_collector",
    SECTION / "problems" / "d_simultaneous_wins",
]

def main() -> int:
    return run_section_checks(34, PROBLEMS, ROOT)


if __name__ == "__main__":
    raise SystemExit(main())
