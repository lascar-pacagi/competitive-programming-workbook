from __future__ import annotations

import argparse
import random
from pathlib import Path


def solve(values: list[int]) -> int:
    answer = 0
    for i in range(len(values)):
        for j in range(i):
            answer += values[i] == values[j]
    return answer


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    rng = random.Random(args.seed)
    args.out_dir.mkdir(parents=True, exist_ok=True)
    for case_id in range(args.count):
        if case_id == 0:
            n = 65_537
            values = [0] * n
            stem = args.out_dir / f"case_{case_id:03d}"
            stem.with_suffix(".in").write_text(
                f"1\n{n}\n" + " ".join(map(str, values)) + "\n",
                encoding="utf-8",
            )
            stem.with_suffix(".out").write_text(
                f"{n * (n - 1) // 2}\n",
                encoding="utf-8",
            )
            continue
        t = rng.randint(1, 10)
        blocks = [str(t)]
        answers: list[str] = []
        for _ in range(t):
            n = rng.randint(1, 60)
            values = [rng.randint(-8, 8) for _ in range(n)]
            blocks.extend((str(n), " ".join(map(str, values))))
            answers.append(str(solve(values)))
        stem = args.out_dir / f"case_{case_id:03d}"
        stem.with_suffix(".in").write_text("\n".join(blocks) + "\n", encoding="utf-8")
        stem.with_suffix(".out").write_text("\n".join(answers) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
