import argparse
import random
from pathlib import Path


def distinct(t):
    return len({t[i:j] for i in range(len(t)) for j in range(i + 1, len(t) + 1)})


def make_case(rng):
    n = rng.randint(1, 14)
    alphabet = "ab" if rng.random() < 0.5 else "abc"
    if rng.random() < 0.2:
        s = "a" * n
    elif rng.random() < 0.2:
        unit = "".join(rng.choice(alphabet) for _ in range(rng.randint(1, 3)))
        s = (unit * n)[:n]
    else:
        s = "".join(rng.choice(alphabet) for _ in range(n))
    q = rng.randint(1, 20)
    queries = []
    for _ in range(q):
        l = rng.randint(1, n)
        queries.append((l, rng.randint(l, n)))
    text = f"{s}\n{q}\n" + "".join(f"{l} {r}\n" for l, r in queries)
    answers = [distinct(s[l - 1:r]) for l, r in queries]
    return text, "\n".join(map(str, answers)) + "\n"


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
