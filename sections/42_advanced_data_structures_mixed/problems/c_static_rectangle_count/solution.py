import sys,bisect
class BIT:
    def __init__(self,n): self.n=n; self.bit=[0]*(n+1)
    def add(self,i,x):
        while i<=self.n: self.bit[i]+=x; i+=i&-i
    def sum(self,i):
        s=0
        while i>0: s+=self.bit[i]; i-=i&-i
        return s
def main():
    data=list(map(int,sys.stdin.buffer.read().split()))
    if not data: return
    n,q=data[0],data[1]; idx=2; pts=[]; ys=[]
    for _ in range(n): x,y=data[idx],data[idx+1]; idx+=2; pts.append((x,y)); ys.append(y)
    events=[]; ans=[0]*q
    for qi in range(q):
        x1,y1,x2,y2=data[idx],data[idx+1],data[idx+2],data[idx+3]; idx+=4; ys+= [y1,y2]
        events.append((x2,y1,y2,qi,1)); events.append((x1-1,y1,y2,qi,-1))
    ys=sorted(set(ys)); pts.sort(); events.sort(); bit=BIT(len(ys)); p=0
    for x,y1,y2,qi,sgn in events:
        while p<n and pts[p][0]<=x:
            bit.add(bisect.bisect_left(ys,pts[p][1])+1,1); p+=1
        l=bisect.bisect_left(ys,y1)+1; r=bisect.bisect_right(ys,y2)
        ans[qi]+=sgn*(bit.sum(r)-bit.sum(l-1))
    print("\n".join(map(str,ans)))
if __name__=="__main__": main()
