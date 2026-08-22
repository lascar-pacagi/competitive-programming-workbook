from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT))
from tools.section_checker import run_section_checks
SECTION=Path(__file__).resolve().parent
PROBLEMS=[SECTION/"problems"/x for x in (
        'a_sequence_cut_paste',
        'b_reversible_range_ledger',
        'c_dynamic_forest_xor',
        'd_threshold_component_size',
)]
if __name__=="__main__":raise SystemExit(run_section_checks(83,PROBLEMS,ROOT))
