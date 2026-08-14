import sys
def main():
    p,t=sys.stdin.read().split();s=p+"#"+t;z=[0]*len(s);l=r=0
    for i in range(1,len(s)):
        if i<=r:z[i]=min(r-i+1,z[i-l])
        while i+z[i]<len(s) and s[z[i]]==s[i+z[i]]:z[i]+=1
        if i+z[i]-1>r:l,r=i,i+z[i]-1
    print(" ".join(str(min(len(p),z[len(p)+1+i])) for i in range(len(t))))
if __name__=="__main__":main()
