"""Friendly checker for Section 73."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from tools.section_checker import run_section_checks

SECTION = Path(__file__).resolve().parent
PROBLEMS = [
    SECTION / "problems" / x
    for x in (
        "a_hull_statistics",
        "b_farthest_pair",
        "c_sum_polygon_queries",
        "d_convex_polygon_distance",
    )
]
if __name__ == "__main__":
    raise SystemExit(run_section_checks(73, PROBLEMS, ROOT))
