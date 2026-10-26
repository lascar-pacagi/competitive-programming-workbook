"""Maximum-size workloads; expected answers follow from the construction."""
import argparse
from pathlib import Path


def write(folder, name, text, answer):
    (folder / (name + '.in')).write_text(text)
    (folder / (name + '.out')).write_text(answer)


def build(folder):
    n, m, capacity = 250, 4000, 10**9
    edges = [(v, v + 1, capacity) for v in range(1, n)]
    edges += [(1, 2, capacity)] * (m - len(edges))
    links = ''.join(f'{u} {v} {c}\n' for u, v, c in edges)
    limits = [capacity] * n
    write(folder, 'long_chain_parallel', f'{n} {m}\n' + ' '.join(map(str, limits)) + '\n' + links, str(capacity) + '\n')
    limits[n // 2] = 0
    write(folder, 'closed_relay', f'{n} {m}\n' + ' '.join(map(str, limits)) + '\n' + links, '0\n')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--out-dir', type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    build(args.out_dir)


if __name__ == '__main__':
    main()
