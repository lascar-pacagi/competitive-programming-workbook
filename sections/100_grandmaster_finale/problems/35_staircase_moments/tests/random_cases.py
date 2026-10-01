import argparse
import random
from pathlib import Path

MOD = 998244353


def brute(n, a, b, c):
    f = g = h = 0
    for x in range(n + 1):
        q = (a * x + b) // c
        f += q
        g += x * q
        h += q * q
    return f % MOD, g % MOD, h % MOD


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, default=25)
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)
    for i in range(args.count):
        rows = []
        for _ in range(rng.randint(1, 20)):
            top = rng.choice([5, 50, 10**9, 10**18])
            n = rng.randint(0, 2000)
            a = rng.randint(0, top)
            b = rng.randint(0, top)
            c = rng.randint(1, top)
            rows.append((n, a, b, c))
        stem = args.out_dir / f"case{i:03d}"
        stem.with_suffix(".in").write_text(f"{len(rows)}\n" + "".join(f"{n} {a} {b} {c}\n" for n, a, b, c in rows))
        stem.with_suffix(".out").write_text("".join("%d %d %d\n" % brute(*r) for r in rows))


if __name__ == "__main__":
    main()
