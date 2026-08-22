"""Adversarial full-limit tests for the published kernels in Problems 31--40."""
from __future__ import annotations
import argparse,hashlib,math,subprocess,tempfile
from pathlib import Path
from stress_finale_round6 import Case,run,c58,k58,c59,k59
ROOT=Path(__file__).resolve().parents[1];BASE=ROOT/'sections/100_grandmaster_finale/problems'

def c31(size):return f'{size}\n1 '+('0 '*(size-2))+('0\n' if size>1 else '\n')
def k31(out,size):assert out.split()==['0']*size

def c34(k):
 n=1<<k;row=('1 '*(n-1))+'1\n';return f'{k}\n{row}{row}'
def k34(out,k):assert out.split()==[str(1<<k)]*(1<<k)

def c35(size):return f'{size}\n'+''.join(f'{x} 1\n' for x in range(size))
def k35(out,size):assert out.split()==['1']+['0']*(size-1)

P=1000000007;Q=1000000009;SEM=P*Q;LAM=math.lcm(P-1,Q-1)
def c36(size):return f'{size}\n'+f'{SEM}\n'*size
def k36(out,size):assert out.split()==[str(LAM)]*size

def c37(size):return f'{size}\n'+''.join(f'1000000007 1 {2+i}\n' for i in range(size))
def lines(out,size):assert len(out.split())==size

def c38(size):return f'{size}\n'+''.join(f'2 {pow(2,123456,1000000007)} 1000000007\n' for _ in range(size))
def k38(out,size):assert out.split()==['123456']*size

def c39(size):return f'{size}\n'+('1000000 '*(size-1))+'1000000\n'

def phi(n):
 r=n;p=2
 while p*p<=n:
  if n%p==0:
   r-=r//p
   while n%p==0:n//=p
  p+=1
 if n>1:r-=r//n
 return r
def gcd_sum(n):return sum(d*phi(n//d) for d in range(1,n+1) if n%d==0)%1000000007
def c40(size):return f'{size}\n'+('1000000 '*(size-1))+'1000000\n'
def k40(out,size):assert out.split()==[str(gcd_sum(1000000))]*size

CASES=[Case('31_connected_structure_series',c31,k31,200000),Case('32_rational_recurrence_samples',c59,k59,200000),Case('33_subset_partition_spectrum',c58,k58,16),Case('34_xor_walk_spectrum',c34,k34,20),Case('35_polynomial_constraint_recovery',c35,k35,50000),Case('36_factorized_exponent_tower',c36,k36,200),Case('37_modular_root_catalogue',c37,lines,50),Case('38_composite_discrete_log',c38,k38,100),Case('39_summatory_multiplicative_blocks',c39,lines,200000),Case('40_gcd_convolution_queries',c40,k40,200000)]

def main():
 p=argparse.ArgumentParser();p.add_argument('--profile',choices=('quick','full'),default='quick');p.add_argument('--problem',action='append');p.add_argument('--lang',choices=('cpp','py','both'),default='both');p.add_argument('--timeout',type=int,default=240);a=p.parse_args();wanted=set(a.problem or [])
 with tempfile.TemporaryDirectory(prefix='finale-r4-') as td:
  for case in [c for c in CASES if not wanted or c.slug[:2] in wanted]:
   if a.profile=='full':size=case.full_size
   elif case.slug.startswith(('33_','34_')):size=max(8,case.full_size-6)
   else:size=max(1,int(case.full_size*.01))
   data=case.make(size);outputs={};binary=Path(td)/case.slug
   if a.lang in ('cpp','both'):
    subprocess.run(['g++','-std=c++20','-O2','-pipe',str(BASE/case.slug/'solution.cpp'),'-o',str(binary)],check=True);outputs['cpp'],e,r=run([str(binary)],data,a.timeout);case.check(outputs['cpp'],size);print(f'{case.slug} cpp {e:.3f}s, {r/1024:.1f} MiB')
   if a.lang in ('py','both'):
    outputs['py'],e,r=run(['python3',str(BASE/case.slug/'solution.py')],data,a.timeout);case.check(outputs['py'],size);print(f'{case.slug} py  {e:.3f}s, {r/1024:.1f} MiB')
   if len(outputs)==2:assert outputs['cpp'].split()==outputs['py'].split()
   print('  invariant OK, output sha256='+hashlib.sha256(next(iter(outputs.values())).encode()).hexdigest()[:12])
if __name__=='__main__':main()
