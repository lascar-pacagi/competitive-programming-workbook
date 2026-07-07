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
    lines=sys.stdin.read().splitlines(); pat=lines[0]; text=lines[1]; s=pat+"#"+text; p=pi(s); ans=[]
    for i,v in enumerate(p):
        if v==len(pat): ans.append(i-2*len(pat)+1)
    print(len(ans)); print(" ".join(map(str,ans)) if ans else "")
if __name__=="__main__": main()
