import sys
def main():
 d=list(map(int,sys.stdin.buffer.read().split()));a=d[1:];n=len(a);dp=[0]*n
 for l in range(n-1,-1,-1):
  dp[l]=a[l]
  for r in range(l+1,n):dp[r]=max(a[l]-dp[r],a[r]-dp[r-1])
 print(dp[-1])
if __name__=='__main__':main()
