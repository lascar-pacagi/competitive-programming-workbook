"""Friendly checker for Section 1."""

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
    SECTION / "problems" / "a_sum_constraints",
    SECTION / "problems" / "b_until_threshold",
    SECTION / "problems" / "c_token_budget",
    SECTION / "problems" / "d_batch_pages",
]

def main() -> int:
    return run_section_checks(1, PROBLEMS, ROOT)


if __name__ == "__main__":
    raise SystemExit(main())
