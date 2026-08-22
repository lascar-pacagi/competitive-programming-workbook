#include <bits/stdc++.h>
using namespace std;
const int MOD=1e9+7;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n,m;
    cin>>n>>m;
    vector<string>g(n);
    for(auto&s:g)cin>>s;
    vector<int>dp(1<<m);
    dp[0]=1;
    for(int r=0;r<n;r++) {
        int blocked=0;
        for(int c=0;c<m;c++)if(g[r][c]=='#')blocked|=1<<c;
        vector<int>nd(1<<m);
        for(int in=0;in<1<<m;in++)if(dp[in]&&!(in&blocked)) {
            function<void(int,int,int)>fill=[&](int c,int used,int out) {
                if(c==m) {
                    nd[out]=(nd[out]+dp[in])%MOD;
                    return;
                }
                int bit=1<<c;
                if((used|blocked)&bit)fill(c+1,used,out);
                else {
                    if(c+1<m&&!((used|blocked)&(bit<<1)))fill(c+2,used|bit|(bit<<1),out);
                    if(r+1<n&&g[r+1][c]=='.')fill(c+1,used|bit,out|bit);
                }
            }
            ;
            fill(0,in,0);
        }
        dp.swap(nd);
    }
    cout<<dp[0]<<'\n';
}
