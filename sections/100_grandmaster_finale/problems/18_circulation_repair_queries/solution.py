import sys
def main():
    it=iter(map(int,sys.stdin.buffer.read().split())); n=next(it);m=next(it);q=next(it); reach=[1<<i for i in range(n)]
    for _ in range(m):
        u=next(it)-1;v=next(it)-1;l=next(it);h=next(it);f=next(it)
        if f<h: reach[u]|=1<<v
        if f>l: reach[v]|=1<<u
    for k in range(n):
        bit=1<<k; add=reach[k]
        for i in range(n):
            if reach[i]&bit: reach[i]|=add
    out=[]
    for _ in range(q):
        u=next(it)-1;v=next(it)-1;out.append("YES" if reach[v]>>u&1 else "NO")
    print("\n".join(out))
if __name__=="__main__":main()
