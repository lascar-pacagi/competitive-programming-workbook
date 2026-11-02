"""Maximum-size cases with answers derived from their construction."""
import argparse
from pathlib import Path


def write(folder, name, text, answer):
    (folder / (name + '.in')).write_text(text)
    (folder / (name + '.out')).write_text(str(answer) + '\n')


def build(folder):
    n,c=60,10**6
    pairs=sorted({tuple(sorted((u,(u+d)%n))) for u in range(n) for d in range(1,6)})
    assert len(pairs)==300
    text=f'{n} {len(pairs)}\n'+' '.join(['20']*n)+'\n'
    text+=''.join(f'{u+1} {v+1} {c}\n' for u,v in pairs)
    # Every vertex has degree 10: no subset has density above 10*c/(2*20).
    write(folder,'regular_large_rewards',text,'250000 1')
    pairs=[(0,1)]
    for u in range(2,n):
        for v in range(u+1,n):
            pairs.append((u,v))
            if len(pairs)==300:break
        if len(pairs)==300:break
    text=f'{n} {len(pairs)}\n'+' '.join(['1','1']+['20']*(n-2))+'\n'
    text+=''.join(f'{u+1} {v+1} {c if u==0 else 1}\n' for u,v in pairs)
    write(folder,'small_profitable_component',text,'500000 1')

    # Two isolated 30-cycles have close but different ratios. Every proper
    # subset has ratio below 1000; the full first cycle is slightly better.
    costs = [19] + [20] * 59
    edges = []
    for offset, total in [(0, 599001), (30, 600001)]:
        for i in range(30):
            u, v = sorted((offset + i, offset + (i + 1) % 30))
            edges.append((u, v, total // 30 + (i < total % 30)))
    used = {(u, v) for u, v, w in edges}
    for u in range(n):
        for v in range(u + 1, n):
            if (u, v) not in used:
                edges.append((u, v, 0))
                if len(edges) == 300:
                    break
        if len(edges) == 300:
            break
    text = f'{n} {len(edges)}\n' + ' '.join(map(str, costs)) + '\n'
    text += ''.join(f'{u+1} {v+1} {w}\n' for u, v, w in edges)
    write(folder, 'close_exact_ratios', text, '599001 599')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--out-dir', type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    build(args.out_dir)


if __name__ == '__main__':
    main()
