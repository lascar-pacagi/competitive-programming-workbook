from __future__ import annotations

import argparse
import random
from pathlib import Path


def solve_case(s: str) -> str:
    x = 0
    y = 0
    best = 0
    for ch in s:
        if ch == "U":
            y += 1
        elif ch == "D":
            y -= 1
        elif ch == "L":
            x -= 1
        else:
            x += 1
        best = max(best, abs(x) + abs(y))
    return f"{x} {y} {best}"


def build_case(rng: random.Random) -> tuple[str, str]:
    t = rng.randint(1, 30)
    lines = [str(t)]
    answers: list[str] = []
    alphabet = "UDLR"
    for _ in range(t):
        if rng.random() < 0.2:
            ch = rng.choice(alphabet)
            s = ch * rng.randint(1, 60)
        else:
            s = "".join(rng.choice(alphabet) for _ in range(rng.randint(1, 80)))
        lines.append(s)
        answers.append(solve_case(s))
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

