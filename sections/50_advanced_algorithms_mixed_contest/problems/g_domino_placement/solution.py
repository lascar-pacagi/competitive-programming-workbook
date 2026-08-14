import sys
def main():
    data=sys.stdin.read().split();n,m=map(int,data[:2]);g=data[2:];match=[-1]*(n*m);seen=[0]*(n*m);stamp=0
    def dfs(cell):
        if seen[cell]==stamp:return False
        seen[cell]=stamp;r,c=divmod(cell,m)
        for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
            nr,nc=r+dr,c+dc
            if 0<=nr<n and 0<=nc<m and g[nr][nc]==".":
                v=nr*m+nc
                if match[v]==-1 or dfs(match[v]):match[v]=cell;return True
        return False
    ans=0
    for r in range(n):
        for c in range(m):
            if g[r][c]=="." and (r+c)%2==0:
                stamp+=1;ans+=dfs(r*m+c)
    print(ans)
if __name__=="__main__":main()
