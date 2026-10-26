"""Small randomized cases with an independent exact slicing oracle."""
from pathlib import Path
import argparse
import random


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--count', type=int, required=True)
    parser.add_argument('--seed', type=int, required=True)
    parser.add_argument('--out-dir', type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)
    for i in range(args.count):
        n = rng.randint(1, 90)
        mode = i % 4
        if mode == 0:
            text = rng.choice('abc') * n
        elif mode == 1:
            half = ''.join(rng.choices('abc', k=n // 2))
            text = half + (rng.choice('abc') if n % 2 else '') + half[::-1]
        else:
            text = ''.join(rng.choices('abcd', k=n))
        queries = [(1, n), (1, 1), (n, n)]
        for _ in range(rng.randint(1, 80)):
            l = rng.randint(1, n)
            r = rng.randint(l, n)
            queries.append((l, r))
        lines = [text, str(len(queries))] + [f'{l} {r}' for l, r in queries]
        expected = []
        for l, r in queries:
            part = text[l - 1:r]
            expected.append('YES' if part == part[::-1] else 'NO')
        stem = args.out_dir / f'case{i:03d}'
        stem.with_suffix('.in').write_text('\n'.join(lines) + '\n')
        stem.with_suffix('.out').write_text('\n'.join(expected) + '\n')


if __name__ == '__main__':
    main()
