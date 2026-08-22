"""Adversarial full-limit invariant tests for finale Problems 11--20."""
from __future__ import annotations
import argparse,hashlib,subprocess,tempfile
from pathlib import Path
from stress_finale_round6 import Case,run,c53,size_line_count,c54,one_integer,c61,k61
ROOT=Path(__file__).resolve().parents[1];BASE=ROOT/'sections/100_grandmaster_finale/problems'

def k11(out,_):
 # All 250 return arcs are forced to 12 units.
 expected=sum(12*(i%11)+66 for i in range(250));assert out.strip()==str(expected)

def c12(_):
 n=200;K=100;profits=[2*(n-i) for i in range(n)];edges=[]
 for i in range(2000):
  base=0 if i%2==0 else K;u=base+(i*17)%(K);v=base+(i*31+1)%K
  edges.append((u+1,v+1))
 return f'{n} 2000 {K}\n'+' '.join(map(str,profits))+'\n'+''.join(f'{u} {v}\n' for u,v in edges)
def k12(out,_):assert out.strip()==str(sum(2*(200-i) for i in range(100)))

def c13(_):
 rows=[(i,i+1,i,i) for i in range(1,100)]
 for i in range(201):rows.append((i%99+1,i%99+2,i%17+1,1000+i))
 return '100 300 99\n'+''.join(f'{u} {v} {c} {w}\n' for u,v,c,w in rows)
def k13(out,_):assert out.strip()=='99'

def c14(_):
 rows=[]
 for u in range(1,201):
  for v in range(1,201):
   if u!=v and len(rows)<5000:rows.append((u,v))
 return '200 5000\n'+('1 '*199)+'1\n'+''.join(f'{u} {v} 1\n' for u,v in rows)
def k14(out,_):assert out.strip()=='200'

def c15(size):
 rows=[(2*i+1,2*i+2,1) for i in range(30)]
 i=0
 while len(rows)<900:
  u=i%60+1;v=(i*17+13)%60+1;i+=1
  if u!=v:rows.append((u,v,1))
 return f'60 900 {size}\n'+''.join(f'{u} {v} {d}\n' for u,v,d in rows)+''.join(f'{i%30+1}\n' for i in range(size))
def k15(out,size):assert out.split()==['1']*size

def c17(size):return f'{size}\n'+' '.join(map(str,range(size,0,-1)))+'\n'+''.join(f'{i} {i+1}\n' for i in range(1,size))
def k17(out,size):assert out.strip()==str((size//2)*((size+1)//2))

def c18(size):
 n=700;m=5000;rows=[(i+1,(i+1)%n+1) for i in range(n)];i=0
 while len(rows)<m:
  u=i%n+1;v=(i*37+11)%n+1;i+=1
  if u!=v:rows.append((u,v))
 qs=''.join(f'{i%n+1} {(i*97+3)%n+1}\n' for i in range(size))
 return f'{n} {m} {size}\n'+''.join(f'{u} {v} 0 1 0\n' for u,v in rows)+qs
def k18(out,size):assert out.split()==['YES']*size

def c19(_):return '5000 2500\n'+('1 '*4999)+'1\n'
def k19(out,_):assert out.strip()=='10000'

CASES=[
 Case('11_bounded_convex_shipping',c54,k11,1),Case('12_parametric_quota_cut',c12,k12,1),Case('13_rainbow_bottleneck_forest',c13,k13,1),Case('14_rooted_broadcast_choice',c14,k14,1),Case('15_pairing_under_thresholds',c15,k15,200000),Case('16_all_pairs_cut_statistics',c53,size_line_count,200000),Case('17_isotonic_tree_labels',c17,k17,200000),Case('18_circulation_repair_queries',c18,k18,200000),Case('19_convex_resource_schedule',c19,k19,1),Case('20_laminar_assignment',c61,k61,1)]

def main():
 p=argparse.ArgumentParser();p.add_argument('--profile',choices=('quick','full'),default='quick');p.add_argument('--problem',action='append');p.add_argument('--lang',choices=('cpp','py','both'),default='both');p.add_argument('--timeout',type=int,default=180);a=p.parse_args();wanted=set(a.problem or [])
 with tempfile.TemporaryDirectory(prefix='finale-r2-') as td:
  for case in [c for c in CASES if not wanted or c.slug[:2] in wanted]:
   size=case.full_size if a.profile=='full' else (max(10,int(case.full_size*.01)) if case.full_size>1 else 1);data=case.make(size);outputs={};binary=Path(td)/case.slug
   if a.lang in ('cpp','both'):
    subprocess.run(['g++','-std=c++20','-O2','-pipe',str(BASE/case.slug/'solution.cpp'),'-o',str(binary)],check=True);outputs['cpp'],e,r=run([str(binary)],data,a.timeout);case.check(outputs['cpp'],size);print(f'{case.slug} cpp {e:.3f}s, {r/1024:.1f} MiB')
   if a.lang in ('py','both'):
    outputs['py'],e,r=run(['python3',str(BASE/case.slug/'solution.py')],data,a.timeout);case.check(outputs['py'],size);print(f'{case.slug} py  {e:.3f}s, {r/1024:.1f} MiB')
   if len(outputs)==2:assert outputs['cpp'].split()==outputs['py'].split()
   print('  invariant OK, output sha256='+hashlib.sha256(next(iter(outputs.values())).encode()).hexdigest()[:12])
if __name__=='__main__':main()
