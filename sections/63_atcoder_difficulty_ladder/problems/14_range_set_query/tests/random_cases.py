from __future__ import annotations

import argparse
import itertools
import random
from pathlib import Path


def all_routes(n: int, m: int) -> list[list[tuple[int, int]]]:
    routes: list[list[tuple[int, int]]] = []
    for down_positions in itertools.combinations(range(n + m - 2), n - 1):
        down_set = set(down_positions)
        r = c = 0
        route = [(r, c)]
        for step in range(n + m - 2):
            if step in down_set:
                r += 1
            else:
                c += 1
            route.append((r, c))
        routes.append(route)
    return routes


def exhaustive_oracle(grid: list[list[int]]) -> int:
    n, m = len(grid), len(grid[0])
    routes = all_routes(n, m)
    best = -(1 << 100)
    for first in routes:
        for second in routes:
            visited = set(first)
            visited.update(second)
            best = max(best, sum(grid[r][c] for r, c in visited))
    return best


def encode(grid: list[list[int]]) -> str:
    return f"{len(grid)} {len(grid[0])}\n" + "\n".join(
        " ".join(map(str, row)) for row in grid
    ) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    rng = random.Random(args.seed)
    args.out_dir.mkdir(parents=True, exist_ok=True)

    for i in range(args.count):
        n = rng.randint(1, 5)
        m = rng.randint(1, 5)
        grid = [[rng.randint(-20, 30) for _ in range(m)] for _ in range(n)]
        case = encode(grid)
        (args.out_dir / f"case_{i:03d}.in").write_text(case)
        (args.out_dir / f"case_{i:03d}.out").write_text(f"{exhaustive_oracle(grid)}\n")

    # The large case verifies the intended state-space bound without embedding
    # the dynamic program in this independent tiny-case oracle.
    large = [[0] * 70 for _ in range(70)]
    (args.out_dir / "scale.in").write_text(encode(large))
    (args.out_dir / "scale.out").write_text("0\n")


if __name__ == "__main__":
    main()
