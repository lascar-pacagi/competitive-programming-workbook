import sys
def main():
    data=sys.stdin.buffer.read().split()
    if not data:return
    n,q=map(int,data[:2]); bit=[0]*(n+1); on=[False]*(n+1); out=[]; j=2
    def add(i,v):
        while i<=n: bit[i]+=v;i+=i&-i
    def total():
        i=n;s=0
        while i:s+=bit[i];i-=i&-i
        return s
    def kth(k):
        p=0;d=1<<(n.bit_length()-1)
        while d:
            np=p+d
            if np<=n and bit[np]<k:p=np;k-=bit[np]
            d//=2
        return p+1
    for _ in range(q):
        c=data[j];x=int(data[j+1]);j+=2
        if c==b'T':add(x,-1 if on[x] else 1);on[x]=not on[x]
        else:out.append(str(kth(x) if total()>=x else -1))
    print('\n'.join(out))
if __name__=="__main__":main()
