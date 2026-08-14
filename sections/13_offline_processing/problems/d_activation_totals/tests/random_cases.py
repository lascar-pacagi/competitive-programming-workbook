from __future__ import annotations
import argparse,random
from pathlib import Path
def main():
 p=argparse.ArgumentParser();p.add_argument('--count',type=int,required=True);p.add_argument('--seed',type=int,required=True);p.add_argument('--out-dir',type=Path,required=True);x=p.parse_args();x.out_dir.mkdir(parents=True,exist_ok=True);g=random.Random(x.seed)
 for c in range(x.count):
  if c==0:n=q=200000;a=[(i,1) for i in range(n)];z=list(range(n));ans=list(range(1,n+1))
  else:
   n=g.randint(1,40);q=g.randint(1,40);a=[(g.randint(-20,20),g.randint(-30,30)) for _ in range(n)];z=[g.randint(-25,25) for _ in range(q)];ans=[sum(w for v,w in a if v<=y) for y in z]
  lines=[f'{n} {q}']+[f'{v} {w}' for v,w in a]+[' '.join(map(str,z))];s=x.out_dir/f'case{c:03d}';s.with_suffix('.in').write_text('\n'.join(lines)+'\n');s.with_suffix('.out').write_text(' '.join(map(str,ans))+'\n')
if __name__=='__main__':main()
