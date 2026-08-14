import bisect,sys
def main():
    d=sys.stdin.buffer.read().split()
    if not d:return
    q=int(d[0]);j=1;ops=[];xs=[]
    for _ in range(q):
        c=d[j];j+=1
        if c==b'U':x,y,v=map(int,d[j:j+3]);j+=3;ops.append((c,x,y,v));xs.append(x)
        else:x1,y1,x2,y2=map(int,d[j:j+4]);j+=4;ops.append((c,x1,y1,x2,y2))
    xs=sorted(set(xs));n=len(xs);ys=[[]for _ in range(n+1)]
    for o in ops:
        if o[0]==b'U':
            i=bisect.bisect_left(xs,o[1])+1
            while i<=n:ys[i].append(o[2]);i+=i&-i
    ys=[sorted(set(v)) for v in ys];bits=[[0]*(len(v)+1) for v in ys]
    def update(x,y,v):
        i=bisect.bisect_left(xs,x)+1
        while i<=n:
            k=bisect.bisect_left(ys[i],y)+1
            while k<len(bits[i]):bits[i][k]+=v;k+=k&-k
            i+=i&-i
    def pref(x,y):
        ans=0;i=bisect.bisect_right(xs,x)
        while i:
            k=bisect.bisect_right(ys[i],y)
            while k:ans+=bits[i][k];k-=k&-k
            i-=i&-i
        return ans
    out=[]
    for o in ops:
        if o[0]==b'U':update(o[1],o[2],o[3])
        else:
            _,x1,y1,x2,y2=o;out.append(str(pref(x2,y2)-pref(x1-1,y2)-pref(x2,y1-1)+pref(x1-1,y1-1)))
    print('\n'.join(out))
if __name__=="__main__":main()
