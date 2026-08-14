"""Tiny brute-force generators for the progressive mixed-contest additions."""

from __future__ import annotations

import argparse
import itertools
import random
from collections import deque
from pathlib import Path


def tree(rng: random.Random, n: int):
    edges = [(rng.randrange(v), v) for v in range(1, n)]
    g = [[] for _ in range(n)]
    for u, v in edges:
        g[u].append(v); g[v].append(u)
    parent = [-1] * n
    order = [0]
    for u in order:
        for v in g[u]:
            if v != parent[u]: parent[v] = u; order.append(v)
    children = [[] for _ in range(n)]
    for v in range(1, n): children[parent[v]].append(v)
    descendants = []
    for root in range(n):
        seen = []
        stack = [root]
        while stack:
            u = stack.pop(); seen.append(u); stack.extend(children[u])
        descendants.append(seen)
    return edges, g, parent, descendants


def path(g, source, target):
    parent = {source: -1}; q = deque([source])
    while q:
        u = q.popleft()
        if u == target: break
        for v in g[u]:
            if v not in parent: parent[v] = u; q.append(v)
    result = []; u = target
    while u != -1: result.append(u); u = parent[u]
    return result


def case(name: str, rng: random.Random):
    if name == "g_streaming_room_count":
        n=rng.randint(1,12);starts=sorted(rng.randint(0,15) for _ in range(n));meet=[(s,s+rng.randint(1,7)) for s in starts];active=[];best=0;out=[]
        for s,e in meet:active=[x for x in active if x>s];active.append(e);best=max(best,len(active));out.append(best)
        return f"{n}\n"+"".join(f"{s} {e}\n" for s,e in meet)," ".join(map(str,out))+"\n"
    if name == "h_toggle_kth_active":
        n=rng.randint(1,12);q=rng.randint(1,30);on=set();ops=[];out=[]
        for _ in range(q):
            if rng.random()<.55:i=rng.randrange(n);ops.append(f"T {i+1}");on.symmetric_difference_update({i})
            else:k=rng.randint(1,n+2);ops.append(f"K {k}");v=sorted(on);out.append(v[k-1]+1 if k<=len(v) else -1)
        return f"{n} {q}\n"+"\n".join(ops)+"\n","\n".join(map(str,out))+("\n" if out else "")
    if name == "i_dynamic_maximum_subarray":
        n=rng.randint(1,10);q=rng.randint(1,20);a=[rng.randint(-9,9) for _ in range(n)];initial=a[:];ops=[];out=[]
        for _ in range(q):
            i=rng.randrange(n);x=rng.randint(-9,9);a[i]=x;ops.append(f"{i+1} {x}");out.append(max(sum(a[l:r]) for l in range(n) for r in range(l+1,n+1)))
        return f"{n} {q}\n"+" ".join(map(str,initial))+"\n"+"\n".join(ops)+"\n","\n".join(map(str,out))+"\n"
    if name == "j_sliding_median_cost":
        n=rng.randint(1,15);k=rng.randint(1,n);a=[rng.randint(-9,9) for _ in range(n)];out=[]
        for i in range(n-k+1):v=sorted(a[i:i+k]);m=v[(k-1)//2];out.append(sum(abs(x-m) for x in v))
        return f"{n} {k}\n"+" ".join(map(str,a))+"\n"," ".join(map(str,out))+"\n"
    if name == "k_budget_prefix_search":
        n=rng.randint(1,12);q=rng.randint(1,25);a=[rng.randint(-9,9) for _ in range(n)];initial=a[:];ops=[];out=[]
        for _ in range(q):
            if rng.random()<.45:i=rng.randrange(n);x=rng.randint(-9,9);a[i]=x;ops.append(f"U {i+1} {x}")
            else:
                l=rng.randrange(n);b=rng.randint(-15,20);s=0;answer=-1
                for r in range(l,n):
                    s+=a[r]
                    if s>b:answer=r+1;break
                ops.append(f"Q {l+1} {b}");out.append(answer)
        return f"{n} {q}\n"+" ".join(map(str,initial))+"\n"+"\n".join(ops)+"\n","\n".join(map(str,out))+("\n" if out else "")
    if name == "l_dynamic_inversion_swaps":
        n=rng.randint(1,12);q=rng.randint(1,25);a=list(range(1,n+1));rng.shuffle(a);initial=a[:];ops=[];out=[]
        for _ in range(q):i=rng.randrange(n);j=rng.randrange(n);a[i],a[j]=a[j],a[i];ops.append(f"{i+1} {j+1}");out.append(sum(a[x]>a[y] for x in range(n) for y in range(x+1,n)))
        return f"{n} {q}\n"+" ".join(map(str,initial))+"\n"+"\n".join(ops)+"\n","\n".join(map(str,out))+"\n"

    if name in {"e_subtree_add_point_query","f_dynamic_path_maximum","g_subtree_value_count","j_subtree_kth_smallest","l_path_add_path_maximum"}:
        n=rng.randint(1,11);q=rng.randint(1,22);edges,g,parent,desc=tree(rng,n);a=[rng.randint(-9,9) for _ in range(n)];initial=a[:];edge_text="".join(f"{u+1} {v+1}\n" for u,v in edges);ops=[];out=[]
        if name == "e_subtree_add_point_query":
            for _ in range(q):
                u=rng.randrange(n)
                if rng.random()<.55:x=rng.randint(-7,7);ops.append(f"A {u+1} {x}");[a.__setitem__(v,a[v]+x) for v in desc[u]]
                else:ops.append(f"Q {u+1}");out.append(a[u])
        elif name == "f_dynamic_path_maximum":
            for _ in range(q):
                u=rng.randrange(n)
                if rng.random()<.45:x=rng.randint(-9,9);a[u]=x;ops.append(f"U {u+1} {x}")
                else:v=rng.randrange(n);ops.append(f"Q {u+1} {v+1}");out.append(max(a[x] for x in path(g,u,v)))
        elif name == "g_subtree_value_count":
            for _ in range(q):u=rng.randrange(n);lo=rng.randint(-10,5);hi=rng.randint(lo,10);ops.append(f"{u+1} {lo} {hi}");out.append(sum(lo<=a[v]<=hi for v in desc[u]))
        elif name == "j_subtree_kth_smallest":
            for _ in range(q):u=rng.randrange(n);k=rng.randint(1,len(desc[u]));ops.append(f"{u+1} {k}");out.append(sorted(a[v] for v in desc[u])[k-1])
        else:
            for _ in range(q):
                u=rng.randrange(n);v=rng.randrange(n);vertices=path(g,u,v)
                if rng.random()<.55:x=rng.randint(-7,7);ops.append(f"A {u+1} {v+1} {x}");[a.__setitem__(w,a[w]+x) for w in vertices]
                else:ops.append(f"M {u+1} {v+1}");out.append(max(a[w] for w in vertices))
        return f"{n} {q}\n"+" ".join(map(str,initial))+"\n"+edge_text+"\n".join(ops)+"\n","\n".join(map(str,out))+("\n" if out else "")
    if name == "h_connectivity_countdown":
        n=rng.randint(2,9);all_edges=[(u,v) for u in range(n) for v in range(u+1,n)];rng.shuffle(all_edges);edges=all_edges[:rng.randint(1,len(all_edges))];m=len(edges);q=rng.randint(1,25);active=set(range(m));ops=[];out=[]
        for _ in range(q):
            if rng.random()<.4 and active:e=rng.choice(tuple(active));active.remove(e);ops.append(f"D {e+1}")
            else:
                u=rng.randrange(n);v=rng.randrange(n);adj=[[]for _ in range(n)]
                for e in active:x,y=edges[e];adj[x].append(y);adj[y].append(x)
                seen={u};todo=[u]
                for x in todo:
                    for y in adj[x]:
                        if y not in seen:seen.add(y);todo.append(y)
                ops.append(f"Q {u+1} {v+1}");out.append("YES" if v in seen else "NO")
        return f"{n} {m} {q}\n"+"".join(f"{u+1} {v+1}\n" for u,v in edges)+"\n".join(ops)+"\n","\n".join(out)+("\n" if out else "")
    if name == "i_persistent_version_sums":
        n=rng.randint(1,10);q=rng.randint(1,25);initial=[rng.randint(-9,9) for _ in range(n)];versions=[initial[:]];ops=[];out=[]
        for _ in range(q):
            v=rng.randrange(len(versions))
            if rng.random()<.55:i=rng.randrange(n);x=rng.randint(-9,9);new=versions[v][:];new[i]=x;versions.append(new);ops.append(f"U {v} {i+1} {x}")
            else:l=rng.randrange(n);r=rng.randrange(l,n);ops.append(f"Q {v} {l+1} {r+1}");out.append(sum(versions[v][l:r+1]))
        return f"{n} {q}\n"+" ".join(map(str,initial))+"\n"+"\n".join(ops)+"\n","\n".join(map(str,out))+("\n" if out else "")
    if name == "k_sparse_rectangle_sums":
        q=rng.randint(1,25);points={};ops=[];out=[]
        for _ in range(q):
            if rng.random()<.6:x=rng.randint(-4,4);y=rng.randint(-4,4);v=rng.randint(-7,7);points[x,y]=points.get((x,y),0)+v;ops.append(f"U {x} {y} {v}")
            else:x1=rng.randint(-5,3);x2=rng.randint(x1,5);y1=rng.randint(-5,3);y2=rng.randint(y1,5);ops.append(f"Q {x1} {y1} {x2} {y2}");out.append(sum(v for (x,y),v in points.items() if x1<=x<=x2 and y1<=y<=y2))
        return f"{q}\n"+"\n".join(ops)+"\n","\n".join(map(str,out))+("\n" if out else "")
    if name == "l_profitable_disjoint_routes":
        n=rng.randint(2,8);possible=[(u,v) for u in range(n) for v in range(u+1,n)];rng.shuffle(possible);edges=[(u,v,rng.randint(-5,12)) for u,v in possible[:rng.randint(1,min(14,len(possible)))]];k=rng.randint(1,3);adj=[[]for _ in range(n)]
        for idx,(u,v,w) in enumerate(edges):adj[u].append((v,idx,w))
        paths=[]
        def enumerate_paths(u,used,profit):
            if u==n-1:paths.append((frozenset(used),profit));return
            for v,i,w in adj[u]:enumerate_paths(v,used+[i],profit+w)
        enumerate_paths(0,[],0);best=None
        for chosen in itertools.combinations(paths,k):
            sets=[x[0] for x in chosen]
            if sum(map(len,sets))==len(set().union(*sets)):best=max(best or -10**30,sum(x[1] for x in chosen))
        answer="IMPOSSIBLE" if best is None else str(best)
        return f"{n} {len(edges)} {k}\n"+"".join(f"{u+1} {v+1} {w}\n" for u,v,w in edges),answer+"\n"
    raise ValueError(name)


def main(problem: str):
    parser=argparse.ArgumentParser();parser.add_argument("--count",type=int,required=True);parser.add_argument("--seed",type=int,required=True);parser.add_argument("--out-dir",type=Path,required=True);args=parser.parse_args();args.out_dir.mkdir(parents=True,exist_ok=True);rng=random.Random(args.seed)
    for i in range(args.count):
        inp,out=case(problem,rng);stem=args.out_dir/f"case{i:03d}";stem.with_suffix(".in").write_text(inp);stem.with_suffix(".out").write_text(out)
