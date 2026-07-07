from __future__ import annotations

import argparse
import random
from pathlib import Path


def solve(case: str) -> str:
    data = list(map(int, case.split()))
    n = data[0]
    days = data[1 : 1 + n]
    inf = 10**9
    dp = [0, inf, inf]
    for available in days:
        ndp = [min(dp) + 1, inf, inf]
        if available & 1:
            ndp[1] = min(dp[0], dp[2])
        if available & 2:
            ndp[2] = min(dp[0], dp[1])
        dp = ndp
    return f"{min(dp)}\n"


def make_case(rng: random.Random) -> str:
    n = rng.randint(1, 80)
    days = [rng.randint(0, 3) for _ in range(n)]
    return f"{n}\n" + " ".join(map(str, days)) + "\n"


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
