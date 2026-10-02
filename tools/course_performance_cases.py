"""Dispatch constraint-specific performance tests for sections 1--41.

Existing large, construction-based random cases are retained as dedicated
performance cases; new profiles live in the three performance_* modules.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

ROOT=Path(__file__).resolve().parents[1]
PROFILES=ROOT/'tools/course_performance_profiles.json'


def generate(problem: Path, output: Path) -> None:
    profile=json.loads(PROFILES.read_text())[str(problem.resolve().relative_to(ROOT))]
    output.mkdir(parents=True,exist_ok=True)
    if profile['kind']=='construction':
        section=int(problem.parent.parent.name.split('_')[0]);slug=problem.name
        if section<=14:from tools.performance_01_14 import build
        elif section<=28:from tools.performance_15_28 import build
        else:from tools.performance_29_41 import build
        inp,out=build(section,slug)
        (output/'maximum_workload.in').write_text(inp)
        (output/'maximum_workload.out').write_text(out)
        if 15<=section<=28:
            from tools.performance_15_28 import extra_cases
            for name,inp,out in extra_cases(section,slug):
                (output/f'{name}.in').write_text(inp)
                (output/f'{name}.out').write_text(out)
        return
    if profile['kind']!='existing-scale':raise ValueError(profile)
    # Do not invoke the judge here: only the existing input/oracle generator.
    with tempfile.TemporaryDirectory(prefix='cp-existing-scale-') as directory:
        tmp=Path(directory)
        for count in (1,25):
            subprocess.run([sys.executable,str(problem/'tests/random_cases.py'),
                '--count',str(count),'--seed','20261001','--out-dir',directory],cwd=ROOT,check=True)
            candidates=list(tmp.glob('*.in'))
            largest=max(candidates,key=lambda p:p.stat().st_size)
            if largest.stat().st_size>=100_000:break
        if largest.stat().st_size<100_000:raise ValueError(f'Existing scale profile regressed: {problem}')
        expected=largest.with_suffix('.out')
        if not expected.exists():raise FileNotFoundError(expected)
        shutil.copyfile(largest,output/'existing_scale.in')
        shutil.copyfile(expected,output/'existing_scale.out')


def main(problem: Path) -> None:
    parser=argparse.ArgumentParser();parser.add_argument('--out-dir',type=Path,required=True)
    args=parser.parse_args();generate(problem,args.out_dir)
