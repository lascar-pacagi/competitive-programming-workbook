import sys
def main():
    s=sys.stdin.readline().strip(); next=[]; link=[]; length=[]
    next.append({}); link.append(-1); length.append(0); last=0
    for ch in s:
        cur=len(next); next.append({}); length.append(length[last]+1); link.append(0); p=last
        while p!=-1 and ch not in next[p]: next[p][ch]=cur; p=link[p]
        if p==-1: link[cur]=0
        else:
            q=next[p][ch]
            if length[p]+1==length[q]: link[cur]=q
            else:
                clone=len(next); next.append(next[q].copy()); length.append(length[p]+1); link.append(link[q])
                while p!=-1 and next[p].get(ch)==q: next[p][ch]=clone; p=link[p]
                link[q]=link[cur]=clone
        last=cur
    print(sum(length[v]-length[link[v]] for v in range(1,len(next))))
if __name__=="__main__": main()
