from __future__ import annotations
import argparse, random
from pathlib import Path

def slow(parents, weights, u, v):
    seen = {}; total = 0
    x = u
    while x:
        seen[x] = total; total += weights[x]; x = parents[x]
    total = 0; x = v
    while x not in seen:
        total += weights[x]; x = parents[x]
    return total + seen[x]

def main():
    p=argparse.ArgumentParser(); p.add_argument('--count',type=int,required=True); p.add_argument('--seed',type=int,required=True); p.add_argument('--out-dir',type=Path,required=True); a=p.parse_args(); a.out_dir.mkdir(parents=True,exist_ok=True); rng=random.Random(a.seed)
    for c in range(a.count):
        if c == 0:
            n=200000; parents=[0]* (n+1); weights=[0]*(n+1)
            for i in range(2,n+1): parents[i]=i-1; weights[i]=1_000_000_000
            queries=[(n,1)]*200000; answers=[(n-1)*1_000_000_000]*200000
        else:
            n=rng.randint(1,45); parents=[0]*(n+1); weights=[0]*(n+1)
            for i in range(2,n+1): parents[i]=rng.randint(1,i-1); weights[i]=rng.randint(-30,40)
            queries=[(rng.randint(1,n),rng.randint(1,n)) for _ in range(rng.randint(1,80))]; answers=[slow(parents,weights,u,v) for u,v in queries]
        lines=[f'{n} {len(queries)}']+[f'{parents[i]} {weights[i]}' for i in range(2,n+1)]+[f'{u} {v}' for u,v in queries]
        z=a.out_dir/f'case{c:03d}'; z.with_suffix('.in').write_text('\n'.join(lines)+'\n'); z.with_suffix('.out').write_text('\n'.join(map(str,answers))+'\n')
if __name__=='__main__': main()
