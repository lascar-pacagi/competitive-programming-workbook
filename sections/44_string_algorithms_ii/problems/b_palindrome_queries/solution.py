import sys
def main():
    s=sys.stdin.readline().strip(); q=int(sys.stdin.readline()); out=[]
    for _ in range(q):
        l,r=map(int,sys.stdin.readline().split()); sub=s[l-1:r]; out.append("YES" if sub==sub[::-1] else "NO")
    print("\n".join(out))
if __name__=="__main__": main()
