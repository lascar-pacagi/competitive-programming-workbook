from __future__ import annotations

import argparse
import random
from pathlib import Path


def solve(case: str) -> str:
    data = list(map(int, case.split()))
    it = iter(data)
    n = next(it)
    m = next(it)
    total = 1 << n
    full = total - 1
    offers = []
    for _ in range(m):
        cost = next(it)
        k = next(it)
        mask = 0
        for _ in range(k):
            mask |= 1 << (next(it) - 1)
        offers.append((cost, mask))

    inf = 10**18
    dp = [inf] * total
    dp[0] = 0
    for cost, offer in offers:
        ndp = dp[:]
        for mask in range(total):
            value = dp[mask] + cost
            merged = mask | offer
            if value < ndp[merged]:
                ndp[merged] = value
        dp = ndp
    return f"{-1 if dp[full] >= inf else dp[full]}\n"


def make_case(rng: random.Random) -> str:
    n = rng.randint(1, 10)
    m = rng.randint(1, 20)
    lines = [f"{n} {m}"]
    for _ in range(m):
        cost = rng.randint(1, 100)
        skills = [s for s in range(1, n + 1) if rng.random() < 0.35]
        if not skills:
            skills = [rng.randint(1, n)]
        lines.append(f"{cost} {len(skills)} " + " ".join(map(str, skills)))
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
