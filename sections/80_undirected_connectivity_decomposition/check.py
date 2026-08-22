from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT))
from tools.section_checker import run_section_checks
SECTION=Path(__file__).resolve().parent
PROBLEMS=[SECTION/"problems"/x for x in (
        'a_bridge_distance_queries',
        'b_articulation_pair_damage',
        'c_mandatory_station_queries',
        'd_two_edge_completion',
)]
if __name__=="__main__":raise SystemExit(run_section_checks(80,PROBLEMS,ROOT))
