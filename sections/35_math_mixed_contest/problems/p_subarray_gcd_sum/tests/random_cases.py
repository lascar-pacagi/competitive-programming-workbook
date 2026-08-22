import argparse
import math
import random
from pathlib import Path

MOD = 1_000_000_007


def brute(values):
    answer = 0
    for left in range(len(values)):
        current = 0
        for right in range(left, len(values)):
            current = math.gcd(current, values[right])
            answer += current
    return answer % MOD


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    rng = random.Random(args.seed)
    args.out_dir.mkdir(parents=True, exist_ok=True)
    for case in range(args.count):
        values = [rng.randint(1, 40) for _ in range(rng.randint(1, 35))]
        stem = args.out_dir / f"case{case:03d}"
        stem.with_suffix(".in").write_text(
            f"{len(values)}\n" + " ".join(map(str, values)) + "\n"
        )
        stem.with_suffix(".out").write_text(f"{brute(values)}\n")


if __name__ == "__main__":
    main()
