"""Friendly checker for Section 66."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from tools.section_checker import run_section_checks

SECTION = Path(__file__).resolve().parent
PROBLEMS = [
    SECTION / "problems" / "a_primitive_necklaces",
    SECTION / "problems" / "b_totient_interval",
    SECTION / "problems" / "c_wildcard_rotation",
    SECTION / "problems" / "d_weighted_compositions",
    SECTION / "problems" / "e_black_box_walks",
    SECTION / "problems" / "f_gcd_one_size_spectrum",
]

if __name__ == "__main__":
    raise SystemExit(run_section_checks(66, PROBLEMS, ROOT))
