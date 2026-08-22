import argparse, random
from pathlib import Path
def case(r):
 n=r.randint(1,9); m=r.randint(0,18); q=r.randint(1,20); edges=[]; bal=[0]*n
 # Zero is always a feasible circulation; bounds sometimes pin an edge at zero.
 for _ in range(m):
  u=r.randrange(n);v=r.randrange(n);h=r.randint(0,2);edges.append((u,v,0,h,0))
 g=[[] for _ in range(n)]
 for u,v,l,h,f in edges:
  if f<h:g[u].append(v)
  if f>l:g[v].append(u)
 ans=[]; queries=[]
 for _ in range(q):
  u=r.randrange(n);v=r.randrange(n);queries.append((u,v)); seen={v};st=[v]
  while st:
   x=st.pop()
   for y in g[x]:
    if y not in seen:seen.add(y);st.append(y)
  ans.append("YES" if u in seen else "NO")
 text=f"{n} {m} {q}\n"+''.join(f"{u+1} {v+1} {l} {h} {f}\n" for u,v,l,h,f in edges)+''.join(f"{u+1} {v+1}\n" for u,v in queries)
 return text,'\n'.join(ans)+'\n'
def main():
 p=argparse.ArgumentParser();p.add_argument('--count',type=int,default=25);p.add_argument('--seed',type=int,default=1);p.add_argument('--out-dir',type=Path,required=True);a=p.parse_args();a.out_dir.mkdir(parents=True,exist_ok=True);r=random.Random(a.seed)
 for i in range(a.count):
  x,y=case(r);s=a.out_dir/f"case{i:03d}";s.with_suffix('.in').write_text(x);s.with_suffix('.out').write_text(y)
if __name__=='__main__':main()
