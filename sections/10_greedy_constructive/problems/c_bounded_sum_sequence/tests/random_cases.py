from __future__ import annotations

import argparse
import itertools
import random
from pathlib import Path


def brute(n: int, m: int, s: int) -> str:
    best: tuple[int, ...] | None = None
    for seq in itertools.product(range(1, m + 1), repeat=n):
        if sum(seq) == s and (best is None or seq < best):
            best = seq
    if best is None:
        return "IMPOSSIBLE"
    return " ".join(map(str, best))


def build_case(rng: random.Random) -> tuple[str, str]:
    t = rng.randint(1, 20)
    lines = [str(t)]
    answers: list[str] = []
    for _ in range(t):
        n = rng.randint(1, 7)
        m = rng.randint(1, 7)
        s = rng.randint(0, n * m + 5)
        lines.append(f"{n} {m} {s}")
        answers.append(brute(n, m, s))
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

