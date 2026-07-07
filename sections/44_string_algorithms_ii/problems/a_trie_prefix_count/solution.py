import sys
def main():
    lines=sys.stdin.read().splitlines(); n,q=map(int,lines[0].split()); nxt=[]; cnt=[]
    nxt.append({}); cnt.append(0)
    for w in lines[1:1+n]:
        v=0; cnt[v]+=1
        for ch in w:
            if ch not in nxt[v]: nxt[v][ch]=len(nxt); nxt.append({}); cnt.append(0)
            v=nxt[v][ch]; cnt[v]+=1
    out=[]
    for p in lines[1+n:1+n+q]:
        v=0; ok=True
        for ch in p:
            if ch not in nxt[v]: ok=False; break
            v=nxt[v][ch]
        out.append(str(cnt[v] if ok else 0))
    print("\n".join(out))
if __name__=="__main__": main()
