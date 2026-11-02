"""Maximum-size cases with answers derived from their construction."""
import argparse
from pathlib import Path


def write(folder, name, text, answer):
    (folder / (name + '.in')).write_text(text)
    (folder / (name + '.out')).write_text(str(answer) + '\n')


def build(folder):
    n = 250
    text = f'{n} {n} {n*n}\n'
    text += ''.join(f'{u+1} {v+1} {u*(n+1)+v}\n' for u in range(n) for v in range(n))
    write(folder, 'distinct_thresholds', text, n*n-1)
    text = f'{n} {n} {n*n}\n'
    text += ''.join(f'{u+1} {v+1} {0 if u == v else 10**9}\n' for u in range(n) for v in range(n))
    write(folder, 'zero_diagonal', text, 0)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--out-dir', type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    build(args.out_dir)


if __name__ == '__main__':
    main()
