import argparse
import random
from fractions import Fraction
from pathlib import Path


def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


def strict_hull(points):
    pts = sorted(set(points))
    lower, upper = [], []
    for p in pts:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    for p in reversed(pts):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]


def clip_area(poly, a, b):
    """Sutherland--Hodgman with exact fractions: area left of a->b."""
    def side(p):
        return (b[0] - a[0]) * (p[1] - a[1]) - (b[1] - a[1]) * (p[0] - a[0])
    out = []
    m = len(poly)
    for i in range(m):
        p, r = poly[i], poly[(i + 1) % m]
        sp, sr = side(p), side(r)
        if sp >= 0:
            out.append(p)
        if (sp > 0 and sr < 0) or (sp < 0 and sr > 0):
            t = Fraction(sp, sp - sr)
            out.append((p[0] + (r[0] - p[0]) * t, p[1] + (r[1] - p[1]) * t))
    if len(out) < 3:
        return Fraction(0)
    s = 0
    for i in range(len(out)):
        s += out[i][0] * out[(i + 1) % len(out)][1] - out[(i + 1) % len(out)][0] * out[i][1]
    return abs(Fraction(s)) / 2


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, default=25)
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)
    for i in range(args.count):
        span = rng.choice([4, 20, 100000])
        while True:
            poly = strict_hull([(rng.randint(-span, span), rng.randint(-span, span)) for _ in range(rng.randint(3, 25))])
            if len(poly) >= 3:
                break
        if rng.random() < 0.5:
            poly.reverse()
        shift = rng.randrange(len(poly))
        poly = poly[shift:] + poly[:shift]
        queries = []
        for _ in range(rng.randint(1, 20)):
            if rng.random() < 0.3:
                a, b = rng.sample(poly, 2) if len(poly) >= 2 else (poly[0], poly[0])
            else:
                a = (rng.randint(-span, span), rng.randint(-span, span))
                b = a
                while b == a:
                    b = (rng.randint(-span, span), rng.randint(-span, span))
            queries.append((a, b))
        stem = args.out_dir / f"case{i:03d}"
        stem.with_suffix(".in").write_text(f"{len(poly)} {len(queries)}\n" + "".join(f"{x} {y}\n" for x, y in poly)
                                           + "".join(f"{a[0]} {a[1]} {b[0]} {b[1]}\n" for a, b in queries))
        stem.with_suffix(".out").write_text("".join(f"{float(clip_area(poly, a, b))!r}\n" for a, b in queries))


if __name__ == "__main__":
    main()
