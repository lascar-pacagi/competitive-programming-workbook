"""Maximum-size workloads; expected answers follow from the construction."""
import argparse
from pathlib import Path


def write(folder, name, text, answer):
    (folder / (name + '.in')).write_text(text)
    (folder / (name + '.out')).write_text(answer)


def build(folder):
    n = 200000
    alarm = ' '.join(['1000000000'] * n)
    chain = ''.join(f'{v} {v + 1} 1000000000\n' for v in range(1, n))
    answer = ' '.join(str((1 + max(i, n - 1 - i)) * 10**9) for i in range(n)) + '\n'
    write(folder, 'deep_large_delays', f'{n}\n' + alarm + '\n' + chain, answer)
    star = ''.join(f'1 {v} 1\n' for v in range(2, n + 1))
    write(folder, 'equal_best_branches', f'{n}\n' + ' '.join(['0'] * n) + '\n' + star,
          '1 ' + ' '.join(['2'] * (n - 1)) + '\n')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--out-dir', type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    build(args.out_dir)


if __name__ == '__main__':
    main()
