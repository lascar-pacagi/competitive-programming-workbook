"""Friendly checker for Section 70."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from tools.section_checker import run_section_checks

SECTION = Path(__file__).resolve().parent
PROBLEMS = [
    SECTION / "problems" / name
    for name in (
        "a_bounded_circulation",
        "b_exact_cost_shipment",
        "c_quota_assignment",
        "d_min_cost_bounded_circulation",
    )
]
if __name__ == "__main__":
    raise SystemExit(run_section_checks(70, PROBLEMS, ROOT))
