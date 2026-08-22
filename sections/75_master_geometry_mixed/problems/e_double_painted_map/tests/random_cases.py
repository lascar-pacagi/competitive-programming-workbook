import subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
raise SystemExit(
    subprocess.call(
        [
            sys.executable,
            str(ROOT / "tools" / "geometry_advanced_random.py"),
            "double_rect",
            *sys.argv[1:],
        ]
    )
)
