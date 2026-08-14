import sys
def main():
    d=sys.stdin.buffer.read().split();s=d[0];n=len(s);q=int(d[1]);mods=(1_000_000_007,1_000_000_009);base=911_382_323
    powers=[];prefix=[]
    for mod in mods:
        p=[1]*(n+1);h=[0]*(n+1)
        for i,c in enumerate(s):p[i+1]=p[i]*base%mod;h[i+1]=(h[i]*base+c)%mod
        powers.append(p);prefix.append(h)
    def equal(a,b,length):
        for mod,p,h in zip(mods,powers,prefix):
            if (h[a+length]-h[a]*p[length])%mod!=(h[b+length]-h[b]*p[length])%mod:return False
        return True
    out=[];idx=2
    for _ in range(q):
        a,b=int(d[idx])-1,int(d[idx+1])-1;idx+=2;lo,hi=0,n-max(a,b)
        while lo<hi:
            mid=(lo+hi+1)//2
            if equal(a,b,mid):lo=mid
            else:hi=mid-1
        out.append(str(lo))
    print("\n".join(out))
if __name__=="__main__":main()
