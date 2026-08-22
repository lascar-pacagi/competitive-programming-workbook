"""Friendly checker for Section 76."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from tools.section_checker import run_section_checks

SECTION = Path(__file__).resolve().parent
PROBLEMS = [
    SECTION / "problems" / name
    for name in (
        "a_suffix_order_lcp",
        "b_repeated_at_least_k",
        "c_pattern_occurrence_queries",
        "d_disjoint_repeated_substring",
    )
]

if __name__ == "__main__":
    raise SystemExit(run_section_checks(76, PROBLEMS, ROOT))
