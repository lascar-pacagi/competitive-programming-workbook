"""Maximum-size workloads; expected answers follow from the construction."""
import argparse
from pathlib import Path


def write(folder, name, text, answer):
    (folder / (name + '.in')).write_text(text)
    (folder / (name + '.out')).write_text(answer)


def build(folder):
    n, k, gap = 30000, 30, 30000
    positions = [i * gap for i in range(n)]
    size = n // k
    answer = k * (size * size // 4) * gap
    write(folder, 'equally_spaced', f'{n} {k}\n' + ' '.join(map(str, positions)) + '\n', str(answer) + '\n')
    write(folder, 'all_optima_tie', f'{n} {k}\n' + ' '.join(['1000000000'] * n) + '\n', '0\n')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--out-dir', type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    build(args.out_dir)


if __name__ == '__main__':
    main()
