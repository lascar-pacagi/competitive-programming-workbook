"""Friendly checker for Section 57."""
from __future__ import annotations
import os, subprocess, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from tools.section_checker import run_section_checks

SECTION=Path(__file__).resolve().parent
PROBLEMS=[
    SECTION / "problems" / "a_matching_model",
    SECTION / "problems" / "b_small_2sat",
    SECTION / "problems" / "c_capstone_matching",
    SECTION / "problems" / "d_dag_path_cover",
]

def main() -> int:
    return run_section_checks(57, PROBLEMS, ROOT)


if __name__ == "__main__":
    raise SystemExit(main())
