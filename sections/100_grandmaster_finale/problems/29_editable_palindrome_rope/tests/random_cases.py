import argparse,random
from pathlib import Path
def case(r):
 a=list(''.join(r.choice('abc') for _ in range(r.randint(1,18))));s=''.join(a);ops=[];ans=[]
 for _ in range(r.randint(1,40)):
  o=r.choice(['SET','REV','PAL']);l=r.randint(1,len(a))
  if o=='SET':c=r.choice('abc');a[l-1]=c;ops.append(f'SET {l} {c}')
  else:h=r.randint(l,len(a));ops.append(f'{o} {l} {h}');a[l-1:h]=a[l-1:h][::-1] if o=='REV' else a[l-1:h];ans+=([('YES' if a[l-1:h]==a[l-1:h][::-1] else 'NO')] if o=='PAL' else [])
 return s+'\n'+str(len(ops))+'\n'+'\n'.join(ops)+'\n','\n'.join(ans)+('\n' if ans else '')
def main():
 p=argparse.ArgumentParser();p.add_argument('--count',type=int,default=25);p.add_argument('--seed',type=int,default=1);p.add_argument('--out-dir',type=Path,required=True);a=p.parse_args();a.out_dir.mkdir(parents=True,exist_ok=True);r=random.Random(a.seed)
 for i in range(a.count):x,y=case(r);z=a.out_dir/f'case{i:03d}';z.with_suffix('.in').write_text(x);z.with_suffix('.out').write_text(y)
if __name__=='__main__':main()
