from __future__ import annotations

import argparse
import random
from pathlib import Path


def solve(case: str) -> str:
    data = list(map(int, case.split()))
    n, k = data[0], data[1]
    h = data[2:2 + n]
    inf = 10**30
    dp = [inf] * n
    dp[0] = 0
    for i in range(1, n):
        for j in range(max(0, i - k), i):
            dp[i] = min(dp[i], dp[j] + abs(h[j] - h[i]))
    return f"{dp[-1]}\n"


def make_case(rng: random.Random) -> str:
    n = rng.randint(1, 180)
    k = rng.randint(1, 50)
    h = [rng.randint(0, 1000) for _ in range(n)]
    return f"{n} {k}\n" + " ".join(map(str, h)) + "\n"


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

