import argparse
import itertools
import random
from pathlib import Path


def valid(s):
    balance = 0
    for char in s:
        balance += 1 if char == "(" else -1
        if balance < 0:
            return False
    return balance == 0


def oracle(s):
    positions = [i for i, char in enumerate(s) if char == "?"]
    completions = []
    for replacement in itertools.product("()", repeat=len(positions)):
        candidate = list(s)
        for i, char in zip(positions, replacement):
            candidate[i] = char
        candidate = "".join(candidate)
        if valid(candidate):
            completions.append(candidate)
    if not completions:
        return "IMPOSSIBLE"
    answer = list(s)
    for i in positions:
        choices = {completion[i] for completion in completions}
        answer[i] = choices.pop() if len(choices) == 1 else "?"
    return "".join(answer)


def fast(s):
    n = len(s)
    prefix_low = [0] * (n + 1)
    prefix_high = [0] * (n + 1)
    for i, char in enumerate(s):
        if prefix_low[i] > prefix_high[i]:
            prefix_low[i + 1], prefix_high[i + 1] = 1, 0
            continue
        low, high = prefix_low[i], prefix_high[i]
        if char == "(":
            low += 1
            high += 1
        elif char == ")":
            low -= 1
            high -= 1
        else:
            low -= 1
            high += 1
        if low < 0:
            low = (i + 1) & 1
        prefix_low[i + 1], prefix_high[i + 1] = low, high
    if n % 2 or not prefix_low[n] <= 0 <= prefix_high[n]:
        return "IMPOSSIBLE"
    suffix_low = [0] * (n + 1)
    suffix_high = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        if suffix_low[i + 1] > suffix_high[i + 1]:
            suffix_low[i], suffix_high[i] = 1, 0
            continue
        low, high = suffix_low[i + 1], suffix_high[i + 1]
        if s[i] == "(":
            low, high = (1 if low == 0 else low - 1), high - 1
        elif s[i] == ")":
            low, high = low + 1, high + 1
        else:
            low, high = (1 if low == 0 else low - 1), high + 1
        suffix_low[i], suffix_high[i] = low, high
    answer = list(s)
    for i, char in enumerate(s):
        if char != "?":
            continue
        sl, sh = suffix_low[i + 1], suffix_high[i + 1]
        can_open = max(prefix_low[i] + 1, sl) <= min(prefix_high[i] + 1, sh)
        closing_low = max(prefix_low[i], 1) - 1
        can_close = max(closing_low, sl) <= min(prefix_high[i] - 1, sh)
        if can_open and not can_close:
            answer[i] = "("
        elif can_close and not can_open:
            answer[i] = ")"
    return "".join(answer)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)
    fixed = ["?", "??", ")?", "((??", "??????", "?)(?", "((()))",
             "(???)?", "??()??"]
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
        stem.with_suffix(".out").write_text(answer + "\n")


if __name__ == "__main__":
    main()
