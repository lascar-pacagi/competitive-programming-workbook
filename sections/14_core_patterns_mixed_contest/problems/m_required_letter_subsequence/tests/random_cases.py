import argparse
import itertools
import random
from pathlib import Path


def oracle(s, k, required, r):
    candidates = ("".join(s[i] for i in indices)
                  for indices in itertools.combinations(range(len(s)), k))
    return min(word for word in candidates if word.count(required) >= r)


def greedy(s, k, required, r):
    remaining = s.count(required)
    selected_required = 0
    answer = []
    for i, char in enumerate(s):
        while (answer and answer[-1] > char
               and len(answer) - 1 + len(s) - i >= k
               and (answer[-1] != required
                    or selected_required - 1 + remaining >= r)):
            if answer[-1] == required:
                selected_required -= 1
            answer.pop()
        if len(answer) < k:
            if char == required:
                answer.append(char)
                selected_required += 1
            elif k - len(answer) - 1 >= r - selected_required:
                answer.append(char)
        if char == required:
            remaining -= 1
    return "".join(answer)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)
    fixed = [("bbbb", 2, "b", 2), ("dcbaaa", 4, "a", 3),
             ("aaaaaz", 3, "a", 1), ("zabzzb", 4, "b", 2)]
    for case in range(args.count):
        if case < len(fixed):
            s, k, required, r = fixed[case]
        elif case == len(fixed):
            s = ("zyxwvutsrqponmlkjihgfedcba" * 7693)[:200000]
            required, k, r = "m", 150000, 5000
        else:
            n = rng.randint(1, 13)
            alphabet = "abcde"
            s = "".join(rng.choice(alphabet) for _ in range(n))
            required = rng.choice(s)
            r = rng.randint(1, s.count(required))
            k = rng.randint(r, n)
        answer = greedy(s, k, required, r) if len(s) > 20 else oracle(
            s, k, required, r)
        stem = args.out_dir / f"case{case:03d}"
        stem.with_suffix(".in").write_text(f"{s}\n{k} {required} {r}\n")
        stem.with_suffix(".out").write_text(answer + "\n")


if __name__ == "__main__":
    main()
