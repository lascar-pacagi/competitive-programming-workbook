import sys
class DSU:
 def __init__(self,n):self.p=list(range(n+1));self.s=[1]*(n+1)
 def find(self,x):
  while self.p[x]!=x:self.p[x]=self.p[self.p[x]];x=self.p[x]
  return x
 def union(self,a,b):
  a=self.find(a);b=self.find(b)
  if a==b:return
  if self.s[a]<self.s[b]:a,b=b,a
  self.p[b]=a;self.s[a]+=self.s[b]
def main():
 d=list(map(int,sys.stdin.buffer.read().split()));n,m=d[:2]
 if n==1:print(0);return
 e=sorted((d[i+2],d[i],d[i+1]) for i in range(2,2+3*m,3));u=DSU(n)
 for w,a,b in e:
  u.union(a,b)
  if u.find(1)==u.find(n):print(w);return
 print(-1)
if __name__=='__main__':main()
