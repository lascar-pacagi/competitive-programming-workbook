"""Friendly checker for Section 72."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from tools.section_checker import run_section_checks

SECTION = Path(__file__).resolve().parent
PROBLEMS = [
    SECTION / "problems" / name
    for name in (
        "a_exam_room_bounds",
        "b_bounded_exact_shipment",
        "c_selective_quota_profit",
        "d_bounded_convex_allocation",
        "e_exact_red_forest",
        "f_congested_team_assignment",
    )
]
if __name__ == "__main__":
    raise SystemExit(run_section_checks(72, PROBLEMS, ROOT))
