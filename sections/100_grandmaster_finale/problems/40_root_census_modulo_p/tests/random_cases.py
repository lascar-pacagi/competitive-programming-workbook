import argparse
import random
from pathlib import Path

PRIMES = [2, 3, 5, 7, 11, 13, 17, 101, 997, 1009, 2003]


def brute(p, coef):
    count = 0
    for x in range(p):
        v = 0
        for c in reversed(coef):
            v = (v * x + c) % p
        count += v == 0
    return count


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, default=25)
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)
    for i in range(args.count):
        p = rng.choice(PRIMES)
        kind = rng.random()
        if kind < 0.4:
            # product of linear factors (with repeats) times a random factor
            roots = [rng.randrange(p) for _ in range(rng.randint(0, 8))]
            coef = [rng.randrange(p) for _ in range(rng.randint(1, 4))]
            for r in roots:
                coef = [(-r * coef[0]) % p] + [((coef[j - 1] if j - 1 < len(coef) else 0) - r * (coef[j] if j < len(coef) else 0)) % p for j in range(1, len(coef) + 1)]
        else:
            coef = [rng.randrange(p) for _ in range(rng.randint(1, 12))]
        if rng.random() < 0.2:
            coef = [c + p * rng.randint(0, 3) for c in coef]  # unreduced input
        if rng.random() < 0.05:
            coef = [0] * len(coef)
        d = len(coef) - 1
        stem = args.out_dir / f"case{i:03d}"
        stem.with_suffix(".in").write_text(f"{p} {d}\n{' '.join(map(str, coef))}\n")
        stem.with_suffix(".out").write_text(f"{brute(p, [c % p for c in coef])}\n")


if __name__ == "__main__":
    main()
