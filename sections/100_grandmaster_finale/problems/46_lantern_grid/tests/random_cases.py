import argparse
import random
from pathlib import Path

MOD = 1_000_000_007


def gaussian(n, m, grid):
    """Independent oracle: eliminate the full nm x nm system over GF(2)."""
    N = n * m
    rows = []
    for r in range(n):
        for c in range(m):
            eq = 0
            for dr, dc in ((0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)):
                rr, cc = r + dr, c + dc
                if 0 <= rr < n and 0 <= cc < m:
                    eq |= 1 << (rr * m + cc)
            if grid[r][c] == "1":
                eq |= 1 << N
            rows.append(eq)
    rank = 0
    for bit in range(N):
        piv = next((i for i in range(rank, N) if rows[i] >> bit & 1), -1)
        if piv < 0:
            continue
        rows[rank], rows[piv] = rows[piv], rows[rank]
        for i in range(N):
            if i != rank and rows[i] >> bit & 1:
                rows[i] ^= rows[rank]
        rank += 1
    if any(rows[i] == 1 << N for i in range(rank, N)):
        return 0
    return pow(2, N - rank, MOD)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, default=25)
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)
    for i in range(args.count):
        n, m = rng.randint(1, 12), rng.randint(1, 12)
        density = rng.choice([0.0, 0.5, 1.0, rng.random()])
        grid = ["".join("1" if rng.random() < density else "0" for _ in range(m)) for _ in range(n)]
        stem = args.out_dir / f"case{i:03d}"
        stem.with_suffix(".in").write_text(f"{n} {m}\n" + "\n".join(grid) + "\n")
        stem.with_suffix(".out").write_text(f"{gaussian(n, m, grid)}\n")


if __name__ == "__main__":
    main()
