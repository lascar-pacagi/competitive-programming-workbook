import sys,collections
def main():
    data=list(map(int,sys.stdin.buffer.read().split()))
    if not data: return
    n,w=data[0],data[1]; a=data[2:]; dp=[0]*(n+1); dq=collections.deque([0])
    for i in range(1,n+1):
        while dq and dq[0]<i-w: dq.popleft()
        dp[i]=dp[dq[0]]+a[i-1]
        while dq and dp[dq[-1]]>=dp[i]: dq.pop()
        dq.append(i)
    print(dp[n])
if __name__=="__main__": main()
