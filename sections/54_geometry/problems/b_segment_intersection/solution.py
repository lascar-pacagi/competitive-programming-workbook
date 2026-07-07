import sys
def ori(a,b,c): return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
def between(a,b,c): return min(a[0],b[0])<=c[0]<=max(a[0],b[0]) and min(a[1],b[1])<=c[1]<=max(a[1],b[1])
def inter(a,b,c,d):
    o1,o2,o3,o4=ori(a,b,c),ori(a,b,d),ori(c,d,a),ori(c,d,b)
    if o1==0 and between(a,b,c): return True
    if o2==0 and between(a,b,d): return True
    if o3==0 and between(c,d,a): return True
    if o4==0 and between(c,d,b): return True
    return (o1>0)!=(o2>0) and (o3>0)!=(o4>0)
def main():
    data=list(map(int,sys.stdin.buffer.read().split())); t=data[0]; idx=1; out=[]
    for _ in range(t):
        x=data[idx:idx+8]; idx+=8; out.append("YES" if inter((x[0],x[1]),(x[2],x[3]),(x[4],x[5]),(x[6],x[7])) else "NO")
    print("\n".join(out))
if __name__=="__main__": main()
