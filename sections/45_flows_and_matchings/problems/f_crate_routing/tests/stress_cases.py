"""Maximum-size cases with answers derived from their construction."""
import argparse
from pathlib import Path


def write(folder, name, text, answer):
    (folder / (name + '.in')).write_text(text)
    (folder / (name + '.out')).write_text(str(answer) + '\n')


def build(folder):
    n, c = 150, 10**9
    lanes = ''.join(f'{u} {v} {c}\n' for u in range(1, n + 1) for v in range(1, n + 1))
    stock = ' '.join([str(c)] * n) + '\n'
    head = f'{n} {n} {n*n}\n' + stock
    write(folder, 'large_total', head + stock + lanes, n*c)
    demand = ' '.join(['0'] * (n - 1) + [str(c)]) + '\n'
    write(folder, 'one_destination', head + demand + lanes, c)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--out-dir', type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    build(args.out_dir)


if __name__ == '__main__':
    main()
