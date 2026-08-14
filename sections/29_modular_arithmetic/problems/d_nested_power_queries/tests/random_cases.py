from __future__ import annotations

import argparse
import random
from pathlib import Path


MOD = 1_000_000_007


def answer(a, b, c):
    exponent = pow(b, c, MOD - 1)
    return pow(a, exponent, MOD)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)

    special = [
        (2, 2, 30),
        (3, MOD, 10**18),
        (5, MOD - 1, 1),
        (MOD - 1, MOD, 1),
        (123456789, 10**18, 10**18),
        (42, MOD + 1, MOD + 1),
    ]
    notable_b = [1, 2, MOD - 1, MOD, MOD + 1, 10**18]
    notable_c = [1, 2, 30, MOD - 1, MOD, 10**18]

    for case in range(args.count):
        if case == 0:
            query_count = 200000
            rows = [(2, 1, 10**18)] * query_count
        elif case == 1:
            rows = special
            query_count = len(rows)
        else:
            query_count = rng.randint(1, 40)
            rows = []
            for _ in range(query_count):
                a = rng.randint(1, MOD - 1)
                b = rng.choice(notable_b + [rng.randint(1, 10**18)])
                c = rng.choice(notable_c + [rng.randint(1, 10**18)])
                rows.append((a, b, c))

        expected = [str(answer(*query)) for query in rows]
        stem = args.out_dir / f"case{case:03d}"
        input_lines = [str(query_count)]
        input_lines.extend(" ".join(map(str, row)) for row in rows)
        stem.with_suffix(".in").write_text("\n".join(input_lines) + "\n")
        stem.with_suffix(".out").write_text("\n".join(expected) + "\n")


if __name__ == "__main__":
    main()
