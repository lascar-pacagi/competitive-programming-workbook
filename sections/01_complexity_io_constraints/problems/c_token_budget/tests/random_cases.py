from __future__ import annotations

import argparse
import random
from pathlib import Path


def ceil_log2_for_estimate(n: int) -> int:
    return max(1, (n - 1).bit_length())


def classify(n: int, budget: int) -> str:
    log = ceil_log2_for_estimate(n)
    estimates = [
        ("cubic", n * n * n),
        ("quadratic", n * n),
        ("nlogn", n * log),
        ("linear", n),
    ]
    for label, cost in estimates:
        if cost <= budget:
            return label
    return "none"


def build_case(rng: random.Random) -> tuple[str, str]:
    q = rng.randint(1, 80)
    lines = [str(q)]
    answers: list[str] = []
    for _ in range(q):
        if rng.random() < 0.35:
            n = rng.randint(1, 100)
        else:
            n = rng.randint(1, 10**9)
        candidates = [
            0,
            max(0, n - 1),
            n,
            n * ceil_log2_for_estimate(n),
            n * n,
            n * n * n,
            rng.randint(0, 10**18),
        ]
        budget = min(10**18, rng.choice(candidates))
        lines.append(f"{n} {budget}")
        answers.append(classify(n, budget))
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

