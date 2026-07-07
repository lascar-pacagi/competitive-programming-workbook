from __future__ import annotations

import argparse
import random
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
    color = [0] * n
    for start in range(n):
        if color[start] != 0:
            continue
        color[start] = 1
        stack = [(start, 0)]
        while stack:
            u, i = stack[-1]
            if i == len(adj[u]):
                color[u] = 2
                stack.pop()
                continue
            v = adj[u][i]
            stack[-1] = (u, i + 1)
            if color[v] == 0:
                color[v] = 1
                stack.append((v, 0))
            elif color[v] == 1:
                return "CYCLIC\n"
    return "ACYCLIC\n"


def make_case(rng: random.Random) -> str:
    n = rng.randint(1, 60)
    m = 0 if n == 1 else rng.randint(0, 160)
    lines = [f"{n} {m}"]
    for _ in range(m):
        u = rng.randint(1, n)
        v = rng.randint(1, n - 1)
        if v >= u:
            v += 1
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
    for index in range(args.count):
        case = make_case(rng)
        (args.out_dir / f"case_{index:03d}.in").write_text(case, encoding="utf-8")
        (args.out_dir / f"case_{index:03d}.out").write_text(solve(case), encoding="utf-8")


if __name__ == "__main__":
    main()
