import sys
sys.setrecursionlimit(1_000_000)
def main():
    data=list(map(int,sys.stdin.buffer.read().split()))
    if not data: return
    n=data[0]; g=[[] for _ in range(n)]; idx=1
    for _ in range(n-1):
        a,b=data[idx]-1,data[idx+1]-1; idx+=2; g[a].append(b); g[b].append(a)
    parent=[-1]*n; order=[0]
    for u in order:
        for v in g[u]:
            if v!=parent[u]: parent[v]=u; order.append(v)
    sub=[1]*n
    for u in reversed(order[1:]): sub[parent[u]]+=sub[u]
    total=n*(n-1)//2; out=[]
    for u in range(n):
        bad=0
        for v in g[u]:
            s=sub[v] if parent[v]==u else n-sub[u]
            bad+=s*(s-1)//2
        out.append(str(total-bad))
    print(" ".join(out))
if __name__=="__main__": main()
