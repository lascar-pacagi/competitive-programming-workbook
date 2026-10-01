import argparse
import random
from pathlib import Path


def brute(m):
    if m == 1:
        return 1
    a, b = 0, 1
    k = 0
    while True:
        a, b = b, (a + b) % m
        k += 1
        if a == 0 and b == 1:
            return k


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, default=25)
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)
    special = [1, 2, 3, 4, 5, 8, 10, 25, 125, 625, 1000, 3125, 4096, 9973, 10007, 59049, 65536, 99991]
    for i in range(args.count):
        ms = [rng.choice(special + [rng.randint(1, 20000), rng.randint(1, 120000)]) for _ in range(rng.randint(1, 6))]
        stem = args.out_dir / f"case{i:03d}"
        stem.with_suffix(".in").write_text(f"{len(ms)}\n" + "".join(f"{m}\n" for m in ms))
        stem.with_suffix(".out").write_text("".join(f"{brute(m)}\n" for m in ms))


if __name__ == "__main__":
    main()
