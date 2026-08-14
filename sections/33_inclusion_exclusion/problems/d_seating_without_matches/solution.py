import sys
M=1_000_000_007
def main():
 n=int(sys.stdin.buffer.read());f=[1]*(n+1)
 for i in range(1,n+1):f[i]=f[i-1]*i%M
 inv=[1]*(n+1);inv[n]=pow(f[n],M-2,M)
 for i in range(n,0,-1):inv[i-1]=inv[i]*i%M
 print(sum(((-1 if k&1 else 1)*f[n]*inv[k]) for k in range(n+1))%M)
if __name__=='__main__':main()
