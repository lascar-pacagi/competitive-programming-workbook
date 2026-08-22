import argparse
import math
import random
from pathlib import Path


def cross(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def hull(points):
    points = sorted(set(points))
    lower = []
    for point in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], point) <= 0:
            lower.pop()
        lower.append(point)
    upper = []
    for point in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], point) <= 0:
            upper.pop()
        upper.append(point)
    return lower[:-1] + upper[:-1]


def point_segment(point, a, b):
    dx, dy = b[0] - a[0], b[1] - a[1]
    t = ((point[0] - a[0]) * dx + (point[1] - a[1]) * dy) / (dx * dx + dy * dy)
    t = min(1.0, max(0.0, t))
    return math.hypot(point[0] - a[0] - t * dx, point[1] - a[1] - t * dy)


def inside(point, polygon):
    return all(cross(polygon[i], polygon[(i + 1) % len(polygon)], point) >= 0 for i in range(len(polygon)))


def segments_intersect(a, b, c, d):
    def sign(value):
        return (value > 0) - (value < 0)
    ab_c = sign(cross(a, b, c))
    ab_d = sign(cross(a, b, d))
    cd_a = sign(cross(c, d, a))
    cd_b = sign(cross(c, d, b))
    if ab_c == 0 and min(a[0], b[0]) <= c[0] <= max(a[0], b[0]) and min(a[1], b[1]) <= c[1] <= max(a[1], b[1]):
        return True
    if ab_d == 0 and min(a[0], b[0]) <= d[0] <= max(a[0], b[0]) and min(a[1], b[1]) <= d[1] <= max(a[1], b[1]):
        return True
    if cd_a == 0 and min(c[0], d[0]) <= a[0] <= max(c[0], d[0]) and min(c[1], d[1]) <= a[1] <= max(c[1], d[1]):
        return True
    if cd_b == 0 and min(c[0], d[0]) <= b[0] <= max(c[0], d[0]) and min(c[1], d[1]) <= b[1] <= max(c[1], d[1]):
        return True
    return ab_c * ab_d < 0 and cd_a * cd_b < 0


def distance(a, b):
    if any(inside(point, b) for point in a) or any(inside(point, a) for point in b):
        return 0.0
    if any(
        segments_intersect(a[i], a[(i + 1) % len(a)], b[j], b[(j + 1) % len(b)])
        for i in range(len(a)) for j in range(len(b))
    ):
        return 0.0
    answer = math.inf
    for point in a:
        for i in range(len(b)):
            answer = min(answer, point_segment(point, b[i], b[(i + 1) % len(b)]))
    for point in b:
        for i in range(len(a)):
            answer = min(answer, point_segment(point, a[i], a[(i + 1) % len(a)]))
    return answer


def polygon(rng, shift):
    while True:
        points = [(rng.randint(-5, 5) + shift[0], rng.randint(-5, 5) + shift[1]) for _ in range(12)]
        result = hull(points)
        if len(result) >= 3:
            return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, default=30)
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)
    for case in range(args.count):
        a = polygon(rng, (0, 0))
        b = polygon(rng, (rng.randint(-8, 12), rng.randint(-8, 12)))
        text = f"{len(a)}\n" + "".join(f"{x} {y}\n" for x, y in a)
        text += f"{len(b)}\n" + "".join(f"{x} {y}\n" for x, y in b)
        stem = args.out_dir / f"case{case:03d}"
        stem.with_suffix(".in").write_text(text)
        stem.with_suffix(".out").write_text(f"{distance(a, b):.12f}\n")


if __name__ == "__main__":
    main()
