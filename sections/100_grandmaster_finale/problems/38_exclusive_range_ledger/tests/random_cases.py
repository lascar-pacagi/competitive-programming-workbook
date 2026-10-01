import argparse
import random
from pathlib import Path

MOD = 1_000_000_007


def brute(a, l, r, x):
    counts = {0: 1}
    for v in a[l - 1:r]:
        nxt = dict(counts)
        for k, c in counts.items():
            nxt[k ^ v] = nxt.get(k ^ v, 0) + c
        counts = nxt
    return counts.get(x, 0) % MOD


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, default=25)
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)
    for i in range(args.count):
        n = rng.randint(1, 14)
        top = rng.choice([1, 3, 7, 31, 2**30 - 1])
        a = [rng.randint(0, top) for _ in range(n)]
        rows = []
        for _ in range(rng.randint(1, 15)):
            l = rng.randint(1, n)
            r = rng.randint(l, n)
            x = rng.choice([0, rng.randint(0, top), a[rng.randrange(n)]])
            rows.append((l, r, x))
        stem = args.out_dir / f"case{i:03d}"
        stem.with_suffix(".in").write_text(f"{n} {len(rows)}\n{' '.join(map(str, a))}\n" + "".join(f"{l} {r} {x}\n" for l, r, x in rows))
        stem.with_suffix(".out").write_text("".join(f"{brute(a, l, r, x)}\n" for l, r, x in rows))


if __name__ == "__main__":
    main()
