"""Friendly checker for Section 36."""

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
    SECTION / "problems" / "a_point_add_range_sum",
    SECTION / "problems" / "b_inversion_count",
    SECTION / "problems" / "c_range_add_point_query",
    SECTION / "problems" / "d_offline_distinct_queries",
]

def main() -> int:
    return run_section_checks(36, PROBLEMS, ROOT)


if __name__ == "__main__":
    raise SystemExit(main())
