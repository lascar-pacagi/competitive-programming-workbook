from __future__ import annotations

import argparse
import random
from collections import Counter
from pathlib import Path


def winner(values: list[int]) -> str:
    freq = Counter(values)
    best_value = None
    best_count = -1
    for value, count in freq.items():
        if best_value is None or count > best_count or (count == best_count and value < best_value):
            best_value = value
            best_count = count
    return f"{best_value} {best_count}"


def build_case(rng: random.Random) -> tuple[str, str]:
    t = rng.randint(1, 20)
    lines = [str(t)]
    answers: list[str] = []
    for _ in range(t):
        n = rng.randint(1, 100)
        if rng.random() < 0.3:
            values = [rng.choice([-3, -2, -1, 0, 1, 2, 3]) for _ in range(n)]
        else:
            values = [rng.randint(-50, 50) for _ in range(n)]
        lines.append(str(n))
        lines.append(" ".join(map(str, values)))
        answers.append(winner(values))
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

