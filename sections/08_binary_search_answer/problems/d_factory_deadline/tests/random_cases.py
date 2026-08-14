from __future__ import annotations
import argparse, random
from pathlib import Path

def brute(times: list[int], goal: int) -> int:
    minute = 0
    while sum(minute // value for value in times) < goal:
        minute += 1
    return minute

def main() -> None:
    p=argparse.ArgumentParser(); p.add_argument('--count',type=int,required=True); p.add_argument('--seed',type=int,required=True); p.add_argument('--out-dir',type=Path,required=True); a=p.parse_args(); a.out_dir.mkdir(parents=True,exist_ok=True); rng=random.Random(a.seed)
    for case in range(a.count):
        if case == 0:
            n, goal, times = 200_000, 10**9, [1] * 200_000
            inp=f"1\n{n} {goal}\n"+" ".join(map(str,times))+"\n"; out=f"{(goal+n-1)//n}\n"
        else:
            t=rng.randint(1,8); lines=[str(t)]; ans=[]
            for _ in range(t):
                n=rng.randint(1,7); goal=rng.randint(1,100); times=[rng.randint(1,15) for _ in range(n)]
                lines.extend((f"{n} {goal}"," ".join(map(str,times)))); ans.append(str(brute(times,goal)))
            inp="\n".join(lines)+"\n"; out="\n".join(ans)+"\n"
        stem=a.out_dir/f"case_{case:03d}"; stem.with_suffix('.in').write_text(inp); stem.with_suffix('.out').write_text(out)
if __name__=='__main__': main()
