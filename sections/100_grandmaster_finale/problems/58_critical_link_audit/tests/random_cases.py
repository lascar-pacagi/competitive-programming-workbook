import argparse
import random
from pathlib import Path


def reachable(n, links, skip):
    adj = [[] for _ in range(n)]
    for i, (u, v) in enumerate(links):
        if i != skip:
            adj[u].append(v)
    seen = [False] * n
    seen[0] = True
    stack = [0]
    while stack:
        v = stack.pop()
        for w in adj[v]:
            if not seen[w]:
                seen[w] = True
                stack.append(w)
    return sum(seen)


def make_case(rng):
    n = rng.randint(1, 9)
    m = rng.randint(1, 18)
    shape = rng.random()
    links = []
    for _ in range(m):
        if shape < 0.5 and n > 1:
            u = rng.randrange(n)
            v = rng.randrange(n) if rng.random() < 0.3 else min(n - 1, u + 1)
        else:
            u, v = rng.randrange(n), rng.randrange(n)
        links.append((u, v))
    base = reachable(n, links, -1)
    answers = [base - reachable(n, links, i) for i in range(m)]
    text = f"{n} {m}\n" + "".join(f"{u + 1} {v + 1}\n" for u, v in links)
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
