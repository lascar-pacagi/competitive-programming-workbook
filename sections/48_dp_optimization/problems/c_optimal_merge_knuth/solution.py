import sys
def main():
    data=list(map(int,sys.stdin.buffer.read().split()))
    if not data: return
    n=data[0]; a=data[1:]; ps=[0]
    for x in a: ps.append(ps[-1]+x)
    dp=[[0]*n for _ in range(n)]; opt=[[0]*n for _ in range(n)]
    for i in range(n): opt[i][i]=i
    for length in range(2,n+1):
        for l in range(n-length+1):
            r=l+length-1; best=10**30; bestk=l
            for k in range(opt[l][r-1], opt[l+1][r]+1):
                val=dp[l][k]+(dp[k+1][r] if k+1<=r else 0)+ps[r+1]-ps[l]
                if val<best: best=val; bestk=k
            dp[l][r]=best; opt[l][r]=bestk
    print(dp[0][n-1] if n else 0)
if __name__=="__main__": main()
