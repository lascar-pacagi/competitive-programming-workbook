import sys
def main() -> None:
    data=list(map(int,sys.stdin.buffer.read().split()))
    if not data:return
    elapsed=answer=0
    for duration in sorted(data[1:]):
        elapsed+=duration;answer+=elapsed
    print(answer)
if __name__=='__main__':main()
