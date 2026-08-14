from __future__ import annotations

import argparse
import itertools
import random
from pathlib import Path


def construct(pattern: str) -> tuple[int, ...]:
    pending: list[int] = []
    answer: list[int] = []
    for value in range(1, len(pattern) + 2):
        pending.append(value)
        if value == len(pattern) + 1 or pattern[value - 1] == "<":
            answer.extend(reversed(pending))
            pending.clear()
    return tuple(answer)


def valid(permutation: tuple[int, ...], pattern: str) -> bool:
    return all(
        permutation[index] < permutation[index + 1]
        if symbol == "<"
        else permutation[index] > permutation[index + 1]
        for index, symbol in enumerate(pattern)
    )


def brute(pattern: str) -> tuple[int, ...]:
    n = len(pattern) + 1
    return next(candidate for candidate in itertools.permutations(range(1, n + 1)) if valid(candidate, pattern))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)

    for case_id in range(args.count):
        if case_id == 0:
            patterns = ["<>" * 99_999 + "<"]
            answers = [construct(patterns[0])]
        else:
            patterns = [
                "".join(rng.choice("<>") for _ in range(rng.randint(1, 7)))
                for _ in range(rng.randint(1, 10))
            ]
            answers = [brute(pattern) for pattern in patterns]

        rows = [f"{len(pattern) + 1} {pattern}" for pattern in patterns]
        inp = str(len(patterns)) + "\n" + "\n".join(rows) + "\n"
        out = "\n".join(" ".join(map(str, answer)) for answer in answers) + "\n"
        stem = args.out_dir / f"case{case_id:03d}"
        stem.with_suffix(".in").write_text(inp, encoding="utf-8")
        stem.with_suffix(".out").write_text(out, encoding="utf-8")


if __name__ == "__main__":
    main()
