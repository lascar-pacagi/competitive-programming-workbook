import sys
def pi(s):
    p=[0]*len(s)
    for i in range(1,len(s)):
        j=p[i-1]
        while j and s[i]!=s[j]: j=p[j-1]
        if s[i]==s[j]: j+=1
        p[i]=j
    return p
def main():
    s=sys.stdin.readline().strip(); n=len(s); k=n-pi(s)[-1]
    print(k if n%k==0 else n)
if __name__=="__main__": main()
