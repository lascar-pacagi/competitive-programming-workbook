"""Friendly checker for Section 64."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from tools.section_checker import run_section_checks

SECTION = Path(__file__).resolve().parent
PROBLEMS = [
    SECTION / "problems" / "a_gcd_pair_energy",
    SECTION / "problems" / "b_summatory_totient",
    SECTION / "problems" / "c_lcm_pair_spectrum",
    SECTION / "problems" / "d_squarefree_rank",
]

if __name__ == "__main__":
    raise SystemExit(run_section_checks(64, PROBLEMS, ROOT))
