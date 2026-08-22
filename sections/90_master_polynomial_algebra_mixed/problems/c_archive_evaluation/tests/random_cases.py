import subprocess,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[5]
raise SystemExit(subprocess.call([sys.executable,str(ROOT/"tools"/"polynomial_algebra_random.py"),"archive_eval",*sys.argv[1:]]))
