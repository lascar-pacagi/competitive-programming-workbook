from __future__ import annotations

import argparse
import random
from pathlib import Path


def brute(values: list[int], labels: int) -> int:
    best = len(values) + 1
    for left in range(len(values)):
        count = [0] * (labels + 1)
        covered = 0
        for right in range(left, len(values)):
            value = values[right]
            if count[value] == 0:
                covered += 1
            count[value] += 1
            if covered == labels:
                best = min(best, right - left + 1)
                break
    return -1 if best == len(values) + 1 else best


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
            n = labels = 200_000
            values = list(range(1, labels + 1))
            stem = args.out_dir / f"case_{case_id:03d}"
            stem.with_suffix(".in").write_text(
                f"1\n{n} {labels}\n" + " ".join(map(str, values)) + "\n",
                encoding="utf-8",
            )
            stem.with_suffix(".out").write_text(f"{n}\n", encoding="utf-8")
            continue
        tests = rng.randint(1, 8)
        lines = [str(tests)]
        answers: list[str] = []
        for _ in range(tests):
            n = rng.randint(1, 45)
            labels = rng.randint(1, 12)
            values = [rng.randint(1, labels) for _ in range(n)]
            lines.append(f"{n} {labels}")
            lines.append(" ".join(map(str, values)))
            answers.append(str(brute(values, labels)))
        stem = args.out_dir / f"case_{case_id:03d}"
        stem.with_suffix(".in").write_text("\n".join(lines) + "\n", encoding="utf-8")
        stem.with_suffix(".out").write_text("\n".join(answers) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
