from __future__ import annotations

import argparse
import itertools
import random
from pathlib import Path


def brute(durations: list[int], limit: int) -> tuple[int, int]:
    """Independent tiny oracle: enumerate every ordered prefix schedule."""
    best_solved = 0
    best_penalty = 0
    for order in itertools.permutations(range(len(durations))):
        elapsed = 0
        penalty = 0
        for position, index in enumerate(order, start=1):
            elapsed += durations[index]
            if elapsed > limit:
                break
            penalty += elapsed
            if position > best_solved or (position == best_solved and penalty < best_penalty):
                best_solved = position
                best_penalty = penalty
    return best_solved, best_penalty


def small_case(rng: random.Random) -> tuple[str, str]:
    n = rng.randint(1, 8)
    limit = rng.randint(1, 35)
    durations = [rng.randint(1, 15) for _ in range(n)]
    solved, penalty = brute(durations, limit)
    return f"{n} {limit}\n" + " ".join(map(str, durations)) + "\n", f"{solved} {penalty}\n"


def scale_case() -> tuple[str, str]:
    """Long tasks first in input; only the 100,000 short tasks should survive."""
    long_count = 100_000
    short_count = 100_000
    durations = [10**12] * long_count + [1] * short_count
    penalty = short_count * (short_count + 1) // 2
    case = f"{len(durations)} {short_count}\n" + " ".join(map(str, durations)) + "\n"
    return case, f"{short_count} {penalty}\n"


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
