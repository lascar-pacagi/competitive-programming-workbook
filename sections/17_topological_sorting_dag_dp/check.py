"""Friendly checker for Section 17."""

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
    SECTION / "problems" / "a_lexicographic_course_order",
    SECTION / "problems" / "b_longest_dag_path",
    SECTION / "problems" / "c_project_schedule",
    SECTION / "problems" / "d_unique_build_order",
]

def main() -> int:
    return run_section_checks(17, PROBLEMS, ROOT)


if __name__ == "__main__":
    raise SystemExit(main())
