from __future__ import annotations

import argparse
import random
from collections import deque
from pathlib import Path


def solve(case: str) -> str:
    data = list(map(int, case.split()))
    it = iter(data)
    t = next(it)
    out: list[str] = []
    for _ in range(t):
        n = next(it)
        m = next(it)
        adj = [[] for _ in range(n)]
        for _ in range(m):
            u = next(it) - 1
            v = next(it) - 1
            adj[u].append(v)
            adj[v].append(u)
        seen = [False] * n
        sizes: list[int] = []
        for start in range(n):
            if seen[start]:
                continue
            seen[start] = True
            q = deque([start])
            size = 0
            while q:
                u = q.popleft()
                size += 1
                for v in adj[u]:
                    if not seen[v]:
                        seen[v] = True
                        q.append(v)
            sizes.append(size)
        sizes.sort()
        out.append(str(len(sizes)))
        out.append(" ".join(map(str, sizes)))
    return "\n".join(out) + "\n"


def make_case(rng: random.Random) -> str:
    t = rng.randint(1, 5)
    lines = [str(t)]
    for _ in range(t):
        n = rng.randint(1, 35)
        max_edges = min(90, n * (n - 1) // 2)
        m = rng.randint(0, max_edges)
        lines.append(f"{n} {m}")
        edges: list[tuple[int, int]] = []
        for _ in range(m):
            u = rng.randint(1, n)
            v = rng.randint(1, n - 1)
            if v >= u:
                v += 1
            edges.append((u, v))
        for u, v in edges:
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

