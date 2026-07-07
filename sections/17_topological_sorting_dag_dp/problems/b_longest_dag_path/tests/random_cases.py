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
    indeg = [0] * n
    for _ in range(m):
        u = next(it) - 1
        v = next(it) - 1
        adj[u].append(v)
        indeg[v] += 1
    q = deque(i for i in range(n) if indeg[i] == 0)
    dp = [0] * n
    while q:
        u = q.popleft()
        for v in adj[u]:
            dp[v] = max(dp[v], dp[u] + 1)
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    return str(max(dp, default=0)) + "\n"


def make_case(rng: random.Random) -> str:
    n = rng.randint(1, 70)
    perm = list(range(1, n + 1))
    rng.shuffle(perm)
    pos = {v: i for i, v in enumerate(perm)}
    edges: set[tuple[int, int]] = set()
    for _ in range(rng.randint(0, 180)):
        a, b = rng.sample(range(1, n + 1), 2)
        if pos[a] > pos[b]:
            a, b = b, a
        edges.add((a, b))
    lines = [f"{n} {len(edges)}"]
    lines.extend(f"{a} {b}" for a, b in sorted(edges))
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

