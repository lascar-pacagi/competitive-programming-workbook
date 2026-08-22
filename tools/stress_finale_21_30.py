"""Adversarial full-limit invariant tests for finale Problems 21--30."""
from __future__ import annotations
import argparse,hashlib,subprocess,tempfile
from pathlib import Path
from stress_finale_round6 import Case,run,c51,k51
ROOT=Path(__file__).resolve().parents[1];BASE=ROOT/'sections/100_grandmaster_finale/problems'

def c21(size):return 'a'*size+f'\n{size}\n'+''.join(f'{"a" if i%2==0 else "aa"} {i+1}\n' for i in range(size))
def k21(out,size):
 v=list(map(int,out.split()));assert len(v)==size
 for i,x in enumerate(v):limit=size if i%2==0 else size-1;assert x==(i+1 if i+1<=limit else -1)

def c22(size):return '2\n'+'a'*size+'\n'+'a'*size+'\n'
def k22(out,size):assert out.split()==[str(size),str(size)]

def c23(size):return 'a'*size+f'\n{size}\n'+f'1 {size}\n'*size
def k23(out,size):assert out.split()==[str(size)]*size

def c24(size):return 'a'*size+f'\n{size}\n'+f'1 {size} 1\n'*size
def k24(out,size):assert out.split()==[str(size),'1']*size

def c26(size):return f'{size} 0\n'+'a'*size+'\n'+'a'*size+'\n'
def k26(out,size):v=list(map(int,out.split()));assert v==[size,*range(size)]

def c27(size):return 'a'*size+f'\n{size}\n'+'1\n'*size
def k27(out,size):assert out.split()==['a']*size

def c28(size):return 'a'*size+'\n'
def k28(out,size):assert out.strip()==str(size*(size+1)*(size-1)//6)

def c29(size):
 ops=[]
 for i in range(size):ops.append(f'REV 1 {size}\n' if i%2==0 else f'PAL 1 {size}\n')
 return 'a'*size+f'\n{size}\n'+''.join(ops)
def k29(out,size):assert out.split()==['YES']*(size//2)

def c30(_):return '5 5 1000000000000000000\nab\nbc\nca\nabc\ncba\naa\nbb\ncc\nacb\nbac\n'
def k30(out,_):assert len(out.split())==1 and out.strip().isdigit()

CASES=[Case('21_persistent_text_occurrences',c21,k21,100000),Case('22_multi_archive_common_substrings',c22,k22,100000),Case('23_palindromic_range_census',c23,k23,200000),Case('24_lexicographic_substring_laboratory',c24,k24,200000),Case('25_dynamic_pattern_ledger',c51,k51,100000),Case('26_cyclic_match_convolution',c26,k26,200000),Case('27_distinct_substring_rank',c27,k27,200000),Case('28_interval_lcp_aggregates',c28,k28,500000),Case('29_editable_palindrome_rope',c29,k29,200000),Case('30_forbidden_superstring_count',c30,k30,1)]

def main():
 p=argparse.ArgumentParser();p.add_argument('--profile',choices=('quick','full'),default='quick');p.add_argument('--problem',action='append');p.add_argument('--lang',choices=('cpp','py','both'),default='both');p.add_argument('--timeout',type=int,default=180);a=p.parse_args();wanted=set(a.problem or [])
 with tempfile.TemporaryDirectory(prefix='finale-r3-') as td:
  for case in [c for c in CASES if not wanted or c.slug[:2] in wanted]:
   size=case.full_size if a.profile=='full' else (max(10,int(case.full_size*.01)) if case.full_size>1 else 1);data=case.make(size);outputs={};binary=Path(td)/case.slug
   if a.lang in ('cpp','both'):
    subprocess.run(['g++','-std=c++20','-O2','-pipe',str(BASE/case.slug/'solution.cpp'),'-o',str(binary)],check=True);outputs['cpp'],e,r=run([str(binary)],data,a.timeout);case.check(outputs['cpp'],size);print(f'{case.slug} cpp {e:.3f}s, {r/1024:.1f} MiB')
   if a.lang in ('py','both'):
    outputs['py'],e,r=run(['python3',str(BASE/case.slug/'solution.py')],data,a.timeout);case.check(outputs['py'],size);print(f'{case.slug} py  {e:.3f}s, {r/1024:.1f} MiB')
   if len(outputs)==2:assert outputs['cpp'].split()==outputs['py'].split()
   print('  invariant OK, output sha256='+hashlib.sha256(next(iter(outputs.values())).encode()).hexdigest()[:12])
if __name__=='__main__':main()
