import sys
def main():
    d=sys.stdin.buffer.read().split()
    if not d:return
    n,q=map(int,d[:2]);a=list(map(int,d[2:2+n]));total=[0]*(4*n);pref=[0]*(4*n)
    def pull(x):total[x]=total[2*x]+total[2*x+1];pref[x]=max(pref[2*x],total[2*x]+pref[2*x+1])
    def build(x,l,r):
        if r-l==1:total[x]=pref[x]=a[l];return
        m=(l+r)//2;build(2*x,l,m);build(2*x+1,m,r);pull(x)
    def update(x,l,r,p,v):
        if r-l==1:total[x]=pref[x]=v;return
        m=(l+r)//2
        if p<m:update(2*x,l,m,p,v)
        else:update(2*x+1,m,r,p,v)
        pull(x)
    def first(x,l,r,ql,budget,running):
        if r<=ql:return -1,running
        if ql<=l and running+pref[x]<=budget:return -1,running+total[x]
        if r-l==1:return l,running
        m=(l+r)//2;answer,running=first(2*x,l,m,ql,budget,running)
        return (answer,running) if answer>=0 else first(2*x+1,m,r,ql,budget,running)
    build(1,0,n);j=2+n;out=[]
    for _ in range(q):
        c=d[j];i=int(d[j+1])-1;x=int(d[j+2]);j+=3
        if c==b'U':update(1,0,n,i,x)
        else:answer,_=first(1,0,n,i,x,0);out.append(str(answer+1 if answer>=0 else -1))
    print('\n'.join(out))
if __name__=="__main__":main()
