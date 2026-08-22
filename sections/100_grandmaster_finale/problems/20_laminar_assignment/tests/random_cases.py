import argparse,itertools,random
from pathlib import Path
def case(r):
 n=r.randint(1,9);p=[-1]+[r.randrange(v) for v in range(1,n)];kids=[[] for _ in range(n)]
 for v in range(1,n):kids[p[v]].append(v)
 leaves=[v for v in range(n) if not kids[v]];w=r.randint(1,min(5,len(leaves)+1));desc=[]
 for v in range(n):
  st=[v];z=[]
  while st:
   x=st.pop()
   if not kids[x]:z.append(x)
   st+=kids[x]
  desc.append(z)
 offers=[]
 for _ in range(w):offers.append([(r.randrange(n),r.randint(0,12)) for _ in range(r.randint(1,4))])
 best=None
 for ass in itertools.permutations(leaves,w) if w<=len(leaves) else []:
  val=0;ok=True
  for i,x in enumerate(ass):
   z=[c for v,c in offers[i] if x in desc[v]]
   if not z:ok=False;break
   val+=min(z)
  if ok:best=val if best is None else min(best,val)
 text=f"{n} {w}\n"+(' '.join(str(x+1) for x in p[1:])+'\n' if n>1 else '\n')+''.join(str(len(o))+' '+ ' '.join(f"{v+1} {c}" for v,c in o)+'\n' for o in offers)
 return text,('IMPOSSIBLE\n' if best is None else f'{best}\n')
def main():
 p=argparse.ArgumentParser();p.add_argument('--count',type=int,default=25);p.add_argument('--seed',type=int,default=1);p.add_argument('--out-dir',type=Path,required=True);a=p.parse_args();a.out_dir.mkdir(parents=True,exist_ok=True);r=random.Random(a.seed)
 for i in range(a.count):x,y=case(r);s=a.out_dir/f"case{i:03d}";s.with_suffix('.in').write_text(x);s.with_suffix('.out').write_text(y)
if __name__=='__main__':main()
