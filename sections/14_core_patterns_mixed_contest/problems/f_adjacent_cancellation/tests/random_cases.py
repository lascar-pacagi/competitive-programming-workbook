import argparse
import random
from pathlib import Path


def reduce_string(s):
    stack = []
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    return "".join(stack) or "EMPTY"


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
            strings = [("ab" * 50000), "a" * 100000]
        else:
            strings = [
                "".join(rng.choice("abcd") for _ in range(rng.randint(1, 80)))
                for _ in range(rng.randint(1, 12))
            ]
        stem = args.out_dir / f"case{case:03d}"
        stem.with_suffix(".in").write_text(
            str(len(strings)) + "\n" + "\n".join(strings) + "\n"
        )
        stem.with_suffix(".out").write_text(
            "\n".join(map(reduce_string, strings)) + "\n"
        )


if __name__ == "__main__":
    main()
