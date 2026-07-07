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
    s = next(it) - 1
    q_count = next(it)
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = next(it) - 1
        v = next(it) - 1
        adj[u].append(v)
    queries = [next(it) - 1 for _ in range(q_count)]
    dist = [-1] * n
    dist[s] = 0
    q = deque([s])
    while q:
        u = q.popleft()
        for v in adj[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                q.append(v)
    return " ".join(str(dist[x]) for x in queries) + "\n"


def make_case(rng: random.Random) -> str:
    n = rng.randint(1, 60)
    max_edges = min(220, n * n)
    m = rng.randint(0, max_edges)
    s = rng.randint(1, n)
    q_count = rng.randint(1, 80)
    lines = [f"{n} {m} {s} {q_count}"]
    for _ in range(m):
        lines.append(f"{rng.randint(1, n)} {rng.randint(1, n)}")
    queries = [str(rng.randint(1, n)) for _ in range(q_count)]
    lines.append(" ".join(queries))
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

