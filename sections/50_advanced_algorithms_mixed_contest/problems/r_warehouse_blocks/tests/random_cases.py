"""Small randomized cases with an independent exhaustive oracle."""
import argparse
import random
from pathlib import Path

def case(rng):
    from itertools import combinations
    n = rng.randint(1, 11)
    k = rng.randint(1, n)
    positions = sorted(rng.randint(0, 30) for _ in range(n))
    answer = 10**9
    for cuts in combinations(range(1, n), k - 1):
        boundaries = (0,) + cuts + (n,)
        total = 0
        for left, right in zip(boundaries, boundaries[1:]):
            # Try every customer coordinate, without using the median formula.
            total += min(sum(abs(x - warehouse) for x in positions[left:right])
                         for warehouse in positions[left:right])
        answer = min(answer, total)
    return f'{n} {k}\n' + ' '.join(map(str, positions)) + '\n', str(answer) + '\n'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--count', type=int, required=True)
    parser.add_argument('--seed', type=int, required=True)
    parser.add_argument('--out-dir', type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)
    for index in range(args.count):
        text, answer = case(rng)
        stem = args.out_dir / f'random{index:03d}'
        stem.with_suffix('.in').write_text(text)
        stem.with_suffix('.out').write_text(answer)


if __name__ == '__main__':
    main()
