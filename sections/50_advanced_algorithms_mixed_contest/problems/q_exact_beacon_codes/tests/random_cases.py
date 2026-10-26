"""Small randomized cases with an independent exhaustive oracle."""
import argparse
import random
from pathlib import Path

def case(rng):
    n = rng.randint(1, 18)
    k = rng.randint(0, n)
    codes = [rng.randrange(16) for _ in range(n)]
    target = rng.randrange(32)
    answer = 0
    for mask in range(1 << n):
        if mask.bit_count() != k:
            continue
        code = 0
        for i, value in enumerate(codes):
            if mask >> i & 1:
                code ^= value
        answer += code == target
    return f'{n} {k} {target}\n' + ' '.join(map(str, codes)) + '\n', str(answer) + '\n'


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
