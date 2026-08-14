"""Friendly checker for Section 35."""

from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from tools.section_checker import run_section_checks


SECTION = Path(__file__).resolve().parent
PROBLEMS = [
    SECTION / "problems" / "a_blocked_path",
    SECTION / "problems" / "b_coprime_pairs",
    SECTION / "problems" / "c_at_least_one",
    SECTION / "problems" / "d_complete_alphabet",
    SECTION / "problems" / "e_modular_appointment",
    SECTION / "problems" / "f_festival_synchronization",
    SECTION / "problems" / "g_capped_allocation",
    SECTION / "problems" / "h_gcd_one_subsets",
    SECTION / "problems" / "i_exactly_k_colors",
    SECTION / "problems" / "j_target_lcm_subsets",
    SECTION / "problems" / "k_weighted_coupon_collection",
    SECTION / "problems" / "l_random_divisor_descent",
]

def main() -> int:
    return run_section_checks(35, PROBLEMS, ROOT)


if __name__ == "__main__":
    raise SystemExit(main())
