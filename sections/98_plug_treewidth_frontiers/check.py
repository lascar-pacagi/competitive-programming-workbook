from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT))
from tools.section_checker import run_section_checks
SECTION=Path(__file__).resolve().parent
PROBLEMS=[SECTION/"problems"/x for x in (
        'a_tower_domino_tilings',
        'b_connected_cell_sets',
        'c_terminal_steiner_network',
        'd_nice_decomposition_independent_set',
)]
if __name__=="__main__":raise SystemExit(run_section_checks(98,PROBLEMS,ROOT))
