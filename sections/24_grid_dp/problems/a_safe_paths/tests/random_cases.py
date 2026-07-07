from __future__ import annotations

import argparse
import random
from pathlib import Path


MOD = 1_000_000_007


def solve(case: str) -> str:
    lines = case.strip().splitlines()
    n, m = map(int, lines[0].split())
    grid = lines[1:]
    dp = [[0] * m for _ in range(n)]
    if grid[0][0] == ".":
        dp[0][0] = 1
    for r in range(n):
        for c in range(m):
            if grid[r][c] == "#":
                dp[r][c] = 0
                continue
            if r:
                dp[r][c] = (dp[r][c] + dp[r - 1][c]) % MOD
            if c:
                dp[r][c] = (dp[r][c] + dp[r][c - 1]) % MOD
    return f"{dp[-1][-1]}\n"


def make_case(rng: random.Random) -> str:
    n = rng.randint(1, 35)
    m = rng.randint(1, 35)
    rows = []
    for r in range(n):
        row = []
        for c in range(m):
            if (r, c) in {(0, 0), (n - 1, m - 1)}:
                row.append(".")
            else:
                row.append("#" if rng.random() < 0.23 else ".")
        rows.append("".join(row))
    return f"{n} {m}\n" + "\n".join(rows) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    rng = random.Random(args.seed)
    args.out_dir.mkdir(parents=True, exist_ok=True)
    for i in range(args.count):
        case = make_case(rng)
        (args.out_dir / f"case_{i:03d}.in").write_text(case)
        (args.out_dir / f"case_{i:03d}.out").write_text(solve(case))


if __name__ == "__main__":
    main()

