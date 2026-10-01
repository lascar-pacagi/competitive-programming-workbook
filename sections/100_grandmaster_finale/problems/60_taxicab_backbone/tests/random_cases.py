import argparse
import random
from pathlib import Path


def solve(points, queries):
    n = len(points)

    def dist(i, j):
        return abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])

    # Minimax distances by Floyd--Warshall on the bottleneck semiring.
    best = [[dist(i, j) for j in range(n)] for i in range(n)]
    for k in range(n):
        row_k = best[k]
        for i in range(n):
            row_i = best[i]
            via = row_i[k]
            for j in range(n):
                candidate = max(via, row_k[j])
                if candidate < row_i[j]:
                    row_i[j] = candidate
    return [best[a][b] for a, b in queries]


def make_case(rng):
    n = rng.randint(1, 12)
    span = rng.choice([2, 5, 30, 10**9])
    points = [(rng.randint(-span, span), rng.randint(-span, span)) for _ in range(n)]
    if rng.random() < 0.3:
        points = [(v, v * rng.choice([1, -1])) for v, _ in points]  # diagonal ties
    q = rng.randint(1, 15)
    queries = [(rng.randrange(n), rng.randrange(n)) for _ in range(q)]
    text = f"{n} {q}\n" + "".join(f"{a} {b}\n" for a, b in points)
    text += "".join(f"{a + 1} {b + 1}\n" for a, b in queries)
    return text, "\n".join(map(str, solve(points, queries))) + "\n"


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
