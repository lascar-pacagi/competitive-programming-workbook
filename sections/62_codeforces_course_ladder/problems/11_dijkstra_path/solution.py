import sys
def main():
    data=list(map(int,sys.stdin.buffer.read().split())); i=1; out=[]
    for _ in range(data[0]):
        n=data[i]; i+=1; events={}
        for _ in range(n):
            l,r=data[i],data[i+1]; i+=2; events[l]=events.get(l,0)+1; events[r+1]=events.get(r+1,0)-1
        cur=0; best=-1; when=0
        for x in sorted(events):
            cur+=events[x]
            if cur>best: best,when=cur,x
        out.append(f'{best} {when}')
    print('\n'.join(out))
if __name__=='__main__':main()
