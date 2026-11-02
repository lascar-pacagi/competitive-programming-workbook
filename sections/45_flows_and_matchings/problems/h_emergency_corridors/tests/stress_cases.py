"""Maximum-size cases with answers derived from their construction."""
import argparse
from pathlib import Path


def write(folder, name, text, answer):
    (folder / (name + '.in')).write_text(text)
    (folder / (name + '.out')).write_text(str(answer) + '\n')


def build(folder):
    n, m, c = 150, 2000, 10**9
    edges = [(v, v+1) for v in range(1, n)]
    used = set(edges)
    for u in range(1, n+1):
        for v in range(1, n+1):
            if u == v or (u,v) in used:
                continue
            if (u <= 75 and v <= 75) or (u >= 75 and v >= 75):
                edges.append((u,v)); used.add((u,v))
                if len(edges) == m:
                    break
        if len(edges) == m:
            break
    costs = [-1] + [c]*(n-2) + [-1]
    head = f'{n} {m} 1 1\n' + ' '.join(map(str,costs)) + f'\n1\n{n}\n'
    write(folder, 'shared_room', head + ''.join(f'{u} {v}\n' for u,v in edges), c)
    edges[-1] = (1,n)
    write(folder, 'protected_route', head + ''.join(f'{u} {v}\n' for u,v in edges), -1)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--out-dir', type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    build(args.out_dir)


if __name__ == '__main__':
    main()
