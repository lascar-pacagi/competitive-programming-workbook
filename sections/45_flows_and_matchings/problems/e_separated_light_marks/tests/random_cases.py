"""Small cases checked by an independent exhaustive oracle."""
import argparse
import itertools
import random
from collections import deque
from fractions import Fraction
from pathlib import Path

def expected(text):
    lines = text.split()
    h, w = map(int, lines[:2])
    grid = lines[2:]
    cells = [(i, j) for i in range(h) for j in range(w) if grid[i][j] == '.']
    bad = []
    for a, (i, j) in enumerate(cells):
        mask = 0
        for b, (x, y) in enumerate(cells):
            if a == b:
                continue
            if i == x and all(grid[i][z] == '.' for z in range(min(j, y), max(j, y) + 1)):
                mask |= 1 << b
            if j == y and all(grid[z][j] == '.' for z in range(min(i, x), max(i, x) + 1)):
                mask |= 1 << b
        bad.append(mask)
    best = 0
    for mask in range(1 << len(cells)):
        if mask.bit_count() <= best:
            continue
        if all(not (mask >> i & 1) or not (mask & bad[i]) for i in range(len(cells))):
            best = mask.bit_count()
    return str(best) + '\n'

def case(rng):
    h, w = rng.randint(1, 3), rng.randint(1, 4)
    grid = [''.join(rng.choice('.#.') for _ in range(w)) for _ in range(h)]
    return f'{h} {w}\n' + '\n'.join(grid) + '\n'

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--count', type=int, required=True)
    parser.add_argument('--seed', type=int, required=True)
    parser.add_argument('--out-dir', type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)
    for index in range(args.count):
        text = case(rng)
        stem = args.out_dir / f'random{index:03d}'
        stem.with_suffix('.in').write_text(text)
        stem.with_suffix('.out').write_text(expected(text))


if __name__ == '__main__':
    main()
