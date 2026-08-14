from __future__ import annotations
import argparse
import math
import random
from pathlib import Path

def brute(r1, m1, r2, m2, earliest):
    limit = earliest + math.lcm(m1, m2)
    for time in range(earliest, limit + 1):
        if time % m1 == r1 and time % m2 == r2:
            return time
    return -1

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)
    for case_index in range(args.count):
        if case_index == 0:
            queries = [(i % 1_000_000_000, 1_000_000_000,
                        i % 1_000_000_000, 1_000_000_000, 10**18 - i)
                       for i in range(200_000)]
            answers = []
            for r1, m1, _, _, earliest in queries:
                jumps = max(0, (earliest - r1 + m1 - 1) // m1)
                answers.append(r1 + jumps * m1)
        else:
            queries = []
            for _ in range(rng.randint(1, 30)):
                m1 = rng.randint(1, 30)
                m2 = rng.randint(1, 30)
                queries.append((rng.randrange(m1), m1, rng.randrange(m2),
                                m2, rng.randint(0, 250)))
            answers = [brute(*query) for query in queries]
        stem = args.out_dir / f"case{case_index:03d}"
        stem.with_suffix(".in").write_text(
            str(len(queries)) + "\n" +
            "".join(" ".join(map(str, query)) + "\n" for query in queries))
        stem.with_suffix(".out").write_text(
            "\n".join(map(str, answers)) + "\n")

if __name__ == "__main__":
    main()
