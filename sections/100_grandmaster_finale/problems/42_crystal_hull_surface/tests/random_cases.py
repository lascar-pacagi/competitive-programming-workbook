import argparse
import itertools
import math
import random
from pathlib import Path


def orient(a, b, c, d):
    u = [b[k] - a[k] for k in range(3)]
    v = [c[k] - a[k] for k in range(3)]
    w = [d[k] - a[k] for k in range(3)]
    return (u[0] * (v[1] * w[2] - v[2] * w[1]) - u[1] * (v[0] * w[2] - v[2] * w[0]) + u[2] * (v[0] * w[1] - v[1] * w[0]))


def hull_faces(pts):
    """Brute force: a triple is a face iff every other point is strictly on
    one side.  Returns None if some hull plane contains a fourth point."""
    faces = []
    for a, b, c in itertools.combinations(range(len(pts)), 3):
        signs = [orient(pts[a], pts[b], pts[c], pts[d]) for d in range(len(pts)) if d not in (a, b, c)]
        if all(s > 0 for s in signs) or all(s < 0 for s in signs):
            faces.append((a, b, c))
        elif all(s >= 0 for s in signs) or all(s <= 0 for s in signs):
            if any(s == 0 for s in signs) and any(s != 0 for s in signs):
                return None  # supporting plane through four points
    return faces


def area(pts, faces):
    total = 0.0
    for a, b, c in faces:
        u = [pts[b][k] - pts[a][k] for k in range(3)]
        v = [pts[c][k] - pts[a][k] for k in range(3)]
        cr = (u[1] * v[2] - u[2] * v[1], u[2] * v[0] - u[0] * v[2], u[0] * v[1] - u[1] * v[0])
        total += math.sqrt(sum(x * x for x in cr)) / 2
    return total


def make_case(rng):
    while True:
        n = rng.randint(4, 11)
        span = rng.choice([3, 10, 1000, 10**6])
        pts = list({(rng.randint(-span, span), rng.randint(-span, span), rng.randint(-span, span)) for _ in range(n)})
        if len(pts) < 4:
            continue
        faces = hull_faces(pts)
        if faces is None or not faces:
            continue
        # also reject coplanar input (no 3D hull)
        if all(orient(*q, r) == 0 for q in [pts[:3]] for r in pts[3:]):
            continue
        value = area(pts, faces)
        rng.shuffle(pts)
        return pts, value


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, default=25)
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)
    for i in range(args.count):
        pts, value = make_case(rng)
        stem = args.out_dir / f"case{i:03d}"
        stem.with_suffix(".in").write_text(f"{len(pts)}\n" + "".join(f"{x} {y} {z}\n" for x, y, z in pts))
        stem.with_suffix(".out").write_text("%.10f\n" % value)


if __name__ == "__main__":
    main()
