import sys,heapq
def main():
    data=list(map(int,sys.stdin.buffer.read().split()))
    if not data: return
    n=data[0]; jobs=sorted((data[i],data[i+1]) for i in range(1,2*n+1,2)); h=[]
    for d,p in jobs:
        heapq.heappush(h,p)
        if len(h)>d: heapq.heappop(h)
    print(sum(h))
if __name__=="__main__": main()
