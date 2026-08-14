import sys
def main():
 d=list(map(int,sys.stdin.buffer.read().split()));n,q=d[0],d[1];i=2;a=sorted((d[j],d[j+1]) for j in range(i,i+2*n,2));i+=2*n;z=sorted((d[i+k],k) for k in range(q));ans=[0]*q;s=p=0
 for x,k in z:
  while p<n and a[p][0]<=x:s+=a[p][1];p+=1
  ans[k]=s
 print(*ans)
if __name__=='__main__':main()
