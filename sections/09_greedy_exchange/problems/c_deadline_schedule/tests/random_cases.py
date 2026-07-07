from __future__ import annotations

import argparse
import itertools
import random
from pathlib import Path


def feasible(tasks: tuple[tuple[int, int], ...]) -> bool:
    time = 0
    for duration, deadline in sorted(tasks, key=lambda p: p[1]):
        time += duration
        if time > deadline:
            return False
    return True


def brute(tasks: list[tuple[int, int]]) -> int:
    best = 0
    for r in range(len(tasks) + 1):
        for chosen in itertools.combinations(tasks, r):
            if feasible(chosen):
                best = max(best, r)
    return best


def build_case(rng: random.Random) -> tuple[str, str]:
    t = rng.randint(1, 10)
    lines = [str(t)]
    answers: list[str] = []
    for _ in range(t):
        n = rng.randint(1, 10)
        tasks: list[tuple[int, int]] = []
        for _ in range(n):
            duration = rng.randint(1, 12)
            deadline = rng.randint(1, 30)
            tasks.append((duration, deadline))
        lines.append(str(n))
        lines.extend(f"{duration} {deadline}" for duration, deadline in tasks)
        answers.append(str(brute(tasks)))
    return "\n".join(lines) + "\n", "\n".join(answers) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()

    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)
    for i in range(args.count):
        inp, out = build_case(rng)
        stem = args.out_dir / f"case_{i:03d}"
        stem.with_suffix(".in").write_text(inp, encoding="utf-8")
        stem.with_suffix(".out").write_text(out, encoding="utf-8")


if __name__ == "__main__":
    main()

