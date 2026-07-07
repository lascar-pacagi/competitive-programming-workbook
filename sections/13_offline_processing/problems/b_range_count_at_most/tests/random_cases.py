from __future__ import annotations

import argparse
import random
from pathlib import Path


def brute(a: list[int], queries: list[tuple[int, int, int]]) -> list[int]:
    ans: list[int] = []
    for l, r, x in queries:
        ans.append(sum(1 for value in a[l - 1:r] if value <= x))
    return ans


def build_case(rng: random.Random) -> tuple[str, str]:
    t = rng.randint(1, 10)
    lines = [str(t)]
    answers: list[str] = []
    for _ in range(t):
        n = rng.randint(1, 20)
        q = rng.randint(1, 20)
        a = [rng.randint(-20, 20) for _ in range(n)]
        queries: list[tuple[int, int, int]] = []
        for _ in range(q):
            l = rng.randint(1, n)
            r = rng.randint(l, n)
            x = rng.randint(-25, 25)
            queries.append((l, r, x))
        lines.append(f"{n} {q}")
        lines.append(" ".join(map(str, a)))
        lines.extend(f"{l} {r} {x}" for l, r, x in queries)
        answers.extend(map(str, brute(a, queries)))
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

