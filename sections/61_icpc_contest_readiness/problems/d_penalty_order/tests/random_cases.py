from __future__ import annotations
import argparse, itertools, random
from pathlib import Path
def brute(values):
    best=10**30
    for order in itertools.permutations(values):
        elapsed=score=0
        for value in order: elapsed+=value;score+=elapsed
        best=min(best,score)
    return best
def main():
    p=argparse.ArgumentParser();p.add_argument('--count',type=int,required=True);p.add_argument('--seed',type=int,required=True);p.add_argument('--out-dir',type=Path,required=True);a=p.parse_args();a.out_dir.mkdir(parents=True,exist_ok=True);rng=random.Random(a.seed)
    for c in range(a.count):
        values=list(range(1,200001)) if c==0 else [rng.randint(1,30) for _ in range(rng.randint(1,8))]
        answer=sum((len(values)-i)*x for i,x in enumerate(values)) if c==0 else brute(values);z=a.out_dir/f'case{c:03d}';z.with_suffix('.in').write_text(str(len(values))+'\n'+' '.join(map(str,values))+'\n');z.with_suffix('.out').write_text(f'{answer}\n')
if __name__=='__main__':main()
