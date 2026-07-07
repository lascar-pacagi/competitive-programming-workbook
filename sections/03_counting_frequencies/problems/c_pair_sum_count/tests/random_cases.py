from __future__ import annotations

import argparse
import random
from pathlib import Path


def count_pairs(values: list[int], target: int) -> int:
    answer = 0
    for i in range(len(values)):
        for j in range(i + 1, len(values)):
            if values[i] + values[j] == target:
                answer += 1
    return answer


def build_case(rng: random.Random) -> tuple[str, str]:
    t = rng.randint(1, 20)
    lines = [str(t)]
    answers: list[str] = []
    for _ in range(t):
        n = rng.randint(1, 120)
        values = [rng.randint(-30, 30) for _ in range(n)]
        if rng.random() < 0.5 and n >= 2:
            a, b = rng.sample(values, 2)
            target = a + b
        else:
            target = rng.randint(-60, 60)
        lines.append(f"{n} {target}")
        lines.append(" ".join(map(str, values)))
        answers.append(str(count_pairs(values, target)))
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

