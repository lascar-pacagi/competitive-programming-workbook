from __future__ import annotations

import argparse
import itertools
import random
from pathlib import Path


def oracle(n: int, edges: list[tuple[int, int]]) -> str:
    """Enumerate small permutations instead of using the submitted algorithm."""
    valid_orders: list[tuple[int, ...]] = []
    for order in itertools.permutations(range(1, n + 1)):
        position = {vertex: index for index, vertex in enumerate(order)}
        if all(position[a] < position[b] for a, b in edges):
            valid_orders.append(order)
            if len(valid_orders) == 2:
                return "AMBIGUOUS\n"

    if not valid_orders:
        return "IMPOSSIBLE\n"
    return "UNIQUE\n" + " ".join(map(str, valid_orders[0])) + "\n"


def scale_case() -> tuple[str, str]:
    n = 200000
    edges = [(1, 3), (2, 3)]
    edges.extend((vertex, vertex + 1) for vertex in range(3, n))
    lines = [f"{n} {len(edges)}"]
    lines.extend(f"{a} {b}" for a, b in edges)
    return "\n".join(lines) + "\n", "AMBIGUOUS\n"


def small_case(rng: random.Random) -> tuple[str, str]:
    n = rng.randint(1, 8)
    edges = [
        (a, b)
        for a in range(1, n + 1)
        for b in range(1, n + 1)
        if a != b and rng.random() < 0.20
    ]
    lines = [f"{n} {len(edges)}"]
    lines.extend(f"{a} {b}" for a, b in edges)
    case = "\n".join(lines) + "\n"
    return case, oracle(n, edges)


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
