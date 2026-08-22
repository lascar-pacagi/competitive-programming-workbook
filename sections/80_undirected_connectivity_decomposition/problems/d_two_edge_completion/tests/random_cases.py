import subprocess,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[5]
raise SystemExit(subprocess.call([sys.executable,str(ROOT/"tools"/"graph_decomposition_random.py"),"bridge_completion",*sys.argv[1:]]))
