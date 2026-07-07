import sys
def main():
    data=list(map(int,sys.stdin.buffer.read().split()))
    if not data: return
    n,m=data[0],data[1]; moves=data[2:]; win=[False]*(n+1)
    for i in range(1,n+1): win[i]=any(i>=x and not win[i-x] for x in moves)
    print("WIN" if win[n] else "LOSE")
if __name__=="__main__": main()
