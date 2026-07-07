from __future__ import annotations

import argparse
import random
from pathlib import Path


def solve(jobs: list[tuple[int, int, int]], m: int) -> tuple[int, int]:
    load = [0] * (m + 1)
    for l, r, w in jobs:
        for time in range(l, r + 1):
            load[time] += w
    best = load[1]
    best_time = 1
    for time in range(2, m + 1):
        if load[time] > best:
            best = load[time]
            best_time = time
    return best, best_time


def build_case(rng: random.Random) -> tuple[str, str]:
    t = rng.randint(1, 15)
    lines = [str(t)]
    answers: list[str] = []
    for _ in range(t):
        m = rng.randint(1, 80)
        n = rng.randint(1, 80)
        jobs: list[tuple[int, int, int]] = []
        lines.append(f"{n} {m}")
        for _ in range(n):
            l = rng.randint(1, m)
            r = rng.randint(l, m)
            w = rng.randint(-20, 30)
            jobs.append((l, r, w))
            lines.append(f"{l} {r} {w}")
        best, time = solve(jobs, m)
        answers.append(f"{best} {time}")
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

