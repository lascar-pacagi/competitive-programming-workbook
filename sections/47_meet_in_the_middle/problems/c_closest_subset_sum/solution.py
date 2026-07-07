import sys,bisect
def sums(a):
    res=[0]
    for x in a: res += [y+x for y in res]
    return res
def main():
    data=list(map(int,sys.stdin.buffer.read().split()))
    if not data: return
    n,t=data[0],data[1]; a=data[2:]; L=sums(a[:n//2]); R=sorted(sums(a[n//2:])); best=10**30
    for s in L:
        i=bisect.bisect_left(R,t-s)
        for j in (i-1,i):
            if 0<=j<len(R): best=min(best,abs(s+R[j]-t))
    print(best)
if __name__=="__main__": main()
