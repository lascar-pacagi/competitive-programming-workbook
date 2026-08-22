"""Independent tiny oracles for Sections 79--81."""
from __future__ import annotations
import argparse,itertools,random
from pathlib import Path

def reach(n,edges,start,blocked=-1,skip=-1,directed=True):
 g=[[] for _ in range(n)]
 for i,(u,v) in enumerate(edges):
  if i==skip or u==blocked or v==blocked:continue
  g[u].append(v)
  if not directed:g[v].append(u)
 seen={start} if start!=blocked else set();st=list(seen)
 while st:
  u=st.pop()
  for v in g[u]:
   if v not in seen:seen.add(v);st.append(v)
 return seen

def comps(n,edges):
 remaining=set(range(n));parts=[]
 while remaining:
  s=next(iter(remaining));a=reach(n,edges,s);b=reach(n,[(v,u) for u,v in edges],s);part=a&b;parts.append(part);remaining-=part
 return parts

def undirected_connected(n,edges,blocked=-1,skip=-1):
 starts=[v for v in range(n) if v!=blocked]
 return not starts or len(reach(n,edges,starts[0],blocked,skip,False))==len(starts)

def random_directed(rng,n):return [(u,v) for u in range(n) for v in range(n) if rng.random()<.22]
def random_connected(rng,n):
 e=[(v,rng.randrange(v)) for v in range(1,n)]
 for u in range(n):
  for v in range(u+1,n):
   if (u,v) not in e and (v,u) not in e and rng.random()<.22:e.append((u,v))
 return e
def fmt(n,e,extra=""):return f"{n} {len(e)}{extra}\n"+"".join(f"{u+1} {v+1}\n" for u,v in e)

def case(kind,rng):
 n=rng.randint(2,8)
 if kind in {"condensation","sink_size","strong_repairs"}:
  e=random_directed(rng,n);p=comps(n,e);at={v:i for i,c in enumerate(p) for v in c};ins=[0]*len(p);outs=[0]*len(p)
  for u,v in e:
   if at[u]!=at[v]:outs[at[u]]=ins[at[v]]=1
  if kind=="condensation":ans=f"{len(p)} {ins.count(0)} {outs.count(0)}\n"
  elif kind=="sink_size":
   z=[i for i,x in enumerate(outs) if not x];ans=f"{len(p[z[0]]) if len(z)==1 else 0}\n"
  else:ans=f"{0 if len(p)==1 else max(ins.count(0),outs.count(0))}\n"
  return fmt(n,e),ans
 if kind=="twosat":
  m=rng.randint(1,12);clauses=[(rng.choice((-1,1))*rng.randint(1,n),rng.choice((-1,1))*rng.randint(1,n)) for _ in range(m)]
  ok=any(all(((mask>>(abs(a)-1)&1)==(a>0)) or ((mask>>(abs(b)-1)&1)==(b>0)) for a,b in clauses) for mask in range(1<<n))
  return f"{n} {m}\n"+"".join(f"{a} {b}\n" for a,b in clauses),("YES\n" if ok else "NO\n")
 if kind in {"dominators","dominator_subtree"}:
  e=[(v-1,v) for v in range(1,n)]+random_directed(rng,n);e=list(dict.fromkeys(e));dom=[]
  for target in range(n):dom.append({v for v in range(n) if v==target or target not in reach(n,e,0,v)})
  if kind=="dominators":a=sorted(v+1 for v in dom[n-1] if v not in (0,n-1));return fmt(n,e),f"{len(a)}\n"+" ".join(map(str,a))+"\n"
  qs=list(range(n));return fmt(n,e,f" {n}")+"".join(f"{v+1}\n" for v in qs),"".join(f"{sum(v in d for d in dom)}\n" for v in qs)
 if kind in {"bridge_distance","articulation_damage","mandatory","bridge_completion","robbins","failed_vertex"}:
  e=random_connected(rng,n);bridges=[not undirected_connected(n,e,skip=i) for i in range(len(e))]
  if kind=="articulation_damage":
   vals=[]
   for c in range(n):
    val=0
    for u in range(n):
     for v in range(u+1,n):
      if c not in (u,v) and v not in reach(n,e,u,c,directed=False):val+=1
    vals.append(val)
   return fmt(n,e)," ".join(map(str,vals))+"\n"
  if kind=="bridge_completion":
   # Contract nonbridges and count leaves.
   cid=[-1]*n;c=0;g=[[] for _ in range(n)]
   for i,(u,v) in enumerate(e):
    if not bridges[i]:g[u].append(v);g[v].append(u)
   for s in range(n):
    if cid[s]>=0:continue
    cid[s]=c;st=[s]
    while st:
     u=st.pop()
     for v in g[u]:
      if cid[v]<0:cid[v]=c;st.append(v)
    c+=1
   deg=[0]*c
   for i,(u,v) in enumerate(e):
    if bridges[i]:deg[cid[u]]+=1;deg[cid[v]]+=1
   return fmt(n,e),f"{(sum(x==1 for x in deg)+1)//2}\n"
  if kind=="robbins":return fmt(n,e),("NO\n" if any(bridges) else "YES\n")
  q=12;queries=[tuple(rng.randrange(n) for _ in range(3 if kind in {"mandatory","failed_vertex"} else 2)) for _ in range(q)]
  if kind=="bridge_distance":
   out=[]
   for u,v in queries:out.append(sum(bridges[i] and ((u in reach(n,e,0,skip=i,directed=False)) != (v in reach(n,e,0,skip=i,directed=False))) for i in range(len(e))))
   return fmt(n,e,f" {q}")+"".join(f"{u+1} {v+1}\n" for u,v in queries),"".join(f"{x}\n" for x in out)
  out=[]
  for u,v,c in queries:
   mandatory=c in (u,v) or v not in reach(n,e,u,c,directed=False)
   out.append(mandatory if kind=="mandatory" else not mandatory)
  return fmt(n,e,f" {q}")+"".join(f"{u+1} {v+1} {c+1}\n" for u,v,c in queries),"".join("YES\n" if x else "NO\n" for x in out)
 # Euler cases use tiny exhaustive permutation oracle.
 if kind in {"euler","word_chain"}:
  if kind=="euler":
   m=rng.randint(0,7);e=[(rng.randrange(n),rng.randrange(n)) for _ in range(m)];valid=[]
   for p in itertools.permutations(range(m)):
    if (not p and not m) or (e[p[0]][0]==0 and all(e[p[i]][1]==e[p[i+1]][0] for i in range(m-1))):valid.append([0]+[e[i][1] for i in p])
   ans="IMPOSSIBLE\n" if not valid else " ".join(str(x+1) for x in min(valid))+"\n";return fmt(n,e),ans
  m=rng.randint(1,7);words=[]
  for i in range(m):words.append(chr(97+rng.randrange(3))+chr(100+i)+chr(97+rng.randrange(3)))
  valid=[p for p in itertools.permutations(words) if all(p[i][-1]==p[i+1][0] for i in range(m-1))];ans="IMPOSSIBLE\n" if not valid else " ".join(min(valid))+"\n";return f"{m}\n"+"\n".join(words)+"\n",ans
 raise ValueError(kind)

def main():
 p=argparse.ArgumentParser();p.add_argument("kind");p.add_argument("--count",type=int,default=20);p.add_argument("--seed",type=int,default=1);p.add_argument("--out-dir",type=Path,required=True);a=p.parse_args();a.out_dir.mkdir(parents=True,exist_ok=True);r=random.Random(a.seed)
 for i in range(a.count):x,y=case(a.kind,r);s=a.out_dir/f"case{i:03d}";s.with_suffix(".in").write_text(x);s.with_suffix(".out").write_text(y)
if __name__=="__main__":main()
