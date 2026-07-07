import sys
def main():
    lines=sys.stdin.read().split(); s=lines[0]; q=int(lines[1]); idx=2; out=[]
    for _ in range(q):
        l1,r1,l2,r2=map(int,lines[idx:idx+4]); idx+=4; out.append("YES" if s[l1-1:r1]==s[l1-1:r1][::-1] else "NO")
    print("\n".join(out))
if __name__=="__main__": main()
