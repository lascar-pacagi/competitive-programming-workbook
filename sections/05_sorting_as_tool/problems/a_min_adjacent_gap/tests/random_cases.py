from __future__ import annotations

import argparse
import random
from pathlib import Path


def min_gap(values: list[int]) -> int:
    values = sorted(values)
    return min(values[i] - values[i - 1] for i in range(1, len(values)))


def build_case(rng: random.Random) -> tuple[str, str]:
    t = rng.randint(1, 20)
    lines = [str(t)]
    answers: list[str] = []
    for _ in range(t):
        n = rng.randint(2, 100)
        if rng.random() < 0.25:
            values = [rng.randint(-5, 5) for _ in range(n)]
        else:
            values = [rng.randint(-10**9, 10**9) for _ in range(n)]
        lines.append(str(n))
        lines.append(" ".join(map(str, values)))
        answers.append(str(min_gap(values)))
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

