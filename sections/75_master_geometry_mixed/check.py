"""Friendly checker for Section 75."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from tools.section_checker import run_section_checks

SECTION = Path(__file__).resolve().parent
PROBLEMS = [
    SECTION / "problems" / x
    for x in (
        "a_convex_lattice_shield",
        "b_maximum_triangle",
        "c_robot_collision_translations",
        "d_weighted_crossings",
        "e_double_painted_map",
        "f_fortress_queries",
    )
]
if __name__ == "__main__":
    raise SystemExit(run_section_checks(75, PROBLEMS, ROOT))
