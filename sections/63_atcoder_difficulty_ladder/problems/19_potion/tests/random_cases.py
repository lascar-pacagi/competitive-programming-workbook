from __future__ import annotations
import argparse, random
from pathlib import Path
MOD=1_000_000_007
def slow(a,b,c):
 exponent=b**c;result=1
 for _ in range(exponent):result=result*a%MOD
 return result
def main():
 p=argparse.ArgumentParser();p.add_argument('--count',type=int,required=True);p.add_argument('--seed',type=int,required=True);p.add_argument('--out-dir',type=Path,required=True);x=p.parse_args();x.out_dir.mkdir(parents=True,exist_ok=True);r=random.Random(x.seed)
 for k in range(x.count):
  if k==0:q=200000;rows=[(2,1,10**18)]*q;ans=['2']*q
  else:q=r.randint(1,20);rows=[(r.randint(1,30),r.randint(1,5),r.randint(1,5)) for _ in range(q)];ans=[str(slow(*z)) for z in rows]
  z=x.out_dir/f'case{k:03d}';z.with_suffix('.in').write_text(str(q)+'\n'+'\n'.join(' '.join(map(str,row)) for row in rows)+'\n');z.with_suffix('.out').write_text('\n'.join(ans)+'\n')
if __name__=='__main__':main()
