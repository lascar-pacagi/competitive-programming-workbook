import argparse
import fractions
import random
from pathlib import Path


MOD = 1_000_000_007


def proper_divisors(value):
    return [divisor for divisor in range(1, value) if value % divisor == 0]


def fraction_oracle(maximum):
    expected = [fractions.Fraction(0) for _ in range(maximum + 1)]
    for value in range(2, maximum + 1):
        divisors = proper_divisors(value)
        expected[value] = 1 + sum(expected[d] for d in divisors) / len(divisors)
    return expected


def to_mod(value):
    return value.numerator % MOD * pow(value.denominator, MOD - 2, MOD) % MOD


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)

    for case in range(args.count):
        queries = [1, 2, 4, 6] if case == 0 else [
            rng.randint(1, 100) for _ in range(rng.randint(1, 30))
        ]
        expected = fraction_oracle(max(queries))
        answers = [to_mod(expected[value]) for value in queries]
        stem = args.out_dir / f"case{case:03d}"
        stem.with_suffix(".in").write_text(
            f"{len(queries)}\n" + " ".join(map(str, queries)) + "\n"
        )
        stem.with_suffix(".out").write_text(
            "\n".join(map(str, answers)) + "\n"
        )


if __name__ == "__main__":
    main()
