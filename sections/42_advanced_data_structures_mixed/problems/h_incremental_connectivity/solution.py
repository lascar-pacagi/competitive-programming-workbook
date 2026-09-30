import sys

def main():
    data=sys.stdin.buffer.read().split()
    if not data:return
    n,q=map(int,data[:2]);parent=list(range(n));size=[1]*n;pos=2;out=[]
    def find(u):
        while parent[u]!=u:parent[u]=parent[parent[u]];u=parent[u]
        return u
    for _ in range(q):
        op=data[pos];u,v=int(data[pos+1])-1,int(data[pos+2])-1;pos+=3
        u,v=find(u),find(v)
        if op==b'A':
            if u!=v:
                if size[u]<size[v]:u,v=v,u
                parent[v]=u;size[u]+=size[v]
        else:out.append('YES' if u==v else 'NO')
    print('\n'.join(out))

if __name__ == "__main__": main()
