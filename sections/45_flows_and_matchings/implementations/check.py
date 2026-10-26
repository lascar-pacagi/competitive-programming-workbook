"""Check both reusable language implementations against exhaustive small oracles."""
from functools import lru_cache
from pathlib import Path
import random
import subprocess
import tempfile

from dinic import Dinic
from bipartite_matching import BipartiteMatching

HERE = Path(__file__).resolve().parent


def cut_oracle(n, edges):
    return min(sum(c for u, v, c in edges if mask >> u & 1 and not mask >> v & 1)
               for mask in range(1 << n) if mask & 1 and not mask >> (n - 1) & 1)


def matching_oracle(n, m, edges):
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)

    @lru_cache(None)
    def visit(u, mask):
        if u == n:
            return 0
        return max([visit(u + 1, mask)] + [1 + visit(u + 1, mask | 1 << v)
                   for v in adj[u] if not mask >> v & 1])
    return visit(0, 0)


def verify_flow(n, edges, value, flows, side, optimum):
    assert value == optimum, (value, optimum, edges)
    balance = [0] * n
    for (u, v, c), f in zip(edges, flows):
        assert 0 <= f <= c
        balance[u] += f
        balance[v] -= f
    assert balance == [value] + [0] * (n - 2) + [-value]
    assert side[0] and not side[-1]
    assert sum(c for u, v, c in edges if side[u] and not side[v]) == value


def verify_matching(n, m, edges, pairs, optimum):
    assert len(pairs) == optimum
    assert len({u for u, _ in pairs}) == len(pairs)
    assert len({v for _, v in pairs}) == len(pairs)
    assert all((u, v) in edges for u, v in pairs)


def main():
    rng = random.Random(450044)
    flows = [(6, [(0, 1, 1), (0, 2, 1), (1, 3, 1), (1, 4, 1),
                  (2, 3, 1), (3, 5, 1), (4, 5, 1)], 2)]
    for _ in range(250):
        n = rng.randint(2, 7)
        edges = [(rng.randrange(n), rng.randrange(n), rng.choice([0, 1, 3, 10**9]))
                 for _ in range(rng.randrange(22))]
        flows.append((n, edges, cut_oracle(n, edges)))
    flows.append((10000, [(u, u + 1, 7) for u in range(9999)], 7))
    matches = [(2, 2, [(0, 0), (0, 1), (1, 0)], 2), (0, 0, [], 0)]
    for _ in range(250):
        n, m = rng.randrange(8), rng.randrange(8)
        edges = [(u, v) for u in range(n) for v in range(m) if rng.random() < .45]
        matches.append((n, m, edges, matching_oracle(n, m, edges)))
    for n, edges, optimum in flows:
        network = Dinic(n)
        ids = [network.add_edge(*edge) for edge in edges]
        value = network.max_flow(0, n - 1)
        verify_flow(n, edges, value, [network.cap[e ^ 1] for e in ids],
                    network.reachable(0), optimum)
        assert network.max_flow(0, n - 1) == 0
    for n, m, edges, optimum in matches:
        matching = BipartiteMatching(n, m)
        for edge in edges:
            matching.add_edge(*edge)
        pairs = matching.maximum_matching()
        verify_matching(n, m, edges, pairs, optimum)
        assert matching.maximum_matching() == pairs
        assert all(matching.right[v] == u for u, v in pairs)

    adapter = r'''
#include <iostream>
#include "dinic.hpp"
#include "bipartite_matching.hpp"
int main() {
    char kind;
    while (std::cin >> kind) {
        int n, m, count;
        if (kind == 'F') {
            std::cin >> n >> count;
            Dinic graph(n);
            for (int i=0,u,v; i<count; ++i) {
                long long c; std::cin >> u >> v >> c;
                graph.add_edge(u,v,c);
            }
            std::cout << graph.max_flow(0,n-1);
            for (int i=0; i<count; ++i) std::cout << ' ' << graph.edges[2*i+1].cap;
            for (bool b:graph.reachable(0)) std::cout << ' ' << b;
            if (graph.max_flow(0,n-1)!=0) return 2;
        } else {
            std::cin >> n >> m >> count;
            BipartiteMatching graph(n,m);
            for (int i=0,u,v;i<count;++i) {std::cin >> u >> v; graph.add_edge(u,v);}
            auto pairs=graph.maximum_matching();
            std::cout << pairs.size();
            for(auto [u,v]:pairs) std::cout << ' ' << u << ' ' << v;
            if (graph.maximum_matching()!=pairs) return 3;
        }
        std::cout << '\n';
    }
}
'''
    data = []
    for n, edges, _ in flows:
        data.append(f'F {n} {len(edges)}\n' + '\n'.join(f'{u} {v} {c}' for u, v, c in edges))
    for n, m, edges, _ in matches:
        data.append(f'M {n} {m} {len(edges)}\n' + '\n'.join(f'{u} {v}' for u, v in edges))
    with tempfile.TemporaryDirectory(prefix='flow45-check-') as folder:
        cpp = Path(folder) / 'adapter.cpp'
        executable = Path(folder) / 'adapter'
        cpp.write_text(adapter)
        subprocess.run(['g++', '-std=c++17', '-O2', '-I', str(HERE), str(cpp), '-o', str(executable)], check=True)
        result = subprocess.run([str(executable)], input='\n'.join(data) + '\n',
                                text=True, capture_output=True, check=True)
    lines = iter(result.stdout.splitlines())
    for n, edges, optimum in flows:
        row = list(map(int, next(lines).split()))
        verify_flow(n, edges, row[0], row[1:1 + len(edges)], row[1 + len(edges):], optimum)
    for n, m, edges, optimum in matches:
        row = list(map(int, next(lines).split()))
        pairs = list(zip(row[1::2], row[2::2]))
        assert len(pairs) == row[0]
        verify_matching(n, m, edges, pairs, optimum)
    print(f'Accepted: {len(flows)} flow and {len(matches)} matching cases in C++ and Python.')


if __name__ == '__main__':
    main()
