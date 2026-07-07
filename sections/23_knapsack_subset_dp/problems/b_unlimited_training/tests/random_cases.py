from __future__ import annotations

import argparse
import random
from pathlib import Path


def solve(case: str) -> str:
    data = list(map(int, case.split()))
    it = iter(data)
    n = next(it)
    w = next(it)
    dp = [0] * (w + 1)
    for _ in range(n):
        cost = next(it)
        value = next(it)
        if cost > w:
            continue
        for cap in range(cost, w + 1):
            dp[cap] = max(dp[cap], dp[cap - cost] + value)
    return f"{max(dp)}\n"


def make_case(rng: random.Random) -> str:
    n = rng.randint(1, 40)
    w = rng.randint(0, 250)
    lines = [f"{n} {w}"]
    for _ in range(n):
        cost = rng.randint(1, max(1, w + 10))
        value = rng.randint(0, 200)
        lines.append(f"{cost} {value}")
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

