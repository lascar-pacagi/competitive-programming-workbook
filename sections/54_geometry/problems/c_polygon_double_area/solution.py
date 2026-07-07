import sys
def main():
    data=list(map(int,sys.stdin.buffer.read().split()))
    if not data: return
    n=data[0]; pts=[(data[i],data[i+1]) for i in range(1,2*n+1,2)]; s=0
    for i in range(n):
        x1,y1=pts[i]; x2,y2=pts[(i+1)%n]; s+=x1*y2-y1*x2
    print(abs(s))
if __name__=="__main__": main()
