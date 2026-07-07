from __future__ import annotations

import argparse
import random
from pathlib import Path


MOD = 1_000_000_007
RIGHT = 0
DOWN = 1


def solve(case: str) -> str:
    lines = case.strip().splitlines()
    n, m, k = map(int, lines[0].split())
    grid = lines[1:]
    if grid[0][0] == "#" or grid[n - 1][m - 1] == "#":
        return "0\n"
    if n == 1 and m == 1:
        return "1\n"
    dp = [[[[0, 0] for _ in range(k + 1)] for _ in range(m)] for _ in range(n)]
    if m > 1 and grid[0][1] == ".":
        dp[0][1][0][RIGHT] = 1
    if n > 1 and grid[1][0] == ".":
        dp[1][0][0][DOWN] = 1
    for r in range(n):
        for c in range(m):
            if grid[r][c] == "#":
                continue
            for turns in range(k + 1):
                if c > 0 and grid[r][c - 1] == ".":
                    dp[r][c][turns][RIGHT] = (
                        dp[r][c][turns][RIGHT] + dp[r][c - 1][turns][RIGHT]
                    ) % MOD
                    if turns:
                        dp[r][c][turns][RIGHT] = (
                            dp[r][c][turns][RIGHT] + dp[r][c - 1][turns - 1][DOWN]
                        ) % MOD
                if r > 0 and grid[r - 1][c] == ".":
                    dp[r][c][turns][DOWN] = (
                        dp[r][c][turns][DOWN] + dp[r - 1][c][turns][DOWN]
                    ) % MOD
                    if turns:
                        dp[r][c][turns][DOWN] = (
                            dp[r][c][turns][DOWN] + dp[r - 1][c][turns - 1][RIGHT]
                        ) % MOD
    ans = 0
    for turns in range(k + 1):
        ans = (ans + dp[n - 1][m - 1][turns][RIGHT] + dp[n - 1][m - 1][turns][DOWN]) % MOD
    return f"{ans}\n"


def make_case(rng: random.Random) -> str:
    n = rng.randint(1, 12)
    m = rng.randint(1, 12)
    k = rng.randint(0, min(10, n + m))
    rows = []
    for r in range(n):
        row = []
        for c in range(m):
            if (r, c) in {(0, 0), (n - 1, m - 1)}:
                row.append(".")
            else:
                row.append("#" if rng.random() < 0.18 else ".")
        rows.append("".join(row))
    return f"{n} {m} {k}\n" + "\n".join(rows) + "\n"


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

