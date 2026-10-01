import argparse
import itertools
import math
import random
from pathlib import Path


def brute(pts, k):
    """Minimum radius over every disc determined by 2 or 3 points."""
    if k <= 1:
        return 0.0
    cand = []
    for a, b in itertools.combinations(pts, 2):
        cand.append(((a[0] + b[0]) / 2, (a[1] + b[1]) / 2, math.dist(a, b) / 2))
    for a, b, c in itertools.combinations(pts, 3):
        d = 2 * (a[0] * (b[1] - c[1]) + b[0] * (c[1] - a[1]) + c[0] * (a[1] - b[1]))
        if d == 0:
            continue
        ux = ((a[0] ** 2 + a[1] ** 2) * (b[1] - c[1]) + (b[0] ** 2 + b[1] ** 2) * (c[1] - a[1]) + (c[0] ** 2 + c[1] ** 2) * (a[1] - b[1])) / d
        uy = ((a[0] ** 2 + a[1] ** 2) * (c[0] - b[0]) + (b[0] ** 2 + b[1] ** 2) * (a[0] - c[0]) + (c[0] ** 2 + c[1] ** 2) * (b[0] - a[0])) / d
        cand.append((ux, uy, math.dist((ux, uy), a)))
    best = math.inf
    for cx, cy, r in cand:
        if r < best and sum(1 for p in pts if math.dist((cx, cy), p) <= r * (1 + 1e-9) + 1e-9) >= k:
            best = r
    return best


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, default=25)
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)
    for i in range(args.count):
        n = rng.randint(1, 12)
        span = rng.choice([3, 20, 10000])
        pts = [(rng.randint(-span, span), rng.randint(-span, span)) for _ in range(n)]
        if rng.random() < 0.2 and n > 1:
            pts[1] = pts[0]
        k = rng.randint(1, n)
        stem = args.out_dir / f"case{i:03d}"
        stem.with_suffix(".in").write_text(f"{n} {k}\n" + "".join(f"{x} {y}\n" for x, y in pts))
        stem.with_suffix(".out").write_text("%.10f\n" % brute(pts, k))


if __name__ == "__main__":
    main()
