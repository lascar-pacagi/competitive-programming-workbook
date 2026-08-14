import sys
def main():
    data=list(map(int,sys.stdin.buffer.read().split()))
    n=data[0];d=data[1:]
    dp=[[0]*n for _ in range(n)]
    for length in range(2,n+1):
        for l in range(n-length+1):
            r=l+length-1
            dp[l][r]=min(dp[l][k]+dp[k+1][r]+d[l]*d[k+1]*d[r+1] for k in range(l,r))
    print(dp[0][n-1])
if __name__=="__main__":main()
