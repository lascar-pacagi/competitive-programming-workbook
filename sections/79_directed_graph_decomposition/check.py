from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT))
from tools.section_checker import run_section_checks
SECTION=Path(__file__).resolve().parent
PROBLEMS=[SECTION/"problems"/x for x in (
        'a_condensation_profile',
        'b_clause_satisfiability',
        'c_lexicographic_euler_trail',
        'd_unavoidable_checkpoints',
)]
if __name__=="__main__":raise SystemExit(run_section_checks(79,PROBLEMS,ROOT))
