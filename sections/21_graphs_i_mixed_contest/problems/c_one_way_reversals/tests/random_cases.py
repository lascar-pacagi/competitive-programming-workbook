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
        adj[u].append((v, 0))
        adj[v].append((u, 1))
    inf = 10**9
    dist = [inf] * n
    dist[0] = 0
    dq = deque([0])
    while dq:
        u = dq.popleft()
        for v, w in adj[u]:
            nd = dist[u] + w
            if nd < dist[v]:
                dist[v] = nd
                (dq.appendleft if w == 0 else dq.append)(v)
    return f"{-1 if dist[-1] == inf else dist[-1]}\n"


def make_case(rng: random.Random) -> str:
    n = rng.randint(1, 60)
    m = rng.randint(0, 160)
    lines = [f"{n} {m}"]
    for _ in range(m):
        u = rng.randint(1, n)
        v = rng.randint(1, n)
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

