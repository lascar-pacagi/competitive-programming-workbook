import sys
def main():
 d=list(map(int,sys.stdin.buffer.read().split()));i=1;o=[]
 for _ in range(d[0]):
  n,k,z=d[i:i+3];i+=3;a=sorted((d[j],d[j+1]) for j in range(i,i+2*n,2));i+=2*n;cur=0
  for l,r in a:
   if cur+k-1<l:break
   cur=max(cur,r+1)
  o.append(str(cur if cur+k-1<=z else -1))
 print('\n'.join(o))
if __name__=='__main__':main()
