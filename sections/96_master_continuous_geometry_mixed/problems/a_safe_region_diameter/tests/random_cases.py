import argparse
import math
import random
from pathlib import Path


def make_case(rng):
    width = rng.randint(1, 1000)
    height = rng.randint(1, 1000)
    x = rng.randint(-1000, 1000)
    y = rng.randint(-1000, 1000)
    lines = [
        f"{x} {y} {x + width} {y}",
        f"{x + width} {y} {x + width} {y + height}",
        f"{x + width} {y + height} {x} {y + height}",
        f"{x} {y + height} {x} {y}",
    ]
    return "4\n" + "\n".join(lines) + "\n", f"{math.hypot(width, height):.10f}\n"


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
