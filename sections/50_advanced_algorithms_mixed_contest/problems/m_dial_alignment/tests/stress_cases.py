"""Maximum-size workloads; expected answers follow from the construction."""
import argparse
from pathlib import Path


def write(folder, name, text, answer):
    (folder / (name + '.in')).write_text(text)
    (folder / (name + '.out')).write_text(answer)


def build(folder):
    n = 200000
    write(folder, 'all_offsets', 'a' * n + '\n' + 'a' * n + '\n', str(n) + '\n')
    source = 'a' * (n - 1) + 'b'
    write(folder, 'late_mismatch', source + '\n' + source + '\n', '1\n')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--out-dir', type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    build(args.out_dir)


if __name__ == '__main__':
    main()
