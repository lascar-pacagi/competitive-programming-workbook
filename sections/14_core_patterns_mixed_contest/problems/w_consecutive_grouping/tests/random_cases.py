import argparse
import collections
import functools
import random
from pathlib import Path


def oracle(values):
    values = tuple(sorted(values))

    @functools.lru_cache(None)
    def search(index, groups):
        if index == len(values):
            return all(length >= 3 for _, length in groups)
        value = values[index]
        tried = set()
        for group, (last, length) in enumerate(groups):
            if last == value - 1 and (last, length) not in tried:
                tried.add((last, length))
                after = list(groups)
                after[group] = (value, min(3, length + 1))
                if search(index + 1, tuple(sorted(after))):
                    return True
        after = tuple(sorted(groups + ((value, 1),)))
        return search(index + 1, after)

    return search(0, tuple())


def greedy(values):
    remaining = collections.Counter(values)
    need = collections.Counter()
    for value in sorted(values):
        if remaining[value] == 0:
            continue
        if need[value] > 0:
            remaining[value] -= 1
            need[value] -= 1
            need[value + 1] += 1
        elif remaining[value + 1] > 0 and remaining[value + 2] > 0:
            remaining[value] -= 1
            remaining[value + 1] -= 1
            remaining[value + 2] -= 1
            need[value + 3] += 1
        else:
            return False
    return True


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)
    fixed = [[1, 2], [1, 2, 3], [1, 2, 3, 3, 4, 5],
             [1, 2, 3, 4, 4, 5], [-2, -1, 0, 0, 1, 2],
             [1, 2, 3, 4, 5, 5, 6, 7]]
    for case in range(args.count):
        if case < len(fixed):
            values = fixed[case]
        elif case == len(fixed):
            values = [rng.randint(-10**9, 10**9) for _ in range(200000)]
        else:
            values = [rng.randint(-4, 7)
                      for _ in range(rng.randint(1, 11))]
        answer = greedy(values) if len(values) > 14 else oracle(values)
        stem = args.out_dir / f"case{case:03d}"
        stem.with_suffix(".in").write_text(
            f"{len(values)}\n" + " ".join(map(str, values)) + "\n")
        stem.with_suffix(".out").write_text(
            "YES\n" if answer else "NO\n")


if __name__ == "__main__":
    main()
