import sys
MOD=1_000_000_007
def fib(n):
    if n==0:return 0,1
    a,b=fib(n//2); c=a*((2*b-a)%MOD)%MOD; d=(a*a+b*b)%MOD
    return (d,(c+d)%MOD) if n&1 else (c,d)
def main():
    data=list(map(int,sys.stdin.buffer.read().split())); out=[]
    for i in range(1,len(data),2): out.append(str((fib(data[i+1]+2)[0]-fib(data[i]+1)[0])%MOD))
    print('\n'.join(out))
if __name__=='__main__':main()
