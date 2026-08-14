from __future__ import annotations
import argparse, random
from functools import lru_cache
from pathlib import Path
def brute(n,cuts):
    @lru_cache(maxsize=None)
    def best(left):
        if left==0:return 0
        answer=-10**9
        for cut in cuts:
            if cut<=left:answer=max(answer,best(left-cut)+1)
        return answer
    answer=best(n);return answer if answer>=0 else -1
def main():
    p=argparse.ArgumentParser();p.add_argument('--count',type=int,required=True);p.add_argument('--seed',type=int,required=True);p.add_argument('--out-dir',type=Path,required=True);a=p.parse_args();a.out_dir.mkdir(parents=True,exist_ok=True);rng=random.Random(a.seed)
    for c in range(a.count):
        n,cuts=(200000,[1,77777,199999]) if c==0 else (rng.randint(1,45),[rng.randint(1,15) for _ in range(3)])
        answer=n if c==0 else brute(n,tuple(cuts));z=a.out_dir/f'case{c:03d}';z.with_suffix('.in').write_text(f'{n} {cuts[0]} {cuts[1]} {cuts[2]}\n');z.with_suffix('.out').write_text(f'{answer}\n')
if __name__=='__main__':main()
