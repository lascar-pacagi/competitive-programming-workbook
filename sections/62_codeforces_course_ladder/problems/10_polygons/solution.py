import sys
data=list(map(int,sys.stdin.buffer.read().split()));i=1;out=[]
for _ in range(data[0]):
 n,k,s=data[i:i+3];i+=3
 if s>n*k:out.append('-1');continue
 a=[]
 for p in range(n):
  x=max(0,s-(n-p-1)*k);a.append(x);s-=x
 out.append(' '.join(map(str,a)))
print('\n'.join(out))
