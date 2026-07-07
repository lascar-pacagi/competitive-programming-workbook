from __future__ import annotations

import argparse
import random
from pathlib import Path


def brute(a: list[int]) -> list[int]:
    ans: list[int] = []
    for i, x in enumerate(a):
        value = -1
        for y in a[i + 1:]:
            if y > x:
                value = y
                break
        ans.append(value)
    return ans


def build_case(rng: random.Random) -> tuple[str, str]:
    t = rng.randint(1, 20)
    lines = [str(t)]
    answers: list[str] = []
    for _ in range(t):
        n = rng.randint(1, 20)
        a = [rng.randint(-10, 10) for _ in range(n)]
        lines.append(str(n))
        lines.append(" ".join(map(str, a)))
        answers.append(" ".join(map(str, brute(a))))
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

