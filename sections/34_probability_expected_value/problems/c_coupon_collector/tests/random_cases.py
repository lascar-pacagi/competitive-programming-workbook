from __future__ import annotations

import argparse
import random
from fractions import Fraction
from pathlib import Path


MOD = 1_000_000_007


def solve(case: str) -> str:
    data = list(map(int, case.split()))
    q = data[0]
    out = []
    for n in data[1 : 1 + q]:
        exact = sum(Fraction(1, i) for i in range(1, n + 1)) * n
        out.append(str(exact.numerator % MOD * pow(exact.denominator % MOD, MOD - 2, MOD) % MOD))
    return "\n".join(out) + "\n"


def make_case(rng: random.Random) -> str:
    q = rng.randint(1, 50)
    lines = [str(q)]
    for _ in range(q):
        lines.append(str(rng.randint(1, 50)))
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
