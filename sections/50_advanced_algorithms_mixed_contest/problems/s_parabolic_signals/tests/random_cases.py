"""Small randomized cases with an independent exhaustive oracle."""
import argparse
import random
from pathlib import Path

def case(rng):
    n, q = rng.randint(1, 35), rng.randint(1, 35)
    stations = [(rng.randint(-30, 30), rng.randint(-200, 200)) for _ in range(n)]
    queries = [rng.randint(-40, 40) for _ in range(q)]
    answers = [max(power - (x - position)**2 for position, power in stations)
               for x in queries]
    text = f'{n} {q}\n' + ''.join(f'{p} {b}\n' for p, b in stations)
    text += ' '.join(map(str, queries)) + '\n'
    return text, '\n'.join(map(str, answers)) + '\n'


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
