import argparse,itertools,random
from pathlib import Path
def case(r):
 R=r.randint(0,3);F=r.randint(0,3);L=r.randint(0,7);req=[''.join(r.choice('abc') for _ in range(r.randint(1,3))) for _ in range(R)];bad=[''.join(r.choice('abc') for _ in range(r.randint(1,3))) for _ in range(F)];z=sum(all(x in s for x in req) and all(x not in s for x in bad) for s in map(''.join,itertools.product('abc',repeat=L)));return f'{R} {F} {L}\n'+'\n'.join(req+bad)+('\n' if req or bad else ''),f'{z}\n'
def main():
 p=argparse.ArgumentParser();p.add_argument('--count',type=int,default=25);p.add_argument('--seed',type=int,default=1);p.add_argument('--out-dir',type=Path,required=True);a=p.parse_args();a.out_dir.mkdir(parents=True,exist_ok=True);r=random.Random(a.seed)
 for i in range(a.count):x,y=case(r);z=a.out_dir/f'case{i:03d}';z.with_suffix('.in').write_text(x);z.with_suffix('.out').write_text(y)
if __name__=='__main__':main()
