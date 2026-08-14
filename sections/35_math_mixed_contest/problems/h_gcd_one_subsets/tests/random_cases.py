import argparse
import math
import random
from pathlib import Path


MOD = 1_000_000_007


def brute(values):
    answer = 0
    for mask in range(1, 1 << len(values)):
        current = 0
        for i, value in enumerate(values):
            if mask >> i & 1:
                current = math.gcd(current, value)
        answer += current == 1
    return answer % MOD


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)

    fixed = [[1], [2, 4, 8], [1] * 18]
    for case in range(args.count):
        values = fixed[case] if case < len(fixed) else [
            rng.randint(1, 40) for _ in range(rng.randint(1, 16))
        ]
        answer = brute(values)
        stem = args.out_dir / f"case{case:03d}"
        stem.with_suffix(".in").write_text(
            f"{len(values)}\n" + " ".join(map(str, values)) + "\n"
        )
        stem.with_suffix(".out").write_text(f"{answer}\n")


if __name__ == "__main__":
    main()
