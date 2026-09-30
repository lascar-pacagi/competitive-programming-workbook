import sys

def main():
    data=list(map(int,sys.stdin.buffer.read().split()))
    if not data:return
    m,q=data[:2];size=1
    while size<m:size*=2
    count=[0]*(2*size);out=[];pos=2
    def change(x,delta):
        node=size+x-1;count[node]+=delta;node//=2
        while node:count[node]=count[2*node]+count[2*node+1];node//=2
    def prefix(x):
        left,right=size,size+x;total=0
        while left<right:
            if left&1:total+=count[left];left+=1
            if right&1:right-=1;total+=count[right]
            left//=2;right//=2
        return total
    for _ in range(q):
        op,x=data[pos:pos+2];pos+=2
        if op==1:change(x,1)
        elif op==2:
            if count[size+x-1]:change(x,-1)
        elif op==4:out.append(prefix(x))
        elif x>count[1]:out.append(-1)
        else:
            node=1
            while node<size:
                if count[2*node]>=x:node*=2
                else:x-=count[2*node];node=2*node+1
            out.append(node-size+1)
    print('\n'.join(map(str,out)))
if __name__=='__main__':main()
