import argparse
import random
from pathlib import Path

MOD = 998244353


def brute(N, c):
    """t_n by the quadratic recurrence t_n = sum_s c_s [x^(n-1)] T^s."""
    t = [0] * (N + 1)
    D = len(c) - 1
    # powers[s][k] = [x^k] T^s, extended as t grows
    for n in range(1, N + 1):
        # recompute powers up to degree n-1 using current t (t_k known for k < n)
        powers = [[1] + [0] * (n - 1)]
        for s in range(1, D + 1):
            prev = powers[-1]
            cur = [0] * n
            for i in range(n):
                if prev[i]:
                    for j in range(1, n - i):
                        cur[i + j] += prev[i] * t[j]
            powers.append(cur)
        t[n] = sum(c[s] * powers[s][n - 1] for s in range(D + 1)) % MOD
    return t[1:]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, default=25)
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)
    for i in range(args.count):
        N = rng.randint(1, 30)
        D = rng.randint(0, 5)
        c = [rng.choice([0, 1, 2, rng.randrange(MOD)]) for _ in range(D + 1)]
        if rng.random() < 0.8:
            c[0] = max(c[0], 1)
        stem = args.out_dir / f"case{i:03d}"
        stem.with_suffix(".in").write_text(f"{N} {D}\n{' '.join(map(str, c))}\n")
        stem.with_suffix(".out").write_text(" ".join(map(str, brute(N, c))) + "\n")


if __name__ == "__main__":
    main()
