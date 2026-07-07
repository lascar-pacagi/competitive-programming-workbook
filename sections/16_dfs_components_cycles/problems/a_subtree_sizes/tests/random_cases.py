from __future__ import annotations

import argparse
import random
from pathlib import Path


def solve(case: str) -> str:
    data = list(map(int, case.split()))
    it = iter(data)
    n = next(it)
    adj = [[] for _ in range(n)]
    for _ in range(n - 1):
        u = next(it) - 1
        v = next(it) - 1
        adj[u].append(v)
        adj[v].append(u)
    parent = [-1] * n
    order: list[int] = []
    stack = [0]
    parent[0] = 0
    while stack:
        u = stack.pop()
        order.append(u)
        for v in adj[u]:
            if v == parent[u]:
                continue
            parent[v] = u
            stack.append(v)
    size = [1] * n
    for u in reversed(order):
        if u != 0:
            size[parent[u]] += size[u]
    return " ".join(map(str, size)) + "\n"


def make_case(rng: random.Random) -> str:
    n = rng.randint(1, 80)
    lines = [str(n)]
    for v in range(2, n + 1):
        parent = rng.randint(1, v - 1)
        lines.append(f"{parent} {v}")
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

