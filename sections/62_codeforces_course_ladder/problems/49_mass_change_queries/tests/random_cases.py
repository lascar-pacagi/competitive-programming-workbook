import argparse,random
from pathlib import Path
def main():
 p=argparse.ArgumentParser();p.add_argument('--count',type=int,required=True);p.add_argument('--seed',type=int,required=True);p.add_argument('--out-dir',type=Path,required=True);a=p.parse_args();a.out_dir.mkdir(parents=True,exist_ok=True);g=random.Random(a.seed)
 for c in range(a.count):
  if c==0:
   ops=[(1,1,0)]*100000+[(2,i,0) for i in range(100000)]
   out=[(i,1) for i in range(100000)]
  else:
   ops=[(1,g.randint(-20,20),g.randint(-30,30))];ops += [(1,g.randint(-20,20),g.randint(-30,30)) if g.random()<.6 else (2,g.randint(-30,30),0) for _ in range(g.randint(1,80))]
   if not any(t==2 for t,_,_ in ops): ops.append((2,0,0))
   lines=[];out=[]
   for t,m,b in ops:
    if t==1:lines.append((m,b))
    else:out.append(min((s*m+b,i+1) for i,(s,b) in enumerate(lines)))
  z=a.out_dir/f'case{c:03d}';z.with_suffix('.in').write_text(str(len(ops))+'\n'+'\n'.join(f'{t} {m}'+(f' {b}' if t==1 else '') for t,m,b in ops)+'\n');z.with_suffix('.out').write_text('\n'.join(f'{v} {i}' for v,i in out)+'\n')
if __name__=='__main__':main()
