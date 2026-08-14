import argparse
import itertools
import random
from pathlib import Path


MOD = 1_000_000_007


def brute(length, colors, used):
    return sum(
        len(set(word)) == used
        for word in itertools.product(range(colors), repeat=length)
    ) % MOD


def formula(length, colors, used):
    import math
    onto = sum(
        (-1) ** missing
        * math.comb(used, missing)
        * pow(used - missing, length, MOD)
        for missing in range(used + 1)
    )
    return math.comb(colors, used) * onto % MOD


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)

    fixed = [[(1, 1, 1), (2, 5, 3), (10**18, 20, 20)]]
    for case in range(args.count):
        if case < len(fixed):
            rows = fixed[case]
        else:
            rows = []
            for _ in range(rng.randint(1, 12)):
                length = rng.randint(1, 7)
                colors = rng.randint(1, 6)
                used = rng.randint(1, colors)
                rows.append((length, colors, used))
        answers = [
            brute(*row) if row[0] <= 7 and row[1] <= 6 else formula(*row)
            for row in rows
        ]
        stem = args.out_dir / f"case{case:03d}"
        lines = [str(len(rows))]
        lines.extend(" ".join(map(str, row)) for row in rows)
        stem.with_suffix(".in").write_text("\n".join(lines) + "\n")
        stem.with_suffix(".out").write_text(
            "\n".join(map(str, answers)) + "\n"
        )


if __name__ == "__main__":
    main()
