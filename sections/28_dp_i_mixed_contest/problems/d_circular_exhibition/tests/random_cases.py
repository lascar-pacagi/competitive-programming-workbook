from __future__ import annotations
import argparse, random
from pathlib import Path
def oracle(a):
 best=0;n=len(a)
 if n==1:return max(0,a[0])
 for mask in range(1<<n):
  if all(not(mask>>i&1 and mask>>((i+1)%n)&1) for i in range(n)):best=max(best,sum(a[i] for i in range(n) if mask>>i&1))
 return best
def main():
 p=argparse.ArgumentParser();p.add_argument('--count',type=int,required=True);p.add_argument('--seed',type=int,required=True);p.add_argument('--out-dir',type=Path,required=True);x=p.parse_args();x.out_dir.mkdir(parents=True,exist_ok=True);g=random.Random(x.seed)
 for c in range(x.count):
  if c==0:a=[1]*200000;ans=100000
  else:a=[g.randint(-20,30) for _ in range(g.randint(1,18))];ans=oracle(a)
  z=x.out_dir/f'case{c:03d}';z.with_suffix('.in').write_text(f'{len(a)}\n'+' '.join(map(str,a))+'\n');z.with_suffix('.out').write_text(f'{ans}\n')
if __name__=='__main__':main()
