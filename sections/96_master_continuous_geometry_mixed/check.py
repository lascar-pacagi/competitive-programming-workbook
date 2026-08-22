from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT))
from tools.section_checker import run_section_checks
SECTION=Path(__file__).resolve().parent
PROBLEMS=[SECTION/"problems"/x for x in (
        'a_safe_operating_region',
        'b_round_table_clearance',
        'c_sensor_overlap',
        'd_emergency_broadcast_disk',
        'e_empty_observation_zone',
        'f_low_cost_fiber',
)]
if __name__=="__main__":raise SystemExit(run_section_checks(96,PROBLEMS,ROOT))
