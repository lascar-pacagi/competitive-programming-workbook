"""Independent exhaustive oracles for Sections 97--99."""
import argparse,itertools,math,random
from pathlib import Path
MOD=1_000_000_007
def digit_sum_case(r):
 rows=[];ans=[]
 for _ in range(r.randint(1,12)):
  a=r.randint(0,5000);b=r.randint(a,8000);s=r.randint(0,30);rows.append((a,b,s));ans.append(sum(sum(map(int,str(x)))==s for x in range(a,b+1)))
 return f'{len(rows)}\n'+''.join(f'{a} {b} {s}\n' for a,b,s in rows),'\n'.join(map(str,ans))+'\n'
def pattern_case(r):
 rows=[];ans=[]
 for _ in range(r.randint(1,10)):
  n=r.randint(0,5000);p=str(r.randint(0,199));rows.append((n,p));ans.append(sum(p not in str(x) for x in range(n+1)))
 return f'{len(rows)}\n'+''.join(f'{n} {p}\n' for n,p in rows),'\n'.join(map(str,ans))+'\n'
def digit_sum_story_case(r):
 rows=[];ans=[]
 for _ in range(r.randint(1,8)):
  a=r.randint(0,2000);b=r.randint(a,5000);s=r.randint(0,25);m=r.randint(1,12);rows.append((a,b,s,m));ans.append(sum(sum(map(int,str(x)))==s and x%m==0 for x in range(a,b+1)))
 return f'{len(rows)}\n'+''.join(f'{a} {b} {s} {m}\n' for a,b,s,m in rows),'\n'.join(map(str,ans))+'\n'
def pattern_story_case(r):
 rows=[];ans=[]
 for _ in range(r.randint(1,8)):
  n=r.randint(0,5000);p=str(r.randint(0,99));s=r.randint(0,25);rows.append((n,p,s));ans.append(sum(p not in str(x) and sum(map(int,str(x)))==s for x in range(n+1)))
 return f'{len(rows)}\n'+''.join(f'{n} {p} {s}\n' for n,p,s in rows),'\n'.join(map(str,ans))+'\n'
def tilings(grid):
 if not grid:return 1
 n=len(grid);m=len(grid[0]);free=[(i,j) for i in range(n) for j in range(m) if grid[i][j]=='.'];used=set()
 def dfs():
  try:i,j=next(x for x in free if x not in used)
  except StopIteration:return 1
  ans=0;used.add((i,j))
  for x in ((i+1,j),(i,j+1)):
   if x in free and x not in used:used.add(x);ans+=dfs();used.remove(x)
  used.remove((i,j));return ans
 return dfs()
def grid_cases(kind,r):
 n=r.randint(1,4);m=r.randint(1,4);g=[''.join('#' if r.random()<.2 else '.' for _ in range(m)) for _ in range(n)]
 if kind=='domino':ans=tilings(g)
 else:
  cells=[(i,j) for i in range(n) for j in range(m) if g[i][j]=='.'];ans=0
  for mask in range(1<<len(cells)):
   chosen={cells[i] for i in range(len(cells)) if mask>>i&1}
   if all((i+1,j) not in chosen and (i,j+1) not in chosen for i,j in chosen):ans+=1
 return f'{n} {m}\n'+'\n'.join(g)+'\n',f'{ans}\n'
def connected_case(r):
 h=r.randint(1,4);w=r.randint(1,4);g=[''.join('#' if r.random()<.2 else '.' for _ in range(w)) for _ in range(h)];cells=[(i,j) for i in range(h) for j in range(w) if g[i][j]=='.'];ans=0
 for mask in range(1,1<<len(cells)):
  chosen={cells[i] for i in range(len(cells)) if mask>>i&1};seen={next(iter(chosen))};q=list(seen)
  for x,y in q:
   for z in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
    if z in chosen and z not in seen:seen.add(z);q.append(z)
  ans+=len(seen)==len(chosen)
 return f'{h} {w}\n'+'\n'.join(g)+'\n',f'{ans}\n'
def connected_story_case(r):
 h=r.randint(1,3);w=r.randint(1,4);g=[['#' if r.random()<.2 else '.' for _ in range(w)] for _ in range(h)];open_cells=[(i,j) for i in range(h) for j in range(w) if g[i][j]=='.']
 if not open_cells:g[0][0]='.';open_cells=[(0,0)]
 required=set(r.sample(open_cells,r.randint(1,min(3,len(open_cells)))))
 for i,j in required:g[i][j]='T'
 cells=[(i,j) for i in range(h) for j in range(w) if g[i][j]!='#'];ans=0
 for mask in range(1,1<<len(cells)):
  chosen={cells[i] for i in range(len(cells)) if mask>>i&1}
  if not required<=chosen:continue
  seen={next(iter(chosen))};q=list(seen)
  for x,y in q:
   for z in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
    if z in chosen and z not in seen:seen.add(z);q.append(z)
  ans+=len(seen)==len(chosen)
 return f'{h} {w}\n'+'\n'.join(map(''.join,g))+'\n',f'{ans}\n'
def steiner_case(r):
 n=r.randint(2,7);edges=[]
 for v in range(1,n):edges.append((r.randrange(v),v,r.randint(1,9)))
 for _ in range(r.randint(0,3)):
  u,v=r.sample(range(n),2);edges.append((u,v,r.randint(1,9)))
 k=r.randint(1,min(4,n));term=r.sample(range(n),k);best=10**9
 for mask in range(1<<len(edges)):
  p=list(range(n));cost=0
  def f(x):
   while p[x]!=x:x=p[x]
   return x
  for i,(u,v,w) in enumerate(edges):
   if mask>>i&1:p[f(u)]=f(v);cost+=w
  if all(f(x)==f(term[0]) for x in term):best=min(best,cost)
 text=f'{n} {len(edges)} {k}\n'+''.join(f'{u+1} {v+1} {w}\n' for u,v,w in edges)+' '.join(str(x+1) for x in term)+'\n';return text,f'{best}\n'
def steiner_story_case(r):
 n=r.randint(2,7);edges=[]
 for v in range(1,n):edges.append((r.randrange(v),v,r.randint(1,9)))
 for _ in range(r.randint(0,3)):
  u,v=r.sample(range(n),2);edges.append((u,v,r.randint(1,9)))
 k=r.randint(1,min(4,n));term=r.sample(range(n),k);queries=[r.randint(1,(1<<k)-1) for _ in range(r.randint(1,6))];answers=[]
 for wanted in queries:
  targets=[term[i] for i in range(k) if wanted>>i&1];best=10**9
  for mask in range(1<<len(edges)):
   parent=list(range(n));cost=0
   def find(x):
    while parent[x]!=x:x=parent[x]
    return x
   for i,(u,v,w) in enumerate(edges):
    if mask>>i&1:parent[find(u)]=find(v);cost+=w
   if all(find(x)==find(targets[0]) for x in targets):best=min(best,cost)
  answers.append(best)
 text=f'{n} {len(edges)} {k} {len(queries)}\n'+''.join(f'{u+1} {v+1} {w}\n' for u,v,w in edges)+' '.join(str(x+1) for x in term)+'\n'+'\n'.join(map(str,queries))+'\n';return text,'\n'.join(map(str,answers))+'\n'
def treewidth_case(r):
 n=r.randint(1,8);weights=[r.randint(-5,15) for _ in range(n)];edges=[(i,j) for i in range(n) for j in range(i) if r.random()<.3];best=max(sum(weights[i] for i in range(n) if mask>>i&1) for mask in range(1<<n) if all(not(mask>>u&1 and mask>>v&1) for u,v in edges));nodes=['L']
 for v in range(n):nodes.append(f'I {len(nodes)} {v+1}')
 left=len(nodes);nodes.append('L')
 for v in range(n):nodes.append(f'I {len(nodes)} {v+1}')
 right=len(nodes);nodes.append(f'J {left} {right}');child=len(nodes)
 for v in range(n):nodes.append(f'F {child} {v+1}');child=len(nodes)
 text=f'{n} {len(edges)}\n'+' '.join(map(str,weights))+'\n'+''.join(f'{u+1} {v+1}\n' for u,v in edges)+f'{len(nodes)}\n'+'\n'.join(nodes)+'\n';return text,f'{best}\n'
def treewidth_story_case(r):
 text,_=treewidth_case(r);lines=text.splitlines();n,m=map(int,lines[0].split());weights=[r.randint(0,15) for _ in range(n)];lines[1]=' '.join(map(str,weights));edges=[tuple(int(x)-1 for x in lines[i].split()) for i in range(2,2+m)];best=min(sum(weights[i] for i in range(n) if mask>>i&1) for mask in range(1<<n) if all(mask>>u&1 or mask>>v&1 for u,v in edges));return '\n'.join(lines)+'\n',f'{best}\n'
def tower_story_case(r):
 h=r.randint(0,5);p=r.randint(1,3);w=r.randint(1,4);rows=[''.join('#' if r.random()<.2 else '.' for _ in range(w)) for _ in range(p)];return f'{h} {p} {w}\n'+'\n'.join(rows)+'\n',f'{tilings(rows*h)}\n'
def one(kind,r):
 if kind=='digitsum_story':return digit_sum_story_case(r)
 if kind=='digitpattern_story':return pattern_story_case(r)
 if kind=='tower_story':return tower_story_case(r)
 if kind=='connected_story':return connected_story_case(r)
 if kind=='steiner_story':return steiner_story_case(r)
 if kind=='treewidth_story':return treewidth_story_case(r)
 base=kind
 if base=='digitsum':return digit_sum_case(r)
 if base=='digitpattern':return pattern_case(r)
 if base in {'domino','gridset'}:return grid_cases(base,r)
 if base=='tower':
  h=r.randint(0,6);w=r.randint(1,4);grid=['.'*w for _ in range(h)];return f'{h} {w}\n',f'{tilings(grid)}\n'
 if base=='connected':return connected_case(r)
 if base=='steiner':return steiner_case(r)
 return treewidth_case(r)
def main():
 p=argparse.ArgumentParser();p.add_argument('kind');p.add_argument('--count',type=int,default=20);p.add_argument('--seed',type=int,default=1);p.add_argument('--out-dir',type=Path,required=True);a=p.parse_args();a.out_dir.mkdir(parents=True,exist_ok=True);r=random.Random(a.seed)
 for i in range(a.count):x,y=one(a.kind,r);stem=a.out_dir/f'case{i:03d}';stem.with_suffix('.in').write_text(x);stem.with_suffix('.out').write_text(y)
if __name__=='__main__':main()
