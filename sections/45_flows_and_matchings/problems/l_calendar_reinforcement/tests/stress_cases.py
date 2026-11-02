"""Maximum-size cases with answers derived from their construction."""
import argparse
from pathlib import Path


def write(folder, name, text, answer):
    (folder / (name + '.in')).write_text(text)
    (folder / (name + '.out')).write_text(str(answer) + '\n')


def build(folder):
    n,p,t=80,80,10**9
    cal=''.join(f'{j*t//p} {(j+1)*t//p} 0\n' for j in range(p))
    jobs=f'0 {t} {t}\n'*n
    write(folder,'all_days_required',f'{n} {p}\n'+cal+jobs,n)
    cal=''.join(f'{j*t//p} {(j+1)*t//p} 1\n' for j in range(p))
    jobs=''.join(f'{i} {t-i} {t-2*i}\n' for i in range(n))
    write(folder,'many_calendar_boundaries',f'{n} {p}\n'+cal+jobs,n-1)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--out-dir', type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    build(args.out_dir)


if __name__ == '__main__':
    main()
