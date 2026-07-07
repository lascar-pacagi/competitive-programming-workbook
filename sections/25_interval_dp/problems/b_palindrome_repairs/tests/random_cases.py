from __future__ import annotations

import argparse
import random
from pathlib import Path


def solve(case: str) -> str:
    s = case.strip()
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    for length in range(2, n + 1):
        for l in range(n - length + 1):
            r = l + length - 1
            if s[l] == s[r]:
                dp[l][r] = dp[l + 1][r - 1] if l + 1 <= r - 1 else 0
            else:
                dp[l][r] = 1 + min(dp[l + 1][r], dp[l][r - 1])
    return f"{dp[0][n - 1]}\n"


def make_case(rng: random.Random) -> str:
    n = rng.randint(1, 80)
    alphabet = "abcde"
    s = "".join(rng.choice(alphabet) for _ in range(n))
    return s + "\n"


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

