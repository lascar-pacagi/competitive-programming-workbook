import argparse
import heapq
import random
from pathlib import Path


def oracle(n, graph):
    if n == 1: return 0
    inf = 10**18
    dist = [[inf] * 2 for _ in range(n)]
    heap = []
    for v, w, c in graph[0]:
        if w < dist[v][c]:
            dist[v][c] = w; heapq.heappush(heap, (w, v, c))
    while heap:
        d, u, last = heapq.heappop(heap)
        if d != dist[u][last]: continue
        for v, w, c in graph[u]:
            if c != last and d + w < dist[v][c]:
                dist[v][c] = d + w; heapq.heappush(heap, (d + w, v, c))
    ans = min(dist[-1])
    return -1 if ans == inf else ans


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)
    for case in range(args.count):
        n = rng.randint(1, 10)
        m = rng.randint(0, 30)
        edges = []
        graph = [[] for _ in range(n)]
        for _ in range(m):
            u, v = rng.randrange(n), rng.randrange(n)
            w, c = rng.randint(0, 20), rng.randrange(2)
            edges.append((u, v, w, c)); graph[u].append((v, w, c))
        lines = [f"{n} {m}"] + [
            f"{u+1} {v+1} {w} {'R' if c == 0 else 'B'}" for u, v, w, c in edges
        ]
        stem = args.out_dir / f"case{case:03d}"
        stem.with_suffix(".in").write_text("\n".join(lines) + "\n")
        stem.with_suffix(".out").write_text(f"{oracle(n, graph)}\n")


if __name__ == "__main__":
    main()
