import argparse
import itertools
import random
from pathlib import Path


def make_case(rng: random.Random) -> tuple[str, str]:
    n = rng.randint(2, 5)
    m = rng.randint(1, 7)
    edges = []
    for _ in range(m):
        u, v = rng.sample(range(n), 2)
        lower = rng.randint(0, 2)
        upper = lower + rng.randint(0, 2)
        c = rng.randint(0, 6)
        d = rng.randint(0, 5)
        edges.append((u, v, lower, upper, c, d))
    best = None
    ranges = [range(lower, upper + 1) for _, _, lower, upper, _, _ in edges]
    for flow in itertools.product(*ranges):
        balance = [0] * n
        cost = 0
        for amount, (u, v, _, _, c, d) in zip(flow, edges):
            balance[u] -= amount
            balance[v] += amount
            cost += c * amount + d * amount * (amount - 1) // 2
        if all(value == 0 for value in balance):
            best = cost if best is None else min(best, cost)
    text = f"{n} {m}\n" + "".join(
        f"{u + 1} {v + 1} {lower} {upper} {c} {d}\n"
        for u, v, lower, upper, c, d in edges)
    return text, ("IMPOSSIBLE\n" if best is None else f"{best}\n")


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
