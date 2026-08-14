"""Friendly checker for Section 59."""
from __future__ import annotations
import os, subprocess, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from tools.section_checker import run_section_checks

SECTION=Path(__file__).resolve().parent
PROBLEMS=[
    SECTION / "problems" / "a_team_assignment",
    SECTION / "problems" / "b_team_scoreboard",
    SECTION / "problems" / "c_template_fibonacci",
    SECTION / "problems" / "d_contest_schedule",
]

def main() -> int:
    return run_section_checks(59, PROBLEMS, ROOT)


if __name__ == "__main__":
    raise SystemExit(main())
