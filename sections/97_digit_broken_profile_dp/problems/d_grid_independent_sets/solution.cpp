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
    vector<int>valid;
    for(int x=0;x<1<<m;x++)if(!(x&(x<<1)))valid.push_back(x);
    vector<int>dp(1<<m);
    dp[0]=1;
    for(auto row:g) {
        int blocked=0;
        for(int c=0;c<m;c++)if(row[c]=='#')blocked|=1<<c;
        vector<int>nd(1<<m);
        for(int x:valid)if(!(x&blocked))for(int y:valid)if(!(x&y))nd[x]=(nd[x]+dp[y])%MOD;
        dp.swap(nd);
    }
    cout<<accumulate(dp.begin(),dp.end(),0LL)%MOD<<'\n';
}
