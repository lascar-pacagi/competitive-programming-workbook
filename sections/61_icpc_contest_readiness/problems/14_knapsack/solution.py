import sys
def main():
 d=list(map(int,sys.stdin.buffer.read().split()));a=d[1:];total=sum(a);p=bytearray(total+1);p[0]=1
 for x in a:
  for s in range(total,x-1,-1):
   if p[s-x]:p[s]=1
 print(min(total-2*s for s in range(total//2+1) if p[s]))
if __name__=='__main__':main()
