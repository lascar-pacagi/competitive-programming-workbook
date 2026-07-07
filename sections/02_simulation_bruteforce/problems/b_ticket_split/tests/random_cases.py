from __future__ import annotations

import argparse
import random
from pathlib import Path


def find_split(n: int, s: int, a: int, b: int, c: int) -> str:
    for x in range(n + 1):
        for y in range(n - x + 1):
            z = n - x - y
            if a * x + b * y + c * z == s:
                return f"{x} {y} {z}"
    return "-1"


def build_case(rng: random.Random) -> tuple[str, str]:
    t = rng.randint(1, 30)
    lines = [str(t)]
    answers: list[str] = []
    for _ in range(t):
        n = rng.randint(0, 60)
        a = rng.randint(0, 100)
        b = rng.randint(0, 100)
        c = rng.randint(0, 100)
        if rng.random() < 0.65:
            x = rng.randint(0, n)
            y = rng.randint(0, n - x)
            z = n - x - y
            s = a * x + b * y + c * z
        else:
            s = rng.randint(0, max(1, 100 * max(1, n) + 50))
        lines.append(f"{n} {s} {a} {b} {c}")
        answers.append(find_split(n, s, a, b, c))
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

