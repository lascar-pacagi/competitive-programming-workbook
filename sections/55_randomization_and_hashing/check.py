"""Friendly checker for Section 55."""
from __future__ import annotations
import os, subprocess, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from tools.section_checker import run_section_checks

SECTION=Path(__file__).resolve().parent
PROBLEMS=[
    SECTION / "problems" / "a_equal_substrings",
    SECTION / "problems" / "b_palindrome_substrings",
    SECTION / "problems" / "c_anagram_substrings",
    SECTION / "problems" / "d_longest_repeat",
]

def main() -> int:
    return run_section_checks(55, PROBLEMS, ROOT)


if __name__ == "__main__":
    raise SystemExit(main())
