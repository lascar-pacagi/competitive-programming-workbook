from __future__ import annotations

import argparse
import random
from fractions import Fraction
from pathlib import Path

MOD = 1_000_000_007


def oracle(events):
    result = Fraction(0)
    for mask in range(1 << len(events)):
        probability = Fraction(1)
        wins = 0
        for index, (p, q) in enumerate(events):
            if mask >> index & 1:
                probability *= Fraction(p, q)
                wins += 1
            else:
                probability *= Fraction(q - p, q)
        result += probability * (wins * (wins - 1) // 2)
    return result.numerator * pow(result.denominator, MOD - 2, MOD) % MOD


def write_case(directory, number, events, answer):
    stem = directory / f"case{number:03d}"
    stem.with_suffix(".in").write_text(str(len(events)) + "\n" + "\n".join(f"{p} {q}" for p, q in events) + "\n")
    stem.with_suffix(".out").write_text(str(answer) + "\n")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)
    for number in range(args.count):
        if number == 0:
            events = [(1, 2)] * 200_000
            answer = (200_000 * 199_999 // 2) * pow(4, MOD - 2, MOD) % MOD
        else:
            events = []
            for _ in range(rng.randint(1, 10)):
                q = rng.randint(1, 9)
                events.append((rng.randint(0, q - 1), q))
            answer = oracle(events)
        write_case(args.out_dir, number, events, answer)


if __name__ == "__main__":
    main()
