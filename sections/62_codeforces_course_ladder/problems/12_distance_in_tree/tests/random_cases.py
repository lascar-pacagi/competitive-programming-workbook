from __future__ import annotations

import argparse
import random
from pathlib import Path


def brute(values: list[int], limit: int) -> int:
    answer = 0
    for left in range(len(values)):
        low = high = values[left]
        for right in range(left, len(values)):
            low = min(low, values[right])
            high = max(high, values[right])
            if high - low <= limit:
                answer += 1
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
            n = 200_000
            values = [7] * n
            lines = ["1", f"{n} 0", " ".join(map(str, values))]
            expected = f"{n * (n + 1) // 2}\n"
        else:
            tests = rng.randint(1, 8)
            lines = [str(tests)]
            answers: list[str] = []
            for _ in range(tests):
                n = rng.randint(1, 45)
                limit = rng.randint(0, 20)
                values = [rng.randint(-20, 20) for _ in range(n)]
                lines.extend((f"{n} {limit}", " ".join(map(str, values))))
                answers.append(str(brute(values, limit)))
            expected = "\n".join(answers) + "\n"
        stem = args.out_dir / f"case_{case_id:03d}"
        stem.with_suffix(".in").write_text("\n".join(lines) + "\n", encoding="utf-8")
        stem.with_suffix(".out").write_text(expected, encoding="utf-8")


if __name__ == "__main__":
    main()
