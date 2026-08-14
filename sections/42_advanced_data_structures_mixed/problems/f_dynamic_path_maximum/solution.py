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
    z=1
    while z<n:z*=2
    tree=[-10**30]*(2*z)
    for u in range(n):tree[z+pos[u]]=a[u]
    for i in range(z-1,0,-1):tree[i]=max(tree[2*i],tree[2*i+1])
    def rq(l,r):
        ans=-10**30;l+=z;r+=z+1
        while l<r:
            if l&1:ans=max(ans,tree[l]);l+=1
            if r&1:r-=1;ans=max(ans,tree[r])
            l//=2;r//=2
        return ans
    out=[]
    for _ in range(q):
        c=d[j];u=int(d[j+1])-1;v=int(d[j+2]);j+=3
        if c==b'U':
            x=z+pos[u];tree[x]=v;x//=2
            while x:tree[x]=max(tree[2*x],tree[2*x+1]);x//=2
        else:
            v-=1;ans=-10**30
            while head[u]!=head[v]:
                if dep[head[u]]<dep[head[v]]:u,v=v,u
                ans=max(ans,rq(pos[head[u]],pos[u]));u=par[head[u]]
            if dep[u]>dep[v]:u,v=v,u
            out.append(str(max(ans,rq(pos[u],pos[v]))))
    print('\n'.join(out))
if __name__=="__main__":main()
