from __future__ import annotations

import argparse
import math
import random
from pathlib import Path


def build_case(rng: random.Random) -> tuple[str, str]:
    t = rng.randint(1, 200)
    values: list[int] = []
    for _ in range(t):
        if rng.random() < 0.35:
            x = rng.randint(0, 1_000_000_000)
            delta = rng.choice([-1, 0, 1])
            values.append(max(0, min(10**18, x * x + delta)))
        else:
            values.append(rng.randint(0, 10**18))
    lines = [str(t), *map(str, values)]
    answers = [str(math.isqrt(n) if math.isqrt(n) ** 2 == n else math.isqrt(n) + 1) for n in values]
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

