"""Maximum-size cases with answers derived from their construction."""
import argparse
from pathlib import Path


def write(folder, name, text, answer):
    (folder / (name + '.in')).write_text(text)
    (folder / (name + '.out')).write_text(str(answer) + '\n')


def build(folder):
    n = 60
    write(folder, 'open_floor', f'{n} {n}\n' + ('.' * n + '\n') * n, n)
    grid = [''.join('.' if (i + j) % 2 == 0 else '#' for j in range(n)) for i in range(n)]
    write(folder, 'isolated_marks', f'{n} {n}\n' + '\n'.join(grid) + '\n', n * n // 2)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--out-dir', type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    build(args.out_dir)


if __name__ == '__main__':
    main()
