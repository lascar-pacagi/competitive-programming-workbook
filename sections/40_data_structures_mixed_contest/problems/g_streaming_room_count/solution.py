import heapq, sys
def main():
    data=list(map(int,sys.stdin.buffer.read().split()))
    if not data:return
    n=data[0]; ends=[]; answer=0; out=[]; j=1
    for _ in range(n):
        s,e=data[j:j+2]; j+=2
        while ends and ends[0]<=s: heapq.heappop(ends)
        heapq.heappush(ends,e); answer=max(answer,len(ends)); out.append(str(answer))
    print(*out)
if __name__=="__main__":main()
