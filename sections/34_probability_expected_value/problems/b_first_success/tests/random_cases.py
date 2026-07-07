from __future__ import annotations

import argparse
import random
from fractions import Fraction
from pathlib import Path


MOD = 1_000_000_007


def solve(case: str) -> str:
    data = list(map(int, case.split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        p, q = data[idx], data[idx + 1]
        idx += 2
        exact = Fraction(q, p)
        out.append(str(exact.numerator % MOD * pow(exact.denominator % MOD, MOD - 2, MOD) % MOD))
    return "\n".join(out) + "\n"


def make_case(rng: random.Random) -> str:
    t = rng.randint(1, 50)
    lines = [str(t)]
    for _ in range(t):
        q = rng.randint(1, 200)
        p = rng.randint(1, q)
        lines.append(f"{p} {q}")
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
