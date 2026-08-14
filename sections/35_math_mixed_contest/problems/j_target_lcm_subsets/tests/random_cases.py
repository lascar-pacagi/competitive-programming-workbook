import argparse
import math
import random
from pathlib import Path


MOD = 1_000_000_007


def brute(values, target):
    answer = 0
    for mask in range(1, 1 << len(values)):
        current = 1
        for i, value in enumerate(values):
            if mask >> i & 1:
                current = math.lcm(current, value)
        answer += current == target
    return answer % MOD


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)

    fixed = [([1, 1, 2], 1), ([2, 3, 5], 30), ([4, 8, 16], 8)]
    for case in range(args.count):
        if case < len(fixed):
            values, target = fixed[case]
        else:
            target = rng.randint(1, 60)
            values = [rng.randint(1, 70) for _ in range(rng.randint(1, 16))]
        answer = brute(values, target)
        stem = args.out_dir / f"case{case:03d}"
        stem.with_suffix(".in").write_text(
            f"{len(values)} {target}\n" + " ".join(map(str, values)) + "\n"
        )
        stem.with_suffix(".out").write_text(f"{answer}\n")


if __name__ == "__main__":
    main()
