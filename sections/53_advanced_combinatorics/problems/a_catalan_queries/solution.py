import sys
MOD=1_000_000_007
def main():
    data=list(map(int,sys.stdin.buffer.read().split()))
    if not data: return
    qs=data[1:1+data[0]]; N=max(qs+[0])*2; fact=[1]*(N+1)
    for i in range(1,N+1): fact[i]=fact[i-1]*i%MOD
    inv=[1]*(N+1); inv[N]=pow(fact[N],MOD-2,MOD)
    for i in range(N,0,-1): inv[i-1]=inv[i]*i%MOD
    def C(n,k): return fact[n]*inv[k]%MOD*inv[n-k]%MOD if 0<=k<=n else 0
    print("\n".join(str(C(2*n,n)*pow(n+1,MOD-2,MOD)%MOD) for n in qs))
if __name__=="__main__": main()
