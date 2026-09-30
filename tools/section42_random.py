"""Section 42 generators with independent direct graph/array oracles."""
from __future__ import annotations
import argparse
import random
from pathlib import Path
from tools.progressive_mixed_random import tree, path


def case(name: str, rng: random.Random):
    if name == 'h_incremental_connectivity':
        n=rng.randint(1,12);q=30;g=[set() for _ in range(n)];ops=[];out=[]
        for _ in range(q):
            u,v=rng.randrange(n),rng.randrange(n)
            if rng.random()<.5:
                ops.append(f'A {u+1} {v+1}');g[u].add(v);g[v].add(u)
            else:
                seen={u};todo=[u]
                for x in todo:
                    for y in g[x]:
                        if y not in seen:seen.add(y);todo.append(y)
                ops.append(f'Q {u+1} {v+1}');out.append('YES' if v in seen else 'NO')
        return f'{n} {q}\n'+'\n'.join(ops)+'\n','\n'.join(out)+'\n'
    if name == 'k_static_weighted_rectangles':
        n=rng.randint(1,15);q=20;points=[(rng.randint(-4,4),rng.randint(-4,4),rng.randint(-9,9)) for _ in range(n)];ops=[];out=[]
        for _ in range(q):
            a=rng.randint(-5,4);c=rng.randint(a,5);b=rng.randint(-5,4);d=rng.randint(b,5)
            ops.append(f'{a} {b} {c} {d}');out.append(sum(w for x,y,w in points if a<=x<=c and b<=y<=d))
        return f'{n} {q}\n'+''.join(f'{x} {y} {w}\n' for x,y,w in points)+'\n'.join(ops)+'\n','\n'.join(map(str,out))+'\n'
    n=rng.randint(1,13);q=30;edges,g,parent,desc=tree(rng,n)
    a=[rng.randint(-9,9) for _ in range(n)];initial=a[:];ops=[];out=[]
    for _ in range(q):
        u=rng.randrange(n)
        if name == 'f_dynamic_subtree_maximum':
            if rng.random()<.5:
                x=rng.randint(-10,10);a[u]=x;ops.append(f'U {u+1} {x}')
            else:ops.append(f'Q {u+1}');out.append(max(a[v] for v in desc[u]))
        elif name == 'l_subtree_add_maximum':
            if rng.random()<.5:
                x=rng.randint(-10,10);ops.append(f'A {u+1} {x}')
                for v in desc[u]:a[v]+=x
            else:ops.append(f'Q {u+1}');out.append(max(a[v] for v in desc[u]))
        elif name == 'i_subtree_assign_add_sum':
            op=rng.randint(1,3)
            if op==3:ops.append(f'3 {u+1}');out.append(sum(a[v] for v in desc[u]))
            else:
                x=rng.randint(-10,10);ops.append(f'{op} {u+1} {x}')
                for v in desc[u]:a[v]=x if op==1 else a[v]+x
        elif name == 'j_static_vertex_path_sums':
            v=rng.randrange(n);ops.append(f'{u+1} {v+1}');out.append(sum(a[w] for w in path(g,u,v)))
        elif name == 'g_subtree_value_count':
            lo=rng.randint(-12,9);hi=rng.randint(lo,12);ops.append(f'{u+1} {lo} {hi}');out.append(sum(lo<=a[v]<=hi for v in desc[u]))
        else:raise ValueError(name)
    inp=f'{n} {q}\n'+' '.join(map(str,initial))+'\n'+''.join(f'{u+1} {v+1}\n' for u,v in edges)+'\n'.join(ops)+'\n'
    return inp,'\n'.join(map(str,out))+('\n' if out else '')


def main(name: str):
    parser=argparse.ArgumentParser();parser.add_argument('--count',type=int,required=True);parser.add_argument('--seed',type=int,required=True);parser.add_argument('--out-dir',type=Path,required=True);args=parser.parse_args()
    args.out_dir.mkdir(parents=True,exist_ok=True);rng=random.Random(args.seed)
    for i in range(args.count):
        inp,out=case(name,rng);stem=args.out_dir/f'case{i:03d}';stem.with_suffix('.in').write_text(inp);stem.with_suffix('.out').write_text(out)
