from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT))
from tools.section_checker import run_section_checks
SECTION=Path(__file__).resolve().parent
PROBLEMS=[SECTION/"problems"/x for x in (
        'a_rational_series',
        'b_connected_series',
        'c_archive_evaluation',
        'd_recover_polynomial',
        'e_or_convolution',
        'f_disjoint_cover_counts',
)]
if __name__=="__main__":raise SystemExit(run_section_checks(90,PROBLEMS,ROOT))
