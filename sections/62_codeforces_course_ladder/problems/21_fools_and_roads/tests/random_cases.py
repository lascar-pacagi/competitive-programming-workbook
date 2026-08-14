from __future__ import annotations
import argparse, heapq, random
from pathlib import Path
def oracle(n,e):
 if n==1:return 0
 g=[[] for _ in range(n+1)]
 for u,v,w in e:g[u].append((v,w));g[v].append((u,w))
 inf=10**30;d=[inf]*(n+1);d[1]=0;q=[(0,1)]
 while q:
  x,u=heapq.heappop(q)
  if x!=d[u]:continue
  for v,w in g[u]:
   y=max(x,w)
   if y<d[v]:d[v]=y;heapq.heappush(q,(y,v))
 return -1 if d[n]==inf else d[n]
def main():
 p=argparse.ArgumentParser();p.add_argument('--count',type=int,required=True);p.add_argument('--seed',type=int,required=True);p.add_argument('--out-dir',type=Path,required=True);a=p.parse_args();a.out_dir.mkdir(parents=True,exist_ok=True);r=random.Random(a.seed)
 for c in range(a.count):
  if c==0:
   n=100001;e=[(i,i+1,7) for i in range(1,n)]+[(i,i+2,100) for i in range(1,n-1)]+[(1,n,100)];ans=7
  else:
   n=r.randint(1,35);e=[]
   for _ in range(r.randint(0,100)):
    if n==1:break
    u,v=r.sample(range(1,n+1),2);e.append((u,v,r.randint(0,30)))
   ans=oracle(n,e)
  z=a.out_dir/f'case{c:03d}';z.with_suffix('.in').write_text('\n'.join([f'{n} {len(e)}']+[f'{u} {v} {w}' for u,v,w in e])+'\n');z.with_suffix('.out').write_text(f'{ans}\n')
if __name__=='__main__':main()
