import bisect,math,sys
def main():
    d=list(map(int,sys.stdin.buffer.read().split()))
    if not d:return
    n,q=d[:2];a=d[2:2+n];bit=[0]*(n+1);inv=0
    def pref(i):
        s=0
        while i:s+=bit[i];i-=i&-i
        return s
    for seen,x in enumerate(a):
        inv+=seen-pref(x)
        i=x
        while i<=n:bit[i]+=1;i+=i&-i
    B=max(1,int(math.sqrt(n))+1);nb=(n+B-1)//B;blocks=[]
    for b in range(nb):blocks.append(sorted(a[b*B:min(n,(b+1)*B)]))
    def rebuild(b):blocks[b]=sorted(a[b*B:min(n,(b+1)*B)])
    def count(l,r,lo,hi):
        ans=0
        while l<=r and l%B:ans+=lo<a[l]<hi;l+=1
        while l+B-1<=r:
            v=blocks[l//B];ans+=bisect.bisect_left(v,hi)-bisect.bisect_right(v,lo);l+=B
        while l<=r:ans+=lo<a[l]<hi;l+=1
        return ans
    out=[];p=2+n
    for _ in range(q):
        i,j=d[p]-1,d[p+1]-1;p+=2
        if i>j:i,j=j,i
        if i!=j:
            x,y=a[i],a[j];delta=1+2*count(i+1,j-1,min(x,y),max(x,y));inv+=delta if x<y else -delta
            a[i],a[j]=y,x;rebuild(i//B)
            if i//B!=j//B:rebuild(j//B)
        out.append(str(inv))
    print('\n'.join(out))
if __name__=="__main__":main()
