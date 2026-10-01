import argparse
import random
from pathlib import Path


def components(n, edges):
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            x = parent[x]
        return x

    count = n
    for u, v in edges:
        a, b = find(u), find(v)
        if a != b:
            parent[a] = b
            count -= 1
    return count


def make_case(rng):
    n = rng.randint(1, 8)
    m = rng.randint(1, 16)
    edges = [(rng.randrange(n), rng.randrange(n)) for _ in range(m)]
    q = rng.randint(1, 20)
    queries = []
    for _ in range(q):
        l = rng.randint(1, m)
        queries.append((l, rng.randint(l, m)))
    text = f"{n} {m} {q}\n" + "".join(f"{u + 1} {v + 1}\n" for u, v in edges)
    text += "".join(f"{l} {r}\n" for l, r in queries)
    answers = [components(n, edges[l - 1:r]) for l, r in queries]
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
