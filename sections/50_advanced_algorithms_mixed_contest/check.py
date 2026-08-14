"""Friendly checker for Section 50."""

from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from tools.section_checker import run_section_checks


SECTION = Path(__file__).resolve().parent
PROBLEMS = [
    SECTION / "problems" / "a_dag_grundy",
    SECTION / "problems" / "b_general_crt",
    SECTION / "problems" / "c_fast_fibonacci",
    SECTION / "problems" / "d_fibonacci_range_sum",
    SECTION / "problems" / "e_pattern_prefix_matches",
    SECTION / "problems" / "f_suffix_lcp_queries",
    SECTION / "problems" / "g_domino_placement",
    SECTION / "problems" / "h_weighted_tree_distances",
    SECTION / "problems" / "i_balanced_subset_difference",
    SECTION / "problems" / "j_monge_partition_table",
    SECTION / "problems" / "k_online_line_dp",
    SECTION / "problems" / "l_profitable_disjoint_routes",
]

def main() -> int:
    return run_section_checks(50, PROBLEMS, ROOT)


if __name__ == "__main__":
    raise SystemExit(main())
