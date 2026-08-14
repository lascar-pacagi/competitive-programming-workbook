import sys
def main() -> None:
    data=list(map(int,sys.stdin.buffer.read().split()))
    if not data:return
    n,*cuts=data;dp=[-10**9]*(n+1);dp[0]=0
    for length in range(1,n+1):
        for cut in cuts:
            if cut<=length:dp[length]=max(dp[length],dp[length-cut]+1)
    print(dp[n] if dp[n]>=0 else -1)
if __name__=='__main__':main()
