import sys
def main():
    data=list(map(int,sys.stdin.buffer.read().split()))
    if not data: return
    n,q=data[0],data[1]; idx=2; LOG=max(1,(n+1).bit_length())
    up=[[0]*(n+1) for _ in range(LOG)]; depth=[0]*(n+1)
    for v in range(2,n+1):
        p=data[idx]; idx+=1; up[0][v]=p; depth[v]=depth[p]+1
    for k in range(1,LOG):
        for v in range(1,n+1): up[k][v]=up[k-1][up[k-1][v]]
    def lift(v,d):
        for k in range(LOG):
            if d>>k & 1: v=up[k][v]
        return v
    def lca(a,b):
        if depth[a]<depth[b]: a,b=b,a
        a=lift(a,depth[a]-depth[b])
        if a==b: return a
        for k in range(LOG-1,-1,-1):
            if up[k][a]!=up[k][b]: a=up[k][a]; b=up[k][b]
        return up[0][a]
    out=[]
    for _ in range(q):
        u,v,k=data[idx],data[idx+1],data[idx+2]; idx+=3; c=lca(u,v); left=depth[u]-depth[c]+1; total=depth[u]+depth[v]-2*depth[c]+1
        if k<1 or k>total: out.append("-1")
        elif k<=left: out.append(str(lift(u,k-1)))
        else: out.append(str(lift(v,total-k)))
    print("\n".join(out))
if __name__=="__main__": main()
