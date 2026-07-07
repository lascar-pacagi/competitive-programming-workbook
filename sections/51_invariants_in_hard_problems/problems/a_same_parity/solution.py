import sys
def main():
    data=list(map(int,sys.stdin.buffer.read().split()))
    if not data: return
    a=data[1:]; print("YES" if all(x%2==a[0]%2 for x in a) else "NO")
if __name__=="__main__": main()
