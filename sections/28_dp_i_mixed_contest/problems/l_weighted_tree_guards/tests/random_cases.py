import argparse
import itertools
import random
from pathlib import Path


def oracle(cost, edges):
    n = len(cost)
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    answer = sum(cost)
    for selected in itertools.product((False, True), repeat=n):
        valid = all(selected[u] or any(selected[v] for v in graph[u])
                    for u in range(n))
        if valid:
            answer = min(answer, sum(cost[u] for u in range(n)
                                     if selected[u]))
    return answer


def optimized(cost, edges):
    n = len(cost)
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    parent = [-2] * n
    parent[0] = -1
    order = [0]
    for u in order:
        for v in graph[u]:
            if v != parent[u]:
                parent[v] = u
                order.append(v)
    infinity = 10**30
    dp = [[0, 0, 0] for _ in range(n)]
    for u in reversed(order):
        selected = cost[u]
        base = 0
        force = infinity
        awaiting = 0
        for v in graph[u]:
            if parent[v] != u:
                continue
            selected += min(dp[v])
            best = min(dp[v][0], dp[v][1])
            base += best
            force = min(force, dp[v][0] - best)
            awaiting += dp[v][1]
        dp[u] = [selected, base + force, awaiting]
    return min(dp[0][0], dp[0][1])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)
    fixed = [([7], []), ([5, 1], [(0, 1)]),
             ([10, 1, 10], [(0, 1), (1, 2)]),
             ([1, 10, 10, 10], [(0, 1), (0, 2), (0, 3)])]

    for case in range(args.count):
        if case < len(fixed):
            cost, edges = fixed[case]
        elif case == len(fixed):
            n = 200000
            cost = [rng.randint(1, 10**9) for _ in range(n)]
            edges = [(rng.randrange(vertex), vertex)
                     for vertex in range(1, n)]
        else:
            n = rng.randint(1, 13)
            cost = [rng.randint(1, 30) for _ in range(n)]
            edges = [(rng.randrange(vertex), vertex)
                     for vertex in range(1, n)]
        answer = optimized(cost, edges) if len(cost) > 15 else oracle(cost, edges)
        stem = args.out_dir / f"case{case:03d}"
        lines = [str(len(cost)), " ".join(map(str, cost))]
        lines.extend(f"{u + 1} {v + 1}" for u, v in edges)
        stem.with_suffix(".in").write_text("\n".join(lines) + "\n")
        stem.with_suffix(".out").write_text(f"{answer}\n")


if __name__ == "__main__":
    main()
