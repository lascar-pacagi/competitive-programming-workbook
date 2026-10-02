"""Run fixed and dedicated performance cases against course reference solutions."""
from __future__ import annotations
import argparse
import atexit
from concurrent.futures import ThreadPoolExecutor
import json
from pathlib import Path
import sys
import shutil
import time

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from tools.judge import TEMP_DIRS, command_for, discover_fixed_cases, generate_stress_cases, load_manifest, run_case, source_for


def cleanup() -> None:
    for directory in TEMP_DIRS:
        shutil.rmtree(directory,ignore_errors=True)


atexit.register(cleanup)


def check(problem: Path, languages: list[str]) -> list[dict]:
    results=[];manifest=load_manifest(problem)
    try:cases=discover_fixed_cases(problem)+generate_stress_cases(problem)
    except Exception as exc:return [{'problem':str(problem.relative_to(ROOT)),'lang':'generator','ok':False,'message':str(exc)}]
    if not any(case.name.startswith('stress/') for case in cases):
        return [{'problem':str(problem.relative_to(ROOT)),'lang':'generator','ok':False,'message':'No dedicated performance case'}]
    for lang in languages:
        try:command=command_for(source_for(problem,lang,'solution'),lang)
        except Exception as exc:
            results.append({'problem':str(problem.relative_to(ROOT)),'lang':lang,'ok':False,'message':str(exc)});continue
        for case in cases:
            start=time.monotonic();ok,message=run_case(command,case,float(manifest.get('time_limit_seconds',2)),manifest.get('checker','tokens'))
            results.append({'problem':str(problem.relative_to(ROOT)),'lang':lang,'case':case.name,'seconds':round(time.monotonic()-start,3),'ok':ok,'message':message[:2500]})
    return results


def main() -> int:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--through',type=int,default=42)
    parser.add_argument('--from-section',type=int,default=1)
    parser.add_argument('--lang',choices=['cpp','py','both'],default='both')
    parser.add_argument('--workers',type=int,default=1,help='use 1 for reliable wall-clock timing')
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args();languages=['cpp','py'] if args.lang=='both' else [args.lang];problems=[]
    for section in sorted((ROOT/'sections').iterdir()):
        if section.is_dir() and section.name.split('_')[0].isdigit() and args.from_section<=int(section.name.split('_')[0])<=args.through:
            problems.extend(path.parent for path in sorted((section/'problems').glob('*/manifest.json')))
    rows=[]
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        for i,result in enumerate(pool.map(lambda p:check(p,languages),problems),1):
            rows.extend(result)
            failures=[r for r in result if not r['ok']]
            if failures:
                for r in failures:print('FAIL',r['problem'],r['lang'],r.get('case',''),r['message'],flush=True)
            elif i%5==0 or i==len(problems):print(f'{i}/{len(problems)} problems checked',flush=True)
            args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(rows,indent=2)+'\n')
    failures=sum(not r['ok'] for r in rows)
    print(f'{len(problems)} problems; {len(rows)} executions; {failures} failures.',flush=True)
    return bool(failures)


if __name__=='__main__':raise SystemExit(main())
