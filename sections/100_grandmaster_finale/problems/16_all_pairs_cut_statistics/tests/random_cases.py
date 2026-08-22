import argparse
import random
from pathlib import Path


def make_case(rng: random.Random) -> tuple[str, str]:
    n = rng.randint(1, 8)
    possible = [(u, v) for u in range(n) for v in range(u + 1, n)]
    m = 0 if not possible else rng.randint(0, min(15, len(possible) + 4))
    edges = []
    for _ in range(m):
        u, v = rng.choice(possible)
        edges.append((u, v, rng.randint(1, 12)))
    q = rng.randint(1, 12)
    queries = [rng.randint(0, 30) for _ in range(q)]

    pair_cuts = []
    for s in range(n):
        for t in range(s + 1, n):
            best = None
            for mask in range(1 << n):
                if not (mask >> s & 1) or (mask >> t & 1):
                    continue
                capacity = sum(c for u, v, c in edges
                               if ((mask >> u) & 1) != ((mask >> v) & 1))
                best = capacity if best is None else min(best, capacity)
            pair_cuts.append(best)
    answers = [sum(value >= threshold for value in pair_cuts)
               for threshold in queries]
    text = f"{n} {m} {q}\n"
    text += "".join(f"{u + 1} {v + 1} {capacity}\n"
                    for u, v, capacity in edges)
    text += "".join(f"{threshold}\n" for threshold in queries)
    return text, "".join(f"{answer}\n" for answer in answers)


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
