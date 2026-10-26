"""Small randomized cases with an independent exhaustive oracle."""
import argparse
import random
from pathlib import Path

def case(rng):
    n = rng.randint(1, 35)
    source = ''.join(rng.choice('abc') for _ in range(n))
    if rng.randrange(3):
        offset = rng.randrange(n)
        target = source[offset:] + source[:offset]
    else:
        target = ''.join(rng.choice('abc') for _ in range(n))
    answer = sum(source[k:] + source[:k] == target for k in range(n))
    return source + '\n' + target + '\n', str(answer) + '\n'


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
