import argparse
import itertools
import random
from pathlib import Path


def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


def general_points(rng, n, span):
    while True:
        xs = rng.sample(range(-span, span + 1), n)
        pts = [(x, rng.randint(-span, span)) for x in xs]
        if all(cross(a, b, c) != 0 for a, b, c in itertools.combinations(pts, 3)):
            return pts


def inside(pts, i, j, k):
    a, b, c = pts[i], pts[j], pts[k]
    s = 1 if cross(a, b, c) > 0 else -1
    return sum(1 for t, p in enumerate(pts) if t not in (i, j, k)
               and s * cross(a, b, p) > 0 and s * cross(b, c, p) > 0 and s * cross(c, a, p) > 0)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, default=25)
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)
    for i in range(args.count):
        n = rng.randint(3, 14)
        pts = general_points(rng, n, rng.choice([20, 100, 10**9]))
        queries = [tuple(rng.sample(range(n), 3)) for _ in range(rng.randint(1, 20))]
        stem = args.out_dir / f"case{i:03d}"
        stem.with_suffix(".in").write_text(f"{n} {len(queries)}\n" + "".join(f"{x} {y}\n" for x, y in pts)
                                           + "".join(f"{a + 1} {b + 1} {c + 1}\n" for a, b, c in queries))
        stem.with_suffix(".out").write_text("".join(f"{inside(pts, *t)}\n" for t in queries))


if __name__ == "__main__":
    main()
