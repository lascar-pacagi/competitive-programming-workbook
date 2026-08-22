import argparse
import random
from pathlib import Path


def make_case(rng: random.Random) -> tuple[str, str]:
    n = rng.randint(1, 11)
    values = [rng.randint(-5, 5) for _ in range(n)]
    parent = [-1] + [rng.randrange(v) for v in range(1, n)]
    children = [[] for _ in range(n)]
    for v in range(1, n):
        children[parent[v]].append(v)

    low, high = min(values), max(values)
    width = high - low + 1
    dp = [[0] * width for _ in range(n)]
    for u in range(n - 1, -1, -1):
        for label in range(low, high + 1):
            cost = abs(label - values[u])
            for v in children[u]:
                cost += min(dp[v][child_label - low]
                            for child_label in range(label, high + 1))
            dp[u][label - low] = cost
    answer = min(dp[0])

    text = f"{n}\n" + " ".join(map(str, values)) + "\n"
    text += "".join(f"{parent[v] + 1} {v + 1}\n" for v in range(1, n))
    return text, f"{answer}\n"


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
