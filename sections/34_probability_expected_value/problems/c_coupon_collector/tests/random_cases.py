from __future__ import annotations

import argparse
import random
from fractions import Fraction
from pathlib import Path


MOD = 1_000_000_007
LIMIT = 1_000_000


def prepare_answers(limit: int) -> list[int]:
    inverse = [0] * (limit + 1)
    harmonic = [0] * (limit + 1)
    inverse[1] = 1
    for value in range(1, limit + 1):
        if value >= 2:
            inverse[value] = (
                MOD - (MOD // value) * inverse[MOD % value] % MOD
            ) % MOD
        harmonic[value] = (harmonic[value - 1] + inverse[value]) % MOD
    return [value * harmonic[value] % MOD for value in range(limit + 1)]


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
    prepared = None
    for i in range(args.count):
        if i == 0:
            # Forces shared preprocessing: summing 1..n independently for
            # every query would require about 2e11 iterations.
            queries = [LIMIT] * 200_000
            case = str(len(queries)) + "\n" + "\n".join(map(str, queries)) + "\n"
            prepared = prepare_answers(LIMIT)
            expected = (str(prepared[LIMIT]) + "\n") * len(queries)
        else:
            case = make_case(rng)
            expected = solve(case)
        (args.out_dir / f"case_{i:03d}.in").write_text(case)
        (args.out_dir / f"case_{i:03d}.out").write_text(expected)


if __name__ == "__main__":
    main()
