import sys
MOD=1_000_000_007
def main():
 d=list(map(int,sys.stdin.buffer.read().split()));o=[]
 for i in range(d[0]):
  a,b,c=d[1+3*i:4+3*i];o.append(str(pow(a,pow(b,c,MOD-1),MOD)))
 print('\n'.join(o))
if __name__=='__main__':main()
