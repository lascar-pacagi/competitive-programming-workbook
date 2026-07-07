import sys
def main():
    data=list(map(int,sys.stdin.buffer.read().split()))
    if not data: return
    n,c=data[0],data[1]; x=data[2:]; dp=[0]*n
    for i in range(1,n):
        dp[i]=min(dp[j]+(x[i]-x[j])**2+c for j in range(i))
    print(dp[-1])
if __name__=="__main__": main()
