from __future__ import annotations

import argparse
import random
from collections import deque
from pathlib import Path


def solve(case: str) -> str:
    data = list(map(int, case.split()))
    it = iter(data)
    n = next(it)
    m = next(it)
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = next(it) - 1
        v = next(it) - 1
        adj[u].append(v)
        adj[v].append(u)
    seen = [False] * n
    for start in range(n):
        if seen[start]:
            continue
        vertices = 0
        edge_twice = 0
        seen[start] = True
        q = deque([start])
        while q:
            u = q.popleft()
            vertices += 1
            edge_twice += len(adj[u])
            for v in adj[u]:
                if not seen[v]:
                    seen[v] = True
                    q.append(v)
        if edge_twice // 2 >= vertices:
            return "CYCLIC\n"
    return "ACYCLIC\n"


def make_case(rng: random.Random) -> str:
    n = rng.randint(1, 60)
    possible = [(u, v) for u in range(1, n + 1) for v in range(u + 1, n + 1)]
    rng.shuffle(possible)
    m = rng.randint(0, min(len(possible), 120))
    edges = possible[:m]
    lines = [f"{n} {m}"]
    lines.extend(f"{u} {v}" for u, v in edges)
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()

    rng = random.Random(args.seed)
    args.out_dir.mkdir(parents=True, exist_ok=True)
    for index in range(args.count):
        case = make_case(rng)
        (args.out_dir / f"case_{index:03d}.in").write_text(case, encoding="utf-8")
        (args.out_dir / f"case_{index:03d}.out").write_text(solve(case), encoding="utf-8")


if __name__ == "__main__":
    main()

