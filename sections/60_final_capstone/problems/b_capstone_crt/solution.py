import sys,math
def eg(a,b):
    if b==0: return (abs(a),1 if a>=0 else -1,0)
    g,x,y=eg(b,a%b); return g,y,x-(a//b)*y
def main():
    data=list(map(int,sys.stdin.buffer.read().split()))
    if not data: return
    t=data[0]; idx=1; out=[]
    for _ in range(t):
        a,m,b,n=data[idx],data[idx+1],data[idx+2],data[idx+3]; idx+=4; g,x,y=eg(m,n)
        if (b-a)%g: out.append("NO")
        else:
            l=m//g*n; k=((b-a)//g*x)%(n//g); out.append(f"{(a+m*k)%l} {l}")
    print("\n".join(out))
if __name__=="__main__": main()
