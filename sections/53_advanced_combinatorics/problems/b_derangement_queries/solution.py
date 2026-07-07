import sys
MOD=1_000_000_007
def main():
    data=list(map(int,sys.stdin.buffer.read().split()))
    if not data: return
    qs=data[1:1+data[0]]; N=max(qs+[1]); d=[0]*(N+1); d[0]=1
    if N>=1: d[1]=0
    for i in range(2,N+1): d[i]=(i-1)*(d[i-1]+d[i-2])%MOD
    print("\n".join(str(d[n]) for n in qs))
if __name__=="__main__": main()
