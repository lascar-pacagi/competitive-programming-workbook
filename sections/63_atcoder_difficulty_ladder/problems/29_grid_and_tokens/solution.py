import heapq, sys
def main() -> None:
 data=list(map(int,sys.stdin.buffer.read().split()));q=data[1:];heapq.heapify(q);answer=0
 while len(q)>1:
  total=heapq.heappop(q)+heapq.heappop(q);answer+=total;heapq.heappush(q,total)
 print(answer)
if __name__ == "__main__": main()
