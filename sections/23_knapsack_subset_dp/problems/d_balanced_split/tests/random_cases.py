from __future__ import annotations
import argparse, random
from pathlib import Path
def oracle(a):
 total=sum(a);best=total
 for mask in range(1<<len(a)):
  s=sum(x for i,x in enumerate(a) if mask>>i&1);best=min(best,abs(total-2*s))
 return best
def main():
 p=argparse.ArgumentParser();p.add_argument('--count',type=int,required=True);p.add_argument('--seed',type=int,required=True);p.add_argument('--out-dir',type=Path,required=True);x=p.parse_args();x.out_dir.mkdir(parents=True,exist_ok=True);r=random.Random(x.seed)
 for c in range(x.count):
  if c==0:a=[1000]*100
  else:a=[r.randint(1,50) for _ in range(r.randint(1,18))]
  ans=0 if c==0 else oracle(a);z=x.out_dir/f'case{c:03d}';z.with_suffix('.in').write_text(f'{len(a)}\n'+' '.join(map(str,a))+'\n');z.with_suffix('.out').write_text(f'{ans}\n')
if __name__=='__main__':main()
