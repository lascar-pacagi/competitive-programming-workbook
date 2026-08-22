"""Friendly checker for Section 65."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from tools.section_checker import run_section_checks

SECTION = Path(__file__).resolve().parent
PROBLEMS = [
    SECTION / "problems" / "a_cyclic_agreement",
    SECTION / "problems" / "b_bounded_sum_product",
    SECTION / "problems" / "c_huge_linear_recurrence",
    SECTION / "problems" / "d_recurrence_recovery",
]

if __name__ == "__main__":
    raise SystemExit(run_section_checks(65, PROBLEMS, ROOT))
