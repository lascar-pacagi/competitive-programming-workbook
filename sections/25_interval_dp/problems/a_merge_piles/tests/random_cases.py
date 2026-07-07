from __future__ import annotations

import argparse
import random
from pathlib import Path


def solve(case: str) -> str:
    data = list(map(int, case.split()))
    n = data[0]
    a = data[1:1 + n]
    pref = [0]
    for x in a:
        pref.append(pref[-1] + x)
    dp = [[0] * n for _ in range(n)]
    for length in range(2, n + 1):
        for l in range(n - length + 1):
            r = l + length - 1
            add = pref[r + 1] - pref[l]
            dp[l][r] = min(dp[l][k] + dp[k + 1][r] + add for k in range(l, r))
    return f"{dp[0][n - 1]}\n"


def make_case(rng: random.Random) -> str:
    n = rng.randint(1, 35)
    a = [rng.randint(1, 1000) for _ in range(n)]
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

