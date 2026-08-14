"""Friendly checker for Section 51."""
from __future__ import annotations
import os, subprocess, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from tools.section_checker import run_section_checks

SECTION=Path(__file__).resolve().parent
PROBLEMS=[
    SECTION / "problems" / "a_same_parity",
    SECTION / "problems" / "b_xor_balanced_splits",
    SECTION / "problems" / "c_same_residue",
    SECTION / "problems" / "d_adjacent_flip_distance",
]

def main() -> int:
    return run_section_checks(51, PROBLEMS, ROOT)


if __name__ == "__main__":
    raise SystemExit(main())
