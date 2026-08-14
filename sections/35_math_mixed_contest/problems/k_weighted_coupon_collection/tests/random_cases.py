import argparse
import random
from pathlib import Path


MOD = 1_000_000_007


def markov_oracle(weight):
    n = len(weight)
    total = sum(weight)
    full = (1 << n) - 1
    expected = [0] * (1 << n)
    for mask in range(full - 1, -1, -1):
        unseen_weight = 0
        numerator = total
        for i, value in enumerate(weight):
            if not (mask >> i & 1):
                unseen_weight += value
                numerator += value * expected[mask | (1 << i)]
        expected[mask] = numerator % MOD * pow(unseen_weight, MOD - 2, MOD) % MOD
    return expected[0]


def inclusion_exclusion(weight):
    total = sum(weight)
    answer = 0
    for mask in range(1, 1 << len(weight)):
        selected = sum(weight[i] for i in range(len(weight)) if mask >> i & 1)
        term = total * pow(selected, MOD - 2, MOD) % MOD
        answer += term if mask.bit_count() & 1 else -term
    return answer % MOD


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)

    fixed = [[7], [1, 2], [1] * 20]
    for case in range(args.count):
        weight = fixed[case] if case < len(fixed) else [
            rng.randint(1, 30) for _ in range(rng.randint(1, 9))
        ]
        answer = (
            markov_oracle(weight)
            if len(weight) <= 9
            else inclusion_exclusion(weight)
        )
        stem = args.out_dir / f"case{case:03d}"
        stem.with_suffix(".in").write_text(
            f"{len(weight)}\n" + " ".join(map(str, weight)) + "\n"
        )
        stem.with_suffix(".out").write_text(f"{answer}\n")


if __name__ == "__main__":
    main()
