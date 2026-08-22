"""Friendly checker for Section 78."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from tools.section_checker import run_section_checks

SECTION = Path(__file__).resolve().parent
PROBLEMS = [
    SECTION / "problems" / name
    for name in (
        "a_minimum_rotation",
        "b_repetition_spectrum",
        "c_kth_substring_with_multiplicity",
        "d_common_distinct_substrings",
        "e_palindrome_frequency_value",
        "f_multi_archive_commonality",
    )
]

if __name__ == "__main__":
    raise SystemExit(run_section_checks(78, PROBLEMS, ROOT))
