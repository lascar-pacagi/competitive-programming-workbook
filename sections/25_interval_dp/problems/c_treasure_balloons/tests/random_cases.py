from __future__ import annotations

import argparse
import random
from pathlib import Path


def solve(case: str) -> str:
    data = list(map(int, case.split()))
    n = data[0]
    a = [1] + data[1:1 + n] + [1]
    dp = [[0] * (n + 2) for _ in range(n + 2)]
    for length in range(1, n + 1):
        for l in range(1, n - length + 2):
            r = l + length - 1
            dp[l][r] = max(
                dp[l][k - 1] + dp[k + 1][r] + a[l - 1] * a[k] * a[r + 1]
                for k in range(l, r + 1)
            )
    return f"{dp[1][n]}\n"


def make_case(rng: random.Random) -> str:
    n = rng.randint(1, 35)
    a = [rng.randint(1, 20) for _ in range(n)]
    return f"{n}\n" + " ".join(map(str, a)) + "\n"


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

