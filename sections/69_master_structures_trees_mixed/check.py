"""Friendly checker for Section 69."""
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT))
from tools.section_checker import run_section_checks
SECTION=Path(__file__).resolve().parent
PROBLEMS=[SECTION/"problems"/name for name in (
 "a_snapshot_rank","b_seasonal_component_size","c_route_matrices",
 "d_beacon_distance_sum","e_weighted_marked_pairs","f_subtree_frequency_profile")]
if __name__=="__main__":raise SystemExit(run_section_checks(69,PROBLEMS,ROOT))
