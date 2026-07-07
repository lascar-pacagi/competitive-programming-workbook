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
    qn = next(it)
    duration = [next(it) for _ in range(n)]
    adj = [[] for _ in range(n)]
    indeg = [0] * n
    for _ in range(m):
        a = next(it) - 1
        b = next(it) - 1
        adj[a].append(b)
        indeg[b] += 1
    queries = [next(it) - 1 for _ in range(qn)]
    start = [0] * n
    finish = duration[:]
    dq = deque(i for i in range(n) if indeg[i] == 0)
    processed = 0
    while dq:
        u = dq.popleft()
        processed += 1
        finish[u] = start[u] + duration[u]
        for v in adj[u]:
            start[v] = max(start[v], finish[u])
            indeg[v] -= 1
            if indeg[v] == 0:
                dq.append(v)
    if processed != n:
        return "IMPOSSIBLE\n"
    return " ".join(str(finish[x]) for x in queries) + "\n"


def make_case(rng: random.Random) -> str:
    n = rng.randint(1, 60)
    qn = rng.randint(1, 80)
    duration = [rng.randint(1, 1000) for _ in range(n)]
    edges: set[tuple[int, int]] = set()
    if rng.random() < 0.8:
        perm = list(range(1, n + 1))
        rng.shuffle(perm)
        pos = {v: i for i, v in enumerate(perm)}
        if n >= 2:
            for _ in range(rng.randint(0, 160)):
                a, b = rng.sample(range(1, n + 1), 2)
                if pos[a] > pos[b]:
                    a, b = b, a
                edges.add((a, b))
    else:
        if n >= 2:
            cyc = rng.sample(range(1, n + 1), rng.randint(2, min(n, 7)))
            for i in range(len(cyc)):
                edges.add((cyc[i], cyc[(i + 1) % len(cyc)]))
        if n >= 2:
            for _ in range(rng.randint(0, 60)):
                a, b = rng.sample(range(1, n + 1), 2)
                edges.add((a, b))
    lines = [f"{n} {len(edges)} {qn}", " ".join(map(str, duration))]
    lines.extend(f"{a} {b}" for a, b in sorted(edges))
    lines.append(" ".join(str(rng.randint(1, n)) for _ in range(qn)))
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
