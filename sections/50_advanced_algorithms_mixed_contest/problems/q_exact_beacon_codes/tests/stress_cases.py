"""Maximum-size workloads; expected answers follow from the construction."""
import argparse
from pathlib import Path


def write(folder, name, text, answer):
    (folder / (name + '.in')).write_text(text)
    (folder / (name + '.out')).write_text(answer)


def build(folder):
    from math import comb
    write(folder, 'equal_codes_many_subsets', '40 20 0\n' + ' '.join(['0'] * 40) + '\n', str(comb(40, 20)) + '\n')
    values = [1 << i for i in range(20)] * 2
    write(folder, 'paired_independent_bits', '40 20 0\n' + ' '.join(map(str, values)) + '\n', str(comb(20, 10)) + '\n')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--out-dir', type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    build(args.out_dir)


if __name__ == '__main__':
    main()
