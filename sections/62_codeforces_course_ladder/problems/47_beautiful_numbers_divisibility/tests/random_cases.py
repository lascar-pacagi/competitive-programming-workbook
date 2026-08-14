from __future__ import annotations

import argparse
import random
from pathlib import Path


def brute(values: list[int], target: int) -> int:
    best = -1
    for mask in range(1 << len(values)):
        total = 0
        count = 0
        for index, value in enumerate(values):
            if (mask >> index) & 1:
                total += value
                count += 1
        if total == target:
            best = max(best, count)
    return best


def small_case(rng: random.Random) -> tuple[str, str]:
    """Independent tiny oracle: enumerate every full-array subset mask."""
    n = rng.randint(1, 15)
    values = [rng.randint(-12, 12) for _ in range(n)]
    target = rng.randint(-35, 35)
    answer = brute(values, target)
    return f"{n} {target}\n" + " ".join(map(str, values)) + "\n", f"{answer}\n"


def scale_case() -> tuple[str, str]:
    """Thirty-six unique powers make the all-items answer directly known."""
    n = 36
    values = [1 << index for index in range(n)]
    target = sum(values)
    return f"{n} {target}\n" + " ".join(map(str, values)) + "\n", "36\n"


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
