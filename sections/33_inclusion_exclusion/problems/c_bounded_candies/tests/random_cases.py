from __future__ import annotations

import argparse
import itertools
import random
from pathlib import Path


MOD = 1_000_000_007


def brute(n: int, s: int, b: int) -> int:
    ans = 0
    for values in itertools.product(range(b + 1), repeat=n):
        if sum(values) == s:
            ans += 1
    return ans % MOD


def solve(case: str) -> str:
    data = list(map(int, case.split()))
    q = data[0]
    idx = 1
    out = []
    for _ in range(q):
        n, s, b = data[idx], data[idx + 1], data[idx + 2]
        idx += 3
        out.append(str(brute(n, s, b)))
    return "\n".join(out) + "\n"


def make_case(rng: random.Random) -> str:
    q = rng.randint(1, 20)
    lines = [str(q)]
    for _ in range(q):
        n = rng.randint(1, 7)
        b = rng.randint(0, 5)
        s = rng.randint(0, n * b + 3)
        lines.append(f"{n} {s} {b}")
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
