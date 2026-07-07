import sys
def main():
    data=list(map(int,sys.stdin.buffer.read().split()))
    if not data: return
    q=data[0]; idx=1; lines=[]; out=[]
    for _ in range(q):
        t=data[idx]; idx+=1
        if t==1:
            m,b=data[idx],data[idx+1]; idx+=2; lines.append((m,b))
        else:
            x=data[idx]; idx+=1; out.append(str(max(m*x+b for m,b in lines)))
    print("\n".join(out))
if __name__=="__main__": main()
