import sys,math
MOD=1_000_000_007
def main():
    data=list(map(int,sys.stdin.buffer.read().split()))
    if not data: return
    t=data[0]; idx=1; out=[]
    for _ in range(t):
        n,k=data[idx],data[idx+1]; idx+=2; s=0
        for r in range(n): s=(s+pow(k,math.gcd(n,r),MOD))%MOD
        out.append(str(s*pow(n,MOD-2,MOD)%MOD))
    print("\n".join(out))
if __name__=="__main__": main()
