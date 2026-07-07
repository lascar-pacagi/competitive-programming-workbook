from __future__ import annotations

import argparse
import random
from pathlib import Path


def steps(x: int, y: int) -> int:
    ans = 0
    while x < y:
        x = 2 * x + 1
        ans += 1
    return ans


def build_case(rng: random.Random) -> tuple[str, str]:
    t = rng.randint(1, 40)
    lines = [str(t)]
    answers: list[str] = []
    for _ in range(t):
        x = rng.randint(1, 10**9)
        if rng.random() < 0.25:
            y = rng.randint(1, x)
        else:
            y = rng.randint(x, 10**18)
        lines.append(f"{x} {y}")
        answers.append(str(steps(x, y)))
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

