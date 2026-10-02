"""Inventory actual default-size test inputs for a range of course sections.

Large byte/numeric sizes are evidence of scale, not proof of an adversarial
workload. Small bounded/exponential problems need individual constraint review.
The inventory deliberately does not label small cases as verified TLE coverage.
"""
from __future__ import annotations
import argparse
from concurrent.futures import ThreadPoolExecutor
import json
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT=Path(__file__).resolve().parents[1]


def measure(path: Path, kind: str) -> dict:
    with path.open() as stream: first=stream.readline().strip()
    return {'kind':kind,'name':path.name,'bytes':path.stat().st_size,'first_line':first[:100]}


def inspect(problem: Path, count: int, seed: int) -> dict:
    rows=[measure(p,'fixed') for p in sorted((problem/'tests').glob('*.in'))]
    errors=[]
    for filename,kind in [('random_cases.py','random'),('stress_cases.py','stress')]:
        generator=problem/'tests'/filename
        if not generator.exists():continue
        with tempfile.TemporaryDirectory(prefix='cp-performance-audit-') as directory:
            cmd=[sys.executable,str(generator),'--out-dir',directory]
            if kind=='random':cmd+=['--count',str(count),'--seed',str(seed)]
            try:
                subprocess.run(cmd,cwd=ROOT,check=True,capture_output=True,timeout=120)
                cases=sorted(Path(directory).glob('*.in'))
                if not cases:errors.append(f'{kind}: no generated inputs')
                for path in cases:
                    if not path.with_suffix('.out').exists():errors.append(f'{kind}: missing answer for {path.name}')
                    rows.append(measure(path,kind))
            except (subprocess.CalledProcessError,subprocess.TimeoutExpired) as exc:
                errors.append(f'{kind}: {str(exc)[:200]}')
    biggest=max(rows,key=lambda x:x['bytes'],default=None)
    # A million-iteration scalar problem can have a tiny input; retain first
    # lines for manual review instead of inventing a universal size criterion.
    return {'problem':str(problem.relative_to(ROOT)),'cases':len(rows),
            'largest':biggest,'large_input_observed':any(r['bytes']>=100_000 for r in rows),
            'dedicated_stress':(problem/'tests/stress_cases.py').exists(),
            'errors':errors}


def write_report(result: dict, path: Path) -> None:
    rows=result['problems'];large=sum(r['large_input_observed'] for r in rows)
    errors=sum(bool(r['errors']) for r in rows)
    dedicated=sum(r['dedicated_stress'] for r in rows)
    validation=result.get('validation',[])
    validated={r['problem'] for r in validation}
    failures=sum(not r['ok'] for r in validation)
    lines=[f"# Performance test audit: sections 1–{result['through']}", "",
           f"Examined {len(rows)} local problems using fixed tests, {result['random_count']} random cases "
           f"per generator (seed {result['seed']}), and dedicated performance generators.", "",
           f"Dedicated performance generators: {dedicated}/{len(rows)}. Generator failures: {errors}.", "",
           "The normal judge runs these tests even with `--random-count 0`, under each "
           "manifest's existing per-case deadline. Sections 1–41 use the explicit profile "
           "registry in `tools/course_performance_profiles.json`; section 42 uses its own "
           "construction generators. Existing large cases are preserved as dedicated "
           "tests, independent of the requested random count.", "",
           "## Workload review", "",
           "The added cases exercise constraint-scale arrays, query streams, long trees, "
           "dense graphs, grids, sieve bounds, DP dimensions, and bounded exponential "
           "searches. Expected answers come from construction identities or existing "
           "generator oracles. Small randomized cases remain useful for correctness.", "",
           f"{large} problems produced an input of at least 100 KB; {len(rows)-large} did not. "
           "File size is only an inventory aid: a scalar limit, cubic DP, or subset search "
           "can require substantial work from a small input. Dedicated cases were reviewed "
           "against the individual constraints rather than this byte threshold.", "",
           "Section 42 H includes three n=q=200000 workloads: growing paths, reversed "
           "unions, and disconnected paths. BFS-per-query implementations in both "
           "C++ and Python exceeded the existing 3-second deadline. A C++ linear "
           "range-sum implementation passed section 36 A’s sample but exceeded its "
           "2-second deadline on the dedicated varying-range workload.", "",
           "## Reference validation", ""]
    if validation:
        lines += [f"Checked {len(validated)} problems in C++ and Python: {len(validation)} "
                  f"fixed/performance executions, {failures} failures.", ""]
    lines += ["The new workloads exposed two Python reference bottlenecks. Section 20 C "
              "(Warp Maze) now uses a padded flat grid, rejects stale 0-1 BFS entries, "
              "and stops when the goal is settled. Its tests include an unreachable "
              "goal that requires exploring a million-cell region. Section 35 O "
              "(GCD Sum) now preprocesses answers using smallest prime factors and "
              "the prime-power recurrence, replacing divisor scans per query. Its "
              "test uses 200000 distinct large queries. Both editorials were updated; "
              "no time limits or course prerequisites were changed.", "",
              "Reference validation used three workers for the full course; final "
              "revised cases were rechecked sequentially. For reproducible local timing, "
              "use one worker. These checks establish reference acceptance on this "
              "machine, not a machine-independent guarantee that every slower approach "
              "will be rejected.", "",
              "## Reproduce", "", "```bash",
              f"python3 tools/check_performance_tests.py --through {result['through']} "
              "--workers 1 --output /tmp/performance-reference-results.json",
              f"python3 tools/audit_performance_tests.py --through {result['through']} "
              f"--count {result['random_count']} --seed {result['seed']} "
              "--output /tmp/performance-audit.json --report PERFORMANCE_AUDIT_01_42.md "
              "--validation /tmp/performance-reference-results.json",
              "```", "",
              "## Inventory", "",
              "Every row records actual generated/fixed input size and the presence "
              "of a dedicated generator. Input names refer to temporary generated "
              "files when the kind is random or stress.", "",
              "| Problem | Cases | Largest input (bytes) | First line | Evidence |",
              "|---|---:|---:|---|---|"]
    for row in rows:
        largest=row['largest'];problem=row['problem']
        evidence='dedicated stress' if row['dedicated_stress'] else ('large input observed' if row['large_input_observed'] else 'review limits')
        if row['errors']:evidence='GENERATOR ERROR'
        header=largest['first_line'].replace('|','\\|') if largest else ''
        lines.append(f"| [{problem.split('/')[1][:2]} {problem.split('/')[-1]}]({problem}/README.md) "
                     f"| {row['cases']} | {largest['bytes'] if largest else 0} | `{header}` | {evidence} |")
    path.parent.mkdir(parents=True,exist_ok=True);path.write_text('\n'.join(lines)+'\n')


def main() -> None:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--through',type=int,default=42)
    parser.add_argument('--count',type=int,default=25)
    parser.add_argument('--seed',type=int,default=20261001)
    parser.add_argument('--workers',type=int,default=4)
    parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--report',type=Path)
    parser.add_argument('--validation',type=Path,help='JSON from check_performance_tests.py')
    args=parser.parse_args();problems=[]
    for section in sorted((ROOT/'sections').iterdir()):
        if not section.is_dir() or not section.name.split('_')[0].isdigit():continue
        if 1<=int(section.name.split('_')[0])<=args.through:
            problems.extend(sorted((section/'problems').glob('*/manifest.json')))
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        rows=list(pool.map(lambda path:inspect(path.parent,args.count,args.seed),problems))
    result={'through':args.through,'random_count':args.count,'seed':args.seed,
            'large_input_threshold_bytes':100_000,'problems':rows}
    if args.validation:result['validation']=json.loads(args.validation.read_text())
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    if args.report:write_report(result,args.report)
    print(f"Audited {len(rows)} problems; {sum(r['large_input_observed'] for r in rows)} have inputs >=100KB; "
          f"{sum(bool(r['errors']) for r in rows)} generator failures.")


if __name__=='__main__':main()
