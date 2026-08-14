from __future__ import annotations
import argparse, random
from pathlib import Path
def oracle(a,l,r):
 if l==r:return a[l]
 return max(a[l]-oracle(a,l+1,r),a[r]-oracle(a,l,r-1))
def main():
 p=argparse.ArgumentParser();p.add_argument('--count',type=int,required=True);p.add_argument('--seed',type=int,required=True);p.add_argument('--out-dir',type=Path,required=True);x=p.parse_args();x.out_dir.mkdir(parents=True,exist_ok=True);g=random.Random(x.seed)
 for c in range(x.count):
  if c==0:a=[1]*3000;ans=0
  else:a=[g.randint(-30,40) for _ in range(g.randint(1,16))];ans=oracle(a,0,len(a)-1)
  z=x.out_dir/f'case{c:03d}';z.with_suffix('.in').write_text(f'{len(a)}\n'+' '.join(map(str,a))+'\n');z.with_suffix('.out').write_text(f'{ans}\n')
if __name__=='__main__':main()
