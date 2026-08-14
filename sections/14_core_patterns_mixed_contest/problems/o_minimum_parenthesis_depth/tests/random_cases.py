import argparse
import itertools
import random
from pathlib import Path


def depth(s):
    balance = maximum = 0
    for char in s:
        balance += 1 if char == "(" else -1
        if balance < 0:
            return None
        maximum = max(maximum, balance)
    return maximum if balance == 0 else None


def oracle(s):
    positions = [i for i, char in enumerate(s) if char == "?"]
    best = None
    for replacement in itertools.product("()", repeat=len(positions)):
        candidate = list(s)
        for i, char in zip(positions, replacement):
            candidate[i] = char
        current = depth(candidate)
        if current is not None:
            best = current if best is None else min(best, current)
    return -1 if best is None else best


def feasible(s, limit):
    low = high = 0
    for prefix, char in enumerate(s, 1):
        if char == "(":
            low += 1
            high += 1
        elif char == ")":
            low -= 1
            high -= 1
        else:
            low -= 1
            high += 1
        parity = prefix & 1
        if low < 0:
            low = parity
        high = min(high, limit)
        if high & 1 != parity:
            high -= 1
        if low > high:
            return False
    return low == 0


def fast(s):
    if len(s) % 2 or not feasible(s, len(s)):
        return -1
    low, high = 1, len(s)
    while low < high:
        middle = (low + high) // 2
        if feasible(s, middle):
            high = middle
        else:
            low = middle + 1
    return low


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)
    fixed = [
        "?", "??", "????", "((??))", "(()?)?", ")???", "(((())))",
        "(?))", "(?)?", "??))", "((?)))", "(?()))",
    ]
    for case in range(args.count):
        if case < len(fixed):
            s = fixed[case]
        elif case == len(fixed):
            s = "?" * 200000
        else:
            s = "".join(rng.choice("()?") for _ in range(rng.randint(1, 14)))
        answer = fast(s) if len(s) > 20 else oracle(s)
        stem = args.out_dir / f"case{case:03d}"
        stem.with_suffix(".in").write_text(s + "\n")
        stem.with_suffix(".out").write_text(f"{answer}\n")


if __name__ == "__main__":
    main()
