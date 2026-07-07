from __future__ import annotations

import argparse
import heapq
import random
from pathlib import Path


def solve(case: str) -> str:
    data = list(map(int, case.split()))
    it = iter(data)
    n = next(it)
    m = next(it)
    adj = [[] for _ in range(n)]
    indeg = [0] * n
    for _ in range(m):
        a = next(it) - 1
        b = next(it) - 1
        adj[a].append(b)
        indeg[b] += 1
    heap = [i for i in range(n) if indeg[i] == 0]
    heapq.heapify(heap)
    order: list[int] = []
    while heap:
        u = heapq.heappop(heap)
        order.append(u)
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                heapq.heappush(heap, v)
    if len(order) != n:
        return "IMPOSSIBLE\n"
    return " ".join(str(x + 1) for x in order) + "\n"


def make_case(rng: random.Random) -> str:
    n = rng.randint(1, 60)
    edges: set[tuple[int, int]] = set()
    if rng.random() < 0.75:
        perm = list(range(1, n + 1))
        rng.shuffle(perm)
        pos = {v: i for i, v in enumerate(perm)}
        attempts = rng.randint(0, 160)
        for _ in range(attempts):
            a, b = rng.sample(range(1, n + 1), 2)
            if pos[a] > pos[b]:
                a, b = b, a
            edges.add((a, b))
    else:
        if n >= 2:
            k = rng.randint(2, min(n, 8))
            cycle = rng.sample(range(1, n + 1), k)
            for i in range(k):
                edges.add((cycle[i], cycle[(i + 1) % k]))
        for _ in range(rng.randint(0, 80)):
            a, b = rng.sample(range(1, n + 1), 2)
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

