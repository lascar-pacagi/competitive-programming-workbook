import sys
def main():
    data=list(map(int,sys.stdin.buffer.read().split()))
    if not data: return
    t=data[0]; idx=1; out=[]
    for _ in range(t):
        n=data[idx]; idx+=1; x=0
        for v in data[idx:idx+n]: x^=v
        idx+=n; out.append("WIN" if x else "LOSE")
    print("\n".join(out))
if __name__=="__main__": main()
