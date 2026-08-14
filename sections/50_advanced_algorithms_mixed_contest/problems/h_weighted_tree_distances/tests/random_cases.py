import argparse,random
from collections import deque
from pathlib import Path
def main():
    p=argparse.ArgumentParser();p.add_argument("--count",type=int,required=True);p.add_argument("--seed",type=int,required=True);p.add_argument("--out-dir",type=Path,required=True);a=p.parse_args();a.out_dir.mkdir(parents=True,exist_ok=True);rng=random.Random(a.seed)
    for z in range(a.count):
        n=rng.randint(1,20);w=[rng.randint(0,10)for _ in range(n)];edges=[(i,rng.randrange(i))for i in range(1,n)];g=[[]for _ in range(n)]
        for u,v in edges:g[u].append(v);g[v].append(u)
        out=[]
        for s in range(n):
            dist=[-1]*n;dist[s]=0;q=deque([s])
            while q:
                u=q.popleft()
                for v in g[u]:
                    if dist[v]<0:dist[v]=dist[u]+1;q.append(v)
            out.append(str(sum(x*y for x,y in zip(w,dist))))
        lines=[str(n)," ".join(map(str,w))]+[f"{u+1} {v+1}"for u,v in edges];stem=a.out_dir/f"case{z:03d}";stem.with_suffix(".in").write_text("\n".join(lines)+"\n");stem.with_suffix(".out").write_text(" ".join(out)+"\n")
if __name__=="__main__":main()
