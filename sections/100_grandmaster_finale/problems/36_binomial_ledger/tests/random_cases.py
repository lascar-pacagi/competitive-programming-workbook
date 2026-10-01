import argparse
import math
import random
from pathlib import Path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, default=25)
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)
    special = [1, 2, 4, 8, 9, 27, 32, 64, 100, 128, 243, 720, 1024, 30030, 65536, 510510, 1000000, 999983, 531441, 524288]
    for i in range(args.count):
        m = rng.choice(special + [rng.randint(1, 10**6)])
        rows = []
        for _ in range(rng.randint(1, 20)):
            n = rng.choice([rng.randint(0, 60), rng.randint(0, 3000), rng.randint(0, 40000)])
            k = rng.randint(0, n + 2)
            rows.append((n, k))
        answers = [math.comb(n, k) % m if k <= n else 0 for n, k in rows]
        stem = args.out_dir / f"case{i:03d}"
        stem.with_suffix(".in").write_text(f"{m} {len(rows)}\n" + "".join(f"{n} {k}\n" for n, k in rows))
        stem.with_suffix(".out").write_text("\n".join(map(str, answers)) + "\n")


if __name__ == "__main__":
    main()
