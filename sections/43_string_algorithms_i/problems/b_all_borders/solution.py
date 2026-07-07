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
    s=sys.stdin.readline().strip(); p=pi(s); ans=[]; k=p[-1] if s else 0
    while k: ans.append(k); k=p[k-1]
    print(" ".join(map(str,ans[::-1])))
if __name__=="__main__": main()
