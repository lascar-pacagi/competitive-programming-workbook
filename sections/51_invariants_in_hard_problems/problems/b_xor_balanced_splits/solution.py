import sys
def main():
    data=list(map(int,sys.stdin.buffer.read().split()))
    if not data: return
    a=data[1:]; total=0
    for x in a: total^=x
    pref=ans=0
    for x in a[:-1]:
        pref^=x
        if pref==(total^pref): ans+=1
    print(ans)
if __name__=="__main__": main()
