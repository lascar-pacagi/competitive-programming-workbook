import subprocess,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[5]
raise SystemExit(subprocess.call([sys.executable,str(ROOT/"tools"/"dynamic_structures_random.py"),"cut_paste",*sys.argv[1:]]))
