from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT))
from tools.section_checker import run_section_checks
SECTION=Path(__file__).resolve().parent
PROBLEMS=[SECTION/"problems"/x for x in (
        'a_range_kth',
        'b_range_frequency',
        'c_range_cap_sum',
        'd_range_modulo_sum',
)]
if __name__=="__main__":raise SystemExit(run_section_checks(82,PROBLEMS,ROOT))
