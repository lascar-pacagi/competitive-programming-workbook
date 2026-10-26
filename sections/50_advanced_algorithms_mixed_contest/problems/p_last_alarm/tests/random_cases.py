"""Small randomized cases with an independent exhaustive oracle."""
import argparse
import random
from pathlib import Path

def case(rng):
    n = rng.randint(1, 30)
    alarm = [rng.randint(0, 30) for _ in range(n)]
    edges = [(rng.randrange(v), v, rng.randint(1, 12)) for v in range(1, n)]
    adj = [[] for _ in range(n)]
    for u, v, d in edges:
        adj[u].append((v, d))
        adj[v].append((u, d))
    answers = []
    for root in range(n):
        stack = [(root, -1, 0)]
        latest = 0
        while stack:
            u, parent, distance = stack.pop()
            latest = max(latest, alarm[u] + distance)
            stack.extend((v, u, distance + d) for v, d in adj[u] if v != parent)
        answers.append(latest)
    text = str(n) + '\n' + ' '.join(map(str, alarm)) + '\n'
    text += ''.join(f'{u + 1} {v + 1} {d}\n' for u, v, d in edges)
    return text, ' '.join(map(str, answers)) + '\n'


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
