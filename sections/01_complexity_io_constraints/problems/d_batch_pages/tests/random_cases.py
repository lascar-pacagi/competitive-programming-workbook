from __future__ import annotations

import argparse
import random
from pathlib import Path


def expected(pairs: list[tuple[int, int]]) -> str:
    out: list[str] = []
    for n, k in pairs:
        if n == 0:
            out.append("0 0")
            continue
        complete, remainder = divmod(n, k)
        pages = complete + (remainder != 0)
        empty = 0 if remainder == 0 else k - remainder
        out.append(f"{pages} {empty}")
    return "\n".join(out) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    rng = random.Random(args.seed)
    args.out_dir.mkdir(parents=True, exist_ok=True)
    for case in range(args.count):
        q = rng.randint(1, 80)
        pairs = [(rng.randrange(0, 10**18 + 1), rng.randint(1, 10**18)) for _ in range(q)]
        inp = str(q) + "\n" + "\n".join(f"{n} {k}" for n, k in pairs) + "\n"
        stem = f"case{case:03d}"
        (args.out_dir / f"{stem}.in").write_text(inp, encoding="utf-8")
        (args.out_dir / f"{stem}.out").write_text(expected(pairs), encoding="utf-8")


if __name__ == "__main__":
    main()
