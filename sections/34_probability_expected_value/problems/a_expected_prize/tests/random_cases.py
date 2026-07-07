from __future__ import annotations

import argparse
import random
from fractions import Fraction
from pathlib import Path


MOD = 1_000_000_007


def solve(case: str) -> str:
    data = list(map(int, case.split()))
    n = data[0]
    idx = 1
    exact = Fraction(0, 1)
    for _ in range(n):
        p, q, v = data[idx], data[idx + 1], data[idx + 2]
        idx += 3
        exact += Fraction(p * v, q)
    return f"{exact.numerator % MOD * pow(exact.denominator % MOD, MOD - 2, MOD) % MOD}\n"


def make_case(rng: random.Random) -> str:
    n = rng.randint(1, 30)
    lines = [str(n)]
    for _ in range(n):
        q = rng.randint(1, 30)
        p = rng.randint(0, q)
        v = rng.randint(0, 200)
        lines.append(f"{p} {q} {v}")
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
