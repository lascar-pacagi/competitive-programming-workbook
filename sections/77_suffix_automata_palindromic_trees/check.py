"""Friendly checker for Section 77."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from tools.section_checker import run_section_checks

SECTION = Path(__file__).resolve().parent
PROBLEMS = [
    SECTION / "problems" / name
    for name in (
        "a_kth_distinct_substring",
        "b_longest_common_substring",
        "c_palindrome_prefix_profile",
        "d_shortest_absent_word",
    )
]

if __name__ == "__main__":
    raise SystemExit(run_section_checks(77, PROBLEMS, ROOT))
