import sys
def main():
    d=sys.stdin.buffer.read().split()
    if not d:return
    n,q=map(int,d[:2]);a=list(map(int,d[2:2+n]));g=[[]for _ in range(n)];j=2+n
    for _ in range(n-1):u,v=int(d[j])-1,int(d[j+1])-1;j+=2;g[u].append(v);g[v].append(u)
    par=[-1]*n;dep=[0]*n;order=[0]
    for u in order:
        for v in g[u]:
            if v!=par[u]:par[v]=u;dep[v]=dep[u]+1;order.append(v)
    size=[1]*n;heavy=[-1]*n
    for u in reversed(order[1:]):
        size[par[u]]+=size[u]
        if heavy[par[u]]<0 or size[u]>size[heavy[par[u]]]:heavy[par[u]]=u
    head=[0]*n;pos=[0]*n;timer=0;todo=[(0,0)]
    while todo:
        u,h=todo.pop()
        while u!=-1:
            head[u]=h;pos[u]=timer;timer+=1
            for v in g[u]:
                if v!=par[u] and v!=heavy[u]:todo.append((v,v))
            u=heavy[u]
    flat=[0]*n
    for u in range(n):flat[pos[u]]=a[u]
    mx=[0]*(4*n);lazy=[0]*(4*n)
    def build(x,l,r):
        if r-l==1:mx[x]=flat[l];return
        m=(l+r)//2;build(2*x,l,m);build(2*x+1,m,r);mx[x]=max(mx[2*x],mx[2*x+1])
    def add(x,l,r,ql,qr,v):
        if ql>=r or qr<=l:return
        if ql<=l and r<=qr:mx[x]+=v;lazy[x]+=v;return
        m=(l+r)//2;add(2*x,l,m,ql,qr,v);add(2*x+1,m,r,ql,qr,v);mx[x]=lazy[x]+max(mx[2*x],mx[2*x+1])
    def get(x,l,r,ql,qr,carry=0):
        if ql>=r or qr<=l:return -10**30
        if ql<=l and r<=qr:return mx[x]+carry
        m=(l+r)//2;carry+=lazy[x];return max(get(2*x,l,m,ql,qr,carry),get(2*x+1,m,r,ql,qr,carry))
    build(1,0,n);out=[]
    def parts(u,v):
        while head[u]!=head[v]:
            if dep[head[u]]<dep[head[v]]:u,v=v,u
            yield pos[head[u]],pos[u]+1;u=par[head[u]]
        if dep[u]>dep[v]:u,v=v,u
        yield pos[u],pos[v]+1
    for _ in range(q):
        c=d[j];u=int(d[j+1])-1;v=int(d[j+2])-1;j+=3
        if c==b'A':
            value=int(d[j]);j+=1
            for l,r in parts(u,v):add(1,0,n,l,r,value)
        else:out.append(str(max(get(1,0,n,l,r) for l,r in parts(u,v))))
    print('\n'.join(out))
if __name__=="__main__":main()
