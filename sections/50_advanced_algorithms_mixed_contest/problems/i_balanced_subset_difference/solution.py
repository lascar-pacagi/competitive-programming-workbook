import bisect,sys
def sums(a):
    out=[0]
    for x in a:out += [v+x for v in out]
    return out
def main():
    d=list(map(int,sys.stdin.buffer.read().split()));n=d[0];a=d[1:];left=sums(a[:n//2]);right=sorted(sums(a[n//2:]));total=sum(a);best=10**40
    for x in left:
        target=(total-2*x+1)//2;i=bisect.bisect_left(right,target)
        for j in (i-1,i):
            if 0<=j<len(right):best=min(best,abs(total-2*(x+right[j])))
    print(best)
if __name__=="__main__":main()
