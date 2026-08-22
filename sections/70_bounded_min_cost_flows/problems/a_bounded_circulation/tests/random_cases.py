import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
raise SystemExit(
    subprocess.call(
        [
            sys.executable,
            str(ROOT / "tools" / "flow_convex_random.py"),
            "circulation",
            *sys.argv[1:],
        ]
    )
)
