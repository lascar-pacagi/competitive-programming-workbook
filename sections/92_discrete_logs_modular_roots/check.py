from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT))
from tools.section_checker import run_section_checks
SECTION=Path(__file__).resolve().parent
PROBLEMS=[SECTION/"problems"/x for x in (
        'a_smallest_primitive_root',
        'b_prime_discrete_log',
        'c_general_discrete_log',
        'd_modular_square_roots',
)]
if __name__=="__main__":raise SystemExit(run_section_checks(92,PROBLEMS,ROOT))
