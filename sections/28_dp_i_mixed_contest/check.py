"""Friendly checker for Section 28."""

from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from tools.section_checker import run_section_checks


SECTION = Path(__file__).resolve().parent
PROBLEMS = [
    SECTION / "problems" / "a_training_schedule",
    SECTION / "problems" / "b_two_carts",
    SECTION / "problems" / "c_prerequisite_tree",
    SECTION / "problems" / "d_circular_exhibition",
    SECTION / "problems" / "e_one_diagonal_path",
    SECTION / "problems" / "f_matrix_chain",
    SECTION / "problems" / "g_hamiltonian_route",
    SECTION / "problems" / "h_sliding_jump_cost",
    SECTION / "problems" / "i_grouped_cargo",
    SECTION / "problems" / "j_minimum_starting_energy",
    SECTION / "problems" / "k_last_crystal_removed",
    SECTION / "problems" / "l_weighted_tree_guards",
]

def main() -> int:
    return run_section_checks(28, PROBLEMS, ROOT)


if __name__ == "__main__":
    raise SystemExit(main())
