"""Adversarial full-limit invariant tests for finale Problems 01--10."""
from __future__ import annotations
import argparse, hashlib, subprocess, tempfile
from pathlib import Path

from stress_finale_round6 import Case, run, c52, k52, tree_distance, k_tree_distance, c62, k62, c65, k65

ROOT=Path(__file__).resolve().parents[1];BASE=ROOT/'sections/100_grandmaster_finale/problems'

def c01(size):
 n=q=size;vals=' '.join(map(str,range(1,n+1)));edges=''.join(f'{i} {i+1}\n' for i in range(1,n));queries=f'1 {n}\n'*q
 return f'{n} {q}\n{vals}\n{edges}{queries}'
def k01(out,size):
 vals=out.split();assert len(vals)==2*size;median=size//2 if size%2==0 else size//2+1;cost=(size//2)*((size+1)//2)
 assert all(vals[i]==str(median) and vals[i+1]==str(cost) for i in range(0,len(vals),2))

def c03(size):
 half=size//2;rows=[]
 for i in range(1,half+1):rows.append(f'{i-1} A 0 {half-i-1}\n')
 for i in range(half+1,size+1):rows.append(f'{i-1} Q 0\n')
 return f'{size}\n'+''.join(rows)
def k03(out,size):
 half=size//2;v=out.split();assert len(v)==2*(size-half);assert all(v[i]=='-1' and v[i+1]==str(half) for i in range(0,len(v),2))

def c05(size):
 n=size//2+1;links=''.join(f'LINK {i} {i+1}\n' for i in range(1,n));a=(size-(n-1))//2;ops=links+f'AFFINE 1 {n} 1 1\n'*a+f'SUM 1 {n}\n'*(size-(n-1)-a)
 return f'{n} {size}\n'+('0 '*(n-1))+'0\n'+ops
def k05(out,size):
 n=size//2+1;a=(size-(n-1))//2;count=size-(n-1)-a;expected=str(n*a%1000000007);assert out.split()==[expected]*count

def c07(size):
 n=size;q=size//2;edges=''.join(f'{i} {i+1} 1\n' for i in range(1,n));return f'{n} {q}\n{edges}'+f'2 1 {n}\n'*q
def k07(out,size):assert out.split()==['1','1']*(size//2)

def c08(size):
 n=q=size;edges=''.join(f'{i} {i+1}\n' for i in range(1,n));ops=[]
 for i in range(q):ops.append(f'U 1 {i+1}\n' if i%2==0 else f'K 1 {n//2}\n')
 return f'{n} {q}\n'+('0 '*(n-1))+'0\n'+edges+''.join(ops)
def k08(out,size):assert out.split()==['0']*(size//2)

def c09(size):
 n=q=size;edges=''.join(f'{i} {i+1}\n' for i in range(1,n));return f'{n} {q}\n'+'a'*n+'\n'+edges+f'1 {n} {n} 1\n'*q
def k09(out,size):assert out.split()==[str(size),'0']*size

CASES=[
 Case('01_temporal_path_median',c01,k01,200000),
 Case('02_bipartite_timeline',c52,k52,200000),
 Case('03_versioned_convex_dp',c03,k03,200000),
 Case('04_historical_rectangle_selection',c62,k62,100000),
 Case('05_dynamic_forest_ledger',c05,k05,200000),
 Case('06_colored_distance_census',tree_distance,k_tree_distance,100000),
 Case('07_virtual_tree_firewall',c07,k07,200000),
 Case('08_subtree_order_laboratory',c08,k08,30000),
 Case('09_ancestral_pattern_index',c09,k09,100000),
 Case('10_kruskal_time_machine',c65,k65,200000),]

def main():
 p=argparse.ArgumentParser();p.add_argument('--profile',choices=('quick','full'),default='quick');p.add_argument('--problem',action='append');p.add_argument('--lang',choices=('cpp','py','both'),default='both');p.add_argument('--timeout',type=int,default=180);a=p.parse_args();wanted=set(a.problem or [])
 cases=[c for c in CASES if not wanted or c.slug[:2] in wanted]
 with tempfile.TemporaryDirectory(prefix='finale-r1-') as td:
  temp=Path(td)
  for case in cases:
   size=case.full_size if a.profile=='full' else max(10,int(case.full_size*.01));data=case.make(size);outputs={}
   if a.lang in ('cpp','both'):
    binary=temp/case.slug;subprocess.run(['g++','-std=c++20','-O2','-pipe',str(BASE/case.slug/'solution.cpp'),'-o',str(binary)],check=True)
    outputs['cpp'],elapsed,rss=run([str(binary)],data,a.timeout);case.check(outputs['cpp'],size);print(f'{case.slug} cpp {elapsed:.3f}s, {rss/1024:.1f} MiB')
   if a.lang in ('py','both'):
    outputs['py'],elapsed,rss=run(['python3',str(BASE/case.slug/'solution.py')],data,a.timeout);case.check(outputs['py'],size);print(f'{case.slug} py  {elapsed:.3f}s, {rss/1024:.1f} MiB')
   if len(outputs)==2:assert outputs['cpp'].split()==outputs['py'].split()
   print('  invariant OK, output sha256='+hashlib.sha256(next(iter(outputs.values())).encode()).hexdigest()[:12])
if __name__=='__main__':main()
