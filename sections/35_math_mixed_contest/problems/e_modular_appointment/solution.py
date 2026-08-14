import math,sys
def eg(a,b):
    if b==0:return (a,1,0)
    g,x,y=eg(b,a%b);return g,y,x-a//b*y
def main():
    d=list(map(int,sys.stdin.buffer.read().split()));q=d[0];i=1;out=[]
    for _ in range(q):
        a,b,c,m=d[i:i+4];i+=4;t=(b-c)%m;g,x,_=eg(a,m)
        out.append("-1" if t%g else str((t//g*x)%(m//g)))
    print("\n".join(out))
if __name__=="__main__":main()
