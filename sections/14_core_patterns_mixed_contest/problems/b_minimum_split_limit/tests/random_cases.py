from __future__ import annotations

import argparse
import functools
import random
from pathlib import Path


def brute(a: list[int], d: int) -> int:
    n = len(a)
    pref = [0]
    for x in a:
        pref.append(pref[-1] + x)

    @functools.lru_cache(maxsize=None)
    def dp(pos: int, groups_left: int) -> int:
        if pos == n:
            return 0
        if groups_left == 0:
            return 10**18
        best = 10**18
        for end in range(pos + 1, n + 1):
            group_sum = pref[end] - pref[pos]
            best = min(best, max(group_sum, dp(end, groups_left - 1)))
        return best

    return dp(0, d)


def build_case(rng: random.Random) -> tuple[str, str]:
    t = rng.randint(1, 12)
    lines = [str(t)]
    answers: list[str] = []
    for _ in range(t):
        n = rng.randint(1, 9)
        d = rng.randint(1, n)
        a = [rng.randint(1, 20) for _ in range(n)]
        lines.append(f"{n} {d}")
        lines.append(" ".join(map(str, a)))
        answers.append(str(brute(a, d)))
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

