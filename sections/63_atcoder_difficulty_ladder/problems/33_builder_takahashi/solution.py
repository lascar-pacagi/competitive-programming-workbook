import sys
def main():
 s=sys.stdin.buffer.readline().strip();n=len(s);pi=[0]*n;cnt=[0]*(n+1)
 for i in range(1,n):
  j=pi[i-1]
  while j and s[i]!=s[j]:j=pi[j-1]
  if s[i]==s[j]:j+=1
  pi[i]=j
 for x in pi:cnt[x]+=1
 for i in range(n-1,0,-1):cnt[pi[i-1]]+=cnt[i]
 print(*(cnt[i]+1 for i in range(1,n+1)))
if __name__=='__main__':main()
