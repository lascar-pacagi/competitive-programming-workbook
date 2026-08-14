import argparse
import random
from collections import deque
from pathlib import Path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)
    for case in range(args.count):
        n = rng.randint(2, 16)
        edges = [(u, v) for u in range(n) for v in range(u + 1, n) if rng.random() < .18]
        stations = rng.sample(range(n), rng.randint(1, n))
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v); graph[v].append(u)
        dist = [-1] * n
        q = deque(stations)
        for s in stations: dist[s] = 0
        while q:
            u = q.popleft()
            for v in graph[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1; q.append(v)
        far = max(dist)
        answer = f"{dist.count(-1)} {dist.index(far)+1} {far}\n"
        lines = [f"{n} {len(edges)} {len(stations)}"]
        lines += [f"{u+1} {v+1}" for u, v in edges]
        lines.append(" ".join(str(s+1) for s in stations))
        stem = args.out_dir / f"case{case:03d}"
        stem.with_suffix(".in").write_text("\n".join(lines) + "\n")
        stem.with_suffix(".out").write_text(answer)


if __name__ == "__main__":
    main()
