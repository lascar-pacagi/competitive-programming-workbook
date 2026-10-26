"""Full-limit cases with construction oracles independent of rolling hashes."""
from pathlib import Path
import argparse


def write_case(folder, name, text, queries, answers):
    (folder / f'{name}.in').write_text(
        text + '\n' + str(len(queries)) + '\n'
        + '\n'.join(f'{l} {r}' for l, r in queries) + '\n'
    )
    (folder / f'{name}.out').write_text('\n'.join(answers) + '\n')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--out-dir', type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    n = q = 200000
    queries = [(1 + i % 20000, n - i % 20000) for i in range(q)]
    write_case(args.out_dir, 'all_equal_long_ranges', 'a' * n,
               queries, ['YES'] * q)

    center = 100000  # 1-based position of the only b.
    text = 'a' * (center - 1) + 'b' + 'a' * (n - center)
    queries = []
    answers = []
    for i in range(q):
        margin = (i // 4) % 20000
        choices = [
            (1 + margin, 199999 - margin),
            (2 + margin, 199999 - margin),
            (1 + margin, 200000 - margin),
            (200000 - margin, 200000),
        ]
        l, r = choices[i % 4]
        queries.append((l, r))
        # If b is present, it must be the exact center of a palindrome.
        palindrome = not (l <= center <= r) or l + r == 2 * center
        answers.append('YES' if palindrome else 'NO')
    write_case(args.out_dir, 'single_exception_mixed_ranges', text,
               queries, answers)


if __name__ == '__main__':
    main()
