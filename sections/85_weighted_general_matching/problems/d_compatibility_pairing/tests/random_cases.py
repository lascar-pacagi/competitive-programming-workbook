import subprocess,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[5]
raise SystemExit(subprocess.call([sys.executable,str(ROOT/"tools"/"matching_matroids_random.py"),"compat_pairing",*sys.argv[1:]]))
