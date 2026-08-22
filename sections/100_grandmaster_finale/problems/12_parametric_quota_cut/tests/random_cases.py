import argparse
import random
from pathlib import Path


def make_case(rng: random.Random) -> tuple[str, str]:
    while True:
        n = rng.randint(1, 10)
        profits = [rng.randint(-10, 14) for _ in range(n)]
        dependencies = []
        for u in range(n):
            for v in range(n):
                if u != v and rng.random() < 0.08:
                    dependencies.append((u, v))
        closed = []
        for mask in range(1 << n):
            if all(not (mask >> u & 1) or (mask >> v & 1)
                   for u, v in dependencies):
                profit = sum(profits[i] for i in range(n) if mask >> i & 1)
                closed.append((mask.bit_count(), profit))
        candidates = []
        for penalty in range(-16, 17):
            best_value = max(profit - penalty * size for size, profit in closed)
            winners = [(size, profit) for size, profit in closed
                       if profit - penalty * size == best_value]
            sizes = {size for size, _ in winners}
            if len(sizes) == 1:
                size = next(iter(sizes))
                exact_best = max(profit for candidate_size, profit in closed
                                 if candidate_size == size)
                candidates.append((size, exact_best))
        if candidates:
            k, answer = rng.choice(candidates)
            break
    text = f"{n} {len(dependencies)} {k}\n"
    text += " ".join(map(str, profits)) + "\n"
    text += "".join(f"{u + 1} {v + 1}\n" for u, v in dependencies)
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
