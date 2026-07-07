from __future__ import annotations

import argparse, heapq, random
from pathlib import Path


def solve(case: str) -> str:
    data = list(map(int, case.split())); it = iter(data); n = next(it); m = next(it)
    cost = [[next(it) for _ in range(m)] for _ in range(n)]
    inf = 10**30; dist = [[inf]*m for _ in range(n)]; dist[0][0] = cost[0][0]
    heap = [(dist[0][0], 0, 0)]
    while heap:
        d, r, c = heapq.heappop(heap)
        if d != dist[r][c]: continue
        for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
            nr, nc = r+dr, c+dc
            if 0 <= nr < n and 0 <= nc < m:
                nd = d + cost[nr][nc]
                if nd < dist[nr][nc]:
                    dist[nr][nc] = nd; heapq.heappush(heap, (nd, nr, nc))
    return f"{dist[n-1][m-1]}\n"


def make_case(rng: random.Random) -> str:
    n = rng.randint(1, 25); m = rng.randint(1, 25)
    lines = [f"{n} {m}"]
    for _ in range(n):
        lines.append(" ".join(str(rng.randint(0, 1000)) for _ in range(m)))
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

