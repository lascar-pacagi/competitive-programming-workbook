import argparse
import math
import random
from pathlib import Path


def solve_query(r1, m1, r2, m2):
    g = math.gcd(m1, m2)
    if (r2 - r1) % g:
        return -1
    reduced = m2 // g
    multiplier = (r2 - r1) // g * pow(m1 // g, -1, reduced)
    return (r1 + m1 * (multiplier % reduced)) % (m1 // g * m2)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)

    fixed = [
        [(0, 1, 0, 1), (0, 2, 1, 4), (3, 4, 5, 6)],
        [(999999999, 10**9, 999999998, 999999999)],
    ]
    for case in range(args.count):
        if case < len(fixed):
            rows = fixed[case]
        else:
            q = rng.randint(1, 30)
            rows = []
            for _ in range(q):
                m1 = rng.randint(1, 10**9)
                m2 = rng.randint(1, 10**9)
                rows.append((rng.randrange(m1), m1, rng.randrange(m2), m2))
        lines = [str(len(rows))]
        lines.extend(" ".join(map(str, row)) for row in rows)
        answers = [str(solve_query(*row)) for row in rows]
        stem = args.out_dir / f"case{case:03d}"
        stem.with_suffix(".in").write_text("\n".join(lines) + "\n")
        stem.with_suffix(".out").write_text("\n".join(answers) + "\n")


if __name__ == "__main__":
    main()
