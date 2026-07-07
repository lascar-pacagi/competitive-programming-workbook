import sys,bisect
def sums(a):
    res=[0]
    for x in a: res += [y+x for y in res]
    return res
def main():
    data=list(map(int,sys.stdin.buffer.read().split()))
    if not data: return
    n,x=data[0],data[1]; a=data[2:]; left=sums(a[:n//2]); right=sorted(sums(a[n//2:])); ans=0
    for s in left: ans+=bisect.bisect_right(right,x-s)
    print(ans)
if __name__=="__main__": main()
