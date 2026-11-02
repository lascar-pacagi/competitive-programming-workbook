"""Maximum-size cases with answers derived from their construction."""
import argparse
from pathlib import Path


def write(folder, name, text, answer):
    (folder / (name + '.in')).write_text(text)
    (folder / (name + '.out')).write_text(str(answer) + '\n')


def build(folder):
    n,e,c=100,2000,10**9
    pairs=[(i,i) for i in range(1,n+1)]
    used=set(pairs)
    for u in range(1,n+1):
        for v in range(1,n+1):
            if (u,v) not in used:
                pairs.append((u,v));used.add((u,v))
                if len(pairs)==e:break
        if len(pairs)==e:break
    bounds=f'{c} {c}\n'*(2*n)
    links=''.join(f'{u} {v} {c}\n' for u,v in pairs)
    write(folder,'fixed_large_quotas',f'{n} {n} {e} {n*c}\n'+bounds+links,'YES')
    # Every row/column could supply/receive c, but column n has no lane.
    pairs=[(i,i) for i in range(1,n)]+[(n,1)]
    used=set(pairs)
    for u in range(1,n+1):
        for v in range(1,n):
            if (u,v) not in used:
                pairs.append((u,v));used.add((u,v))
                if len(pairs)==e:break
        if len(pairs)==e:break
    bounds=f'0 {c}\n'*(2*n)
    links=''.join(f'{u} {v} {c}\n' for u,v in pairs)
    write(folder,'missing_destination',f'{n} {n} {e} {n*c}\n'+bounds+links,'NO')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--out-dir', type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    build(args.out_dir)


if __name__ == '__main__':
    main()
