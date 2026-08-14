from __future__ import annotations
import argparse, functools, heapq, random
from pathlib import Path
def oracle(values):
 @functools.lru_cache(None)
 def solve(state):
  if len(state)==1:return 0
  best=10**30
  for i in range(len(state)):
   for j in range(i+1,len(state)):
    nxt=list(state);b=nxt.pop(j);a=nxt.pop(i);nxt.append(a+b);best=min(best,a+b+solve(tuple(sorted(nxt))))
  return best
 return solve(tuple(sorted(values)))
def write(d,k,a,ans):
 z=d/f'case{k:03d}';z.with_suffix('.in').write_text(str(len(a))+'\n'+' '.join(map(str,a))+'\n');z.with_suffix('.out').write_text(str(ans)+'\n')
def main():
 p=argparse.ArgumentParser();p.add_argument('--count',type=int,required=True);p.add_argument('--seed',type=int,required=True);p.add_argument('--out-dir',type=Path,required=True);x=p.parse_args();x.out_dir.mkdir(parents=True,exist_ok=True);r=random.Random(x.seed)
 for k in range(x.count):
  if k==0:
   a=[1]*200000;q=a[:];heapq.heapify(q);ans=0
   while len(q)>1:
    s=heapq.heappop(q)+heapq.heappop(q);ans+=s;heapq.heappush(q,s)
  else:a=[r.randint(1,30) for _ in range(r.randint(1,7))];ans=oracle(a)
  write(x.out_dir,k,a,ans)
if __name__=='__main__':main()
