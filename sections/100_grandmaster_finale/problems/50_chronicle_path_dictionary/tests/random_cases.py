import argparse
import random
from pathlib import Path


def path_string(n, adj, labels, u, v):
    parent = {u: None}
    stack = [u]
    while stack:
        x = stack.pop()
        for y in adj[x]:
            if y not in parent:
                parent[y] = x
                stack.append(y)
    out = []
    x = v
    while x is not None:
        out.append(labels[x])
        x = parent[x]
    return "".join(reversed(out))


def count(text, p):
    return sum(text.startswith(p, i) for i in range(len(text)))


def make_case(rng):
    n = rng.randint(1, 12)
    alphabet = rng.choice(["a", "ab", "abc"])
    labels = [""] + [rng.choice(alphabet) for _ in range(n)]
    adj = [[] for _ in range(n + 1)]
    edges = []
    for v in range(2, n + 1):
        p = v - 1 if rng.random() < 0.4 else rng.randint(1, v - 1)
        adj[p].append(v)
        adj[v].append(p)
        edges.append((p, v) if rng.random() < 0.5 else (v, p))
    rng.shuffle(edges)
    q = rng.randint(1, 15)
    queries = []
    for _ in range(q):
        u, v = rng.randint(1, n), rng.randint(1, n)
        text = path_string(n, adj, labels, u, v)
        if rng.random() < 0.6 and text:
            i = rng.randrange(len(text))
            p = text[i:i + rng.randint(1, 5)]
        else:
            p = "".join(rng.choice(alphabet) for _ in range(rng.randint(1, 4)))
        queries.append((u, v, p, count(text, p)))
    lines = [f"{n} {q}", "".join(labels[1:])]
    lines += [f"{a} {b}" for a, b in edges]
    lines += [f"{u} {v} {p}" for u, v, p, _ in queries]
    return "\n".join(lines) + "\n", "".join(f"{c}\n" for *_, c in queries)


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
