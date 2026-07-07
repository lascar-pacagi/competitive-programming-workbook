from __future__ import annotations

import argparse
import random
from pathlib import Path


MOD = 1_000_000_007


def solve(case: str) -> str:
    data = list(map(int, case.split()))
    n = data[0]
    adj = [[] for _ in range(n)]
    it = iter(data[1:])
    for u, v in zip(it, it):
        u -= 1
        v -= 1
        adj[u].append(v)
        adj[v].append(u)
    parent = [-1] * n
    parent[0] = 0
    order = [0]
    for u in order:
        for v in adj[u]:
            if parent[v] == -1:
                parent[v] = u
                order.append(v)
    white = [1] * n
    black = [1] * n
    for u in reversed(order):
        for v in adj[u]:
            if parent[v] == u:
                white[u] = white[u] * (white[v] + black[v]) % MOD
                black[u] = black[u] * white[v] % MOD
    return f"{(white[0] + black[0]) % MOD}\n"


def make_case(rng: random.Random) -> str:
    n = rng.randint(1, 100)
    lines = [str(n)]
    for v in range(2, n + 1):
        u = rng.randint(1, v - 1)
        lines.append(f"{u} {v}")
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    rng = random.Random(args.seed)
    args.out_dir.mkdir(parents=True, exist_ok=True)
    for i in range(args.count):
        case = make_case(rng)
        (args.out_dir / f"case_{i:03d}.in").write_text(case)
        (args.out_dir / f"case_{i:03d}.out").write_text(solve(case))


if __name__ == "__main__":
    main()

