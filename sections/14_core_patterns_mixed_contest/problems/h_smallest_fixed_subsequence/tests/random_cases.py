import argparse
import itertools
import random
from pathlib import Path


def oracle(s, k):
    return min(
        "".join(s[index] for index in chosen)
        for chosen in itertools.combinations(range(len(s)), k)
    )


def greedy(s, k):
    remove = len(s) - k
    stack = []
    for char in s:
        while remove and stack and stack[-1] > char:
            stack.pop()
            remove -= 1
        stack.append(char)
    return "".join(stack[:k])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)
    for case in range(args.count):
        if case == 0:
            s = "zyxwvutsrqponmlkjihgfedcba" * 7693
            s = s[:200000]
            k = 100000
            answer = greedy(s, k)
        else:
            s = "".join(rng.choice("abcde") for _ in range(rng.randint(1, 14)))
            k = rng.randint(1, len(s))
            answer = oracle(s, k)
        stem = args.out_dir / f"case{case:03d}"
        stem.with_suffix(".in").write_text(f"{s}\n{k}\n")
        stem.with_suffix(".out").write_text(answer + "\n")


if __name__ == "__main__":
    main()
