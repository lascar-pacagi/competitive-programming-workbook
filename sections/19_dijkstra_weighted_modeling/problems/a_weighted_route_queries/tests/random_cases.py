from __future__ import annotations

import argparse, heapq, random
from pathlib import Path


def solve(case: str) -> str:
    data = list(map(int, case.split())); it = iter(data)
    n = next(it); m = next(it); s = next(it) - 1; qn = next(it)
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = next(it) - 1; v = next(it) - 1; w = next(it)
        adj[u].append((v, w))
    queries = [next(it) - 1 for _ in range(qn)]
    inf = 10**30; dist = [inf] * n; dist[s] = 0; heap = [(0, s)]
    while heap:
        d, u = heapq.heappop(heap)
        if d != dist[u]: continue
        for v, w in adj[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd; heapq.heappush(heap, (nd, v))
    return " ".join(str(-1 if dist[x] == inf else dist[x]) for x in queries) + "\n"


def make_case(rng: random.Random) -> str:
    n = rng.randint(1, 60); m = rng.randint(0, 180); s = rng.randint(1, n); q = rng.randint(1, 80)
    lines = [f"{n} {m} {s} {q}"]
    for _ in range(m):
        lines.append(f"{rng.randint(1,n)} {rng.randint(1,n)} {rng.randint(0,1000)}")
    lines.append(" ".join(str(rng.randint(1, n)) for _ in range(q)))
    return "\n".join(lines) + "\n"


def main() -> None:
    p = argparse.ArgumentParser(); p.add_argument("--count", type=int, required=True); p.add_argument("--seed", type=int, required=True); p.add_argument("--out-dir", type=Path, required=True)
    args = p.parse_args(); rng = random.Random(args.seed); args.out_dir.mkdir(parents=True, exist_ok=True)
    for i in range(args.count):
        case = make_case(rng)
        (args.out_dir / f"case_{i:03d}.in").write_text(case)
        (args.out_dir / f"case_{i:03d}.out").write_text(solve(case))


if __name__ == "__main__":
    main()

