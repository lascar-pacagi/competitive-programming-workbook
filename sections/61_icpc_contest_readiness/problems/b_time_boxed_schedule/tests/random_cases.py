from __future__ import annotations

import argparse
import random
from pathlib import Path


def best_count(tasks: list[tuple[int, int]]) -> int:
    answer = 0
    for mask in range(1 << len(tasks)):
        chosen = [tasks[i] for i in range(len(tasks)) if mask >> i & 1]
        elapsed = 0
        feasible = True
        for duration, deadline in sorted(chosen, key=lambda task: task[1]):
            elapsed += duration
            if elapsed > deadline:
                feasible = False
                break
        if feasible:
            answer = max(answer, len(chosen))
    return answer


def make_case(rng: random.Random) -> tuple[str, str]:
    n = rng.randint(1, 15)
    tasks = [(rng.randint(1, 25), rng.randint(1, 90)) for _ in range(n)]
    text = str(n) + "\n" + "\n".join(f"{d} {deadline}" for d, deadline in tasks) + "\n"
    return text, f"{best_count(tasks)}\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)
    for case_id in range(args.count):
        case, expected = make_case(rng)
        (args.out_dir / f"case{case_id:03}.in").write_text(case, encoding="utf-8")
        (args.out_dir / f"case{case_id:03}.out").write_text(expected, encoding="utf-8")


if __name__ == "__main__":
    main()
