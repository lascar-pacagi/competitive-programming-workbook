from __future__ import annotations

import argparse
import random
from pathlib import Path


def oracle(cost: list[int], edges: list[tuple[int, int]]) -> int:
    """Enumerate all activated subsets for tiny independent cases."""
    n = len(cost)
    best = sum(cost)
    for mask in range(1 << n):
        if all((mask >> u & 1) or (mask >> v & 1) for u, v in edges):
            best = min(best, sum(cost[i] for i in range(n) if mask >> i & 1))
    return best


def write_case(
    out_dir: Path,
    number: int,
    cost: list[int],
    edges: list[tuple[int, int]],
    expected: int | None = None,
) -> None:
    lines = [str(len(cost)), " ".join(map(str, cost))]
    lines.extend(f"{u + 1} {v + 1}" for u, v in edges)
    if expected is None:
        expected = oracle(cost, edges)
    stem = out_dir / f"case{number:03d}"
    stem.with_suffix(".in").write_text("\n".join(lines) + "\n", encoding="utf-8")
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
            write_case(
                args.out_dir,
                case,
                [1] * n,
                [(vertex, vertex + 1) for vertex in range(n - 1)],
                expected=n // 2,
            )
        else:
            n = rng.randint(1, 18)
            cost = [rng.randint(1, 30) for _ in range(n)]
            edges = [(vertex, rng.randrange(vertex)) for vertex in range(1, n)]
            rng.shuffle(edges)
            write_case(args.out_dir, case, cost, edges)


if __name__ == "__main__":
    main()
