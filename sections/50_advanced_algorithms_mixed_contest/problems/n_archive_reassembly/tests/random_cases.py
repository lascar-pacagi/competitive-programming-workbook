"""Small randomized cases with an independent exhaustive oracle."""
import argparse
import random
from pathlib import Path

def case(rng):
    source = ''.join(rng.choice('abc') for _ in range(rng.randint(1, 12)))
    target = ''.join(rng.choice('abc' if rng.randrange(4) else 'abcd')
                     for _ in range(rng.randint(1, 18)))
    pieces = {source[l:r] for l in range(len(source))
              for r in range(l + 1, len(source) + 1)}
    dp = [0] + [1000] * len(target)
    for end in range(1, len(target) + 1):
        for start in range(end):
            if target[start:end] in pieces:
                dp[end] = min(dp[end], dp[start] + 1)
    answer = dp[-1] if dp[-1] < 1000 else -1
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
