from __future__ import annotations

import argparse
import math
import random
from collections import Counter
from pathlib import Path


MOD = 1_000_000_007


def solve(case: str) -> str:
    s = case.strip()
    ans = math.factorial(len(s))
    for c in Counter(s).values():
        ans //= math.factorial(c)
    return f"{ans % MOD}\n"


def make_case(rng: random.Random) -> str:
    n = rng.randint(1, 14)
    alphabet = "abcde"
    return "".join(rng.choice(alphabet) for _ in range(n)) + "\n"


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
