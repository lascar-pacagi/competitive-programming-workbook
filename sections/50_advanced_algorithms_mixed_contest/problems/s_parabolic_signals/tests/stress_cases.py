"""Maximum-size workloads; expected answers follow from the construction."""
import argparse
from pathlib import Path


def write(folder, name, text, answer):
    (folder / (name + '.in')).write_text(text)
    (folder / (name + '.out')).write_text(answer)


def build(folder):
    n = q = 200000
    positions = [2 * i - n for i in range(n)]
    stations = ''.join(f'{p} 0\n' for p in positions)
    queries = ' '.join(map(str, reversed(positions))) + '\n'
    write(folder, 'many_envelope_winners', f'{n} {q}\n' + stations + queries, '0\n' * q)
    stations = '1000000 -1000000000000\n' * (n - 1) + '1000000 1000000000000\n'
    queries = '-1000000 1000000 ' * (q // 2) + '\n'
    write(folder, 'equal_slopes_large_negative', f'{n} {q}\n' + stations + queries,
          '-3000000000000\n1000000000000\n' * (q // 2))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--out-dir', type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    build(args.out_dir)


if __name__ == '__main__':
    main()
