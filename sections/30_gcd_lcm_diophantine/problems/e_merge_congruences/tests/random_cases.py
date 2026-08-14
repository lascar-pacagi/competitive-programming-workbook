from __future__ import annotations
import argparse
import math
import random
from pathlib import Path

def brute(r1, m1, r2, m2):
    for x in range(math.lcm(m1, m2)):
        if x % m1 == r1 and x % m2 == r2:
            return x
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
                        i % 1_000_000_000, 1_000_000_000)
                       for i in range(200_000)]
            answers = [query[0] for query in queries]
        else:
            queries = []
            answers = []
            for _ in range(rng.randint(1, 30)):
                m1 = rng.randint(1, 35)
                m2 = rng.randint(1, 35)
                query = (rng.randrange(m1), m1, rng.randrange(m2), m2)
                queries.append(query)
                answers.append(brute(*query))
        stem = args.out_dir / f"case{case_index:03d}"
        stem.with_suffix(".in").write_text(
            str(len(queries)) + "\n" +
            "".join(" ".join(map(str, query)) + "\n" for query in queries))
        stem.with_suffix(".out").write_text(
            "\n".join(map(str, answers)) + "\n")

if __name__ == "__main__":
    main()
