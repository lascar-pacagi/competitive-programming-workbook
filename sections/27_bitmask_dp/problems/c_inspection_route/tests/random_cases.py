from __future__ import annotations

import argparse
import itertools
import random
from pathlib import Path


def solve(case: str) -> str:
    data = list(map(int, case.split()))
    it = iter(data)
    n = next(it)
    c = [[next(it) for _ in range(n)] for _ in range(n)]
    if n == 1:
        return "0\n"
    if n <= 9:
        best = 10**18
        for middle in itertools.permutations(range(1, n)):
            route = (0,) + middle + (0,)
            total = sum(c[route[i]][route[i + 1]] for i in range(len(route) - 1))
            best = min(best, total)
        return f"{best}\n"

    total = 1 << n
    inf = 10**18
    dp = [[inf] * n for _ in range(total)]
    dp[1][0] = 0
    for mask in range(total):
        if not mask & 1:
            continue
        for last in range(n):
            cur = dp[mask][last]
            if cur >= inf:
                continue
            for nxt in range(n):
                if not (mask >> nxt) & 1:
                    nm = mask | (1 << nxt)
                    dp[nm][nxt] = min(dp[nm][nxt], cur + c[last][nxt])
    full = total - 1
    return f"{min(dp[full][last] + c[last][0] for last in range(n))}\n"


def make_case(rng: random.Random) -> str:
    n = rng.randint(1, 9)
    mat = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(0 if i == j else rng.randint(1, 200))
        mat.append(row)
    lines = [str(n)]
    lines.extend(" ".join(map(str, row)) for row in mat)
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
