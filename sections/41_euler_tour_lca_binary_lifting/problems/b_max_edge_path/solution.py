import sys
def main():
    data=list(map(int,sys.stdin.buffer.read().split()))
    if not data: return
    n,q=data[0],data[1]; idx=2; LOG=max(1,(n+1).bit_length())
    up=[[0]*(n+1) for _ in range(LOG)]; mx=[[0]*(n+1) for _ in range(LOG)]; depth=[0]*(n+1)
    for v in range(2,n+1):
        p,w=data[idx],data[idx+1]; idx+=2; up[0][v]=p; mx[0][v]=w; depth[v]=depth[p]+1
    for k in range(1,LOG):
        for v in range(1,n+1):
            mid=up[k-1][v]; up[k][v]=up[k-1][mid]; mx[k][v]=max(mx[k-1][v],mx[k-1][mid])
    def lift(v,d):
        ans=0; bit=0
        while d:
            if d&1: ans=max(ans,mx[bit][v]); v=up[bit][v]
            d//=2; bit+=1
        return v,ans
    out=[]
    for _ in range(q):
        a,b=data[idx],data[idx+1]; idx+=2; ans=0
        if depth[a]<depth[b]: a,b=b,a
        a,val=lift(a,depth[a]-depth[b]); ans=max(ans,val)
        if a!=b:
            for k in range(LOG-1,-1,-1):
                if up[k][a]!=up[k][b]:
                    ans=max(ans,mx[k][a],mx[k][b]); a=up[k][a]; b=up[k][b]
            ans=max(ans,mx[0][a],mx[0][b])
        out.append(str(ans))
    print("\n".join(out))
if __name__=="__main__": main()
