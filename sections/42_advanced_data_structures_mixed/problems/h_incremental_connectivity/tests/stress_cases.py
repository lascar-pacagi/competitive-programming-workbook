"""Full-limit DSU cases; expected answers follow directly from graph construction."""
from __future__ import annotations
import argparse
from pathlib import Path


def generate(out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    n = q = 200_000
    # Each query follows one more edge in a growing path. Repeated BFS/DFS
    # performs quadratic total work although the correct DSU is near-linear.
    with (out_dir / 'growing_path.in').open('w') as inp, (out_dir / 'growing_path.out').open('w') as out:
        inp.write(f'{n} {q}\n')
        for v in range(2, 100_002):
            inp.write(f'A {v-1} {v}\nQ 1 {v}\n'); out.write('YES\n')
    # Union(parent(u), parent(v)) without balancing can make vertex 1 the
    # bottom of a long parent chain. Repeated queries also expose missing
    # compression. Queries to isolated vertices must still answer NO.
    with (out_dir / 'reverse_unions.in').open('w') as inp, (out_dir / 'reverse_unions.out').open('w') as out:
        inp.write(f'{n} {q}\n')
        for v in range(2, 100_002): inp.write(f'A {v} {v-1}\n')
        for i in range(100_000):
            if i % 2: inp.write('Q 1 200000\n'); out.write('NO\n')
            else: inp.write('Q 1 100001\n'); out.write('YES\n')
    # Failed searches must explore an entire large component; endpoints in
    # different components never acquire a connecting edge.
    with (out_dir / 'disconnected_paths.in').open('w') as inp, (out_dir / 'disconnected_paths.out').open('w') as out:
        inp.write(f'{n} {q}\n')
        for start in (1, 50_001):
            for v in range(start+1, start+50_000): inp.write(f'A {v-1} {v}\n')
        for i in range(100_002):
            if i % 3 == 0: inp.write('Q 1 50001\n'); out.write('NO\n')
            elif i % 3 == 1: inp.write('Q 1 50000\n'); out.write('YES\n')
            else: inp.write('Q 200000 200000\n'); out.write('YES\n')


def main() -> None:
    parser=argparse.ArgumentParser();parser.add_argument('--out-dir',type=Path,required=True)
    args=parser.parse_args();generate(args.out_dir)


if __name__ == '__main__': main()
