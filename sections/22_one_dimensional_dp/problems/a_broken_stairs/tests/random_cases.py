from __future__ import annotations

import argparse
import random
from pathlib import Path


MOD = 1_000_000_007


def solve(case: str) -> str:
    data = list(map(int, case.split()))
    n, b = data[0], data[1]
    broken = [False] * (n + 1)
    for x in data[2:2 + b]:
        broken[x] = True
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        if broken[i]:
            continue
        dp[i] = dp[i - 1]
        if i >= 2:
            dp[i] = (dp[i] + dp[i - 2]) % MOD
    return f"{dp[n]}\n"


def make_case(rng: random.Random) -> str:
    n = rng.randint(1, 300)
    steps = list(range(1, n + 1))
    rng.shuffle(steps)
    b = rng.randint(0, min(n, 80))
    broken = sorted(steps[:b])
    lines = [f"{n} {b}"]
    if b:
        lines.append(" ".join(map(str, broken)))
    return "\n".join(lines) + "\n"


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

