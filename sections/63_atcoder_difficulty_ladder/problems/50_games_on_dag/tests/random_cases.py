from __future__ import annotations
import argparse,random
from pathlib import Path
def brute(n,e):
 d=[[10**12]*n for _ in range(2)];d[0][0]=0
 for _ in range(2*n):
  for a,b,w in e:
   for u in range(2):
    d[u][b]=min(d[u][b],d[u][a]+w);d[u][a]=min(d[u][a],d[u][b]+w)
   d[1][b]=min(d[1][b],d[0][a]);d[1][a]=min(d[1][a],d[0][b])
 return min(d[0][-1],d[1][-1])
def main():
 p=argparse.ArgumentParser();p.add_argument('--count',type=int,required=True);p.add_argument('--seed',type=int,required=True);p.add_argument('--out-dir',type=Path,required=True);a=p.parse_args();a.out_dir.mkdir(parents=True,exist_ok=True);r=random.Random(a.seed)
 for c in range(a.count):
  if c==0:n=200000;e=[(i,i+1,1) for i in range(1,n)];ans=n-2
  else:
   n=r.randint(2,8);e=[(i,r.randint(1,i-1),r.randint(1,20)) for i in range(2,n+1)];e += [(r.randint(1,n),r.randint(1,n),r.randint(1,20)) for _ in range(r.randint(0,5))];e=[x for x in e if x[0]!=x[1]];ans=brute(n,[(x-1,y-1,w) for x,y,w in e])
  z=a.out_dir/f'case{c:03d}';z.with_suffix('.in').write_text(f'{n} {len(e)}\n'+'\n'.join(f'{x} {y} {w}' for x,y,w in e)+'\n');z.with_suffix('.out').write_text(f'{ans}\n')
if __name__=='__main__':main()
