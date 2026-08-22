import argparse
import random
from pathlib import Path


def make_case(rng: random.Random) -> tuple[str, str]:
    n = rng.randint(1, 35)
    m = 0 if n == 1 else rng.randint(0, min(90, n * (n - 1) // 2 + 8))
    q = rng.randint(1, 70)
    values = [rng.randint(-25, 25) for _ in range(n)]
    edges = []
    for _ in range(m):
        u, v = rng.sample(range(n), 2)
        edges.append((u, v, rng.randint(-10, 20)))
    queries = []
    answers = []
    thresholds = [weight for _, _, weight in edges] + [rng.randint(-12, 22)]
    for _ in range(q):
        vertex = rng.randrange(n)
        threshold = rng.choice(thresholds)
        parent = list(range(n))

        def find(x):
            while parent[x] != x:
                x = parent[x]
            return x

        for u, v, weight in edges:
            if weight <= threshold:
                a, b = find(u), find(v)
                parent[a] = b
        component = [i for i in range(n) if find(i) == find(vertex)]
        k = rng.randint(1, len(component))
        answers.append(sorted(values[i] for i in component)[k - 1])
        queries.append((vertex, threshold, k))
    text = f"{n} {m} {q}\n" + " ".join(map(str, values)) + "\n"
    text += "".join(f"{u + 1} {v + 1} {w}\n" for u, v, w in edges)
    text += "".join(f"{v + 1} {threshold} {k}\n"
                    for v, threshold, k in queries)
    return text, "\n".join(map(str, answers)) + "\n"


def main() -> None:
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
