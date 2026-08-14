from array import array
import sys
def main():
    d=sys.stdin.buffer.read().split()
    if not d:return
    n,q=map(int,d[:2]);a=list(map(int,d[2:2+n]))
    left=array('i',[0]);right=array('i',[0]);total=array('q',[0])
    def node(l=0,r=0,s=0):left.append(l);right.append(r);total.append(s);return len(total)-1
    def build(l,r):
        if r-l==1:return node(s=a[l])
        m=(l+r)//2;x=node(build(l,m),build(m,r));total[x]=total[left[x]]+total[right[x]];return x
    def update(old,l,r,p,v):
        x=node(left[old],right[old],total[old])
        if r-l==1:total[x]=v;return x
        m=(l+r)//2
        if p<m:left[x]=update(left[old],l,m,p,v)
        else:right[x]=update(right[old],m,r,p,v)
        total[x]=total[left[x]]+total[right[x]];return x
    def query(x,l,r,ql,qr):
        if ql>=r or qr<=l:return 0
        if ql<=l and r<=qr:return total[x]
        m=(l+r)//2;return query(left[x],l,m,ql,qr)+query(right[x],m,r,ql,qr)
    roots=[build(0,n)];j=2+n;out=[]
    for _ in range(q):
        c=d[j];v=int(d[j+1]);l=int(d[j+2]);j+=3
        if c==b'U':x=int(d[j]);j+=1;roots.append(update(roots[v],0,n,l-1,x))
        else:r=int(d[j]);j+=1;out.append(str(query(roots[v],0,n,l-1,r)))
    print('\n'.join(out))
if __name__=="__main__":main()
