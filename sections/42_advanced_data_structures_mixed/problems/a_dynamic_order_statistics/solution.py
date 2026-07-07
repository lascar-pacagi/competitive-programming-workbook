import sys
class BIT:
    def __init__(self,n): self.n=n; self.bit=[0]*(n+1)
    def add(self,i,x):
        while i<=self.n: self.bit[i]+=x; i+=i&-i
    def sum(self,i):
        s=0
        while i>0: s+=self.bit[i]; i-=i&-i
        return s
    def kth(self,k):
        if k<1 or k>self.sum(self.n): return -1
        pos=0; step=1<<self.n.bit_length()
        while step:
            nxt=pos+step
            if nxt<=self.n and self.bit[nxt]<k: pos=nxt; k-=self.bit[nxt]
            step//=2
        return pos+1
def main():
    data=list(map(int,sys.stdin.buffer.read().split())); 
    if not data: return
    m,q=data[0],data[1]; bit=BIT(m); cnt=[0]*(m+1); idx=2; out=[]
    for _ in range(q):
        t,x=data[idx],data[idx+1]; idx+=2
        if t==1: cnt[x]+=1; bit.add(x,1)
        elif t==2:
            if cnt[x]: cnt[x]-=1; bit.add(x,-1)
        elif t==3: out.append(str(bit.kth(x)))
        else: out.append(str(bit.sum(x)))
    print("\n".join(out))
if __name__=="__main__": main()
