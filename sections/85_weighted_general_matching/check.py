from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT))
from tools.section_checker import run_section_checks
SECTION=Path(__file__).resolve().parent
PROBLEMS=[SECTION/"problems"/x for x in (
        'a_assignment_cost',
        'b_forbidden_profit_assignment',
        'c_general_pairing',
        'd_compatibility_pairing',
)]
if __name__=="__main__":raise SystemExit(run_section_checks(85,PROBLEMS,ROOT))
