from __future__ import annotations

import argparse
import itertools
import random
from pathlib import Path


def brute(pos: list[int], k: int) -> int:
    best = 0
    for comb in itertools.combinations(sorted(pos), k):
        gap = min(comb[i] - comb[i - 1] for i in range(1, k))
        best = max(best, gap)
    return best


def build_case(rng: random.Random) -> tuple[str, str]:
    t = rng.randint(1, 12)
    lines = [str(t)]
    answers: list[str] = []
    for _ in range(t):
        n = rng.randint(2, 10)
        k = rng.randint(2, n)
        pos = sorted(rng.randint(-50, 50) for _ in range(n))
        lines.append(f"{n} {k}")
        lines.append(" ".join(map(str, pos)))
        answers.append(str(brute(pos, k)))
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
