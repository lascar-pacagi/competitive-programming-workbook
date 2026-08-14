import argparse
import itertools
import random
from pathlib import Path


def oracle(s, k):
    keep = len(s) - k
    return min("".join(s[i] for i in indices)
               for indices in itertools.combinations(range(len(s)), keep))


def greedy(s, k):
    answer = []
    for digit in s:
        while k and answer and answer[-1] > digit:
            answer.pop()
            k -= 1
        answer.append(digit)
    return "".join(answer[:len(answer) - k])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)
    fixed = [("1111", 2), ("1000", 1), ("10200", 1), ("987654", 5)]
    for case in range(args.count):
        if case < len(fixed):
            s, k = fixed[case]
        elif case == len(fixed):
            s = "".join(str(rng.randrange(10)) for _ in range(200000))
            k = 100000
        else:
            n = rng.randint(1, 13)
            s = "".join(str(rng.randrange(10)) for _ in range(n))
            k = rng.randrange(n)
        answer = greedy(s, k) if len(s) > 20 else oracle(s, k)
        stem = args.out_dir / f"case{case:03d}"
        stem.with_suffix(".in").write_text(f"{s}\n{k}\n")
        stem.with_suffix(".out").write_text(answer + "\n")


if __name__ == "__main__":
    main()
