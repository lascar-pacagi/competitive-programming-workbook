"""Independent small oracles and construction-based performance cases."""
import argparse
from pathlib import Path
import random


def random_case(name, rng):
    n = rng.randint(1, 14); q = 40
    if name == 'i_dynamic_brackets':
        s = [rng.choice('()') for _ in range(n)]; initial = ''.join(s)
        ops = []; out = []
        for _ in range(q):
            if rng.random() < .4:
                i = rng.randrange(n); s[i] = ')' if s[i] == '(' else '('
                ops.append(f'T {i+1}')
            else:
                l = rng.randrange(n); r = rng.randrange(l, n)
                ops.append(f'Q {l+1} {r+1}')
                balance = 0; valid = True
                for c in s[l:r+1]:
                    balance += 1 if c == '(' else -1
                    if balance < 0: valid = False
                out.append('YES' if valid and balance == 0 else 'NO')
        return f'{n} {q}\n{initial}\n'+'\n'.join(ops)+'\n','\n'.join(out)+'\n'
    if name == 'i_rerooted_subtree_sums':
        edges = [(rng.randrange(v), v) for v in range(1, n)]
        rng.shuffle(edges); g = [[] for _ in range(n)]
        for u, v in edges: g[u].append(v); g[v].append(u)
        a = [rng.randint(-10, 10) for _ in range(n)]; initial = a[:]
        root = 0; ops = []; out = []
        for _ in range(q):
            u = rng.randrange(n); op = rng.choice('RUQQ')
            if op == 'R': root = u; ops.append(f'R {u+1}')
            elif op == 'U':
                a[u] = rng.randint(-10, 10); ops.append(f'U {u+1} {a[u]}')
            else:
                parent = [-1]*n; parent[root] = root; todo = [root]
                for v in todo:
                    for w in g[v]:
                        if parent[w] == -1: parent[w] = v; todo.append(w)
                descendants = [u]
                for v in descendants:
                    descendants.extend(w for w in g[v] if parent[w] == v and w != v)
                out.append(sum(a[v] for v in descendants)); ops.append(f'Q {u+1}')
        return f'{n} {q}\n'+' '.join(map(str, initial))+'\n'+''.join(f'{u+1} {v+1}\n' for u,v in edges)+'\n'.join(ops)+'\n','\n'.join(map(str, out))+'\n'
    if name == 'j_minimum_bottleneck_routes':
        m = rng.randint(0, 35); edges = []
        inf = 10**18; d = [[inf]*n for _ in range(n)]
        for i in range(n): d[i][i] = 0
        for _ in range(m):
            u, v, w = rng.randrange(n), rng.randrange(n), rng.randint(0, 20)
            edges.append((u, v, w)); d[u][v] = d[v][u] = min(d[u][v], w)
        # Minimax Floyd-Warshall has no spanning-tree assumptions.
        for k in range(n):
            for u in range(n):
                for v in range(n): d[u][v] = min(d[u][v], max(d[u][k], d[k][v]))
        queries = [(rng.randrange(n), rng.randrange(n)) for _ in range(q)]
        return f'{n} {m} {q}\n'+''.join(f'{u+1} {v+1} {w}\n' for u,v,w in edges)+''.join(f'{u+1} {v+1}\n' for u,v in queries),''.join(f'{d[u][v] if d[u][v] != inf else -1}\n' for u,v in queries)
    if name == 'k_sliding_window_inversions':
        k = rng.randint(1, n); a = [rng.randint(-5, 5) for _ in range(n)]
        out = [sum(a[i] > a[j] for i in range(l,l+k) for j in range(i+1,l+k)) for l in range(n-k+1)]
        return f'{n} {k}\n'+' '.join(map(str,a))+'\n',' '.join(map(str,out))+'\n'
    raise ValueError(name)


def stress_cases(name):
    n = q = 200000
    if name == 'i_dynamic_brackets':
        # A closing bracket moved to the front keeps total balance zero.
        ops = 'T 1\nT 200000\nQ 1 200000\nT 1\nT 200000\nQ 1 200000\n'
        count = q//6*6
        yield 'prefix_violation', f'{n} {count}\n'+'()'*(n//2)+'\n'+ops*(count//6),'NO\nYES\n'*(count//6)
        yield 'long_ranges', f'{n} {q}\n'+'()'*(n//2)+'\n'+''.join(f'Q {2*(i%(n//4))+1} {n}\n' for i in range(q)), 'YES\n'*q
    elif name == 'i_rerooted_subtree_sums':
        header = f'{n} {q}\n'+'1 '*n+'\n'+''.join(f'{i} {i+1}\n' for i in range(1,n))
        ops = []; out = []
        for i in range(q//4):
            x = i+1; u = i+2
            ops.extend([f'R {n}',f'U 1 {x}',f'Q {u}',f'R 1'])
            out.append(x+u-1)
        yield 'changing_root_chain', header+'\n'.join(ops)+'\n','\n'.join(map(str,out))+'\n'
        yield 'ancestor_lifting', header+f'R {n}\n'+''.join(f'Q {i}\n' for i in range(1,q)), ''.join(f'{i}\n' for i in range(1,q))
    elif name == 'j_minimum_bottleneck_routes':
        # A cheap chain wins over one expensive shortcut; final vertex isolated.
        edges = ''.join(f'{i} {i+1} {i}\n' for i in range(1,n-1))+f'1 {n-1} 1000000000\n1 1 0\n'
        queries = []; out = []
        for i in range(q):
            u = i%n+1; queries.append(f'1 {u}')
            out.append(-1 if u==n else max(0,u-1))
        yield 'cycle_and_isolated_vertex',f'{n} {n} {q}\n'+edges+'\n'.join(queries)+'\n','\n'.join(map(str,out))+'\n'
    elif name == 'k_sliding_window_inversions':
        k = n//2
        yield 'decreasing',f'{n} {k}\n'+' '.join(map(str,range(n,0,-1)))+'\n',(str(k*(k-1)//2)+' ')*(n-k+1)+'\n'
        yield 'equal_values',f'{n} {k}\n'+'7 '*n+'\n','0 '*(n-k+1)+'\n'
    else: raise ValueError(name)


def main(name, stress=False):
    parser = argparse.ArgumentParser()
    parser.add_argument('--out-dir', type=Path, required=True)
    if not stress:
        parser.add_argument('--count', type=int, required=True)
        parser.add_argument('--seed', type=int, required=True)
    args = parser.parse_args(); args.out_dir.mkdir(parents=True, exist_ok=True)
    if stress: cases = stress_cases(name)
    else:
        rng = random.Random(args.seed)
        cases = ((f'case{i:03d}', *random_case(name, rng)) for i in range(args.count))
    for stem, inp, out in cases:
        (args.out_dir/f'{stem}.in').write_text(inp)
        (args.out_dir/f'{stem}.out').write_text(out)
