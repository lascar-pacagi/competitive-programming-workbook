from __future__ import annotations

import argparse, heapq, random
from pathlib import Path


def solve(case: str) -> str:
    data = list(map(int, case.split())); it = iter(data); n = next(it); m = next(it)
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = next(it)-1; v = next(it)-1; w = next(it)
        adj[u].append((v,w))
    inf = 10**30; dist = [[inf, inf] for _ in range(n)]; dist[0][0] = 0; heap = [(0,0,0)]
    while heap:
        d,u,used = heapq.heappop(heap)
        if d != dist[u][used]: continue
        for v,w in adj[u]:
            nd = d + w
            if nd < dist[v][used]:
                dist[v][used] = nd; heapq.heappush(heap,(nd,v,used))
            if used == 0:
                nd = d + w//2
                if nd < dist[v][1]:
                    dist[v][1] = nd; heapq.heappush(heap,(nd,v,1))
    ans = min(dist[-1])
    return f"{-1 if ans == inf else ans}\n"


def make_case(rng: random.Random) -> str:
    n = rng.randint(1,60); m = rng.randint(0,180)
    lines = [f"{n} {m}"]
    for _ in range(m):
        lines.append(f"{rng.randint(1,n)} {rng.randint(1,n)} {rng.randint(0,1000)}")
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

