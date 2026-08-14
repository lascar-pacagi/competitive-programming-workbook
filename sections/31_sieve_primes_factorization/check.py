"""Friendly checker for Section 31."""

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
    SECTION / "problems" / "a_prime_counter",
    SECTION / "problems" / "b_factor_signature",
    SECTION / "problems" / "c_divisor_queries",
    SECTION / "problems" / "d_square_completion",
]

def main() -> int:
    return run_section_checks(31, PROBLEMS, ROOT)


if __name__ == "__main__":
    raise SystemExit(main())
