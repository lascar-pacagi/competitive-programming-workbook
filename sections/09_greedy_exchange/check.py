"""Friendly checker for Section 9."""

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
    SECTION / "problems" / "a_activity_selection",
    SECTION / "problems" / "b_rescue_boats",
    SECTION / "problems" / "c_deadline_schedule",
    SECTION / "problems" / "d_workshop_badges",
]

def main() -> int:
    return run_section_checks(9, PROBLEMS, ROOT)


if __name__ == "__main__":
    raise SystemExit(main())
