import argparse
import random
from pathlib import Path

MOD = 998244353


def brute(n, r, d):
    total = 0
    rp = 1
    for i in range(n):
        total += rp * pow(i, d, MOD)
        rp = rp * r % MOD
    return total % MOD


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, default=25)
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)
    for i in range(args.count):
        d = rng.choice([0, 1, 2, rng.randint(0, 60)])
        n = rng.choice([0, 1, rng.randint(0, d + 3), rng.randint(0, 3000)])
        r = rng.choice([0, 1, MOD - 1, MOD + 1, rng.randrange(MOD), rng.randint(0, 10**18)])
        stem = args.out_dir / f"case{i:03d}"
        stem.with_suffix(".in").write_text(f"{n} {r} {d}\n")
        stem.with_suffix(".out").write_text(f"{brute(n, r % MOD, d)}\n")


if __name__ == "__main__":
    main()
