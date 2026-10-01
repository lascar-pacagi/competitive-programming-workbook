import argparse
import itertools
import random
from pathlib import Path


def solve(pairs):
    best = -1
    for choice in itertools.product((0, 1), repeat=len(pairs)):
        chosen = sorted(pair[c] for pair, c in zip(pairs, choice))
        gap = min(b - a for a, b in zip(chosen, chosen[1:]))
        best = max(best, gap)
    return best


def make_case(rng):
    n = rng.randint(2, 9)
    span = rng.choice([3, 20, 1000, 10**9])
    pairs = [(rng.randint(0, span), rng.randint(0, span)) for _ in range(n)]
    if rng.random() < 0.2:
        pairs = [(a, a) for a, _ in pairs]
    text = f"{n}\n" + "".join(f"{a} {b}\n" for a, b in pairs)
    return text, f"{solve(pairs)}\n"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, default=25)
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)
    for i in range(args.count):
        case_input, case_output = make_case(rng)
        stem = args.out_dir / f"case{i:03d}"
        stem.with_suffix(".in").write_text(case_input)
        stem.with_suffix(".out").write_text(case_output)


if __name__ == "__main__":
    main()
