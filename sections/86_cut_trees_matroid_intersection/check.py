from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT))
from tools.section_checker import run_section_checks
SECTION=Path(__file__).resolve().parent
PROBLEMS=[SECTION/"problems"/x for x in (
        'a_all_pairs_cut_queries',
        'b_rainbow_forest',
        'c_dual_forest',
        'd_directed_arborescence',
)]
if __name__=="__main__":raise SystemExit(run_section_checks(86,PROBLEMS,ROOT))
