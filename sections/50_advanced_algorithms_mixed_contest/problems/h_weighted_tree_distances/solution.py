import sys
def main():
    d=list(map(int,sys.stdin.buffer.read().split()));n=d[0];w=d[1:n+1];g=[[]for _ in range(n)];idx=n+1
    for _ in range(n-1):u,v=d[idx]-1,d[idx+1]-1;idx+=2;g[u].append(v);g[v].append(u)
    par=[-1]*n;depth=[0]*n;order=[0]
    for u in order:
        for v in g[u]:
            if v!=par[u]:par[v]=u;depth[v]=depth[u]+1;order.append(v)
    sub=w[:]
    for v in reversed(order[1:]):sub[par[v]]+=sub[v]
    total=sum(w);ans=[0]*n;ans[0]=sum(w[i]*depth[i] for i in range(n))
    for u in order:
        for v in g[u]:
            if par[v]==u:ans[v]=ans[u]+total-2*sub[v]
    print(" ".join(map(str,ans)))
if __name__=="__main__":main()
