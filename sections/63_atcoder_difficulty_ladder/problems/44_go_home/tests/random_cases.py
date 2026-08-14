from __future__ import annotations

import argparse
import random
from fractions import Fraction
from pathlib import Path


def on_segment(point: tuple[int, int], a: tuple[int, int], b: tuple[int, int]) -> bool:
    px, py = point
    ax, ay = a
    bx, by = b
    return (
        (bx - ax) * (py - ay) == (by - ay) * (px - ax)
        and min(ax, bx) <= px <= max(ax, bx)
        and min(ay, by) <= py <= max(ay, by)
    )


def strictly_inside(point: tuple[int, int], polygon: list[tuple[int, int]]) -> bool:
    """Independent tiny oracle: exact ray crossing, with boundary excluded."""
    px, py = point
    crossings = 0
    for index, a in enumerate(polygon):
        b = polygon[(index + 1) % len(polygon)]
        if on_segment(point, a, b):
            return False
        ax, ay = a
        bx, by = b
        if (ay > py) != (by > py):
            intersection_x = Fraction(ax * (by - ay) + (bx - ax) * (py - ay), by - ay)
            if intersection_x > px:
                crossings ^= 1
    return bool(crossings)


def count_interior_by_grid(polygon: list[tuple[int, int]]) -> int:
    min_x = min(x for x, _ in polygon)
    max_x = max(x for x, _ in polygon)
    min_y = min(y for _, y in polygon)
    max_y = max(y for _, y in polygon)
    return sum(
        strictly_inside((x, y), polygon)
        for x in range(min_x, max_x + 1)
        for y in range(min_y, max_y + 1)
    )


def small_polygon(rng: random.Random) -> list[tuple[int, int]]:
    x0 = rng.randint(-8, 4)
    y0 = rng.randint(-8, 4)
    width = rng.randint(1, 8)
    height = rng.randint(1, 8)
    kind = rng.randrange(3)
    if kind == 0:
        return [(x0, y0), (x0 + width, y0), (x0 + width, y0 + height), (x0, y0 + height)]
    if kind == 1:
        return [(x0, y0), (x0 + width, y0), (x0, y0 + height)]
    # A rectangle with a deliberate collinear vertex on its lower boundary.
    width *= 2
    return [
        (x0, y0),
        (x0 + width // 2, y0),
        (x0 + width, y0),
        (x0 + width, y0 + height),
        (x0, y0 + height),
    ]


def small_case(rng: random.Random) -> tuple[str, str]:
    polygon = small_polygon(rng)
    expected = count_interior_by_grid(polygon)
    case = str(len(polygon)) + "\n" + "\n".join(f"{x} {y}" for x, y in polygon) + "\n"
    return case, f"{expected}\n"


def scale_case() -> tuple[str, str]:
    """A subdivided 10^12-by-10^12 square forces wide integer arithmetic."""
    side = 10**12
    steps = 50_000
    delta = side // steps
    points: list[tuple[int, int]] = []
    points.extend((index * delta, 0) for index in range(steps))
    points.extend((side, index * delta) for index in range(steps))
    points.extend((side - index * delta, side) for index in range(steps))
    points.extend((0, side - index * delta) for index in range(steps))
    case = str(len(points)) + "\n" + "\n".join(f"{x} {y}" for x, y in points) + "\n"
    return case, "999999999998000000000001\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()

    rng = random.Random(args.seed)
    args.out_dir.mkdir(parents=True, exist_ok=True)
    for number in range(args.count):
        case, expected = scale_case() if number == 0 else small_case(rng)
        (args.out_dir / f"case_{number:03d}.in").write_text(case)
        (args.out_dir / f"case_{number:03d}.out").write_text(expected)


if __name__ == "__main__":
    main()
