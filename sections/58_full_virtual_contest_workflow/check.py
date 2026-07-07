"""Friendly checker for Section 58."""
from __future__ import annotations
import os, subprocess, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
SECTION=Path(__file__).resolve().parent
PROBLEMS=[
    SECTION / "problems" / "a_scoreboard_rank",
    SECTION / "problems" / "b_split_workload",
    SECTION / "problems" / "c_quick_mst_decision",
]
def main()->int:
    target=os.environ.get("CP_TARGET","student"); print(f"Section 58: checking {target} submissions...\n", flush=True)
    for problem in PROBLEMS:
        for lang in ("cpp","py"):
            r=subprocess.run([sys.executable,"tools/judge.py",str(problem),"--lang",lang,"--random-count","25"],cwd=ROOT)
            if r.returncode: return r.returncode
    print("\nSection 58 complete: all checked submissions were accepted."); return 0
if __name__=="__main__": raise SystemExit(main())
