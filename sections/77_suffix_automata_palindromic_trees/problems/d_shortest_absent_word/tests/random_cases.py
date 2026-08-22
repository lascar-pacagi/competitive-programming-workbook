import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
raise SystemExit(
    subprocess.call(
        [sys.executable, str(ROOT / "tools" / "suffix_structures_random.py"), "absent_word", *sys.argv[1:]]
    )
)
