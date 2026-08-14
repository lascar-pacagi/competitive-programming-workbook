import argparse
import itertools
import random
from pathlib import Path


MOD = 1_000_000_007


def brute(cap, target):
    return sum(
        sum(values) == target
        for values in itertools.product(*(range(value + 1) for value in cap))
    ) % MOD


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)

    fixed = [([0], 0), ([2, 3, 4], 20), ([1] * 20, 10)]
    for case in range(args.count):
        if case < len(fixed):
            cap, target = fixed[case]
        else:
            n = rng.randint(1, 8)
            cap = [rng.randint(0, 5) for _ in range(n)]
            target = rng.randint(0, sum(cap) + 4)
        if len(cap) <= 8:
            answer = brute(cap, target)
        else:
            answer = 184756
        stem = args.out_dir / f"case{case:03d}"
        stem.with_suffix(".in").write_text(
            f"{len(cap)} {target}\n" + " ".join(map(str, cap)) + "\n"
        )
        stem.with_suffix(".out").write_text(f"{answer}\n")


if __name__ == "__main__":
    main()
