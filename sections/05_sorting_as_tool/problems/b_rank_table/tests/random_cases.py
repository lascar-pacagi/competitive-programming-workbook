from __future__ import annotations

import argparse
import random
import string
from pathlib import Path


def random_name(rng: random.Random, used: set[str]) -> str:
    while True:
        name = "".join(rng.choice(string.ascii_lowercase) for _ in range(rng.randint(1, 8)))
        if name not in used:
            used.add(name)
            return name


def build_case(rng: random.Random) -> tuple[str, str]:
    t = rng.randint(1, 15)
    lines = [str(t)]
    answers: list[str] = []
    for _ in range(t):
        n = rng.randint(1, 60)
        used: set[str] = set()
        rows: list[tuple[str, int, int]] = []
        lines.append(str(n))
        for _ in range(n):
            name = random_name(rng, used)
            score = rng.randint(0, 10)
            penalty = rng.randint(0, 10)
            rows.append((name, score, penalty))
            lines.append(f"{name} {score} {penalty}")
        rows.sort(key=lambda row: (-row[1], row[2], row[0]))
        answers.append(" ".join(row[0] for row in rows))
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

