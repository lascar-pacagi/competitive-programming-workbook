"""Maximum-size cases with answers derived from their construction."""
import argparse
from pathlib import Path


def write(folder, name, text, answer):
    (folder / (name + '.in')).write_text(text)
    (folder / (name + '.out')).write_text(str(answer) + '\n')


def build(folder):
    n,m=60,200
    edges=[(u,v) for u in range(1,n+1) for v in range(1,m+1)]
    write(folder,'complete_reserve',f'{n} {m} {len(edges)}\n'+''.join(f'{u} {v}\n' for u,v in edges),m-n)
    edges=[(1,1)]+[(u,v) for u in range(2,n+1) for v in range(1,m+1)]
    write(folder,'one_fragile_visitor',f'{n} {m} {len(edges)}\n'+''.join(f'{u} {v}\n' for u,v in edges),0)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--out-dir', type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    build(args.out_dir)


if __name__ == '__main__':
    main()
