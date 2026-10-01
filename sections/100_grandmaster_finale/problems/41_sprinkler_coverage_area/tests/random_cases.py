import argparse
import math
import random
from pathlib import Path



def union_length(circles, x):
    spans = []
    for cx, cy, r in circles:
        dx = x - cx
        if abs(dx) < r:
            h = math.sqrt(r * r - dx * dx)
            spans.append((cy - h, cy + h))
    spans.sort()
    total = 0.0
    cur = -math.inf
    for lo, hi in spans:
        if hi <= cur:
            continue
        total += hi - max(lo, cur)
        cur = hi
    return total


def integrate(circles, a, b, steps=1200):
    """Integral of the cross-section length over [a, b].

    Inside a segment the length is a smooth sum of square roots that can only
    be singular at the ends; x = a + (b - a) sin^2(phi) removes those
    singularities, so composite Simpson converges at its full order."""
    w = b - a
    h = (math.pi / 2) / steps
    total = 0.0
    for k in range(steps + 1):
        phi = k * h
        s, c = math.sin(phi), math.cos(phi)
        value = union_length(circles, a + w * s * s) * 2 * w * s * c
        total += value * (1 if k in (0, steps) else 4 if k % 2 else 2)
    return total * h / 3


def brute(circles):
    """Integrate the vertical cross-section length between critical abscissae."""
    xs = set()
    for cx, cy, r in circles:
        xs.add(cx - r)
        xs.add(cx + r)
    for i, (x1, y1, r1) in enumerate(circles):
        for x2, y2, r2 in circles[i + 1:]:
            d = math.hypot(x2 - x1, y2 - y1)
            if d == 0 or d > r1 + r2 or d < abs(r1 - r2):
                continue
            a = (r1 * r1 - r2 * r2 + d * d) / (2 * d)
            h = math.sqrt(max(0.0, r1 * r1 - a * a))
            mx = x1 + a * (x2 - x1) / d
            xs.add(mx + h * (y2 - y1) / d)
            xs.add(mx - h * (y2 - y1) / d)
    xs = sorted(xs)
    total = 0.0
    for a, b in zip(xs, xs[1:]):
        if b - a > 1e-12:
            total += integrate(circles, a, b)
    return total


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, default=25)
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)
    for i in range(args.count):
        n = rng.randint(1, 6)
        span = rng.choice([3, 10, 40])
        circles = [(rng.randint(-span, span), rng.randint(-span, span), rng.randint(1, span)) for _ in range(n)]
        if rng.random() < 0.2:
            circles.append(circles[0])  # duplicate
        if rng.random() < 0.2:
            x, y, r = circles[0]
            circles.append((x + r + 2, y, 2))  # externally tangent
        stem = args.out_dir / f"case{i:03d}"
        stem.with_suffix(".in").write_text(f"{len(circles)}\n" + "".join(f"{x} {y} {r}\n" for x, y, r in circles))
        stem.with_suffix(".out").write_text("%.10f\n" % brute(circles))


if __name__ == "__main__":
    main()
