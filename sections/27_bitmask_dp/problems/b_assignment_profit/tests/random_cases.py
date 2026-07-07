from __future__ import annotations

import argparse
import itertools
import random
from pathlib import Path


def solve(case: str) -> str:
    data = list(map(int, case.split()))
    it = iter(data)
    n = next(it)
    a = [[next(it) for _ in range(n)] for _ in range(n)]
    if n <= 8:
        best = 0
        for perm in itertools.permutations(range(n)):
            best = max(best, sum(a[i][perm[i]] for i in range(n)))
        return f"{best}\n"

    total = 1 << n
    neg = -10**18
    dp = [neg] * total
    dp[0] = 0
    for mask in range(total):
        i = mask.bit_count()
        if i == n:
            continue
        for j in range(n):
            if not (mask >> j) & 1:
                nxt = mask | (1 << j)
                dp[nxt] = max(dp[nxt], dp[mask] + a[i][j])
    return f"{dp[-1]}\n"


def make_case(rng: random.Random) -> str:
    n = rng.randint(1, 9)
    rows = [[rng.randint(0, 200) for _ in range(n)] for _ in range(n)]
    lines = [str(n)]
    lines.extend(" ".join(map(str, row)) for row in rows)
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
