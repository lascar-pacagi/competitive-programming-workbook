import sys
class BIT:
    def __init__(self,n): self.n=n; self.bit=[0]*(n+2)
    def add(self,i,x):
        while i<=self.n: self.bit[i]+=x; i+=i&-i
    def sum(self,i):
        s=0
        while i>0: s+=self.bit[i]; i-=i&-i
        return s
def main():
    data=list(map(int,sys.stdin.buffer.read().split()))
    if not data: return
    n,q=data[0],data[1]; a=data[2:2+n]; b1=BIT(n+1); b2=BIT(n+1)
    def add_range(l,r,x): b1.add(l,x); b1.add(r+1,-x); b2.add(l,x*(l-1)); b2.add(r+1,-x*r)
    def pref(i): return b1.sum(i)*i-b2.sum(i)
    for i,x in enumerate(a,1): add_range(i,i,x)
    idx=2+n; out=[]
    for _ in range(q):
        t=data[idx]; idx+=1
        if t==1:
            l,r,x=data[idx],data[idx+1],data[idx+2]; idx+=3; add_range(l,r,x)
        else:
            l,r=data[idx],data[idx+1]; idx+=2; out.append(str(pref(r)-pref(l-1)))
    print("\n".join(out))
if __name__=="__main__": main()
