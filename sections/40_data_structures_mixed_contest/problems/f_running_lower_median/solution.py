import heapq,sys
def main():
    d=list(map(int,sys.stdin.buffer.read().split()));a=d[1:];lo=[];hi=[];out=[]
    for x in a:
        if not lo or x<=-lo[0]:heapq.heappush(lo,-x)
        else:heapq.heappush(hi,x)
        if len(lo)<len(hi):heapq.heappush(lo,-heapq.heappop(hi))
        if len(lo)>len(hi)+1:heapq.heappush(hi,-heapq.heappop(lo))
        out.append(str(-lo[0]))
    print(" ".join(out))
if __name__=="__main__":main()
