"""Deterministic scale cases for the section 42 query structures.

Expected outputs use construction identities, not the reference solutions.
"""
from __future__ import annotations
import argparse
from pathlib import Path

N=200_000


def case(name: str) -> tuple[str,str]:
    n=q=N
    if name=='a_dynamic_order_statistics':
        half=q//2
        return f'{n} {q}\n'+''.join(f'1 {i}\n' for i in range(1,half+1))+''.join(f'3 {i}\n' for i in range(half,0,-1)),''.join(f'{i}\n' for i in range(half,0,-1))
    if name=='b_range_assign_add':
        ops=[];out=[]
        for i in range(q//4):
            x=i%7-3;delta=-2
            ops.extend([f'1 1 {n} {x}',f'2 {n//2+1} {n} {delta}',f'3 1 {n}',f'3 {n//2+1} {n}'])
            out.extend([n*x+(n//2)*delta,(n//2)*(x+delta)])
        return f'{n} {q}\n'+'0 '*n+'\n'+'\n'.join(ops)+'\n','\n'.join(map(str,out))+'\n'
    if name in {'c_static_rectangle_count','k_static_weighted_rectangles'}:
        weighted=name.startswith('k_');points=''.join(f'{i} {i}'+(' -3' if weighted else '')+'\n' for i in range(1,n+1));ops=[];out=[]
        for i in range(q):
            lo=i%n+1;hi=n
            ops.append(f'{lo} {lo} {hi} {hi}');out.append((hi-lo+1)*(-3 if weighted else 1))
        return f'{n} {q}\n'+points+'\n'.join(ops)+'\n','\n'.join(map(str,out))+'\n'
    if name=='d_nested_ranges_count':
        return f'{n}\n'+''.join(f'{i} {2*n+1-i}\n' for i in range(1,n+1)),' '.join(map(str,range(n-1,-1,-1)))+'\n'+' '.join(map(str,range(n)))+'\n'
    base=f'{n} {q}\n'+'-1 '*n+'\n'+''.join(f'{i} {i+1}\n' for i in range(1,n))
    if name=='e_subtree_add_point_query':
        return base+f'A 1 1\nQ {n}\n'*(q//2),''.join(f'{i}\n' for i in range(q//2))
    if name=='f_dynamic_subtree_maximum':
        ops=[];out=[]
        for i in range(q//2):
            v=i+2;ops.extend([f'U {v} -2',f'Q {v}']);out.append(-1)
        return base+'\n'.join(ops)+'\n','\n'.join(map(str,out))+'\n'
    if name=='g_subtree_value_count':
        return base+''.join(f'{i+1} -1 -1\n' for i in range(q)),''.join(f'{n-i}\n' for i in range(q))
    if name=='i_subtree_assign_add_sum':
        return base+(f'1 1 0\n2 {n} -2\n3 1\n3 {n}\n'*(q//4)),'-2\n'*(q//2)
    if name=='j_static_vertex_path_sums':
        return base+''.join(f'{i+1} {n}\n' for i in range(q)),''.join(f'{-(n-i)}\n' for i in range(q))
    if name=='l_subtree_add_maximum':
        return base+f'A 1 -1\nQ {n}\n'*(q//2),''.join(f'{-i-2}\n' for i in range(q//2))
    raise ValueError(name)


def main(name: str) -> None:
    parser=argparse.ArgumentParser();parser.add_argument('--out-dir',type=Path,required=True)
    args=parser.parse_args();args.out_dir.mkdir(parents=True,exist_ok=True)
    inp,out=case(name);(args.out_dir/'maximum_size.in').write_text(inp);(args.out_dir/'maximum_size.out').write_text(out)
