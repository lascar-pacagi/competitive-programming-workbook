"""Maximum-size cases with answers derived from their construction."""
import argparse
from pathlib import Path


def write(folder, name, text, answer):
    (folder / (name + '.in')).write_text(text)
    (folder / (name + '.out')).write_text(str(answer) + '\n')


def build(folder):
    n, g, c = 120, 200, 10**9
    for kind,name in [(1,'all_open'),(0,'all_closed')]:
        text = f'{n} {g}\n'+' '.join([str(c if kind else -c)]*n)+'\n'
        for k in range(g):
            members = [(k+j)%n+1 for j in range(15)]
            text += f'{kind} {c} 15 '+' '.join(map(str,members))+'\n'
        write(folder,name,text,(n+g)*c if kind else g*c)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--out-dir', type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    build(args.out_dir)


if __name__ == '__main__':
    main()
