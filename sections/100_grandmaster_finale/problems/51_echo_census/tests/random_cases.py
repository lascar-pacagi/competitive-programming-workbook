import argparse
import random
from pathlib import Path


def solve(s):
    found = set()
    n = len(s)
    for i in range(n):
        for L in range(1, (n - i) // 2 + 1):
            if s[i:i + L] == s[i + L:i + 2 * L]:
                found.add(s[i:i + 2 * L])
    return len(found)


def make_case(rng):
    n = rng.randint(1, 40)
    kind = rng.random()
    if kind < 0.15:
        s = "a" * n
    elif kind < 0.35:
        unit = "".join(rng.choice("ab") for _ in range(rng.randint(1, 4)))
        s = (unit * n)[:n]
    elif kind < 0.5:
        a, b = "a", "ab"
        while len(b) < n:
            a, b = b, b + a
        s = b[:n]
    else:
        s = "".join(rng.choice(rng.choice(["ab", "abc", "abcdefghijklmnopqrstuvwxyz"])) for _ in range(n))
    return f"{s}\n", f"{solve(s)}\n"


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
