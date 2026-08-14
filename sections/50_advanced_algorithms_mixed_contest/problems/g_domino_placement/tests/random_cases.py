import argparse,random
from pathlib import Path
def brute(grid):
    n,m=len(grid),len(grid[0]);cells=[i for i in range(n*m) if grid[i//m][i%m]=="."];edges=[]
    for u in cells:
        r,c=divmod(u,m)
        for dr,dc in ((1,0),(0,1)):
            v=(r+dr)*m+c+dc
            if r+dr<n and c+dc<m and grid[r+dr][c+dc]==".":edges.append((u,v))
    best=0
    def rec(index,used,count):
        nonlocal best
        if index==len(edges):best=max(best,count);return
        rec(index+1,used,count);u,v=edges[index]
        if not(used>>u&1 or used>>v&1):rec(index+1,used|1<<u|1<<v,count+1)
    rec(0,0,0);return best
def main():
    p=argparse.ArgumentParser();p.add_argument("--count",type=int,required=True);p.add_argument("--seed",type=int,required=True);p.add_argument("--out-dir",type=Path,required=True);a=p.parse_args();a.out_dir.mkdir(parents=True,exist_ok=True);rng=random.Random(a.seed)
    for z in range(a.count):
        n,m=rng.randint(1,4),rng.randint(1,4);g=["".join("#" if rng.random()<.25 else "." for _ in range(m)) for _ in range(n)];stem=a.out_dir/f"case{z:03d}";stem.with_suffix(".in").write_text(f"{n} {m}\n"+"\n".join(g)+"\n");stem.with_suffix(".out").write_text(f"{brute(g)}\n")
if __name__=="__main__":main()
