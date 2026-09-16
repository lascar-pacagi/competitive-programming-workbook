import argparse
import itertools
import random
from pathlib import Path


def brute(n, projects, chosen, bounds, profits):
    options = []
    for worker in range(n):
        eligible = [-1]
        eligible.extend(
            project for project in range(projects)
            if (worker, project) in profits
        )
        options.append(eligible)
    best = None
    for assignment in itertools.product(*options):
        if sum(project >= 0 for project in assignment) != chosen:
            continue
        counts = [0] * projects
        value = 0
        for worker, project in enumerate(assignment):
            if project >= 0:
                counts[project] += 1
                value += profits[worker, project]
        if all(low <= count <= high
               for count, (low, high) in zip(counts, bounds)):
            best = value if best is None else max(best, value)
    return "IMPOSSIBLE" if best is None else str(best)


def make_case(rng):
    n = rng.randint(1, 7)
    projects = rng.randint(1, 3)
    chosen = rng.randint(0, n)
    bounds = []
    for _ in range(projects):
        high = rng.randint(0, n)
        low = rng.randint(0, high)
        bounds.append((low, high))
    profits = {}
    for worker in range(n):
        for project in range(projects):
            if rng.random() < 0.65:
                profits[worker, project] = rng.randint(0, 20)

    lines = [f"{n} {projects} {len(profits)} {chosen}"]
    lines.extend(f"{low} {high}" for low, high in bounds)
    lines.extend(
        f"{worker + 1} {project + 1} {profit}"
        for (worker, project), profit in profits.items()
    )
    expected = brute(n, projects, chosen, bounds, profits)
    return "\n".join(lines) + "\n", expected + "\n"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)
    for case_id in range(args.count):
        case, expected = make_case(rng)
        stem = f"case_{case_id:03d}"
        (args.out_dir / f"{stem}.in").write_text(case)
        (args.out_dir / f"{stem}.out").write_text(expected)


if __name__ == '__main__':
    main()
