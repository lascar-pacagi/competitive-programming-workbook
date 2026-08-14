from __future__ import annotations

import argparse
import itertools
import random
from pathlib import Path


def brute(intervals: list[tuple[int, int]]) -> int:
    candidates = sorted({right for _, right in intervals})
    for count in range(len(candidates) + 1):
        for chosen in itertools.combinations(candidates, count):
            if all(any(left <= day <= right for day in chosen) for left, right in intervals):
                return count
    raise AssertionError("every interval's right endpoint is a valid candidate")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    rng = random.Random(args.seed)
    args.out_dir.mkdir(parents=True, exist_ok=True)

    for case_id in range(args.count):
        if case_id == 0:
            n = 200_000
            intervals = [(index, index) for index in range(n)]
            lines = ["1", str(n)]
            lines.extend(f"{left} {right}" for left, right in intervals)
            expected = f"{n}\n"
        else:
            tests = rng.randint(1, 5)
            lines = [str(tests)]
            answers: list[str] = []
            for _ in range(tests):
                n = rng.randint(1, 10)
                intervals = []
                for _ in range(n):
                    left = rng.randint(-8, 8)
                    right = rng.randint(left, 10)
                    intervals.append((left, right))
                lines.append(str(n))
                lines.extend(f"{left} {right}" for left, right in intervals)
                answers.append(str(brute(intervals)))
            expected = "\n".join(answers) + "\n"
        stem = args.out_dir / f"case_{case_id:03d}"
        stem.with_suffix(".in").write_text("\n".join(lines) + "\n", encoding="utf-8")
        stem.with_suffix(".out").write_text(expected, encoding="utf-8")


if __name__ == "__main__":
    main()
