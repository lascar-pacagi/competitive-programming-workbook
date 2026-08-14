import sys
def main():
    d=sys.stdin.buffer.read().split()
    if not d:return
    n,q=map(int,d[:2]);a=list(map(int,d[2:2+n]));g=[[]for _ in range(n)];p=2+n
    for _ in range(n-1):
        u,v=int(d[p])-1,int(d[p+1])-1;p+=2;g[u].append(v);g[v].append(u)
    tin=[0]*n;tout=[0]*n;parent=[-1]*n;timer=0;stack=[(0,0)]
    while stack:
        u,state=stack.pop()
        if state==0:
            timer+=1;tin[u]=timer;stack.append((u,1))
            for v in reversed(g[u]):
                if v!=parent[u]:parent[v]=u;stack.append((v,0))
        else:tout[u]=timer
    bit=[0]*(n+2)
    def add(i,x):
        while i<=n+1:bit[i]+=x;i+=i&-i
    def get(i):
        s=0
        while i:s+=bit[i];i-=i&-i
        return s
    out=[]
    for _ in range(q):
        c=d[p];u=int(d[p+1])-1;p+=2
        if c==b'A':x=int(d[p]);p+=1;add(tin[u],x);add(tout[u]+1,-x)
        else:out.append(str(a[u]+get(tin[u])))
    print('\n'.join(out))
if __name__=="__main__":main()
