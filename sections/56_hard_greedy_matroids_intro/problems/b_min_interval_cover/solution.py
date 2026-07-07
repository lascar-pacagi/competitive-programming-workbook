import sys
def main():
    data=list(map(int,sys.stdin.buffer.read().split()))
    if not data: return
    T,n=data[0],data[1]; seg=sorted((data[i],data[i+1]) for i in range(2,2+2*n,2)); i=ans=0; cur=0
    while cur<T:
        best=cur
        while i<n and seg[i][0]<=cur: best=max(best,seg[i][1]); i+=1
        if best==cur: print(-1); return
        cur=best; ans+=1
    print(ans)
if __name__=="__main__": main()
