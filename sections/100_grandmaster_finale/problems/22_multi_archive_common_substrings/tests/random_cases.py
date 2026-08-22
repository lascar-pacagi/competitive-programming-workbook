import argparse,random
from pathlib import Path
def case(r):
 k=r.randint(1,5);ss=[''.join(r.choice('abc') for _ in range(r.randint(1,9))) for _ in range(k)];sets=[]
 for s in ss:sets.append({s[i:j] for i in range(len(s)) for j in range(i+1,len(s)+1)})
 z=set.intersection(*sets);return str(k)+'\n'+'\n'.join(ss)+'\n',f'{max(map(len,z),default=0)} {len(z)}\n'
def main():
 p=argparse.ArgumentParser();p.add_argument('--count',type=int,default=25);p.add_argument('--seed',type=int,default=1);p.add_argument('--out-dir',type=Path,required=True);a=p.parse_args();a.out_dir.mkdir(parents=True,exist_ok=True);r=random.Random(a.seed)
 for i in range(a.count):x,y=case(r);z=a.out_dir/f'case{i:03d}';z.with_suffix('.in').write_text(x);z.with_suffix('.out').write_text(y)
if __name__=='__main__':main()
