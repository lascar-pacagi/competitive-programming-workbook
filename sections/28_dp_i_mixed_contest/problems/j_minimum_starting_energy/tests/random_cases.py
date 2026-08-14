import argparse
import random
from pathlib import Path


def oracle(grid):
    n, m = len(grid), len(grid[0])
    answer = None

    def search(row, column, total, minimum):
        nonlocal answer
        total += grid[row][column]
        minimum = min(minimum, total)
        if row == n - 1 and column == m - 1:
            required = max(0, -minimum)
            answer = required if answer is None else min(answer, required)
            return
        if row + 1 < n:
            search(row + 1, column, total, minimum)
        if column + 1 < m:
            search(row, column + 1, total, minimum)

    search(0, 0, 0, 0)
    return answer


def optimized(grid):
    n, m = len(grid), len(grid[0])
    infinity = 10**30
    need = [infinity] * m
    for row in range(n - 1, -1, -1):
        for column in range(m - 1, -1, -1):
            if row == n - 1 and column == m - 1:
                need[column] = max(0, -grid[row][column])
            else:
                after = infinity
                if row + 1 < n:
                    after = min(after, need[column])
                if column + 1 < m:
                    after = min(after, need[column + 1])
                need[column] = max(0, after - grid[row][column])
    return need[0]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)
    fixed = [[[5]], [[-5]], [[0]], [[-2, -3], [10, -20]],
             [[1, -100, 100], [-1, -1, -1]]]

    for case in range(args.count):
        if case < len(fixed):
            grid = fixed[case]
        elif case == len(fixed):
            grid = [[rng.randint(-10**9, 10**9) for _ in range(500)]
                    for _ in range(500)]
        else:
            n = rng.randint(1, 6)
            m = rng.randint(1, 6)
            grid = [[rng.randint(-20, 20) for _ in range(m)]
                    for _ in range(n)]
        answer = optimized(grid) if len(grid) + len(grid[0]) > 13 else oracle(grid)
        stem = args.out_dir / f"case{case:03d}"
        lines = [f"{len(grid)} {len(grid[0])}"]
        lines.extend(" ".join(map(str, row)) for row in grid)
        stem.with_suffix(".in").write_text("\n".join(lines) + "\n")
        stem.with_suffix(".out").write_text(f"{answer}\n")


if __name__ == "__main__":
    main()
