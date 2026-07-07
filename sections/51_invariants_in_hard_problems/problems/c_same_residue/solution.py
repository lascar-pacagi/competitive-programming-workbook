import sys
def main():
    data=list(map(int,sys.stdin.buffer.read().split()))
    if not data: return
    n,k=data[0],data[1]; a=data[2:]; print("YES" if len({x%k for x in a})==1 else "NO")
if __name__=="__main__": main()
