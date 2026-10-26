"""Small randomized cases with an independent exhaustive oracle."""
import argparse
import random
from pathlib import Path

def case(rng):
    n = rng.randint(2, 5)
    limits = [rng.randint(0, 9) for _ in range(n)]
    choices = [(u, v) for u in range(n - 1) for v in range(1, n) if u != v]
    edges = [(*rng.choice(choices), rng.randint(0, 9)) for _ in range(rng.randint(0, 12))]
    split = [(2 * v, 2 * v + 1, limits[v]) for v in range(n)]
    split += [(2 * u + 1, 2 * v, c) for u, v, c in edges]
    # Enumerate every possible source side in the transformed tiny network.
    answer = min(sum(c for u, v, c in split if mask >> u & 1 and not mask >> v & 1)
                 for mask in range(1, 1 << (2 * n), 2)
                 if not mask >> (2 * n - 1) & 1)
    text = f'{n} {len(edges)}\n' + ' '.join(map(str, limits)) + '\n'
    text += ''.join(f'{u + 1} {v + 1} {c}\n' for u, v, c in edges)
    return text, str(answer) + '\n'


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
