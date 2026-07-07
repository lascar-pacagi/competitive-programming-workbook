from __future__ import annotations

import argparse
import itertools
import random
from pathlib import Path


def valid(s: str) -> bool:
    bal = 0
    for i, ch in enumerate(s):
        bal += 1 if ch == "(" else -1
        if bal < 0:
            return False
        if i + 1 < len(s) and bal == 0:
            return False
    return bal == 0


def brute(s: str) -> str:
    positions = [i for i, ch in enumerate(s) if ch == "?"]
    best: str | None = None
    for bits in itertools.product("()", repeat=len(positions)):
        chars = list(s)
        for pos, ch in zip(positions, bits):
            chars[pos] = ch
        candidate = "".join(chars)
        if valid(candidate) and (best is None or candidate < best):
            best = candidate
    return best if best is not None else "IMPOSSIBLE"


def build_case(rng: random.Random) -> tuple[str, str]:
    t = rng.randint(1, 20)
    lines = [str(t)]
    answers: list[str] = []
    alphabet = ["(", ")", "?"]
    for _ in range(t):
        n = rng.randint(1, 10)
        s = "".join(rng.choice(alphabet) for _ in range(n))
        lines.append(s)
        answers.append(brute(s))
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

