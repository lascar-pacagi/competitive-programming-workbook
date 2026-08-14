from __future__ import annotations
import argparse,random
from pathlib import Path
def brute(a):
 lo=min(x for x,_ in a); hi=max(y for _,y in a); best=-1; when=lo
 for x in range(lo,hi+1):
  c=sum(l<=x<=r for l,r in a)
  if c>best: best,when=c,x
 return f'{best} {when}'
def main():
 p=argparse.ArgumentParser();p.add_argument('--count',type=int,required=True);p.add_argument('--seed',type=int,required=True);p.add_argument('--out-dir',type=Path,required=True);z=p.parse_args();z.out_dir.mkdir(parents=True,exist_ok=True);g=random.Random(z.seed)
 for c in range(z.count):
  if c==0: a=[(0,0) for _ in range(200000)]; lines=['1',str(len(a))]+[f'{l} {r}' for l,r in a]; out='200000 0\n'
  else:
   t=g.randint(1,8); lines=[str(t)]; ans=[]
   for _ in range(t):
    a=[]
    for _ in range(g.randint(1,25)):
     l=g.randint(-30,30);a.append((l,g.randint(l,35)))
    lines.append(str(len(a)));lines.extend(f'{l} {r}' for l,r in a);ans.append(brute(a))
   out='\n'.join(ans)+'\n'
  s=z.out_dir/f'case{c:03d}';s.with_suffix('.in').write_text('\n'.join(lines)+'\n');s.with_suffix('.out').write_text(out)
if __name__=='__main__':main()
