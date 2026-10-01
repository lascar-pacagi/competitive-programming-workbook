import argparse
import random
from pathlib import Path

MOD = 1000000007
LIMIT = 200000


def build_prefix():
    spf = list(range(LIMIT + 1))
    for i in range(2, int(LIMIT ** 0.5) + 1):
        if spf[i] == i:
            for j in range(i * i, LIMIT + 1, i):
                if spf[j] == j:
                    spf[j] = i
    prefix = [0] * (LIMIT + 1)
    f = [0] * (LIMIT + 1)
    if LIMIT >= 1:
        f[1] = 1
        prefix[1] = 1
    for x in range(2, LIMIT + 1):
        p = spf[x]
        e = 0
        y = x
        while y % p == 0:
            y //= p
            e += 1
        f[x] = f[y] * (p ^ e)
        prefix[x] = prefix[x - 1] + f[x]
    return prefix


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, default=25)
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)
    prefix = build_prefix()
    for i in range(args.count):
        kind = rng.random()
        if kind < 0.3:
            n = rng.randint(1, 100)
        elif kind < 0.5:
            n = rng.choice([4, 8, 9, 16, 25, 27, 32, 49, 64, 81, 121, 128, 1024, 65536])
            n += rng.randint(-1, 1)
            n = max(1, n)
        else:
            n = rng.randint(1, LIMIT)
        stem = args.out_dir / f"case{i:03d}"
        stem.with_suffix(".in").write_text(f"{n}\n")
        stem.with_suffix(".out").write_text(f"{prefix[n] % MOD}\n")


if __name__ == "__main__":
    main()
