import argparse
import itertools
import random
from pathlib import Path


def brute(s):
    needed = set(s)
    best = None
    for mask in range(1 << len(s)):
        value = "".join(s[i] for i in range(len(s)) if mask >> i & 1)
        if len(value) == len(needed) and set(value) == needed:
            if len(set(value)) == len(value) and (best is None or value < best):
                best = value
    return best


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)
    for case in range(args.count):
        tests = rng.randint(1, 10)
        strings = [
            "".join(rng.choice("abcde") for _ in range(rng.randint(1, 10)))
            for _ in range(tests)
        ]
        stem = args.out_dir / f"case{case:03d}"
        stem.with_suffix(".in").write_text(str(tests) + "\n" + "\n".join(strings) + "\n")
        stem.with_suffix(".out").write_text("\n".join(map(brute, strings)) + "\n")


if __name__ == "__main__":
    main()
