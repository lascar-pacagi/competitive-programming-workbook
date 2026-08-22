#include <bits/stdc++.h>
using namespace std;
using ll=long long;
const ll INF=4e18;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n,m,k,queries;
    cin>>n>>m>>k>>queries;
    vector<vector<pair<int,int>>>g(n);
    while(m--) {
        int u,v,w;
        cin>>u>>v>>w;
        --u;
        --v;
        g[u].push_back({v,w});
        g[v].push_back({u,w});
    }
    vector<vector<ll>>dp(1<<k,vector<ll>(n,INF));
    for(int i=0,v;i<k;i++)cin>>v,dp[1<<i][v-1]=0;
    for(int mask=1;mask<1<<k;mask++) {
        for(int sub=(mask-1)&mask;sub;sub=(sub-1)&mask) {
            int other=mask^sub;
            if(sub<other)for(int v=0;v<n;v++)dp[mask][v]=min(dp[mask][v],dp[sub][v]+dp[other][v]);
        }
        priority_queue<pair<ll,int>,vector<pair<ll,int>>,greater<pair<ll,int>>>q;
        for(int v=0;v<n;v++)if(dp[mask][v]<INF)q.push({dp[mask][v],v});
        while(!q.empty()) {
            auto[d,u]=q.top();
            q.pop();
            if(d!=dp[mask][u])continue;
            for(auto[v,w]:g[u])if(d+w<dp[mask][v])dp[mask][v]=d+w,q.push({d+w,v});
        }
    }
    while(queries--) {
        int mask;
        cin>>mask;
        ll ans=*min_element(dp[mask].begin(),dp[mask].end());
        if(ans==INF)cout<<"IMPOSSIBLE\n";
        else cout<<ans<<'\n';
    }
}
