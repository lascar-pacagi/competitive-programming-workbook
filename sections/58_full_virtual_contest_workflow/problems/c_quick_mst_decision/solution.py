import sys
def main():
    data=list(map(int,sys.stdin.buffer.read().split()))
    if not data: return
    n,m=data[0],data[1]; edges=[]; total=0; idx=2
    for _ in range(m):
        a,b,w=data[idx],data[idx+1],data[idx+2]; idx+=3; edges.append((w,a-1,b-1)); total+=w
    p=list(range(n))
    def f(x):
        while p[x]!=x: p[x]=p[p[x]]; x=p[x]
        return x
    keep=0; cnt=0
    for w,a,b in sorted(edges):
        ra,rb=f(a),f(b)
        if ra!=rb: p[ra]=rb; keep+=w; cnt+=1
    print(total-keep if cnt==n-1 else -1)
if __name__=="__main__": main()
