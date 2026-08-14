"""Friendly checker for Section 60."""
from __future__ import annotations
import os, subprocess, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from tools.section_checker import run_section_checks

SECTION=Path(__file__).resolve().parent
PROBLEMS=[
    SECTION / "problems" / "a_capstone_subset",
    SECTION / "problems" / "b_capstone_crt",
    SECTION / "problems" / "c_capstone_recurrence",
    SECTION / "problems" / "d_coupon_route",
]

def main() -> int:
    return run_section_checks(60, PROBLEMS, ROOT)


if __name__ == "__main__":
    raise SystemExit(main())
