import sys
def main():
    d=list(map(int,sys.stdin.buffer.read().split()));n=d[0];x=d[1:n+1];m=d[n+1:2*n+1];fee=d[2*n+1:3*n+1];coords=sorted(set(x));inf=10**30;tree=[(0,inf)]*(4*len(coords))
    def value(line,at):return line[0]*at+line[1]
    def add(line,p,l,r):
        mid=(l+r)//2
        if value(tree[p],coords[mid])>value(line,coords[mid]):tree[p],line=line,tree[p]
        if l==r:return
        if value(tree[p],coords[l])>value(line,coords[l]):add(line,p*2,l,mid)
        elif value(tree[p],coords[r])>value(line,coords[r]):add(line,p*2+1,mid+1,r)
    def get(p,l,r,at):
        ans=value(tree[p],coords[at])
        if l==r:return ans
        mid=(l+r)//2
        return min(ans,get(p*2,l,mid,at)if at<=mid else get(p*2+1,mid+1,r,at))
    dp=[0]*n;add((m[0],0),1,0,len(coords)-1)
    for i in range(1,n):
        at=__import__("bisect").bisect_left(coords,x[i]);dp[i]=fee[i]+get(1,0,len(coords)-1,at);add((m[i],dp[i]),1,0,len(coords)-1)
    print(dp[-1])
if __name__=="__main__":main()
