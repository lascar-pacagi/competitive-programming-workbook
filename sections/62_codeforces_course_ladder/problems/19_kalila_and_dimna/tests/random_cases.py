from __future__ import annotations

import argparse
import random
from pathlib import Path


def oracle(n: int, edges: list[tuple[int, int, int]]) -> int:
    """Floyd-Warshall on the explicit two-parity graph for tiny cases."""
    states = 2 * n
    inf = 10**18
    dist = [[inf] * states for _ in range(states)]
    for state in range(states):
        dist[state][state] = 0
    for u, v, weight in edges:
        for parity in range(2):
            source = 2 * u + parity
            target = 2 * v + (parity ^ 1)
            dist[source][target] = min(dist[source][target], weight)

    for middle in range(states):
        for start in range(states):
            through_middle = dist[start][middle]
            if through_middle == inf:
                continue
            for end in range(states):
                candidate = through_middle + dist[middle][end]
                if candidate < dist[start][end]:
                    dist[start][end] = candidate

    answer = dist[0][2 * (n - 1)]
    return -1 if answer == inf else answer


def write_case(
    out_dir: Path,
    number: int,
    n: int,
    edges: list[tuple[int, int, int]],
    expected: int | None = None,
) -> None:
    lines = [f"{n} {len(edges)}"]
    lines.extend(f"{u + 1} {v + 1} {weight}" for u, v, weight in edges)
    stem = out_dir / f"case{number:03d}"
    stem.with_suffix(".in").write_text("\n".join(lines) + "\n", encoding="utf-8")
    if expected is None:
        expected = oracle(n, edges)
    stem.with_suffix(".out").write_text(f"{expected}\n", encoding="utf-8")


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
            edges = [(vertex, vertex + 1, 1) for vertex in range(n - 1)]
            edges.append((0, 2, 1))
            write_case(args.out_dir, case, n, edges, expected=n - 2)
        else:
            n = rng.randint(1, 9)
            m = rng.randint(0, min(22, n * (n - 1)))
            edges = [
                (rng.randrange(n), rng.randrange(n), rng.randint(0, 30))
                for _ in range(m)
            ]
            edges = [(u, v, weight) for u, v, weight in edges if u != v]
            write_case(args.out_dir, case, n, edges)


if __name__ == "__main__":
    main()
