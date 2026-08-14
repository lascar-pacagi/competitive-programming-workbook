from array import array
import bisect,sys
def main():
    d=list(map(int,sys.stdin.buffer.read().split()))
    if not d:return
    n,q=d[:2];a=d[2:2+n];vals=sorted(set(a));g=[[]for _ in range(n)];j=2+n
    for _ in range(n-1):u,v=d[j]-1,d[j+1]-1;j+=2;g[u].append(v);g[v].append(u)
    par=[-1]*n;order=[];stack=[0]
    while stack:
        u=stack.pop();order.append(u)
        for v in g[u]:
            if v!=par[u]:par[v]=u;stack.append(v)
    tin=[0]*n;size=[1]*n
    for i,u in enumerate(order):tin[u]=i
    for u in reversed(order[1:]):size[par[u]]+=size[u]
    left=array('i',[0]);right=array('i',[0]);cnt=array('i',[0])
    def add(old,l,r,p):
        left.append(left[old]);right.append(right[old]);cnt.append(cnt[old]+1);x=len(cnt)-1
        if r-l>1:
            m=(l+r)//2
            if p<m:left[x]=add(left[old],l,m,p)
            else:right[x]=add(right[old],m,r,p)
        return x
    roots=[0]
    for u in order:roots.append(add(roots[-1],0,len(vals),bisect.bisect_left(vals,a[u])))
    def kth(x,y,l,r,k):
        while r-l>1:
            m=(l+r)//2;c=cnt[left[y]]-cnt[left[x]]
            if k<=c:x,y,r=left[x],left[y],m
            else:k-=c;x,y,l=right[x],right[y],m
        return l
    out=[]
    for _ in range(q):
        u,k=d[j]-1,d[j+1];j+=2
        rank=kth(roots[tin[u]],roots[tin[u]+size[u]],0,len(vals),k)
        out.append(str(vals[rank]))
    print('\n'.join(out))
if __name__=="__main__":main()
