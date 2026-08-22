import argparse,random
from pathlib import Path
def case(r):
 n=r.randint(1,10);p=[''.join(r.choice('abc') for _ in range(r.randint(1,5))) for _ in range(n)];active=[0]*n;ops=[];ans=[]
 for _ in range(r.randint(1,35)):
  choices=['?']+(['+'] if not all(active) else [])+(['-'] if any(active) else []);o=r.choice(choices)
  if o=='?':
   s=''.join(r.choice('abc') for _ in range(r.randint(1,14)));ops.append(f'? {s}');ans.append(str(sum(sum(s[j:j+len(x)]==x for j in range(len(s)-len(x)+1)) for i,x in enumerate(p) if active[i])))
  else:
   a=[i for i,x in enumerate(active) if x==(o=='-')];i=r.choice(a);active[i]^=1;ops.append(f'{o} {i+1}')
 return f'{n} {len(ops)}\n'+'\n'.join(p)+'\n'+'\n'.join(ops)+'\n','\n'.join(ans)+('\n' if ans else '')
def main():
 p=argparse.ArgumentParser();p.add_argument('--count',type=int,default=25);p.add_argument('--seed',type=int,default=1);p.add_argument('--out-dir',type=Path,required=True);a=p.parse_args();a.out_dir.mkdir(parents=True,exist_ok=True);r=random.Random(a.seed)
 for i in range(a.count):x,y=case(r);z=a.out_dir/f'case{i:03d}';z.with_suffix('.in').write_text(x);z.with_suffix('.out').write_text(y)
if __name__=='__main__':main()
