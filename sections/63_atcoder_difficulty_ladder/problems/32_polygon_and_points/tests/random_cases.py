from __future__ import annotations

import argparse
import random
from pathlib import Path


def brute(ranges: list[tuple[int, int]]) -> tuple[list[int], list[int]]:
    contains = [0] * len(ranges)
    contained_by = [0] * len(ranges)
    for i, (left_i, right_i) in enumerate(ranges):
        for j, (left_j, right_j) in enumerate(ranges):
            if i == j:
                continue
            if left_i <= left_j and right_j <= right_i:
                contains[i] += 1
            if left_j <= left_i and right_i <= right_j:
                contained_by[i] += 1
    return contains, contained_by


def small_case(rng: random.Random) -> tuple[str, str]:
    """Independent oracle: check every ordered pair of tiny intervals."""
    n = rng.randint(1, 11)
    ranges: list[tuple[int, int]] = []
    for _ in range(n):
        left = rng.randint(-12, 12)
        right = rng.randint(left, 15)
        ranges.append((left, right))
    contains, contained_by = brute(ranges)
    case = str(n) + "\n" + "\n".join(f"{left} {right}" for left, right in ranges) + "\n"
    expected = " ".join(map(str, contains)) + "\n"
    expected += " ".join(map(str, contained_by)) + "\n"
    return case, expected


def scale_case() -> tuple[str, str]:
    """A fully nested chain with directly known counts at maximum size."""
    n = 200_000
    ranges = (f"{index} {400_001 - index}" for index in range(1, n + 1))
    case = str(n) + "\n" + "\n".join(ranges) + "\n"
    contains = " ".join(map(str, range(n - 1, -1, -1)))
    contained_by = " ".join(map(str, range(n)))
    return case, contains + "\n" + contained_by + "\n"


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
