import subprocess,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[5]
raise SystemExit(subprocess.call([sys.executable,str(ROOT/"tools"/"frontier_dp_random.py"),"digitpattern_story",*sys.argv[1:]]))
