"""Friendly checker for Section 22."""

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
    SECTION / "problems" / "a_broken_stairs",
    SECTION / "problems" / "b_training_score",
    SECTION / "problems" / "c_energy_route",
    SECTION / "problems" / "d_exact_change",
]

def main() -> int:
    return run_section_checks(22, PROBLEMS, ROOT)


if __name__ == "__main__":
    raise SystemExit(main())
