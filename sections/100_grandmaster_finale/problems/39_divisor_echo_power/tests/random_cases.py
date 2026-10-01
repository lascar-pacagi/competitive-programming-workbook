import argparse
import random
from pathlib import Path

MOD = 998244353


def dirichlet(a, b, N):
    c = [0] * (N + 1)
    for i in range(1, N + 1):
        if a[i]:
            for j in range(1, N // i + 1):
                c[i * j] = (c[i * j] + a[i] * b[j]) % MOD
    return c


def brute(N, k, f):
    result = [0] * (N + 1)
    result[1] = 1
    base = [0] + f
    while k:
        if k & 1:
            result = dirichlet(result, base, N)
        base = dirichlet(base, base, N)
        k >>= 1
    return result[1:]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, default=25)
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)
    for i in range(args.count):
        N = rng.randint(1, 300)
        k = rng.choice([0, 1, 2, 3, rng.randint(0, 50), rng.randint(0, 10**18)])
        f = [1] + [rng.choice([0, 1, MOD - 1, rng.randrange(MOD)]) for _ in range(N - 1)]
        stem = args.out_dir / f"case{i:03d}"
        stem.with_suffix(".in").write_text(f"{N} {k}\n{' '.join(map(str, f))}\n")
        stem.with_suffix(".out").write_text(" ".join(map(str, brute(N, k, f))) + "\n")


if __name__ == "__main__":
    main()
