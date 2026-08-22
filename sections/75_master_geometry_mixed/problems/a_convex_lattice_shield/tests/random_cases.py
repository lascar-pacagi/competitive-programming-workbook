import subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
raise SystemExit(
    subprocess.call(
        [
            sys.executable,
            str(ROOT / "tools" / "geometry_advanced_random.py"),
            "lattice",
            *sys.argv[1:],
        ]
    )
)
