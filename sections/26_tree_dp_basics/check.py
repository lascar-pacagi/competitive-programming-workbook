"""Friendly checker for Section 26."""

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
    SECTION / "problems" / "a_festival_invite",
    SECTION / "problems" / "b_road_pairing",
    SECTION / "problems" / "c_tree_colorings",
    SECTION / "problems" / "d_road_guards",
]

def main() -> int:
    return run_section_checks(26, PROBLEMS, ROOT)


if __name__ == "__main__":
    raise SystemExit(main())
