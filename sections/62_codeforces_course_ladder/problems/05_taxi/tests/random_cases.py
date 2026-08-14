from __future__ import annotations

import argparse
import itertools
import random
from pathlib import Path


def oracle(values: list[int], k: int) -> int:
    return min(max(team) - min(team) for team in itertools.combinations(values, k))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)
    for case in range(args.count):
        if case == 0:
            n, k = 200_000, 100_000
            values = list(range(n, 0, -1))
            inp = f"1\n{n} {k}\n" + " ".join(map(str, values)) + "\n"
            out = f"{k - 1}\n"
        else:
            t = rng.randint(1, 10)
            lines = [str(t)]
            answers = []
            for _ in range(t):
                n = rng.randint(1, 12)
                k = rng.randint(1, n)
                values = [rng.randint(-30, 30) for _ in range(n)]
                lines.extend((f"{n} {k}", " ".join(map(str, values))))
                answers.append(str(oracle(values, k)))
            inp = "\n".join(lines) + "\n"
            out = "\n".join(answers) + "\n"
        stem = args.out_dir / f"case_{case:03d}"
        stem.with_suffix(".in").write_text(inp, encoding="utf-8")
        stem.with_suffix(".out").write_text(out, encoding="utf-8")


if __name__ == "__main__":
    main()
