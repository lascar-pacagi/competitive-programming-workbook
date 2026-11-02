"""Friendly checker for Section 45."""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from tools.section_checker import run_section_checks

SECTION = Path(__file__).resolve().parent
PROBLEMS = [
    SECTION / "problems" / "a_max_flow",
    SECTION / "problems" / "b_bipartite_matching",
    SECTION / "problems" / "c_min_cut_reachable",
    SECTION / "problems" / "d_project_selection",
    SECTION / "problems" / "e_separated_light_marks",
    SECTION / "problems" / "f_crate_routing",
    SECTION / "problems" / "g_silent_rehearsal",
    SECTION / "problems" / "h_emergency_corridors",
    SECTION / "problems" / "i_directional_relay_modes",
    SECTION / "problems" / "j_exhibit_pacts",
    SECTION / "problems" / "k_quota_manifests",
    SECTION / "problems" / "l_calendar_reinforcement",
    SECTION / "problems" / "m_resilient_reservations",
    SECTION / "problems" / "n_signal_concentration",
]

def main() -> int:
    return run_section_checks(45, PROBLEMS, ROOT)


if __name__ == "__main__":
    raise SystemExit(main())
