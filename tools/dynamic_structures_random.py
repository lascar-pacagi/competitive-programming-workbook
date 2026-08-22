"""Independent tiny oracles for Sections 82--84."""
import argparse,collections,random
from pathlib import Path
MOD=998244353
def path(n,edges,u,v):
 g=[[] for _ in range(n)]
 for a,b in edges:g[a].append(b);g[b].append(a)
 prev={u:-1};q=[u]
 for x in q:
  for y in g[x]:
   if y not in prev:prev[y]=x;q.append(y)
 if v not in prev:return None
 out=[]
 while v!=-1:out.append(v);v=prev[v]
 return out
def case(kind,r):
 n=r.randint(2,10);a=[r.randint(0,30) for _ in range(n)]
 if kind in {'kth','freq','quantile_sum'}:
  qs=[];out=[]
  for _ in range(20):
   l=r.randrange(n);rr=r.randrange(l+1,n+1);x=r.randint(1,rr-l) if kind!='freq' else r.randint(-5,35);qs.append((l+1,rr,x));s=sorted(a[l:rr]);out.append(sum(s[:x]) if kind=='quantile_sum' else (s[x-1] if kind=='kth' else sum(v<=x for v in s)))
  return f'{n} {len(qs)}\n'+' '.join(map(str,a))+'\n'+''.join(f'{l} {rr} {x}\n' for l,rr,x in qs),''.join(f'{x}\n' for x in out)
 if kind in {'cap_sum','clamp','mod_sum'}:
  ops=[];out=[]
  for _ in range(35):
   l=r.randrange(n);rr=r.randrange(l+1,n+1);pick=r.random()
   if pick<.35:ops.append(f'SUM {l+1} {rr}');out.append(sum(a[l:rr]))
   elif kind=='cap_sum':
    x=r.randint(0,30);ops.append(f'CAP {l+1} {rr} {x}');a[l:rr]=[min(v,x) for v in a[l:rr]]
   elif kind=='clamp':
    x=r.randint(0,30);op=r.choice(('LOWER','UPPER'));ops.append(f'{op} {l+1} {rr} {x}');a[l:rr]=[(max(v,x) if op=='LOWER' else min(v,x)) for v in a[l:rr]]
   elif pick<.85:
    x=r.randint(1,15);ops.append(f'MOD {l+1} {rr} {x}');a[l:rr]=[v%x for v in a[l:rr]]
   else:
    i=r.randrange(n);x=r.randint(0,30);ops.append(f'SET {i+1} {x}');a[i]=x
  # Replay from a separately generated start.
  start=[r.randint(0,30) for _ in range(n)];a=start[:];out=[]
  for op in ops:
   z=op.split();l=int(z[1])-1
   if z[0]=='SUM':out.append(sum(a[l:int(z[2])]))
   elif z[0]=='CAP':rr=int(z[2]);x=int(z[3]);a[l:rr]=[min(v,x) for v in a[l:rr]]
   elif z[0]=='LOWER':rr=int(z[2]);x=int(z[3]);a[l:rr]=[max(v,x) for v in a[l:rr]]
   elif z[0]=='UPPER':rr=int(z[2]);x=int(z[3]);a[l:rr]=[min(v,x) for v in a[l:rr]]
   elif z[0]=='MOD':rr=int(z[2]);x=int(z[3]);a[l:rr]=[v%x for v in a[l:rr]]
   else:a[l]=int(z[2])
  return f'{n} {len(ops)}\n'+' '.join(map(str,start))+'\n'+'\n'.join(ops)+'\n',''.join(f'{x}\n' for x in out)
 if kind in {'cut_paste','treap_ledger','string_hash'}:
  if kind=='cut_paste':
   seq=list(range(1,n+1));ops=[]
   for _ in range(25):
    l=r.randrange(n);rr=r.randrange(l+1,n+1);block=seq[l:rr];del seq[l:rr];p=r.randrange(len(seq)+1);seq[p:p]=block;ops.append(f'CUT {l+1} {rr} {p+1}')
   return f'{n} {len(ops)}\n'+'\n'.join(ops)+'\n',' '.join(map(str,seq))+'\n'
  if kind=='treap_ledger':
   seq=a[:];start=seq[:];ops=[];out=[]
   for _ in range(30):
    l=r.randrange(n);rr=r.randrange(l+1,n+1);op=r.choice(('ADD','REV','SUM'))
    if op=='ADD':x=r.randint(-10,10);ops.append(f'ADD {l+1} {rr} {x}');seq[l:rr]=[v+x for v in seq[l:rr]]
    elif op=='REV':ops.append(f'REV {l+1} {rr}');seq[l:rr]=reversed(seq[l:rr])
    else:ops.append(f'SUM {l+1} {rr}');out.append(sum(seq[l:rr]))
   return f'{n} {len(ops)}\n'+' '.join(map(str,start))+'\n'+'\n'.join(ops)+'\n',''.join(f'{x}\n' for x in out)
  seq=[r.choice('abc') for _ in range(n)];start=''.join(seq);ops=[];out=[]
  for _ in range(30):
   op=r.choice(('REV','SET','PAL'))
   if op=='SET':i=r.randrange(n);c=r.choice('abc');seq[i]=c;ops.append(f'SET {i+1} {c}')
   else:
    l=r.randrange(n);rr=r.randrange(l+1,n+1);ops.append(f'{op} {l+1} {rr}')
    if op=='REV':seq[l:rr]=reversed(seq[l:rr])
    else:out.append('YES' if seq[l:rr]==seq[l:rr][::-1] else 'NO')
  return f'{n} {len(ops)}\n{start}\n'+'\n'.join(ops)+'\n','\n'.join(out)+'\n'
 if kind in {'threshold_size','earliest'}:
  m=r.randint(1,18);edges=[]
  for i in range(m):
   u,v=r.sample(range(n),2);edges.append((u,v,r.randint(1,20) if kind=='threshold_size' else i+1))
  qs=[];out=[]
  for _ in range(20):
   if kind=='threshold_size':
    v=r.randrange(n);x=r.randint(0,20)
    seen={v};q=[v];adj=[[] for _ in range(n)]
    for a1,b1,w in edges:
     if w<=x:adj[a1].append(b1);adj[b1].append(a1)
    for z in q:
     for y in adj[z]:
      if y not in seen:seen.add(y);q.append(y)
    out.append(len(seen));qs.append((v+1,x))
   else:
    u,v=r.randrange(n),r.randrange(n);answer=0 if u==v else -1
    if u!=v:
     for time in range(1,m+1):
      if path(n,[(a,b) for a,b,w in edges if w<=time],u,v) is not None:answer=time;break
    qs.append((u+1,v+1));out.append(answer)
  if kind=='threshold_size':inp=f'{n} {m} {len(qs)}\n'+''.join(f'{u+1} {v+1} {w}\n' for u,v,w in edges)
  else:inp=f'{n} {m} {len(qs)}\n'+''.join(f'{u+1} {v+1}\n' for u,v,w in edges)
  return inp+''.join(f'{x} {y}\n' for x,y in qs),''.join(f'{x}\n' for x in out)
 if kind in {'forest_xor','forest_sum','forest_affine'}:
  vals=[r.randint(0,20) for _ in range(n)];start=vals[:];edges=set();ops=[];out=[]
  for _ in range(45):
   pairs=[(u,v) for u in range(n) for v in range(u+1,n) if path(n,edges,u,v) is None];linked=list(edges);connected=[(u,v) for u in range(n) for v in range(u,n) if path(n,edges,u,v) is not None];choices=['SET']+(['LINK'] if pairs else [])+(['CUT'] if linked else [])+(['QUERY'] if connected else [])
   if kind=='forest_affine' and connected:choices.append('AFFINE')
   op=r.choice(choices)
   if op=='LINK':u,v=r.choice(pairs);edges.add((u,v));ops.append(f'LINK {u+1} {v+1}')
   elif op=='CUT':u,v=r.choice(linked);edges.remove((u,v));ops.append(f'CUT {u+1} {v+1}')
   elif op=='SET':u=r.randrange(n);x=r.randint(0,20);vals[u]=x;ops.append(f'SET {u+1} {x}')
   else:
    u,v=r.choice(connected);route=path(n,edges,u,v)
    if op=='AFFINE':a1,b1=r.randint(0,5),r.randint(0,5);ops.append(f'AFFINE {u+1} {v+1} {a1} {b1}');
    if op=='AFFINE':
     for x in route:vals[x]=(a1*vals[x]+b1)%MOD
    else:
     name='XOR' if kind=='forest_xor' else 'SUM';ops.append(f'{name} {u+1} {v+1}');value=0
     for x in route:value=value^vals[x] if kind=='forest_xor' else value+vals[x]
     out.append(value%MOD if kind=='forest_affine' else value)
  return f'{n} {len(ops)}\n'+' '.join(map(str,start))+'\n'+'\n'.join(ops)+'\n',''.join(f'{x}\n' for x in out)
 raise ValueError(kind)
def main():
 p=argparse.ArgumentParser();p.add_argument('kind');p.add_argument('--count',type=int,default=20);p.add_argument('--seed',type=int,default=1);p.add_argument('--out-dir',type=Path,required=True);a=p.parse_args();a.out_dir.mkdir(parents=True,exist_ok=True);r=random.Random(a.seed)
 for i in range(a.count):x,y=case(a.kind,r);s=a.out_dir/f'case{i:03d}';s.with_suffix('.in').write_text(x);s.with_suffix('.out').write_text(y)
if __name__=='__main__':main()
