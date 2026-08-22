"""Independent tiny brute-force cases for Sections 73--75."""

from __future__ import annotations

import argparse
import itertools
import math
import random
from pathlib import Path


def cross(a, b, c=None):
    if c is None:
        return a[0] * b[1] - a[1] * b[0]
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def hull(points):
    p = sorted(set(points))
    if len(p) <= 1:
        return p
    lo = []
    for x in p:
        while len(lo) >= 2 and cross(lo[-2], lo[-1], x) <= 0:
            lo.pop()
        lo.append(x)
    hi = []
    for x in reversed(p):
        while len(hi) >= 2 and cross(hi[-2], hi[-1], x) <= 0:
            hi.pop()
        hi.append(x)
    return lo[:-1] + hi[:-1]


def inside(poly, q):
    if len(poly) == 1:
        return 0 if poly[0] == q else -1
    if len(poly) == 2:
        a, b = poly
        ok = (
            cross(a, b, q) == 0
            and min(a[0], b[0]) <= q[0] <= max(a[0], b[0])
            and min(a[1], b[1]) <= q[1] <= max(a[1], b[1])
        )
        return 0 if ok else -1
    boundary = False
    for i, a in enumerate(poly):
        z = cross(a, poly[(i + 1) % len(poly)], q)
        if z < 0:
            return -1
        boundary |= z == 0
    return 0 if boundary else 1


def points(rng, minimum=1):
    n = rng.randint(minimum, 10)
    return [(rng.randint(-6, 6), rng.randint(-6, 6)) for _ in range(n)]


def convex(rng):
    while True:
        p = hull(points(rng, 6))
        if len(p) >= 3:
            return p


def hull_case(rng, mode):
    p = points(rng, 1 if mode in ("hull", "diameter", "point_hull") else 3)
    h = hull(p)
    text = f"{len(p)}\n" + "\n".join(f"{x} {y}" for x, y in p) + "\n"
    if mode == "hull":
        area = (
            abs(sum(cross(h[i], h[(i + 1) % len(h)]) for i in range(len(h))))
            if h
            else 0
        )
        return text, f"{len(h)} {area}\n"
    if mode == "diameter":
        answer = max(
            ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 for a in p for b in p),
            default=0,
        )
        return text, f"{answer}\n"
    if mode == "lattice":
        if len(h) < 3:
            return hull_case(rng, mode)
        area = abs(
            sum(cross(h[i], h[(i + 1) % len(h)]) for i in range(len(h)))
        )
        boundary = sum(
            math.gcd(
                abs(h[i][0] - h[(i + 1) % len(h)][0]),
                abs(h[i][1] - h[(i + 1) % len(h)][1]),
            )
            for i in range(len(h))
        )
        return text, f"{area} {boundary}\n"
    if mode == "triangle":
        if len(p) < 3:
            return hull_case(rng, mode)
        answer = max(
            abs(cross(a, b, c)) for a, b, c in itertools.combinations(p, 3)
        )
        return text, f"{answer}\n"
    raise AssertionError(mode)


def minkowski_case(rng, collision=False):
    a, b = convex(rng), convex(rng)
    q = rng.randint(5, 15)
    queries = [(rng.randint(-12, 12), rng.randint(-12, 12)) for _ in range(q)]
    sums = [(x[0] + y[0], x[1] + y[1]) for x in a for y in b]
    if collision:
        sums = [(x[0] - y[0], x[1] - y[1]) for x in a for y in b]
    region = hull(sums)
    out = ["YES" if inside(region, x) >= 0 else "NO" for x in queries]
    text = f"{len(a)} {len(b)} {q}\n"
    text += "\n".join(f"{x} {y}" for x, y in a) + "\n"
    text += "\n".join(f"{x} {y}" for x, y in b) + "\n"
    text += "\n".join(f"{x} {y}" for x, y in queries) + "\n"
    return text, "\n".join(out) + "\n"


def orth_case(rng, weighted=False):
    h, v = rng.randint(0, 7), rng.randint(0, 7)
    hs, vs = [], []
    for _ in range(h):
        x1, x2, y = rng.randint(-5, 5), rng.randint(-5, 5), rng.randint(-5, 5)
        hs.append((x1, x2, y, rng.randint(-4, 5) if weighted else 1))
    for _ in range(v):
        x, y1, y2 = rng.randint(-5, 5), rng.randint(-5, 5), rng.randint(-5, 5)
        vs.append((x, y1, y2, rng.randint(-4, 5) if weighted else 1))
    ans = 0
    for x1, x2, y, a in hs:
        for x, y1, y2, b in vs:
            if min(x1, x2) <= x <= max(x1, x2) and min(y1, y2) <= y <= max(
                y1, y2
            ):
                ans += a * b
    text = f"{h} {v}\n"
    if weighted:
        text += "\n".join(f"{x1} {x2} {y} {w}" for x1, x2, y, w in hs) + (
            "\n" if hs else ""
        )
        text += "\n".join(f"{x} {y1} {y2} {w}" for x, y1, y2, w in vs) + (
            "\n" if vs else ""
        )
    else:
        text += "\n".join(f"{x1} {x2} {y}" for x1, x2, y, _ in hs) + (
            "\n" if hs else ""
        )
        text += "\n".join(f"{x} {y1} {y2}" for x, y1, y2, _ in vs) + (
            "\n" if vs else ""
        )
    return text, f"{ans}\n"


def rect_case(rng, required=1):
    n = rng.randint(1, 7)
    rects = [
        (
            rng.randint(-4, 4),
            rng.randint(-4, 4),
            rng.randint(-4, 4),
            rng.randint(-4, 4),
        )
        for _ in range(n)
    ]
    xs = sorted(set(x for r in rects for x in (r[0], r[2])))
    ys = sorted(set(y for r in rects for y in (r[1], r[3])))
    area = 0
    for i in range(len(xs) - 1):
        for j in range(len(ys) - 1):
            mx, my = (xs[i] + xs[i + 1]) / 2, (ys[j] + ys[j + 1]) / 2
            covered = sum(
                min(x1, x2) < mx < max(x1, x2)
                and min(y1, y2) < my < max(y1, y2)
                for x1, y1, x2, y2 in rects
            )
            if covered >= required:
                area += (xs[i + 1] - xs[i]) * (ys[j + 1] - ys[j])
    text = f"{n}\n" + "\n".join(" ".join(map(str, r)) for r in rects) + "\n"
    return text, f"{area}\n"


def closest_case(rng):
    p = points(rng, 2)
    best = min(
        (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2
        for a, b in itertools.combinations(p, 2)
    )
    return (
        f"{len(p)}\n" + "\n".join(f"{x} {y}" for x, y in p) + "\n",
        f"{best}\n",
    )


def point_hull_case(rng):
    p = points(rng)
    h = hull(p)
    queries = [
        (rng.randint(-8, 8), rng.randint(-8, 8))
        for _ in range(rng.randint(5, 15))
    ]
    labels = [
        "OUT" if (z := inside(h, q)) < 0 else "BOUNDARY" if z == 0 else "IN"
        for q in queries
    ]
    text = (
        f"{len(p)} {len(queries)}\n"
        + "\n".join(f"{x} {y}" for x, y in p)
        + "\n"
        + "\n".join(f"{x} {y}" for x, y in queries)
        + "\n"
    )
    return text, "\n".join(labels) + "\n"


GENERATORS = {
    "hull": lambda r: hull_case(r, "hull"),
    "diameter": lambda r: hull_case(r, "diameter"),
    "minkowski": minkowski_case,
    "orth": orth_case,
    "rect": rect_case,
    "double_rect": lambda r: rect_case(r, 2),
    "closest": closest_case,
    "lattice": lambda r: hull_case(r, "lattice"),
    "triangle": lambda r: hull_case(r, "triangle"),
    "collision": lambda r: minkowski_case(r, True),
    "weighted_orth": lambda r: orth_case(r, True),
    "point_hull": point_hull_case,
}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("kind", choices=GENERATORS)
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)
    for case in range(args.count):
        inp, out = GENERATORS[args.kind](rng)
        stem = args.out_dir / f"case{case:03d}"
        stem.with_suffix(".in").write_text(inp)
        stem.with_suffix(".out").write_text(out)


if __name__ == "__main__":
    main()
