"""Friendly checker for Section 71."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from tools.section_checker import run_section_checks

SECTION = Path(__file__).resolve().parent
PROBLEMS = [
    SECTION / "problems" / name
    for name in (
        "a_monotone_l1",
        "b_exact_red_mst",
        "c_convex_allocation",
        "d_weighted_bounded_isotonic",
    )
]
if __name__ == "__main__":
    raise SystemExit(run_section_checks(71, PROBLEMS, ROOT))
