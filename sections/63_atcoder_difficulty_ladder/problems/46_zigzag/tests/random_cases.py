from __future__ import annotations
import argparse, random
from pathlib import Path
def brute(intervals):
    best=0
    for mask in range(1<<len(intervals)):
        chosen=sorted((intervals[i] for i in range(len(intervals)) if mask>>i&1))
        if all(chosen[i][1]<=chosen[i+1][0] for i in range(len(chosen)-1)): best=max(best,len(chosen))
    return best
def main():
    p=argparse.ArgumentParser();p.add_argument('--count',type=int,required=True);p.add_argument('--seed',type=int,required=True);p.add_argument('--out-dir',type=Path,required=True);a=p.parse_args();a.out_dir.mkdir(parents=True,exist_ok=True);rng=random.Random(a.seed)
    for c in range(a.count):
        intervals=[(2*i,2*i+1) for i in range(200000)] if c==0 else [tuple(sorted(rng.sample(range(31),2))) for _ in range(rng.randint(1,16))]
        answer=len(intervals) if c==0 else brute(intervals);z=a.out_dir/f'case{c:03d}';z.with_suffix('.in').write_text(str(len(intervals))+'\n'+'\n'.join(f'{x} {y}' for x,y in intervals)+'\n');z.with_suffix('.out').write_text(f'{answer}\n')
if __name__=='__main__':main()
