import argparse
import random
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, default=30)
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)

    for case in range(args.count):
        rectangles = []
        for _ in range(rng.randint(1, 8)):
            x1, x2 = sorted(rng.sample(range(-4, 6), 2))
            y1, y2 = sorted(rng.sample(range(-4, 6), 2))
            rectangles.append((x1, y1, x2, y2))
        cells = {
            (x, y)
            for x1, y1, x2, y2 in rectangles
            for x in range(x1, x2)
            for y in range(y1, y2)
        }
        perimeter = 0
        for x, y in cells:
            perimeter += sum(
                neighbor not in cells
                for neighbor in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1))
            )
        text = f"{len(rectangles)}\n"
        text += "".join(" ".join(map(str, rectangle)) + "\n" for rectangle in rectangles)
        stem = args.out_dir / f"case{case:03d}"
        stem.with_suffix(".in").write_text(text)
        stem.with_suffix(".out").write_text(f"{len(cells)} {perimeter}\n")


if __name__ == "__main__":
    main()
