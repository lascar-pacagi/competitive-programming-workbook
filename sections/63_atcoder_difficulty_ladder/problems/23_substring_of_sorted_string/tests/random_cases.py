from __future__ import annotations
import argparse,itertools,random
from pathlib import Path
M=1_000_000_007
def brute(n):return sum(all(p[i]!=i for i in range(n)) for p in itertools.permutations(range(n)))
def scale(n):
 a,b=1,0
 for i in range(2,n+1):a,b=b,(i-1)*(a+b)%M
 return b
def main():
 p=argparse.ArgumentParser();p.add_argument('--count',type=int,required=True);p.add_argument('--seed',type=int,required=True);p.add_argument('--out-dir',type=Path,required=True);x=p.parse_args();x.out_dir.mkdir(parents=True,exist_ok=True);r=random.Random(x.seed)
 for k in range(x.count):
  n=1000000 if k==0 else r.randint(1,8);ans=scale(n) if k==0 else brute(n);z=x.out_dir/f'case{k:03d}';z.with_suffix('.in').write_text(f'{n}\n');z.with_suffix('.out').write_text(f'{ans}\n')
if __name__=='__main__':main()
