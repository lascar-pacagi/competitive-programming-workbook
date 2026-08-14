from __future__ import annotations

import argparse
import random
from pathlib import Path


def classify_by_cycle_search(n: int, edges: list[tuple[int, int]]) -> tuple[int, int]:
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    seen = [False] * n
    trees = cyclic = 0
    for start in range(n):
        if seen[start]:
            continue
        has_cycle = False
        stack = [(start, -1)]
        seen[start] = True
        while stack:
            u, parent = stack.pop()
            for v in graph[u]:
                if not seen[v]:
                    seen[v] = True
                    stack.append((v, u))
                elif v != parent:
                    has_cycle = True
        if has_cycle:
            cyclic += 1
        else:
            trees += 1
    return trees, cyclic


def write_case(out_dir: Path, number: int, n: int, edges: list[tuple[int, int]], expected: str | None = None) -> None:
    lines = [f"{n} {len(edges)}"]
    lines.extend(f"{u + 1} {v + 1}" for u, v in edges)
    if expected is None:
        trees, cyclic = classify_by_cycle_search(n, edges)
        expected = f"{trees} {cyclic}\n"
    stem = out_dir / f"case{number:03d}"
    stem.with_suffix(".in").write_text("\n".join(lines) + "\n", encoding="utf-8")
    stem.with_suffix(".out").write_text(expected, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)

    for case in range(args.count):
        if case == 0:
            n = 200_000
            edges = [(v, v + 1) for v in range(n - 1)]
            edges.append((0, n - 1))
            write_case(args.out_dir, case, n, edges, "0 1\n")
            continue
        else:
            n = rng.randint(1, 32)
            edges = []
            for u in range(n):
                for v in range(u + 1, n):
                    if rng.random() < 0.11:
                        edges.append((u, v))
            rng.shuffle(edges)
        write_case(args.out_dir, case, n, edges)


if __name__ == "__main__":
    main()
