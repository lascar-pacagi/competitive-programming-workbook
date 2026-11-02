"""Maximum-size cases with answers derived from their construction."""
import argparse
from pathlib import Path


def write(folder, name, text, answer):
    (folder / (name + '.in')).write_text(text)
    (folder / (name + '.out')).write_text(str(answer) + '\n')


def build(folder):
    n, m, c = 250, 3000, 10**9
    edges = [(u,u+1) for u in range(1,n)] + [(u+1,u) for u in range(1,n)]
    used = set(edges)
    for u in range(1,n+1):
        for v in range(1,n+1):
            if u != v and (u,v) not in used:
                edges.append((u,v));used.add((u,v))
                if len(edges)==m:break
        if len(edges)==m:break
    links = ''.join(f'{u} {v} {c}\n' for u,v in edges)
    write(folder,'uniform_mode',f'{n} {m}\n'+f'0 {c}\n'*n+links,0)
    unary = ''.join('0 1\n' if i < n//2 else '1 0\n' for i in range(n))
    write(folder,'expensive_boundary',f'{n} {m}\n'+unary+links,n//2)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--out-dir', type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    build(args.out_dir)


if __name__ == '__main__':
    main()
