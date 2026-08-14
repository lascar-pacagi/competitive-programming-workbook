import argparse
import itertools
import random
from pathlib import Path


def covers(values, target):
    possible = {0}
    for value in values:
        possible |= {total + value for total in list(possible)}
    return all(value in possible for value in range(1, target + 1))


def oracle(values, target):
    for count in range(target + 1):
        for patches in itertools.combinations_with_replacement(
                range(1, target + 1), count):
            if covers(values + list(patches), target):
                return count


def greedy(values, target):
    values = sorted(values)
    covered = index = patches = 0
    while covered < target:
        if index < len(values) and values[index] <= covered + 1:
            covered += values[index]
            index += 1
        else:
            covered += covered + 1
            patches += 1
    return patches


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)
    fixed = [([], 1), ([], 18), ([1, 2, 4, 8], 15),
             ([2, 2, 2], 10), ([1, 100], 50)]
    for case in range(args.count):
        if case < len(fixed):
            values, target = fixed[case]
        elif case == len(fixed):
            values = [rng.randint(1, 10**18) for _ in range(200000)]
            target = 10**18
        else:
            values = [rng.randint(1, 18)
                      for _ in range(rng.randint(0, 7))]
            target = rng.randint(1, 18)
        answer = greedy(values, target) if len(values) > 10 else oracle(
            values, target)
        stem = args.out_dir / f"case{case:03d}"
        stem.with_suffix(".in").write_text(
            f"{len(values)} {target}\n" + " ".join(map(str, values)) + "\n")
        stem.with_suffix(".out").write_text(f"{answer}\n")


if __name__ == "__main__":
    main()
