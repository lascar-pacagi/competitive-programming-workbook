import argparse
import itertools
import random
from pathlib import Path


def valid(s):
    balance = 0
    for index, char in enumerate(s):
        balance += 1 if char == "(" else -1
        if balance < 0:
            return False
    return balance == 0


def oracle(s):
    positions = [i for i, char in enumerate(s) if char == "?"]
    for choices in itertools.product("()", repeat=len(positions)):
        candidate = list(s)
        for index, char in zip(positions, choices):
            candidate[index] = char
        if valid(candidate):
            return "YES"
    return "NO"


def fast(s):
    if len(s) % 2:
        return "NO"
    low = high = 0
    for index, char in enumerate(s):
        if char == "(":
            low += 1; high += 1
        elif char == ")":
            low -= 1; high -= 1
        else:
            low -= 1; high += 1
        if low < 0:
            low = (index + 1) & 1
        if high < 0:
            return "NO"
    return "YES" if low == 0 else "NO"


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
            strings = ["?" * 100000, ")" + "?" * 99999]
            answers = list(map(fast, strings))
        else:
            strings = [
                "".join(rng.choice("()?") for _ in range(rng.randint(1, 13)))
                for _ in range(rng.randint(1, 10))
            ]
            answers = list(map(oracle, strings))
        stem = args.out_dir / f"case{case:03d}"
        stem.with_suffix(".in").write_text(
            str(len(strings)) + "\n" + "\n".join(strings) + "\n"
        )
        stem.with_suffix(".out").write_text("\n".join(answers) + "\n")


if __name__ == "__main__":
    main()
