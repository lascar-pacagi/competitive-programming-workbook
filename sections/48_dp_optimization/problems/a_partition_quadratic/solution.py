import sys
INF=10**30
def main():
    data=list(map(int,sys.stdin.buffer.read().split()))
    if not data: return
    n,k=data[0],data[1]; a=data[2:]; ps=[0]
    for x in a: ps.append(ps[-1]+x)
    def cost(l,r): return (ps[r]-ps[l])**2
    prev=[INF]*(n+1); prev[0]=0
    for _ in range(k):
        cur=[INF]*(n+1)
        def solve(lo,hi,optl,optr):
            if lo>hi: return
            mid=(lo+hi)//2; best=(INF,optl)
            for j in range(optl,min(optr,mid-1)+1):
                val=prev[j]+cost(j,mid)
                if val<best[0]: best=(val,j)
            cur[mid]=best[0]; solve(lo,mid-1,optl,best[1]); solve(mid+1,hi,best[1],optr)
        solve(1,n,0,n-1); prev=cur
    print(prev[n])
if __name__=="__main__": main()
