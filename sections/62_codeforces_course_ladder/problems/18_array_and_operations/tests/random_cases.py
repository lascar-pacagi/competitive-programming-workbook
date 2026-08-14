from __future__ import annotations

import argparse
import random
from collections import deque
from pathlib import Path


def reachability(n: int, edges: list[tuple[int, int, int]]) -> list[list[bool]]:
    graph = [[] for _ in range(n)]
    for u, v, _ in edges:
        graph[u].append(v)
        graph[v].append(u)

    connected = [[False] * n for _ in range(n)]
    for start in range(n):
        connected[start][start] = True
        queue = deque([start])
        while queue:
            u = queue.popleft()
            for v in graph[u]:
                if not connected[start][v]:
                    connected[start][v] = True
                    queue.append(v)
    return connected


def oracle(n: int, edges: list[tuple[int, int, int]]) -> int:
    original = reachability(n, edges)
    total = sum(weight for _, _, weight in edges)
    best = 0

    for kept_mask in range(1 << len(edges)):
        kept_edges = [
            edge for index, edge in enumerate(edges) if kept_mask & (1 << index)
        ]
        kept_connected = reachability(n, kept_edges)
        valid = all(
            kept_connected[a][b] == original[a][b]
            for a in range(n)
            for b in range(n)
        )
        if valid:
            kept_cost = sum(weight for _, _, weight in kept_edges)
            best = max(best, total - kept_cost)
    return best


def scale_case() -> tuple[str, str]:
    n = 100001
    edges = [(vertex, vertex + 1, 1) for vertex in range(1, n)]
    edges.extend((vertex, vertex + 2, 1000) for vertex in range(1, n - 1))
    edges.append((1, n, 1000))

    lines = [f"{n} {len(edges)}"]
    lines.extend(f"{u} {v} {w}" for u, v, w in edges)
    return "\n".join(lines) + "\n", "100000000\n"


def small_case(rng: random.Random) -> tuple[str, str]:
    n = rng.randint(1, 7)
    pairs = [(u, v) for u in range(n) for v in range(u + 1, n)]
    m = rng.randint(0, min(10, len(pairs) * 2)) if pairs else 0
    edges = [
        (*rng.choice(pairs), rng.randint(0, 20))
        for _ in range(m)
    ]
    lines = [f"{n} {m}"]
    lines.extend(f"{u + 1} {v + 1} {w}" for u, v, w in edges)
    case = "\n".join(lines) + "\n"
    return case, f"{oracle(n, edges)}\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()

    rng = random.Random(args.seed)
    args.out_dir.mkdir(parents=True, exist_ok=True)
    for index in range(args.count):
        if index == 0:
            case, expected = scale_case()
        else:
            case, expected = small_case(rng)
        prefix = args.out_dir / f"case{index:03d}"
        prefix.with_suffix(".in").write_text(case, encoding="utf-8")
        prefix.with_suffix(".out").write_text(expected, encoding="utf-8")


if __name__ == "__main__":
    main()
