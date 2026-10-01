import argparse
import random
from pathlib import Path


def make_case(rng):
    n = rng.randint(1, 13)
    alphabet = rng.choice(["a", "ab", "abc"])
    s = "".join(rng.choice(alphabet) for _ in range(n))
    subs = sorted({s[i:j] for i in range(n) for j in range(i + 1, n + 1)})
    q = rng.randint(1, 25)
    ks = [rng.randint(1, len(subs) + 5) for _ in range(q)]
    if rng.random() < 0.2:
        ks.append(10**18)
    answers = []
    for k in ks:
        if k > len(subs):
            answers.append("-1")
        else:
            t = subs[k - 1]
            answers.append(f"{s.find(t) + 1} {len(t)}")
    text = f"{s}\n{len(ks)}\n" + "".join(f"{k}\n" for k in ks)
    return text, "\n".join(answers) + "\n"


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
