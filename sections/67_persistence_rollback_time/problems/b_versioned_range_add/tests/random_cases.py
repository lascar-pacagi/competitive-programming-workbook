import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[5]
sys.path.insert(0,str(ROOT))
from tools.master_structures_random import main
if __name__=="__main__":main(Path(__file__).resolve().parents[1].name)
