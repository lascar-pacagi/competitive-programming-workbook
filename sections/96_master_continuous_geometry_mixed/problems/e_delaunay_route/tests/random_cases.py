import argparse
import math
import random
from pathlib import Path


def make_case(rng):
    while True:
        points = [
            (rng.randint(-100, 100), rng.randint(-100, 100))
            for _ in range(3)
        ]
        area2 = ((points[1][0] - points[0][0])
                 * (points[2][1] - points[0][1])
                 - (points[1][1] - points[0][1])
                 * (points[2][0] - points[0][0]))
        if area2:
            break
    source, sink = rng.sample(range(3), 2)
    lines = [f"3 {source + 1} {sink + 1}"]
    lines.extend(f"{x} {y}" for x, y in points)
    expected = math.dist(points[source], points[sink])
    return "\n".join(lines) + "\n", f"{expected:.10f}\n"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)
    for case_id in range(args.count):
        case, expected = make_case(rng)
        stem = f"case_{case_id:03d}"
        (args.out_dir / f"{stem}.in").write_text(case)
        (args.out_dir / f"{stem}.out").write_text(expected)


if __name__ == '__main__':
    main()
