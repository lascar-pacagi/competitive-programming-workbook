import bisect,sys
def main():
    d=list(map(int,sys.stdin.buffer.read().split()))
    if not d:return
    n,k=d[:2];a=d[2:];v=sorted(set(a));z=len(v);bc=[0]*(z+1);bs=[0]*(z+1)
    def add(bit,i,x):
        while i<=z:bit[i]+=x;i+=i&-i
    def pref(bit,i):
        s=0
        while i:s+=bit[i];i-=i&-i
        return s
    def change(x,d):
        p=bisect.bisect_left(v,x)+1;add(bc,p,d);add(bs,p,d*x)
    def kth(kth):
        p=0;step=1<<(z.bit_length()-1)
        while step:
            np=p+step
            if np<=z and bc[np]<kth:p=np;kth-=bc[np]
            step//=2
        return p+1
    for x in a[:k]:change(x,1)
    out=[]
    for l in range(n-k+1):
        p=kth((k+1)//2);m=v[p-1];cl=pref(bc,p);sl=pref(bs,p);ct=pref(bc,z);st=pref(bs,z)
        out.append(str(m*cl-sl+st-sl-m*(ct-cl)))
        if l+k<n:change(a[l],-1);change(a[l+k],1)
    print(*out)
if __name__=="__main__":main()
