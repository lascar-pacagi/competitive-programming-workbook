import sys,itertools
def main():
    data=list(map(int,sys.stdin.buffer.read().split()))
    if not data: return
    n,m=data[0],data[1]; clauses=[]; idx=2
    for _ in range(m): clauses.append((data[idx],data[idx+1])); idx+=2
    for mask in range(1<<n):
        ok=True
        for a,b in clauses:
            va=((mask>>(abs(a)-1))&1)==(a>0); vb=((mask>>(abs(b)-1))&1)==(b>0)
            if not (va or vb): ok=False; break
        if ok: print("YES"); return
    print("NO")
if __name__=="__main__": main()
