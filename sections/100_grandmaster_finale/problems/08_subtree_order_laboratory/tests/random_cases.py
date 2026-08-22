import argparse
import random
from pathlib import Path


def make_case(rng: random.Random) -> tuple[str, str]:
    n = rng.randint(1, 45)
    q = rng.randint(1, 90)
    initial = [rng.randint(-25, 25) for _ in range(n)]
    values = initial.copy()
    children = [[] for _ in range(n)]
    edges = []
    for v in range(1, n):
        parent = rng.randrange(v)
        children[parent].append(v)
        edges.append((parent, v))
    subtree = [[] for _ in range(n)]

    def collect(u):
        result = [u]
        for v in children[u]:
            result += collect(v)
        subtree[u] = result
        return result

    collect(0)
    operations = []
    answers = []
    for _ in range(q):
        if rng.random() < 0.48:
            v = rng.randrange(n)
            x = rng.randint(-30, 30)
            values[v] = x
            operations.append(f"U {v + 1} {x}")
        else:
            v = rng.randrange(n)
            k = rng.randint(1, len(subtree[v]))
            answer = sorted(values[x] for x in subtree[v])[k - 1]
            answers.append(answer)
            operations.append(f"K {v + 1} {k}")
    text = f"{n} {q}\n" + " ".join(map(str, initial)) + "\n"
    text += "".join(f"{u + 1} {v + 1}\n" for u, v in edges)
    text += "\n".join(operations) + "\n"
    return text, "\n".join(map(str, answers)) + ("\n" if answers else "")


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
