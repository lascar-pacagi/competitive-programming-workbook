"""Friendly checker for Section 44."""

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
    SECTION / "problems" / "a_trie_prefix_count",
    SECTION / "problems" / "b_palindrome_queries",
    SECTION / "problems" / "c_distinct_substrings",
    SECTION / "problems" / "d_unique_prefix_lengths",
]

def main() -> int:
    return run_section_checks(44, PROBLEMS, ROOT)


if __name__ == "__main__":
    raise SystemExit(main())
