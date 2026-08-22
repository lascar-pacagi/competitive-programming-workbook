import argparse
import random
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)
    for case in range(args.count):
        n = rng.randint(1, 24)
        s = "".join(rng.choice("ACGT") for _ in range(n))
        t = "".join(rng.choice("ACGT") for _ in range(n))
        scores = [sum(s[i] == t[(i + r) % n] for i in range(n)) for r in range(n)]
        best = max(scores)
        stem = args.out_dir / f"case{case:03d}"
        stem.with_suffix(".in").write_text(f"{n}\n{s}\n{t}\n")
        stem.with_suffix(".out").write_text(f"{best} {scores.index(best)}\n")


if __name__ == "__main__":
    main()
