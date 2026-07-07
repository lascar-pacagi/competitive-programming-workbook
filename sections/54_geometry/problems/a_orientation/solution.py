import sys
def main():
    data=list(map(int,sys.stdin.buffer.read().split()))
    if not data: return
    t=data[0]; idx=1; out=[]
    for _ in range(t):
        ax,ay,bx,by,cx,cy=data[idx:idx+6]; idx+=6; v=(bx-ax)*(cy-ay)-(by-ay)*(cx-ax); out.append("LEFT" if v>0 else "RIGHT" if v<0 else "TOUCH")
    print("\n".join(out))
if __name__=="__main__": main()
