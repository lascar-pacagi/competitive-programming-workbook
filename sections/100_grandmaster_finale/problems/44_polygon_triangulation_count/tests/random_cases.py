import argparse
import itertools
import math
import random
from pathlib import Path

MOD = 1_000_000_007


def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


def star_polygon(rng, n, span):
    """Random simple polygon: random radii at sorted random angles."""
    while True:
        angles = sorted(rng.uniform(0, 2 * math.pi) for _ in range(n))
        pts = [(round(math.cos(t) * rng.uniform(span / 8, span)), round(math.sin(t) * rng.uniform(span / 8, span))) for t in angles]
        if len(set(pts)) < n:
            continue
        if any(cross(a, b, c) == 0 for a, b, c in itertools.combinations(pts, 3)):
            continue
        if is_simple(pts):
            return pts


def segments_cross(p1, p2, p3, p4):
    d1, d2 = cross(p1, p2, p3), cross(p1, p2, p4)
    d3, d4 = cross(p3, p4, p1), cross(p3, p4, p2)
    return (d1 > 0) != (d2 > 0) and (d3 > 0) != (d4 > 0)


def is_simple(pts):
    n = len(pts)
    for i in range(n):
        for j in range(i + 1, n):
            if abs(i - j) in (1, n - 1):
                continue
            if segments_cross(pts[i], pts[(i + 1) % n], pts[j], pts[(j + 1) % n]):
                return False
    return True


def point_in_polygon(pts, px, py):
    """Even-odd rule for a point not on the boundary (2x scaled coordinates)."""
    inside = False
    n = len(pts)
    for i in range(n):
        (x1, y1), (x2, y2) = pts[i], pts[(i + 1) % n]
        x1, y1, x2, y2 = 2 * x1, 2 * y1, 2 * x2, 2 * y2
        if (y1 > py) != (y2 > py):
            # x coordinate of the crossing compared with px, exactly
            if (px - x1) * (y2 - y1) < (x2 - x1) * (py - y1) if y2 > y1 else (px - x1) * (y2 - y1) > (x2 - x1) * (py - y1):
                inside = not inside
    return inside


def brute(pts):
    n = len(pts)
    diagonals = []
    for i in range(n):
        for j in range(i + 2, n):
            if i == 0 and j == n - 1:
                continue
            if any(segments_cross(pts[i], pts[j], pts[k], pts[(k + 1) % n]) for k in range(n)
                   if len({i, j, k, (k + 1) % n}) == 4):
                continue
            mx, my = pts[i][0] + pts[j][0], pts[i][1] + pts[j][1]
            if point_in_polygon(pts, mx, my):
                diagonals.append((i, j))
    count = 0
    for subset in itertools.combinations(diagonals, n - 3):
        if all(not segments_cross(pts[a], pts[b], pts[c], pts[d]) for (a, b), (c, d) in itertools.combinations(subset, 2)
               if len({a, b, c, d}) == 4):
            count += 1
    return count % MOD


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, default=25)
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)
    for i in range(args.count):
        n = rng.randint(3, 9)
        pts = star_polygon(rng, n, rng.choice([20, 1000, 10**9]))
        if rng.random() < 0.5:
            pts.reverse()
        shift = rng.randrange(n)
        pts = pts[shift:] + pts[:shift]
        stem = args.out_dir / f"case{i:03d}"
        stem.with_suffix(".in").write_text(f"{n}\n" + "".join(f"{x} {y}\n" for x, y in pts))
        stem.with_suffix(".out").write_text(f"{brute(pts)}\n")


if __name__ == "__main__":
    main()
