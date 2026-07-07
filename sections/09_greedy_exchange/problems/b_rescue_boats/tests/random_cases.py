from __future__ import annotations

import argparse
import functools
import random
from pathlib import Path


def brute(weights: list[int], limit: int) -> int:
    weights = tuple(sorted(weights))

    @functools.lru_cache(maxsize=None)
    def dp(state: tuple[int, ...]) -> int:
        if not state:
            return 0
        n = len(state)
        best = 1 + dp(state[:-1])
        heaviest = state[-1]
        for i in range(n - 1):
            if state[i] + heaviest <= limit:
                nxt = state[:i] + state[i + 1:n - 1]
                best = min(best, 1 + dp(nxt))
        return best

    return dp(weights)


def build_case(rng: random.Random) -> tuple[str, str]:
    t = rng.randint(1, 12)
    lines = [str(t)]
    answers: list[str] = []
    for _ in range(t):
        limit = rng.randint(1, 20)
        n = rng.randint(1, 10)
        weights = [rng.randint(1, limit) for _ in range(n)]
        lines.append(f"{n} {limit}")
        lines.append(" ".join(map(str, weights)))
        answers.append(str(brute(weights, limit)))
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

