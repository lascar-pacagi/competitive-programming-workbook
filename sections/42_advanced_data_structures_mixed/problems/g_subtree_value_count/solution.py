import bisect,sys
def main():
    d=list(map(int,sys.stdin.buffer.read().split()))
    if not d:return
    n,q=d[:2];a=d[2:2+n];g=[[]for _ in range(n)];j=2+n
    for _ in range(n-1):u,v=d[j]-1,d[j+1]-1;j+=2;g[u].append(v);g[v].append(u)
    par=[-1]*n;order=[];stack=[0]
    while stack:
        u=stack.pop();order.append(u)
        for v in g[u]:
            if v!=par[u]:par[v]=u;stack.append(v)
    tin=[0]*n
    for i,u in enumerate(order):tin[u]=i
    size=[1]*n
    for u in reversed(order[1:]):size[par[u]]+=size[u]
    z=1
    while z<n:z*=2
    tree=[[]for _ in range(2*z)]
    for u in range(n):tree[z+tin[u]]=[a[u]]
    for i in range(z-1,0,-1):tree[i]=sorted(tree[2*i]+tree[2*i+1])
    out=[]
    for _ in range(q):
        u,lo,hi=d[j]-1,d[j+1],d[j+2];j+=3;l=z+tin[u];r=l+size[u];ans=0
        while l<r:
            if l&1:v=tree[l];ans+=bisect.bisect_right(v,hi)-bisect.bisect_left(v,lo);l+=1
            if r&1:r-=1;v=tree[r];ans+=bisect.bisect_right(v,hi)-bisect.bisect_left(v,lo)
            l//=2;r//=2
        out.append(str(ans))
    print('\n'.join(out))
if __name__=="__main__":main()
