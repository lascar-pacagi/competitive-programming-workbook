from __future__ import annotations
import argparse,random
from pathlib import Path
def brute(n,e,s):
 out=[]
 for start in range(1,n+1):
  q=[start];d={start:0}
  for u in q:
   for a,b in e:
    v=b if a==u else a if b==u else 0
    if v and v not in d:d[v]=d[u]+1;q.append(v)
  out.append(min((d[x] for x in s if x in d),default=-1))
 return out
def main():
 p=argparse.ArgumentParser();p.add_argument('--count',type=int,required=True);p.add_argument('--seed',type=int,required=True);p.add_argument('--out-dir',type=Path,required=True);a=p.parse_args();a.out_dir.mkdir(parents=True,exist_ok=True);r=random.Random(a.seed)
 for c in range(a.count):
  if c==0:n=200000;e=[(i,i+1) for i in range(1,n)];s=[1];ans=list(range(n))
  else:
   n=r.randint(1,30);e=[]
   for u in range(1,n+1):
    for v in range(u+1,n+1):
     if r.random()<.1:e.append((u,v))
   s=r.sample(range(1,n+1),r.randint(1,n));ans=brute(n,e,s)
  lines=[f'{n} {len(e)} {len(s)}']+[f'{u} {v}' for u,v in e]+[' '.join(map(str,s))];z=a.out_dir/f'case{c:03d}';z.with_suffix('.in').write_text('\n'.join(lines)+'\n');z.with_suffix('.out').write_text(' '.join(map(str,ans))+'\n')
if __name__=='__main__':main()
