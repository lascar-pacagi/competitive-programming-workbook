import sys
def main():
    d=list(map(int,sys.stdin.buffer.read().split()));n,k=d[:2];v=d[2:];cost=[v[i*n:(i+1)*n]for i in range(n)];inf=10**30;prev=[inf]*(n+1);prev[0]=0
    for group in range(1,k+1):
        cur=[inf]*(n+1)
        def solve(lo,hi,optl,optr):
            if lo>hi:return
            mid=(lo+hi)//2;best=optl
            for j in range(optl,min(optr,mid-1)+1):
                value=prev[j]+cost[j][mid-1]
                if value<cur[mid]:cur[mid]=value;best=j
            solve(lo,mid-1,optl,best);solve(mid+1,hi,best,optr)
        solve(group,n,group-1,n-1);prev=cur
    print(prev[n])
if __name__=="__main__":main()
