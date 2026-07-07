from __future__ import annotations

import argparse
import random
from pathlib import Path


def brute(a: list[int], k: int) -> list[int]:
    return [max(a[i:i + k]) for i in range(len(a) - k + 1)]


def build_case(rng: random.Random) -> tuple[str, str]:
    t = rng.randint(1, 20)
    lines = [str(t)]
    answers: list[str] = []
    for _ in range(t):
        n = rng.randint(1, 25)
        k = rng.randint(1, n)
        a = [rng.randint(-20, 20) for _ in range(n)]
        lines.append(f"{n} {k}")
        lines.append(" ".join(map(str, a)))
        answers.append(" ".join(map(str, brute(a, k))))
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

