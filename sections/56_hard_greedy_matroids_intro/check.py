"""Friendly checker for Section 56."""
from __future__ import annotations
import os, subprocess, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from tools.section_checker import run_section_checks

SECTION=Path(__file__).resolve().parent
PROBLEMS=[
    SECTION / "problems" / "a_deadline_profit",
    SECTION / "problems" / "b_min_interval_cover",
    SECTION / "problems" / "c_mst_savings",
    SECTION / "problems" / "d_watch_schedule",
]

def main() -> int:
    return run_section_checks(56, PROBLEMS, ROOT)


if __name__ == "__main__":
    raise SystemExit(main())
