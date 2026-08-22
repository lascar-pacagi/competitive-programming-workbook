"""Independent tiny exhaustive oracles for Sections 85--87."""
import argparse,itertools,random
from pathlib import Path
def matching(n,edges):
 adj=[0]*n
 for u,v in edges:adj[u]|=1<<v;adj[v]|=1<<u
 dp={0:0}
 for mask in range(1<<n):
  if mask not in dp:continue
  free=((1<<n)-1)^mask
  if not free:continue
  bit=free&-free;u=bit.bit_length()-1;dp[mask|bit]=max(dp.get(mask|bit,0),dp[mask])
  z=adj[u]&free
  while z:b=z&-z;dp[mask|bit|b]=max(dp.get(mask|bit|b,0),dp[mask]+1);z-=b
 return max(dp.values())
def forest(n,edges,chosen):
 p=list(range(n))
 def f(x):
  while p[x]!=x:x=p[x]
  return x
 for i in chosen:
  a,b=map(f,edges[i])
  if a==b:return False
  p[a]=b
 return True
def mincut(n,edges,s,t):
 ans=10**9
 for mask in range(1<<n):
  if not(mask>>s&1) or mask>>t&1:continue
  ans=min(ans,sum(c for u,v,c in edges if ((mask>>u)&1)!=((mask>>v)&1)))
 return ans
def arb(n,root,edges):
 incoming=[[i for i,(u,x,w) in enumerate(edges) if x==v and u!=v] for v in range(n)];vertices=[v for v in range(n) if v!=root]
 if any(not incoming[v] for v in vertices):return None
 ans=None
 for choice in itertools.product(*(incoming[v] for v in vertices)):
  g=[[] for _ in range(n)];cost=0
  for i in choice:u,v,w=edges[i];g[u].append(v);cost+=w
  seen={root};q=[root]
  for u in q:
   for v in g[u]:
    if v not in seen:seen.add(v);q.append(v)
  if len(seen)==n:ans=cost if ans is None else min(ans,cost)
 return ans
def case(kind,r):
 n=r.randint(2,7)
 if kind in {'assignment','bottleneck'}:
  a=[[r.randint(-5,20) for _ in range(n)] for _ in range(n)];vals=[sum(a[i][p[i]] for i in range(n)) for p in itertools.permutations(range(n))] if kind=='assignment' else [max(a[i][p[i]] for i in range(n)) for p in itertools.permutations(range(n))];return f'{n}\n'+'\n'.join(' '.join(map(str,row)) for row in a)+'\n',f'{min(vals)}\n'
 if kind=='profit_assignment':
  m=r.randint(n,n+2);a=[[(-1 if r.random()<.25 else r.randint(0,20)) for _ in range(m)] for _ in range(n)];vals=[sum(a[i][p[i]] for i in range(n)) for p in itertools.permutations(range(m),n) if all(a[i][p[i]]>=0 for i in range(n))];ans='IMPOSSIBLE' if not vals else str(max(vals));return f'{n} {m}\n'+'\n'.join(' '.join(map(str,row)) for row in a)+'\n',ans+'\n'
 if kind in {'blossom','roommates'}:
  e=[(u,v) for u in range(n) for v in range(u+1,n) if r.random()<.4];z=matching(n,e);ans=z if kind=='blossom' else n-2*z;return f'{n} {len(e)}\n'+''.join(f'{u+1} {v+1}\n' for u,v in e),f'{ans}\n'
 if kind=='compat_pairing':
  a=[r.randint(0,15) for _ in range(n)];allowed=set(r.sample(range(1,10),r.randint(1,4)));e=[(i,j) for i in range(n) for j in range(i) if abs(a[i]-a[j]) in allowed];return f'{n} {len(allowed)}\n'+' '.join(map(str,a))+'\n'+' '.join(map(str,allowed))+'\n',f'{matching(n,e)}\n'
 if kind in {'gomory_queries','cut_pairs'}:
  # A random tree guarantees connectivity; extra parallel edges are allowed.
  e=[(v,r.randrange(v),r.randint(1,8)) for v in range(1,n)]+[(r.randrange(n),r.randrange(n),r.randint(1,8)) for _ in range(r.randint(0,5))];e=[x for x in e if x[0]!=x[1]];values={(i,j):mincut(n,e,i,j) for i in range(n) for j in range(i)}
  if kind=='gomory_queries':qs=[tuple(r.sample(range(n),2)) for _ in range(15)];return f'{n} {len(e)} {len(qs)}\n'+''.join(f'{u+1} {v+1} {c}\n' for u,v,c in e)+''.join(f'{u+1} {v+1}\n' for u,v in qs),''.join(f'{values[max(u,v),min(u,v)]}\n' for u,v in qs)
  qs=[r.randint(0,20) for _ in range(15)];return f'{n} {len(e)} {len(qs)}\n'+''.join(f'{u+1} {v+1} {c}\n' for u,v,c in e)+''.join(f'{x}\n' for x in qs),''.join(f'{sum(v<=x for v in values.values())}\n' for x in qs)
 if kind in {'rainbow','rainbow_tree'}:
  m=r.randint(1,11);e=[tuple(r.sample(range(n),2)) for _ in range(m)];colors=[r.randrange(5) for _ in range(m)];best=0
  for mask in range(1<<m):
   chosen=[i for i in range(m) if mask>>i&1]
   if len({colors[i] for i in chosen})==len(chosen) and forest(n,e,chosen):best=max(best,len(chosen))
  ans=str(best) if kind=='rainbow' else ('YES' if best==n-1 else 'NO');return f'{n} {m}\n'+''.join(f'{u+1} {v+1} {colors[i]}\n' for i,(u,v) in enumerate(e)),ans+'\n'
 if kind in {'dual_forest','two_map'}:
  n2=r.randint(2,7) if kind=='dual_forest' else n;m=r.randint(1,11);a=[tuple(r.sample(range(n),2)) for _ in range(m)];b=[tuple(r.sample(range(n2),2)) for _ in range(m)];best=0
  for mask in range(1<<m):
   chosen=[i for i in range(m) if mask>>i&1]
   if forest(n,a,chosen) and forest(n2,b,chosen):best=max(best,len(chosen))
  head=f'{n} {n2} {m}\n' if kind=='dual_forest' else f'{n} {m}\n';ans=str(best) if kind=='dual_forest' else ('YES' if best==n-1 else 'NO');return head+''.join(f'{a[i][0]+1} {a[i][1]+1} {b[i][0]+1} {b[i][1]+1}\n' for i in range(m)),ans+'\n'
 if kind in {'arborescence','broadcast'}:
  root=r.randrange(n);m=r.randint(1,12);e=[(r.randrange(n),r.randrange(n),r.randint(-5,12)) for _ in range(m)];answer=arb(n,root,e);return f'{n} {m} {root+1}\n'+''.join(f'{u+1} {v+1} {w}\n' for u,v,w in e),('IMPOSSIBLE\n' if answer is None else f'{answer}\n')
 raise ValueError(kind)
def main():
 p=argparse.ArgumentParser();p.add_argument('kind');p.add_argument('--count',type=int,default=20);p.add_argument('--seed',type=int,default=1);p.add_argument('--out-dir',type=Path,required=True);a=p.parse_args();a.out_dir.mkdir(parents=True,exist_ok=True);r=random.Random(a.seed)
 for i in range(a.count):x,y=case(a.kind,r);s=a.out_dir/f'case{i:03d}';s.with_suffix('.in').write_text(x);s.with_suffix('.out').write_text(y)
if __name__=='__main__':main()
